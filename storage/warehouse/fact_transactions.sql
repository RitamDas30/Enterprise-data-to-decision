CREATE TABLE fact_transactions (
    transaction_id TEXT PRIMARY KEY,
    customer_id TEXT,
    transaction_date DATE,
    amount NUMERIC(12,2),
    channel TEXT,
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
);
