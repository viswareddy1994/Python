from turtle import Turtle
import pandas as pd
import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir,"50_states.csv")

class States:
    def __init__(self):
        self.path = file_path
        self.correct_guesses = []
        self.missing_states = []
        self._score = 0  # Use a different name for the instance variable
        
    def check_user_guess(self, user_input):
        self.df1 = pd.read_csv(self.path)
        self.val = self.df1[self.df1["state"] == user_input]
        
    def get_coordinates(self):
        if not self.val.empty:
            self.state_name = self.val["state"].values[0]
            self.coords = self.val[["x", "y"]].values[0].tolist()
            self.correct_guesses.append(self.state_name)
            
    def get_score(self):  # Changed method name to avoid conflict
        self._score = len(self.correct_guesses)
        return self._score
        
    def update_state(self):
        if hasattr(self, 'coords'):
            self.turtle = Turtle()
            self.turtle.penup()
            self.turtle.hideturtle()
            self.turtle.goto(self.coords)
            self.turtle.write(self.state_name)
        else:
            print("Coordinates not found. Make sure to call get_coordinates() first.")
        
    def remaining_states(self):
        self.all_states = self.df1["state"]
        self.missing_states = [state for state in list(self.all_states) if state not in self.correct_guesses]
        return self.missing_states
        

        
