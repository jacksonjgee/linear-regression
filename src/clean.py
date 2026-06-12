import pandas as pd

def load_data():
    return pd.read_csv("data/USA Housing Dataset.csv")

def clean_data(df):
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df["days_since_first_sale"] = (df["date"] - df["date"].min()).dt.days

    df = df.drop("date", axis=1)

    df_clean = df.select_dtypes(exclude=["object"])

    return df_clean