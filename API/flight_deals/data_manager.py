import requests
from pprint import pprint

SHEETY_API_ENDPOINT = "https://api.sheety.co/0e27e67ccc0cc891460bf43b654b5bf5/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.data = {}
        
    def access_sheety(self):
        self.response = requests.get(url=SHEETY_API_ENDPOINT)
        self.response.raise_for_status()
        self.data = self.response.json()["prices"]
        return self.data

    def update_destination_codes (self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            