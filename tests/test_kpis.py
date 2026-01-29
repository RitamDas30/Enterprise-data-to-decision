import pandas as pd
from analytics.kpis.revenue_kpis import compute_revenue_kpis

def test_compute_revenue_kpis():
    df = pd.DataFrame({
        "customer_id": ["c1", "c2"],
        "total_amount": [100.0, 200.0]
    })

    kpis = compute_revenue_kpis(df)

    assert kpis["total_revenue"] == 300.0
    assert kpis["active_customers"] == 2
