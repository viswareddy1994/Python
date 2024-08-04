# https://dashboard.sheety.co/projects/66ae46755888777a6b6bca32/sheets/prices
API_KEY = "Cv1qrl2YCVVg5NAO5eZEi1rBiIAksj1A"    
API_SECRET = "COqCpdav5WnsEE0l"
ACCESS_TOKEN = "WDw6AxW4utrdIrhxyOQ7b79SgV97"
# token_type = "Bearer"

import requests

# Define the URL and headers
url = "https://test.api.amadeus.com/v1/security/oauth2/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define the payload with your client credentials
payload = {
    "grant_type": "client_credentials",
    "client_id": API_KEY,
    "client_secret": API_SECRET
}

# Make the POST request
response = requests.post(url, headers=headers, data=payload)

# Print the response
print(response.json())
