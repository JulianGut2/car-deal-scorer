import pandas as pd

def clean_data(df):
    df = df[(df["price"] > 1000) & (df["price"] < 150000)] 
    df = df[(df["year"] > 1990) & (df["year"] < 2023)]
    df = df.dropna(subset = ["manufacturer", "model", "odometer", "fuel", "transmission"])
    df = df[["price", "year", "manufacturer", "model", "odometer", "condition", "fuel", "transmission", "drive", "type"]]
    df["condition"] = df["condition"].fillna("unknown")
    df["drive"] = df["drive"].fillna("unknown")
    df["type"] = df["type"].fillna("unknown")

    return df