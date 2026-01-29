-- CREATE TABLE raw_transactions (
--     transaction_id TEXT,
--     customer_id TEXT,
--     amount TEXT,
--     timestamp TEXT,
--     channel TEXT,
--     ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
CREATE TABLE raw_transactions (
    invoice_no TEXT,
    stock_code TEXT,
    description TEXT,
    quantity INTEGER,
    invoice_date TEXT,
    price NUMERIC,
    customer_id TEXT,
    country TEXT,
    ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
