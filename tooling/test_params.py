#!/usr/bin/env python3

import requests

# Define your query params as a dict
params = {"metric": "cpu", "limit": 10}  # You can add more pairs!

# Make the GET request
response = requests.get("https://httpbin.org/get", params=params)

# Check what happened
print(f"Final URL: {response.url}")
print(f"Status code: {response.status_code}")
print(response.text)  # The response body (JSON in this case)
