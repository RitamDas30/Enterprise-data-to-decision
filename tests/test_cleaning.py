import pandas as pd
from processing.cleaning.clean_transactions import clean_transactions

def test_clean_transactions_removes_null_customers_and_invalid_rows():
    df = pd.DataFrame({
        "customer_id": ["c1", None],
        "quantity": [2, 3],
        "price": [10.0, 20.0],
        "invoice_date": ["2024-01-01", "2024-01-02"]
    })

    cleaned = clean_transactions(df)

    # Null customers removed
    assert cleaned["customer_id"].isnull().sum() == 0

    # Business rules enforced
    assert (cleaned["quantity"] > 0).all()
    assert (cleaned["price"] > 0).all()
