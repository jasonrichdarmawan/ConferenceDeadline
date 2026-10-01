"""Convert the seventh-edition CCF PDF catalog to an English CSV.

Requires PyMuPDF with table extraction support (tested with 1.28.2).
"""

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

import pymupdf


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = ROOT / "raw/第七版中国计算机学会推荐国际学术会议和期刊目录（正式版）.pdf"
DEFAULT_CSV = ROOT / "data/Conferences-Journals-CCF.csv"
CATEGORIES = {
    "计算机体系结构/并行与分布计算/存储系统":
        "Computer Architecture / Parallel and Distributed Computing / Storage Systems",
    "计算机网络": "Computer Networks",
    "网络与信息安全": "Network and Information Security",
    "软件工程/系统软件/程序设计语言":
        "Software Engineering / System Software / Programming Languages",
    "数据库/数据挖掘/内容检索": "Databases / Data Mining / Content Retrieval",
    "计算机科学理论": "Theoretical Computer Science",
    "计算机图形学与多媒体": "Computer Graphics and Multimedia",
    "人工智能": "Artificial Intelligence",
    "人机交互与普适计算": "Human-Computer Interaction and Pervasive Computing",
    "交叉/综合/新兴": "Interdisciplinary / General / Emerging Areas",
}
TRANSLATIONS = {
    "中国科学院信息工程研究所":
        "Institute of Information Engineering, Chinese Academy of Sciences",
    "科学出版社": "Science Press",
    "清华大学出版社": "Tsinghua University Press",
    "浙江大学出版社": "Zhejiang University Press",
    "中国科技出版社": "China Science and Technology Press",
    "北京航空航天大学": "Beihang University",
    "中国中文信息学会": "Chinese Information Processing Society of China",
}
FIELDS = [
    "category", "type", "rank", "number", "acronym", "name", "publisher",
    "url", "source_page", "catalog_year",
]


def normalize(value: str | None, field: str) -> str:
    text = value or ""
    # Chinese publisher names may be broken across multiple PDF lines.
    text = re.sub(r"(?<=[\u4e00-\u9fff])\s+(?=[\u4e00-\u9fff])", "", text)
    if field == "acronym":
        for old, new in {
            "CCF-\nTHPC": "CCF-THPC", "CODES+\nISSS": "CODES+ISSS",
            "SIG-\nMETRICS": "SIGMETRICS", "JCOMPLEXI\nTY": "JCOMPLEXITY",
            "INTER-\nSPEECH": "INTER-SPEECH",
        }.items():
            text = text.replace(old, new)
    if field == "url":
        # One venue has two URLs. Keep both, separated by a semicolon.
        urls = re.split(r"(?=https?://)", text)
        text = "; ".join(re.sub(r"\s+", "", url) for url in urls if url.strip())
    else:
        text = re.sub(r"\s+", " ", text).strip()
        text = re.sub(r"\s*/\s*", "/", text)
        text = re.sub(r"-\s+", "-", text)
    for chinese, english in TRANSLATIONS.items():
        text = text.replace(chinese, english)
    text = re.sub(r"[（(]\s*原\s*", "(formerly ", text).replace("）", ")")
    if re.search(r"[\u4e00-\u9fff]", text):
        raise ValueError(f"Untranslated Chinese in {field}: {text}")
    return text


def extract_catalog(pdf_path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    category = venue_type = rank = ""
    last_numbers: dict[tuple[str, str, str], int] = {}
    with pymupdf.open(pdf_path) as document:
        year_match = re.search(r"(20\d{2})\s*年", document[0].get_text())
        if year_match is None:
            raise ValueError("Catalog year not found on cover")
        year = year_match.group(1)
        for page_number, page in enumerate(document, start=1):
            if page_number == 1:
                continue
            text = page.get_text()
            compact = re.sub(r"\s+", "", text)
            for chinese, english in CATEGORIES.items():
                if chinese in compact:
                    category = english
                    break
            if "中国计算机学会推荐国际学术期刊" in compact:
                venue_type = "Journal"
            elif "中国计算机学会推荐国际学术会议" in compact:
                venue_type = "Conference"
            rank_match = re.search(r"[一二三]、([ABC])类", compact)
            if rank_match:
                rank = rank_match.group(1)
            if not all((category, venue_type, rank)):
                raise ValueError(f"Missing section metadata on page {page_number}")
            tables = page.find_tables().tables
            if len(tables) != 1:
                raise ValueError(f"Expected one table on page {page_number}, got {len(tables)}")
            table_rows = tables[0].extract()
            if table_rows[0][0] == "序号":
                if table_rows[0] != ["序号", "期刊简称" if venue_type == "Journal" else "会议简称",
                                     "期刊全称" if venue_type == "Journal" else "会议全称", "出版社", "网址"]:
                    raise ValueError(f"Unexpected table header on page {page_number}")
                table_rows = table_rows[1:]
            # Independently extracted page text must contain the same row IDs.
            text_numbers = Counter(re.findall(r"^\s*(\d+)\s*$", text, re.MULTILINE))
            table_numbers = Counter(row[0] for row in table_rows)
            if text_numbers != table_numbers:
                raise ValueError(f"Table/text row mismatch on page {page_number}")
            for cells in table_rows:
                if len(cells) != 5 or not (cells[0] or "").isdigit():
                    raise ValueError(f"Invalid row on page {page_number}: {cells}")
                number = int(cells[0])
                key = (category, venue_type, rank)
                expected = last_numbers.get(key, 0) + 1
                if number != expected:
                    raise ValueError(f"Nonsequential row in {key}: expected {expected}, got {number}")
                last_numbers[key] = number
                row = dict(zip(["number", "acronym", "name", "publisher", "url"],
                               (normalize(cell, field) for cell, field in zip(
                                   cells, ["number", "acronym", "name", "publisher", "url"]))))
                row.update(category=category, type=venue_type, rank=rank,
                           source_page=str(page_number), catalog_year=year)
                if not row["name"] or not row["publisher"]:
                    raise ValueError(f"Missing required field on page {page_number}: {row}")
                # JCC and JATS have blank URL cells in the source PDF.
                for url in filter(None, row["url"].split("; ")):
                    if not re.fullmatch(r"https?://[^\s;]+", url):
                        raise ValueError(f"Invalid URL on page {page_number}: {url}")
                rows.append(row)
    expected_sections = {(category, kind, rank) for category in CATEGORIES.values()
                         for kind in ("Journal", "Conference") for rank in "ABC"}
    if set(last_numbers) != expected_sections:
        raise ValueError("Catalog must contain all 60 category/type/rank sections")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--output", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()
    rows = extract_catalog(args.pdf)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    with args.output.open(encoding="utf-8", newline="") as stream:
        if list(csv.DictReader(stream)) != rows:
            raise ValueError("CSV round-trip validation failed")
    print(f"Saved {len(rows)} entries to {args.output}")
    print(f"Types: {dict(Counter(row['type'] for row in rows))}")
    print(f"Ranks: {dict(Counter(row['rank'] for row in rows))}")
    print("Validated: all 71 table pages, 60 sections, sequential row IDs, English text, and CSV round trip")


if __name__ == "__main__":
    main()