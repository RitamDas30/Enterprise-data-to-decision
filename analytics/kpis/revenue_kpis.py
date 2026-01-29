def compute_revenue_kpis(df):
    total_revenue = df["total_amount"].sum()
    aov = df["total_amount"].mean()
    active_customers = df["customer_id"].nunique()

    return {
        "total_revenue": total_revenue,
        "average_order_value": aov,
        "active_customers": active_customers
    }
