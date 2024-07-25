import os
import pandas as pd
import datetime as dt

class BirthdayManager:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "../data/birthdays.csv")
        if os.path.exists(self.file_path):
            self.birthday_df = pd.read_csv(self.file_path)
        else:
            self.birthday_df = pd.DataFrame(columns=["name", "email", "year", "month", "day"])

    def add_birthday(self, name, email, year, month, day):
        new_entry = {"name": name, "email": email, "year": year, "month": month, "day": day}
        self.birthday_df = self.birthday_df.append(new_entry, ignore_index=True)
        self.birthday_df.to_csv(self.file_path, index=False)
        
    def get_today_birthdays(self):
        today = dt.datetime.now()
        return self.birthday_df[(self.birthday_df.day == today.day) & (self.birthday_df.month == today.month)]

        
        
        
        