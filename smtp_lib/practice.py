import smtplib

my_email = "vreddy.a3@gmail.com"
password = "sfgd xpoj rofj cdbd"
to_address = "visveswarareddy303@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_address,
                        msg="Subject:Hello From Pyhton\n\nChecking the python code to send email ")

import datetime as dt

now =  dt.datetime.now()
# now =  dt.datetime.today()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
print(year,month,day,day_of_week)

data_of_birth = dt.datetime(year=1994,month=9,day=28,hour=12,minute=00)
age_in_days = (now-data_of_birth).days
age_in_years= age_in_days/365.25
print(age_in_years,age_in_days)