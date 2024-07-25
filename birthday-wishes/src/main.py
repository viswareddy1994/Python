##################### Extra Hard Starting Project ######################
from letter_generator import LetterGenerator
from birthday_manager import BirthdayManager

def main():
    birthday_manager = BirthdayManager()
    letter_generator = LetterGenerator()

    # Uncomment this line if you want to add a new birthday entry
    # birthday_manager.add_birthday("Viswa Reddy", "ambureddy@gmail.com", 1994, 9, 28)

    todays_birthdays_df = birthday_manager.get_today_birthdays()
    for _, row in todays_birthdays_df.iterrows():
        name = row["name"]
        email = row["email"]
        letter_message = letter_generator.generate_letter(name)
        letter_generator.send_email(recipient_email=email, message=letter_message)

if __name__ == "__main__":
    main()




