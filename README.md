# ProConnect API Automation

Automates fetching staff timecard data from Procare Connect API and exports it to Excel.

---

## 🚀 Features

- Authenticate using client credentials
- Fetch staff timecard data (paginated)
- Export to Excel
- Basic summary analysis

---

## ⚙️ Setup

```bash
git clone https://github.com/rkhanna222/pro-connect-api.git
cd pro-connect-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Create a .env file:
PROCARE_BASE_URL=https://your-tenant.procareconnect.com
PROCARE_CLIENT_ID=your_client_id
PROCARE_CLIENT_SECRET=your_client_secret
PROCARE_SCHOOL_ID=your_school_id
