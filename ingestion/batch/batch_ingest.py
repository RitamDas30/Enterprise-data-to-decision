import pandas as pd
from datetime import datetime
import uuid

REQUIRED_COLUMNS = {
    "Invoice",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "Price",
    "Customer ID",
    "Country"
}

def generate_ingestion_id():
    return str(uuid.uuid4())

def read_source(path):
    return pd.read_csv(path, encoding="ISO-8859-1")

def validate_schema(df):
    if not REQUIRED_COLUMNS.issubset(df.columns):
        raise ValueError("Incoming file schema does not match source contract")

def prepare_raw(df):
    df = df.rename(columns={
        "Invoice": "invoice_no",
        "StockCode": "stock_code",
        "Description": "description",
        "Quantity": "quantity",
        "InvoiceDate": "invoice_date",
        "Price": "price",
        "Customer ID": "customer_id",
        "Country": "country"
    })
    df["ingestion_time"] = datetime.utcnow()
    return df

def run_ingestion(file_path):
    ingestion_id = generate_ingestion_id()
    df = read_source(file_path)
    validate_schema(df)
    raw_df = prepare_raw(df)

    print("Ingestion ID:", ingestion_id)
    print("Records:", len(raw_df))
    print(raw_df.head())

    # Later: insert into raw_transactions
    # Later: insert into ingestion_metadata

if __name__ == "__main__":
    run_ingestion(
        "ingestion/batch/sources/online_retail/online_retail_II.csv"
    )
