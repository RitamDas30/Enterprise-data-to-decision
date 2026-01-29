def daily_revenue_trend(df):
    return (
        df.groupby("transaction_date")["total_amount"]
        .sum()
        .sort_index()
    )
