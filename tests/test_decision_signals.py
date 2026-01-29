import pandas as pd
from decision_engine.revenue_signals import detect_revenue_drop

def test_detect_revenue_drop():
    data = pd.Series(
        [1000, 700],
        index=["2024-01-01", "2024-01-02"]
    )

    signals = detect_revenue_drop(data, threshold=0.2)
    assert len(signals) == 1
