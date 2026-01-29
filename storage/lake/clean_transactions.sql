CREATE TABLE clean_transactions (
    transaction_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    amount NUMERIC(12,2),
    transaction_timestamp TIMESTAMP,
    channel TEXT,
    processed_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
