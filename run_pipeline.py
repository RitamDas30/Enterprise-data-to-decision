import pandas as pd

from ingestion.batch.batch_ingest import prepare_raw
from processing.pipeline_controller import run_processing_pipeline
from processing.quality.quality_report import generate_quality_report

from analytics.kpis.revenue_kpis import compute_revenue_kpis
from analytics.persist_analytics import persist_kpis


SOURCE_PATH = "ingestion/batch/sources/online_retail/online_retail_II.csv"

def main():
    print("Loading source data...")
    df = pd.read_csv(SOURCE_PATH, encoding="ISO-8859-1")

    print("Preparing raw layer...")
    raw_df = prepare_raw(df)

    print("Running processing pipeline...")
    curated_df = run_processing_pipeline(raw_df)

    print("Generating quality report...")
    report = generate_quality_report(curated_df)

    print("\nPIPELINE EXECUTED SUCCESSFULLY")
    print("Quality Report:")

    print("Computing KPIs...")
    kpis = compute_revenue_kpis(curated_df)
    print("KPIs:", kpis)

    print("Persisting KPIs...")
    path = persist_kpis(kpis)
    print(f"KPIs persisted at: {path}")




    for k, v in report.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
