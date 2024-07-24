import pandas as pd

# Load the NATO phonetic alphabet data
nato_data_frame = pd.read_csv(r"day_26_list_comprehension\NATO_alphabet\NATO-alphabet-start\nato_phonetic_alphabet.csv")

# Create a dictionary from the data frame
nato_phonetic_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# Function to convert user input to phonetic code words
def generate_phonetic():
    flag = True
    while flag:
        try:
            user_name = input("Enter your name: ").upper()
            code_list = [nato_phonetic_dict[char] for char in user_name]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            print(code_list)
            flag = False

# Run the function
generate_phonetic()

# 2nd method
"""def generate_phonetic():
        try:
            user_name = input("Enter your name: ").upper()
            code_list = [nato_phonetic_dict[char] for char in user_name]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
            generate_phonetic()
            
        else:
            print(code_list)

# Run the function
generate_phonetic()""" 
