def detect_revenue_drop(daily_revenue, threshold=0.2):
    signals = []

    previous = None
    for date, revenue in daily_revenue.items():
        if previous is not None:
            drop = (previous - revenue) / previous
            if drop > threshold:
                signals.append({
                    "date": date,
                    "type": "REVENUE_DROP",
                    "drop_percentage": round(drop * 100, 2)
                })
        previous = revenue

    return signals
