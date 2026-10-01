import argparse
import pandas as pd

def parse_args(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--acronym", type=str)
    parser.add_argument("--name", type=str)
    parser.add_argument("--category", type=str)
    parser.add_argument("--rank", type=str)
    parser.add_argument("--type", type=str)
    return parser.parse_args(argv)

def get_conference_journal(
    df1: pd.DataFrame,
    acronym: str | None = None,
    name: str | None = None,
    category: str | None = None,
    rank: str | None = None,
    type: str | None = None,
):
    df2 = df1.copy()
    if acronym:
        df2 = df2[df2["acronym"].str.contains(acronym, case=False, na=False)]
    if name:
        df2 = df2[df2["name"].str.contains(name, case=False, na=False)]
    if category:
        df2 = df2[df2["category"] == category]
    if rank:
        df2 = df2[df2["rank"] == rank]
    if type:
        df2 = df2[df2["type"] == type]
    return df2