# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# iss_position = (latitude,longitude)
# print(iss_position)

import requests
from datetime import datetime
MY_LAT = 40.058323
MY_LNG = -74.405663

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters,verify=False)
response.raise_for_status()
data = response.json()
sun_rise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sun_set = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sun_rise,sun_set)


current_time = datetime.now().hour
print(current_time)