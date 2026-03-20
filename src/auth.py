import requests
from src.config import BASE_URL, CLIENT_ID, CLIENT_SECRET


def get_access_token():
    url = f"{BASE_URL}/api/v1/authorize"

    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    response = requests.post(
        url,
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=30,
    )
    response.raise_for_status()

    return response.json()["access_token"]