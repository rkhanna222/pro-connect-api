import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("PROCARE_BASE_URL")
CLIENT_ID = os.getenv("PROCARE_CLIENT_ID")
CLIENT_SECRET = os.getenv("PROCARE_CLIENT_SECRET")
SCHOOL_ID = os.getenv("PROCARE_SCHOOL_ID")