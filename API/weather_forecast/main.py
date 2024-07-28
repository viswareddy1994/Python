import requests
import json
from twilio.rest import Client

#You need to aupdate account_sidd and auth_t for code to run now deleting for security reasons


api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": 36.162663,  
    "lon": -86.781601, 
    "appid": "ad9ce3b6b61d759151800d7294cabc38",
    "cnt":4
    }

response = requests.get(url=api_endpoint, params=parameters, verify=False)
# print(response.status_code)
try:
    response.raise_for_status()  # Raise an HTTPError for bad responses
    data = response.json()
    # print(json.dumps(data,indent=4))
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

will_rain = False

for forecast in data["list"]:
    weather_info = forecast["weather"]
    for weather in weather_info:
        weather_condition = weather["id"]
        if weather_condition <700:
            will_rain = True
# if will_rain:
    #uncomment below line and add the varible above
   #client = Client(account_sid, auth_token)
    #message = client.messages.create(
    # from_='whatsapp:+14155238886',
    # body='Its going to rain today, bring Umbrella☔',
    # to='whatsapp:+19454005199'
    # )
    

    # print(message.status)
    
