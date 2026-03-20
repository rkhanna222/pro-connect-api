def analyze_timecard(df):
    if df.empty:
        return "No data available."

    total_records = len(df)
    total_hours = df["hours_attended"].sum()

    summary = f"""
📊 Staff Time Summary
Total Records: {total_records}
Total Hours: {total_hours}
"""

    return summary