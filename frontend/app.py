import streamlit as st
import requests
import pandas as pd
import json

API_BASE = "http://localhost:8000"

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

    col1, col2 = st.columns(2)

    # -------- KPIs --------
    with col1:
        st.subheader("📈 Business KPIs")

        kpi_resp = requests.post(
            f"{API_BASE}/analytics/kpis",
            json={"records": records}
        )

        if kpi_resp.status_code == 200:
            kpis = kpi_resp.json()
            st.metric("Total Revenue", round(kpis["total_revenue"], 2))
            st.metric("Avg Order Value", round(kpis["average_order_value"], 2))
            st.metric("Active Customers", kpis["active_customers"])
        else:
            st.error("Failed to fetch KPIs")

    # -------- Decision Signals --------
    with col2:
        st.subheader("🚨 Decision Signals")

        signal_resp = requests.post(
            f"{API_BASE}/decisions/revenue-drop",
            json={"records": records}
        )

        if signal_resp.status_code == 200:
            signals = signal_resp.json().get("signals", [])
            if signals:
                st.warning("Revenue Drop Detected")
                st.json(signals)
            else:
                st.success("No abnormal revenue drops detected")
        else:
            st.error("Failed to fetch signals")

    st.markdown("---")

    # -------- Preview Data --------
    st.subheader("🔍 Data Preview")
    st.dataframe(pd.DataFrame(records).head(20))

else:
    st.info("Upload a JSON file to explore KPIs and decision signals")
