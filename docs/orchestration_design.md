## Pipeline Orchestration Design

The data pipeline follows DAG-based orchestration principles:
- Ingestion → Cleaning → Quality → Curation
- Each step is independently retryable
- Failures prevent downstream execution

This design aligns with Airflow-style orchestration without introducing operational overhead.
