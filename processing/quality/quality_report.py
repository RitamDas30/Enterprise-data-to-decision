def generate_quality_report(df):
    return {
        "record_count": len(df),
        "null_customer_ids": df["customer_id"].isnull().sum(),
        "min_transaction_value": df["total_amount"].min(),
        "max_transaction_value": df["total_amount"].max()
    }
