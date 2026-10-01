# %%

import pandas as pd
import sys

from project_common.utils import (
    PROJECT_ROOT,
)
from conference_by_month.src.utils import (
    group_conference_by_month,
    get_conferences,
    parse_args,
)

ARGV = (
    [
        "--rank=A",
    ]
    if "ipykernel" in sys.modules
    else None
)
args = parse_args(ARGV)

# %%

df1 = pd.read_csv(
    PROJECT_ROOT / "data" / "Conference-Deadline.csv",
    sep=";",
)
df1["abstract deadline"] = pd.to_datetime(
    df1["abstract deadline"],
    errors="coerce",
    format="%d/%m/%y",
)
df1["paper deadline"] = pd.to_datetime(
    df1["paper deadline"],
    errors="coerce",
    format="%d/%m/%y",
)

print("Top 5 rows of the dataset:")
print(df1.head().to_string(index=False))

# %%

df2 = group_conference_by_month(df1)

df2 = get_conferences(
    df2,
    no_past_deadline=args.no_past_deadline,
    category=args.category,
    acronym=args.acronym,
    name=args.name,
    month=args.month,
    rank=args.rank,
)
df2 = df2.sort_values(
    by=["paper deadline"],
    ascending=[True]
)

print("Filtered conferences:")
columns = [
    "ccf_category",
    "ccf rank",
    "acronym",
    "track",
    "abstract deadline",
    "paper deadline",
    "link",
]
print(df2[columns].to_string(index=False))

# %%
