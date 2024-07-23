# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd
nato_data_frame = pd.read_csv(r"day_26_list_comprehension\NATO_alphabet\NATO-alphabet-start\nato_phonetic_alphabet.csv")
# print(nato_data_frame)
nato_phonetic_dict = {row.letter:row.code for (index,row) in nato_data_frame.iterrows()}
# print(nato_phonetic_df)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("Enter Your name: ").upper()
user_list = [input for input in user_name]
# name_list = [code for (char,code) in nato_phonetic_df.items() if char in user_list ]
print(user_list)
# code_list = [code for (char,code) in nato_phonetic_df.items() if char in user_list]
code_list = [nato_phonetic_dict[char] for char in user_list]
print(code_list)