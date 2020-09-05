import vaex
import dask.dataframe as dd

dfs = [
    dd.read_csv(
        "data/{}.csv".format(country),
        dtype={
            "DISTRICT": "object",
            "POSTCODE": "object",
            "CITY": "object",
            "NUMBER": "object",
        },
    ).assign(country=country)
    for country in ["france", "germany", "italy", "spain", "portugal"]
]

full = dd.concat([f[["LON", "LAT", "STREET", "CITY", "country"]] for f in dfs])

print(full.columns)
full.sample(frac=1.0).to_csv("data/shuffled_with_txt.csv")

df = dd.concat([f[["LON", "LAT", "country"]] for f in dfs])
df.sample(frac=1.0).to_csv("data/large_five.csv")
