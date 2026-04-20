import pandas as pd

df = pd.read_csv("match_results_tour4.csv")

print("Dataset preview:")
print(df.head())

print("\nTotal matches:", len(df))
