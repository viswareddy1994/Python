import os
import random
import smtplib
from email.message import EmailMessage
import json

class LetterGenerator:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        self.letter_paths = [
            os.path.join(script_dir, "../letter_templates/letter_1.txt"),
            os.path.join(script_dir, "../letter_templates/letter_2.txt"),
            os.path.join(script_dir, "../letter_templates/letter_3.txt")
        ]
        self.config = self.load_config()
        self.email_address = self.config["EMAIL_ADDRESS"]
        self.email_password = self.config["EMAIL_PASSWORD"]

    def load_config(self):
        with open(os.path.join(os.path.dirname(__file__), "../config/config.json")) as config_file:
            return json.load(config_file)

    def generate_letter(self, recipient_name):
        random_letter_path = random.choice(self.letter_paths)
        with open(random_letter_path, mode="r") as file:
            letter_content = file.read()
            return letter_content.replace("[NAME]", recipient_name)

    def send_email(self, recipient_email, message):
        msg = EmailMessage()
        msg.set_content(message, charset='utf-8')
        msg['Subject'] = 'Birthday Wishes'
        msg['From'] = self.email_address
        msg['To'] = recipient_email

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=self.email_address, password=self.email_password)
                connection.send_message(msg)
            print(f"Email successfully sent to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {e}")


        