"""Mastering Polars Data Frame: What You Need to Know from Chapter #1"""

import polars as pl
s = pl.Series("a", [1, 2, 3, 4, 5])


data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["a", "b", "c", "d", "e"],
    "score": [4, 5, 6, 7, 8],
}

df = pl.DataFrame(data)

##Write the dataset to a csv / parquet / json & manu other output formats.
df.write_csv('dataset.csv')

## Selectoin Feature enables users to select the desired columns
print(df.select(['id','name']))
## Filter option to filter the dataset.
print(df.filter(pl.col('score')<5))
## To Show the first 2 rows of the dataset.
print(df.head(2))
## To Show the last 2 rows of the dataset.
print(df.tail(2))
## To Show the random  2 rows of the dataset to create  a sample.
print(df.sample(2))
#Describes the dataset column and its metrics.
print(df.describe())
#Explains the schema of the dataframe.
print(df.schema)
#Explain the Column names of the Data Frame into a list.
print(df.columns)

# """
# --- > scan_csv is a function to laziliy scan the dataset and perform operations on it instead of loading the entire dataframe into the system memory.
# --- > filter function is to filter the rows from a condition
# --- > group_by is used to agg the data over a categorical column and use agg functions like sum(),mean(),max(),min().
# """

q = (
    pl.scan_csv("dataset.csv")
    .filter(pl.col("score") > 5)
    .group_by("name")
    .agg(pl.col("age").mean())
)

df = q.collect()
