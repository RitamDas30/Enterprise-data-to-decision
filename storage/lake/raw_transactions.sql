CREATE TABLE raw_transactions (
    transaction_id TEXT,
    customer_id TEXT,
    amount TEXT,
    timestamp TEXT,
    channel TEXT,
    ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
