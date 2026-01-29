def curate_transactions(df):
    df["transaction_date"] = df["invoice_timestamp"].dt.date
    df["total_amount"] = df["quantity"] * df["price"]
    return df[["invoice_no", "customer_id", "transaction_date", "total_amount", "country"]]
