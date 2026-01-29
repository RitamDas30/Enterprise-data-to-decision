from fastapi import APIRouter
import pandas as pd
from api.schemas import TransactionsRequest
from analytics.kpis.revenue_kpis import compute_revenue_kpis

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.post("/kpis")
def calculate_kpis(payload: TransactionsRequest):
    df = pd.DataFrame([r.dict() for r in payload.records])
    return compute_revenue_kpis(df)
