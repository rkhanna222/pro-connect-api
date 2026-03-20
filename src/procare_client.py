import requests
from src.auth import get_access_token
from src.config import BASE_URL, SCHOOL_ID


class ProcareClient:
    def __init__(self):
        self.token = get_access_token()

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
        }

    def get_timecard_page(self, date_from, date_to, page=1, per_page=50):
        url = f"{BASE_URL}/api/v1/staff/timecard"

        params = {
            "school_id": SCHOOL_ID,
            "filters[timecard][date_from]": date_from,
            "filters[timecard][date_to]": date_to,
            "page": page,
            "per_page": per_page,
        }

        response = requests.get(
            url,
            headers=self.get_headers(),
            params=params,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()

    def get_all_timecards(self, date_from, date_to):
        all_rows = []
        page = 1

        while True:
            result = self.get_timecard_page(date_from, date_to, page)
            rows = result.get("timecard", [])
            total = result.get("total", 0)

            if not rows:
                break

            all_rows.extend(rows)
            print(f"Page {page}: {len(all_rows)}/{total}")

            if len(all_rows) >= total:
                break

            page += 1

        return all_rows