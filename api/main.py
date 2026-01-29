from fastapi import FastAPI
import pandas as pd
from analytics.kpis.revenue_kpis import compute_revenue_kpis

app = FastAPI(title="Enterprise Data-to-Decision API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/kpis")
def calculate_kpis(records: list[dict]):
    df = pd.DataFrame(records)
    return compute_revenue_kpis(df)
