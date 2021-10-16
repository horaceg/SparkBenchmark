import numpy as np
import vaex

# dfs = []
# for country in ["france", "germany", "italy", "spain", "portugal"]:
#     df = vaex.open(
#         "data/{}.csv.hdf5".format(country),
#         #  convert=True,
#         #  dtype={
#         #      "DISTRICT": "object",
#         #      "POSTCODE": "object",
#         #      "CITY": "object",
#         #      "NUMBER": "object",
#         #  },
#     )
#     df["country"] = np.repeat([country], df.shape[0])
#     df.export(f"data/{country}.hdf5")
#     # dfs.append(df)

# full = vaex.concat([f[["LON", "LAT", "STREET", "CITY", "country"]] for f in dfs])

full = vaex.open("data/*.hdf5")[["LON", "LAT", "country"]]

print(full.columns)
print(full.shape[0])
# full.sample(frac=1.).export("data/shuffled_with_txt.csv")

# df = vaex.concat([f[["LON", "LAT", "country"]] for f in dfs])
full.sample(frac=1.0).export("data/large_five.csv")