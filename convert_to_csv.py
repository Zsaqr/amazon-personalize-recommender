import pandas as pd

df = pd.read_csv("u.data", sep="\t", names=["userId", "itemId", "rating", "timestamp"])
df.to_csv("interactions.csv", index=False)