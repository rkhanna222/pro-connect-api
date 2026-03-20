import pandas as pd
from src.procare_client import ProcareClient


def fetch_and_save(date_from, date_to):
    client = ProcareClient()

    data = client.get_all_timecards(date_from, date_to)

    df = pd.DataFrame(data)

    file_path = f"data/timecard_{date_from}_to_{date_to}.xlsx"
    df.to_excel(file_path, index=False)

    print(f"Saved {len(df)} records to {file_path}")

    return df