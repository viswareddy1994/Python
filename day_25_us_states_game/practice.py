import pandas as pd

# Get user input and normalize it
# answer_state = input("Enter Your answer: ").title()
# print("User entered:", answer_state)

# Read the CSV file into a DataFrame
df1 = pd.read_csv(r"C:\Python\day_25_us_states_game\50_states.csv")   

# # Filter the DataFrame based on the user input
# val = df1[df1["state"] == answer_state]

# # Check if there are any matching records

# if not val.empty:
#     # Extract the state name, x and y coordinates
#     state_name = val["state"].values[0]
#     cords = val[["x", "y"]].values[0].tolist() 
#     print(f"State: {state_name}, {cords}")
# else:
#     print("State not found.")
    
    
all_states = df1["state"]
# Get correct guesses as a set
# correct_guesses_set = set(self.correct_guesses)
# Calculate missing states
# self.missing_states = list(all_states - correct_guesses_set)

# self.missing_states
print(list(all_states))