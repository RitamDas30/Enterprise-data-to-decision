-- CREATE TABLE curated_transactions (
--     transaction_id TEXT PRIMARY KEY,
--     customer_id TEXT,
--     transaction_date DATE,
--     amount NUMERIC(12,2),
--     channel TEXT
-- );
CREATE TABLE curated_transactions (
    invoice_no TEXT,
    customer_id TEXT,
    transaction_date DATE,
    total_amount NUMERIC(12,2),
    country TEXT
);
