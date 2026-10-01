import argparse
import pandas as pd

def parse_args(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--no-past-deadline",
        action="store_true",
        help="Filter out conferences with passed deadlines",
    )
    parser.add_argument("--category", type=str, nargs="+")
    parser.add_argument("--acronym", type=str)
    parser.add_argument("--name", type=str)
    parser.add_argument("--month", type=str, nargs="+")
    parser.add_argument("--rank", type=str, nargs="+")
    args = parser.parse_args(argv)
    return args

def group_conference_by_month(
    df1: pd.DataFrame,
    date_format: str = "%d/%m/%y",
) -> pd.DataFrame:
    df2 = df1.copy()

    # categorize the conferences by month
    # column "Abstract Deadline" or "Paper Deadline"
    # is used to determine the month of the conference
    df2["month"] = pd.to_datetime(
        df2["abstract deadline"].fillna(df2["paper deadline"]), 
        errors="coerce",
        format=date_format,
    ).dt.month
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    df2["month"] = pd.Categorical(
        df2["month"].map(dict(enumerate(months, start=1))),
        categories=months,
        ordered=True
    )
    return df2

def get_conferences(
    df1: pd.DataFrame,
    no_past_deadline: bool = True,
    category: str | list[str] | None = None,
    acronym: str | None = None,
    name: str | None = None,
    month: str | list[str] | None = None,
    rank: str | list[str] | None = None,
) -> pd.DataFrame:
    df2 = df1.copy()
    if no_past_deadline:
        df2 = df2[df2["paper deadline"] >= pd.Timestamp.now()]
    if category:
        if isinstance(category, str):
            category = [category]
        df2 = df2[df2["ccf_category"].isin(category)]
    if acronym:
        df2 = df2[df2["acronym"] == acronym]
    if name:
        df2 = df2[df2["name"].str.contains(name, case=False, na=False)]
    if month:
        if isinstance(rank, str):
            month = [month]
        df2 = df2[df2["month"].isin(month)]
    if rank:
        if isinstance(rank, str):
            rank = [rank]
        df2 = df2[df2["ccf rank"].isin(rank)]
    return df2