# import pandas as pd

# def clean_transactions(df):
#     df = df.dropna(subset=["customer_id"])
#     df["invoice_timestamp"] = pd.to_datetime(df["invoice_date"], errors="coerce")
#     df = df[df["quantity"] > 0]
#     return df
import pandas as pd

def clean_transactions(df):
    # Drop rows with missing customer ID
    df = df.dropna(subset=["customer_id"])

    # Parse invoice date
    df["invoice_timestamp"] = pd.to_datetime(
        df["invoice_date"], errors="coerce"
    )

    # Remove rows with invalid dates
    df = df.dropna(subset=["invoice_timestamp"])

    # Remove cancellations / returns
    df = df[df["quantity"] > 0]
    df = df[df["price"] > 0]

    return df
