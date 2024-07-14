print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? $:\n"))
tip_percentage = float(input("what percentage tip would like to give?\n"))
num_people = int(input("How many people to split the bill?\n"))
tip_amount = (tip_percentage/100)*bill
total_amount = bill + tip_amount
each_person_pay = round(total_amount/num_people,2)
# print(f"Each person should pay ${each_person_pay}")
print(f"Each person should pay ${each_person_pay:.2f}")
