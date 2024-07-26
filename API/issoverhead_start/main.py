import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 40.058323
MY_LONG = -74.405663
SENDER_EMAIL = "vreddy.a3@gmail.com"
PASSWORD = "sfgd xpoj rofj cdbd"
RECEPIENT_EMAIL = "visveswarareddy303@gmail.com"

def get_iss_positions():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude,iss_longitude

#Your position is within +5 or -5 degrees of the ISS position.

def get_sun_times():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters,verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunrise,sunset



#If the ISS is close to my current position
def compare_iss_local_position():
    iss_latitude,iss_longitude = get_iss_positions()
    sunrise,sunset = get_sun_times()
    current_time = datetime.now().hour
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and (current_time <= sunrise or current_time >= sunset):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEPIENT_EMAIL,
                msg="Subject:REMAINDER TO LOOK UP\n\nHey Viswa, Come out and see the sky ISS is above you"
            )
        print("ISS is overhead")
    else:
        print("ISS is not Overhead")
        
        
while True:
    compare_iss_local_position()
    time.sleep(60)

        




