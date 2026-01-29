from processing.quality.quality_rules import (
    validate_not_null,
    validate_positive_values,
    validate_date_parsing
)

def enforce_clean_contract(df):
    validate_not_null(df, ["customer_id", "invoice_timestamp"])
    validate_positive_values(df, "quantity")
    validate_positive_values(df, "price")
    validate_date_parsing(df, "invoice_timestamp")
    return df

def enforce_curated_contract(df):
    validate_not_null(df, ["customer_id", "transaction_date"])
    validate_positive_values(df, "total_amount")
    return df
