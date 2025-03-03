#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import datetime

def save_api_response(response, operation_name, directory="responses"):
    """
    Saves an API response to a JSON file.
    
    Args:
        response (dict): The API response to save
        operation_name (str): Name of the operation (e.g. 'create_account')
        directory (str): Directory where to save the responses
        
    Returns:
        str: Path to the created file
    """
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Create filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{directory}/{operation_name}_{timestamp}.json"
    
    # Save response as JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(response, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Response from '{operation_name}' saved at: {filename}")
    return filename

def log_operation(operation_name, result, log_file="api_operations.log"):
    """
    Logs the result of an operation to a log file.
    
    Args:
        operation_name (str): Name of the operation
        result (dict): Result of the operation
        log_file (str): Path to the log file
    """
    # Create log directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Get operation status
    success = "✅ SUCCESS" if isinstance(result, dict) and not result.get('error') else "❌ ERROR"
    
    # Format log message
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {success} | {operation_name} | "
    
    if isinstance(result, dict) and result.get('error'):
        log_message += f"Error: {result.get('error')}"
    else:
        # Extract relevant information based on operation type
        if "account" in result:
            log_message += f"Account: {result.get('account', {}).get('code')}"
        elif "id" in result:
            log_message += f"ID: {result.get('id')}"
        else:
            log_message += "Completed successfully"
    
    # Add message to log file
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_message + "\n")