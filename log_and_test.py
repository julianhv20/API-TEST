#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
from src.api_calls import (
    get_account_info, 
    update_account_address, 
    create_account_and_subscribe,
    get_available_plans
)
from src.utils import save_api_response, log_operation

def run_tests_with_logging():
    """Runs API tests and saves both logs and detailed JSON responses"""
    
    # Configure directories
    responses_dir = "responses"
    logs_dir = "logs"
    
    # Create directories if they don't exist
    for directory in [responses_dir, logs_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Log file for operations
    operations_log = f"{logs_dir}/operations.log"
    
    print("=======================================")
    print("🚀 STARTING RECURLY API TESTS...")
    print("=======================================")
    
    # 1. Get account information
    print("\n Getting account information...")
    result = get_account_info()
    save_api_response(result, "get_account_info", responses_dir)
    log_operation("get_account_info", result, operations_log)
    
    # 2. Update address
    print("\n Updating account address...")
    result = update_account_address()
    save_api_response(result, "update_account_address", responses_dir)
    log_operation("update_account_address", result, operations_log)
    
    # 3. Create account with subscription
    print("\n Creating account with subscription...")
    result = create_account_and_subscribe()
    save_api_response(result, "create_account_and_subscribe", responses_dir)
    log_operation("create_account_and_subscribe", result, operations_log)

    # 4. Get Available Plans
    print("\n Getting available plans...")
    result = get_available_plans()
    save_api_response(result, "get_available_plans", responses_dir)
    log_operation("get_available_plans", result, operations_log)
    
    
    print("\n=======================================")
    print("✅ TESTS COMPLETED")
    print("=======================================")
    print(f"📁 Responses saved at: {responses_dir}/")
    print(f"📄 Operations log: {operations_log}")

if __name__ == "__main__":
    run_tests_with_logging() 