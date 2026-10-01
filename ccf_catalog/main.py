# %%

import pandas as pd
import sys

from project_common.utils import (
    PROJECT_ROOT,
)
from ccf_catalog.src.utils import (
    get_conference_journal,
    parse_args,
)

# %%

ARGV = (
    [
        "--category=Artificial Intelligence",
        "--rank=A",
    ]
    if "ipykernel" in sys.modules
    else None
)

args = parse_args(ARGV)

# %%

df1 = pd.read_csv(
    PROJECT_ROOT / "data" / "Conferences-Journals-CCF.csv",
    sep=";",
)
df1["source_page"] = df1["source_page"].astype("Int64")
df1["catalog_year"] = df1["catalog_year"].astype("Int64")

print("Top 5 rows of the dataset:")
print(df1.head().to_string(index=False))

print("Categories:")
print(df1["category"].unique())

# %%

df2 = get_conference_journal(
    df1,
    acronym=args.acronym,
    name=args.name,
    category=args.category,
    rank=args.rank,
    type=args.type,
)

print("Filtered conferences/journals:")
print(
    df2[
        [
            "type", 
            "rank", 
            "acronym", 
            "name", 
            "publisher", 
            "url", 
            "catalog_year",
        ]
    ]
    .to_string(index=False)
)

# %%
