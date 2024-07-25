import datetime as dt
import smtplib
import os
import random

# Email details
sender_email = "vreddy.a3@gmail.com"
receiver_email = "visveswarareddy303@gmail.com"
# password = os.getenv("EMAIL_PASSWORD")  # Use environment variable for password
password = "sfgd xpoj rofj cdbd"

# Path to the quotes file
script_dir = os.path.dirname(__file__)
file_dir = os.path.join(script_dir, "quotes.txt")

# Read quotes from file
try:
    with open(file_dir, mode='r') as file:
        quotes = file.readlines()
    quote = random.choice(quotes)
except FileNotFoundError:
    print(f"Error: The file {file_dir} was not found.")
    exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

# Select the current date
now = dt.datetime.now()
day_of_week = now.weekday()

# Send email if today is Thursday (day_of_week == 3)
if day_of_week == 3:
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=receiver_email,
                msg=f"Subject:Motivational Quote of the Day\n\n{quote}\nBest Regards,\nViswa Reddy."
            )
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
else:
    print("Today is not Thursday, so wait for a motivational quote.")
