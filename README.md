# Recurly API  

Professional Services Engineering - Interview Take Home Assignment

## 📌 Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/julianhv20/API-TEST.git
cd API-TEST
pip install -r requirements.txt
```

## 🔑 Configuration

Create a `.env` file in the root directory with the following content:

```
API_KEY=your_api_key_here
BASE_URL=https://v3.recurly.com
ACCOUNT_ID=your_account_id
```

## 🚀 Available Features

The project includes several API functions for Recurly:

1. **Account Management**
   - Get account information
   - Update account details (name, address)
   - Create new accounts

2. **Subscription Management**
   - Create subscriptions
   - Create purchases with subscriptions

3. **Testing and Logging**
   - Comprehensive test suite
   - Detailed logging of API responses
   - Saving responses to JSON files for analysis

## 💻 Usage Examples

### Running Tests

```bash
python run_tests_with_logs.py
```

### Get Account Information

```python
from src.api_calls import get_account_info

result = get_account_info()
print(result)
```

### Create Account with Subscription

```python
from src.api_calls import create_account_and_subscribe

result = create_account_and_subscribe()
print(result)
```

## 📊 Testing Tools

- **log_and_test.py**: Runs tests and saves both logs and detailed JSON responses

## 🔌 Postman Collection

The project includes a Postman collection for testing the Recurly API directly:

- **Collection Path**: `postman_collection/recurly_api_collection.json`
- **Instructions**: See `postman_collection/INSTRUCTIONS.md` for setup details

Key features of the Postman collection:

- Automatic Base64 encoding of API key
- Pre-configured requests for all major API endpoints
- Environment variable management for easy configuration
- Request validation tests

## 📚 Documentation

For more information about the Recurly API, visit the [official Recurly API documentation](https://developers.recurly.com/api/v2021-02-25/).

## 📝 Notes

- This project uses the Recurly API v2021-02-25.
- All sensitive information should be stored in the `.env` file which is ignored by git.
- Credit card information used in tests is fictional and for testing purposes only.
