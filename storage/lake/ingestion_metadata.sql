CREATE TABLE ingestion_metadata (
    ingestion_id TEXT PRIMARY KEY,
    source_name TEXT,
    record_count INTEGER,
    ingestion_status TEXT,
    ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
