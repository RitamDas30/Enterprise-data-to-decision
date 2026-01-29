-- CREATE TABLE clean_transactions (
--     transaction_id TEXT PRIMARY KEY,
--     customer_id TEXT NOT NULL,
--     amount NUMERIC(12,2),
--     transaction_timestamp TIMESTAMP,
--     channel TEXT,
--     processed_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
CREATE TABLE clean_transactions (
    invoice_no TEXT,
    stock_code TEXT,
    description TEXT,
    quantity INTEGER,
    invoice_timestamp TIMESTAMP,
    price NUMERIC(10,2),
    customer_id TEXT,
    country TEXT,
    processed_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
