#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.api_calls import create_subscription, get_account_info, get_available_plans
import json

def main():
    """
    Script to demonstrate the creation of a new subscription using the Recurly API.
    """
    print("=" * 50)
    print("RECURLY SUBSCRIPTION CREATION EXAMPLE")
    print("=" * 50)
    
    # 1. First get the account information to ensure we have a valid account
    print("\n1. Retrieving account information...")
    account_info = get_account_info()
    
    if "error" in account_info:
        print(f"❌ Error getting account info: {account_info['error']}")
        return
    
    account_code = account_info.get("code")
    print(f"✅ Account found: {account_code}")
    
    # 2. Get available plans to choose one
    print("\n2. Fetching available plans...")
    plans_response = get_available_plans()
    
    if "error" in plans_response:
        print(f"❌ Error getting plans: {plans_response['error']}")
        return
    
    # Extract plan codes from the response
    available_plans = []
    if "data" in plans_response:
        available_plans = [(plan.get("code"), plan.get("name")) for plan in plans_response.get("data", [])]
    
    if not available_plans:
        print("❌ No plans available. Please create a plan first.")
        return
    
    # Display available plans
    print("Available plans:")
    for i, (code, name) in enumerate(available_plans):
        print(f"  {i+1}. {name} (code: {code})")
    
    # For this example, we'll use the first plan
    selected_plan_code = available_plans[0][0]
    print(f"\nSelected plan: {selected_plan_code}")
    
    # 3. Create a subscription with basic parameters
    print("\n3. Creating subscription...")
    
    subscription = create_subscription(
        account_code=account_code,
        plan_code=selected_plan_code,
        currency="USD",
        additional_params={
            "quantity": 1,
            "auto_renew": True,
            "customer_notes": "Subscription created via API for testing purposes"
        }
    )
    
    # 4. Show the result
    if "error" in subscription:
        print(f"❌ Error creating subscription: {subscription['error']}")
    else:
        print("\n✅ Subscription created successfully!")
        print(f"Subscription ID: {subscription.get('id')}")
        print(f"State: {subscription.get('state')}")
        print(f"Plan: {subscription.get('plan', {}).get('name')}")
        print(f"Next billing: {subscription.get('current_period_ends_at')}")
        
        # Save the complete response to a file for reference
        with open("subscription_response.json", "w") as f:
            json.dump(subscription, f, indent=2)
        print("\nComplete response saved to subscription_response.json")

if __name__ == "__main__":
    main() 