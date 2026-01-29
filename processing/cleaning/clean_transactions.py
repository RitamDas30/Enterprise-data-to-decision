import pandas as pd

def clean_transactions(df):
    df = df.dropna(subset=["customer_id"])
    df["invoice_timestamp"] = pd.to_datetime(df["invoice_date"], errors="coerce")
    df = df[df["quantity"] > 0]
    return df
