import streamlit as st
import pandas as pd
import json

import sys
from pathlib import Path

# Add project root to PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))


from analytics.kpis.revenue_kpis import compute_revenue_kpis
from analytics.statistics.daily_trends import daily_revenue_trend
from decision_engine.revenue_signals import detect_revenue_drop

st.set_page_config(
    page_title="Enterprise Data-to-Decision Platform",
    layout="wide"
)

st.title(" Enterprise Data-to-Decision Platform")
st.caption("From raw data to business decisions")

st.markdown("---")

# ---------------- Sidebar ----------------
st.sidebar.header("Controls")
uploaded = st.sidebar.file_uploader(
    "Upload Transactions (JSON)",
    type=["json"]
)

st.sidebar.markdown(
    """
    **Expected fields per record**
    - customer_id  
    - total_amount  
    - country  
    - transaction_date  
    """
)

# ---------------- Main ----------------
if uploaded:
    records = json.load(uploaded)
    df = pd.DataFrame(records)

    col1, col2 = st.columns(2)

    # -------- KPIs --------
    with col1:
        st.subheader(" Business KPIs")

        kpis = compute_revenue_kpis(df)

        st.metric("Total Revenue", round(kpis["total_revenue"], 2))
        st.metric("Avg Order Value", round(kpis["average_order_value"], 2))
        st.metric("Active Customers", kpis["active_customers"])

    # -------- Decision Signals --------
#     with col2:
#         st.subheader(" Decision Signals")

#         trend_df = daily_revenue_trend(df)
#         signals = detect_revenue_drop(trend_df)

#         if signals.get("signals"):
#             st.warning("Revenue Drop Detected")
#             st.json(signals["signals"])
#         else:
#             st.success("No abnormal revenue drops detected")

#     st.markdown("---")

#     # -------- Preview Data --------
#     st.subheader(" Data Preview")
#     st.dataframe(df.head(20))

# else:
#     st.info("Upload a JSON file to explore KPIs and decision signals")

# -------- Decision Signals --------
with col2:
    st.subheader(" Decision Signals")

    trend_df = daily_revenue_trend(df)
    signals = detect_revenue_drop(trend_df)

    if signals:
        st.warning("Revenue Drop Detected")
        st.json(signals)
    else:
        st.success("No abnormal revenue drops detected")

