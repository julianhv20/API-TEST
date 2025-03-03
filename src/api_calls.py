import requests
import json
import logging
from src.config import BASE_URL, HEADERS, ACCOUNT_ID
import time

# Log configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 1️⃣ Get account information
def get_account_info():
    url = f"{BASE_URL}/accounts/{ACCOUNT_ID}"
    logging.info(f"Fetching account info for {ACCOUNT_ID}")
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raises an exception in case of HTTP error

        logging.info("Account info retrieved successfully")
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        return {"error": f"HTTP error: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error: {req_err}")
        return {"error": f"Request error: {req_err}"}

# 2️⃣ Update user address
def update_account_address():
    url = f"{BASE_URL}/accounts/{ACCOUNT_ID}"
    payload = {
        "first_name": "Julian",
        "last_name": "Hincapié",
        "address": {
            "street1": "Calle 123",
            "city": "Medellín",
            "region": "Antioquia",
            "country": "CO"
        }
    }

    try:
        response = requests.put(url, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()

        logging.info("Address updated successfully")
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        return {"error": f"HTTP error: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error: {req_err}")
        return {"error": f"Request error: {req_err}"}

# 3️⃣ Create a new account with subscription
def create_account_and_subscribe():
    url = f"{BASE_URL}/purchases"
    
    # Generate a unique code based on timestamp to avoid duplicates
    unique_code = f"new_user_{int(time.time())}"
    
    # Simplified payload to avoid disallowed parameters
    payload = {
        "currency": "COP",
        "account": {
            "code": unique_code,
            "first_name": "John",
            "last_name": "Doe",
            "email": f"{unique_code}@example.com",
            "billing_info": {
                "address": {
                    "street1": "Avenida Principal 123",
                    "city": "Medellín",
                    "region": "Antioquia",
                    "country": "CO",
                    "postal_code": "050001"  # Added postal code (required)
                },
                "number": "4111111111111111",  # Fictional card number (required)
                "month": "12",                 # Expiration month (required)
                "year": "2030"                 # Expiration year (required)
            }
        },
        "subscriptions": [
            {
                "plan_code": "test_plan_001",
                "quantity": 1
            }
        ]
    }

    logging.info(f"Creating account with code: {unique_code}")
    logging.info(f"Payload: {json.dumps(payload)}")

    try:
        response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
        
        # Log response for diagnostics
        logging.info(f"Response (status {response.status_code}): {response.text}")
        
        response.raise_for_status()

        logging.info("New account and subscription created successfully")
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        return {"error": f"HTTP error: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error: {req_err}")
        return {"error": f"Request error: {req_err}"}

# 4️⃣ Get available plans
def get_available_plans():
    url = f"{BASE_URL}/plans"
    logging.info(f"Fetching available plans from: {url}")
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        
        logging.info("Plans retrieved successfully")
        return response.json()
        
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        return {"error": f"HTTP error: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error: {req_err}")
        return {"error": f"Request error: {req_err}"}

# 5️⃣ Create a new subscription
def create_subscription(account_code, plan_code, currency="USD", additional_params=None):
    """
    Creates a new subscription for an existing account.
    
    Args:
        account_code (str): Code of the account to which the subscription will be assigned
        plan_code (str): Code of the plan to subscribe to
        currency (str): Currency for the subscription (default: USD)
        additional_params (dict): Optional additional parameters for creation
        
    Returns:
        dict: API response with information about the created subscription
    """
    url = f"{BASE_URL}/subscriptions"
    
    # Basic payload with required fields
    payload = {
        "plan_code": plan_code,
        "currency": currency,
        "account": {
            "code": account_code
        }
    }
    
    # If there are additional parameters, add them to the payload
    if additional_params and isinstance(additional_params, dict):
        # For top-level parameters (not inside account)
        for key, value in additional_params.items():
            if key != "account":
                payload[key] = value
            else:
                # For parameters inside account, merge them
                for acc_key, acc_value in additional_params["account"].items():
                    payload["account"][acc_key] = acc_value
    
    logging.info(f"Creating subscription for account: {account_code} with plan: {plan_code}")
    logging.info(f"Payload: {json.dumps(payload)}")
    
    try:
        response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
        
        # Log response for diagnostics
        logging.info(f"Response (status {response.status_code}): {response.text}")
        
        response.raise_for_status()
        
        logging.info("Subscription created successfully")
        return response.json()
        
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        return {"error": f"HTTP error: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error: {req_err}")
        return {"error": f"Request error: {req_err}"}

# Run manual tests
if __name__ == "__main__":
    print("Account Info:", get_account_info())
    print("Updating Address:", update_account_address())
    print("New Subscription:", create_account_and_subscribe())
    print("Available Plans:", get_available_plans())
    # We don't execute the new create_subscription function here because it needs specific parameters
