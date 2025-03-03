# Postman Collection Instructions

## Initial Setup

1. **Import the collection**: 
   - Open Postman
   - Click "Import" (in the upper left corner)
   - Select the `recurly_api_collection.json` file

2. **Configure environment variables**:
   - Create a new environment in Postman (gear icon in the upper right corner)
   - Add the following variables:
     - `api_key`: Your Recurly API key (unencoded)
     - `base_url`: https://v3.recurly.com 
     - `account_id`: The ID of the account you want to use for testing
     - `subscription_id`: (optional) Subscription ID for testing

## Key Features of this Collection

1. **Automatic API Key Encoding**:
   - The collection includes a pre-request script that automatically encodes the API Key in Base64
   - You don't need to manually encode the API Key

2. **Automatic Generation of Unique Codes**:
   - For account creation operations, `{{$timestamp}}` is used to generate unique values
   - This prevents errors from trying to create accounts with the same code

3. **Optimized Payloads**:
   - Request bodies have been updated to include all required fields
   - Required fields such as postal_code in addresses are included

## Troubleshooting

If you encounter errors when executing requests, check:

1. **Correct API Key**: 
   - Make sure the API Key in the environment variables is correct
   - Don't include "Basic " in the API Key, this is added automatically

2. **422 Errors**:
   - Check the response to see which fields are missing or incorrect
   - The collection already includes the minimum required fields for each operation

3. **Postman Console**:
   - Open the Postman console (View > Show Postman Console) to see debugging messages
   - Verify that the "API key encoded successfully" message appears 