import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Constants
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
NUTRI_API_ENDPOINT = os.getenv('NUTRI_API_ENDPOINT')
SHEETY_API_ENDPOINT = os.getenv('SHEETY_API_ENDPOINT')
SHEETY_TOKEN = os.getenv('TOKEN')

WEIGHT_KG = 75
HEIGHT_CM = 175
AGE = 29

def get_current_date():
    return datetime.now().strftime("%d/%m/%Y")

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def get_user_input():
    return input("Enter Your workout info: ")

def get_exercise_details(query):
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': APP_ID,
        'x-app-key': API_KEY
    }
    parameters = {
        'query': query,
        'weight_kg': WEIGHT_KG,
        'height_cm': HEIGHT_CM,
        'age': AGE
    }
    response = requests.post(url=NUTRI_API_ENDPOINT, json=parameters, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()['exercises']

def log_workout(exercises, date, time):
    for workout in exercises:
        exercise = workout['name']
        duration = workout['duration_min']
        calories = workout['nf_calories']
        workout_id = workout['tag_id']
        body = {
            'workout': {
                'date': date,
                'time': time,
                'exercise': exercise.title(),
                'duration': duration,
                'calories': calories,
                'id': workout_id
            }
        }
        headers = {
            "Authorization": SHEETY_TOKEN
        }
        response = requests.post(url=SHEETY_API_ENDPOINT, json=body,headers=headers, verify=False)
        response.raise_for_status()
        print(response.text)

def main():
    date = get_current_date()
    time = get_current_time()
    workout_user_input = get_user_input()
    exercises = get_exercise_details(workout_user_input)
    log_workout(exercises, date, time)

if __name__ == "__main__":
    main()







