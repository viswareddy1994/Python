names = input(list())
# print(names)
# Split the input string into a list of names.
names = names.split(',')
import random

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
selected_person = names[random_choice]
print(f"{selected_person} is going to buy the meal today!")