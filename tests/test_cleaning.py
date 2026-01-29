import pandas as pd
from processing.cleaning.clean_transactions import clean_transactions

def test_clean_transactions_removes_null_customers():
    df = pd.DataFrame({
        "customer_id": ["c1", None],
        "quantity": [2, 3],
        "invoice_date": ["2024-01-01", "2024-01-02"]
    })

    cleaned = clean_transactions(df)
    assert cleaned["customer_id"].isnull().sum() == 0
