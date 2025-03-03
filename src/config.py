from dotenv import load_dotenv
import os
import base64

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
ACCOUNT_ID = os.getenv("ACCOUNT_ID")

# Codificar la API Key en Base64
ENCODED_API_KEY = base64.b64encode(API_KEY.encode()).decode()

HEADERS = {
    "Authorization": f"Basic {ENCODED_API_KEY}",
    "Accept": "application/vnd.recurly.v2021-02-25",
    "Content-Type": "application/json"
}
