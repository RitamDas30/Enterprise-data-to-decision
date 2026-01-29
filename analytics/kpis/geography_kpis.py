def revenue_by_country(df):
    return (
        df.groupby("country")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )
