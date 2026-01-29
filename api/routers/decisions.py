from fastapi import APIRouter
import pandas as pd

from api.schemas import TransactionsRequest
from analytics.statistics.daily_trends import daily_revenue_trend
from decision_engine.revenue_signals import detect_revenue_drop

router = APIRouter(prefix="/decisions", tags=["Decision Signals"])

@router.post("/revenue-drop")
def revenue_drop_signal(payload: TransactionsRequest):
    """
    Detect significant revenue drops based on daily trends.
    """
    df = pd.DataFrame([r.dict() for r in payload.records])

    # Ensure required columns exist
    required_cols = {"transaction_date", "total_amount"}
    if not required_cols.issubset(df.columns):
        return {"error": "Missing required fields"}

    daily_trend = daily_revenue_trend(df)
    signals = detect_revenue_drop(daily_trend)

    return {
        "signal_type": "REVENUE_DROP",
        "signals": signals
    }
