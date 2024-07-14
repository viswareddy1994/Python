MENU = {
    "espresso": {"ingredients": {"water": 50, "milk": 0, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

resources = {"water": 300,"milk": 200,"coffee": 100}
PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25
def  get_resource_info():
    money = 0
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return water,milk,coffee,money

def coffe_info(option):
    coffee_cost = MENU[f'{option}']["cost"]
    water_req = MENU[f'{option}']["ingredients"]["water"]
    milk_req = MENU[f'{option}']["ingredients"]["milk"]
    coffee_req = MENU[f'{option}']["ingredients"]["coffee"]
    return water_req,milk_req,coffee_req,coffee_cost

def calculate_coins(p,n,d,q):
    value = p*PENNY + n*NICKEL + d*DIME + q*QUARTER
    return value

def compare_price(act_price,user_paid):
    if user_paid >= act_price:
        return True
    elif user_paid < act_price:
        print(f"Sorry That's not enough money! ${user_paid} Money refunded")
def update_resources(prompt):
    water, milk, coffee,money = get_resource_info()
    water_req,milk_req,coffee_req,coffee_cost = coffe_info(prompt)
    if water < water_req:
            print(f"Sorry there is not enough water.${total_paid} Money refunded")     
    elif milk < milk_req:
        print(f"Sorry there is not enough Milk.${total_paid} Money refunded")
    elif coffee < coffee_req:
        print(f"Sorry there is not enough coffee.${total_paid} Money refunded") 
        

water, milk, coffee,money = get_resource_info()
while True:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == 'report':
        print(f"current resource values are:\nwater: {water}ml\nMilk: {milk}ml\ncoffee: {coffee}g\nMoney: ${money}")
    elif prompt == 'off':
        break
    else: 
        water_req,milk_req,coffee_req,coffee_cost = coffe_info(prompt)
        print(f"Please insert coins")
        penny_cnt = int(input(f"how many pennies?: "))
        nickel_cnt = int(input(f"how many nickels?: "))
        dime_cnt = int(input(f"how many dimes?: "))
        quarter_cnt = int(input(f"how many quarters?: "))
        total_paid = round(calculate_coins(penny_cnt,nickel_cnt,dime_cnt,quarter_cnt),2)
        actual_price = coffee_cost
        print(total_paid)
        update_resources(prompt)
        if compare_price(actual_price,total_paid):
            print(f"Here is ${total_paid-actual_price} in change\nHere is your {prompt}☕. Enjoy!")
            water-=water_req
            milk -= milk_req
            coffee -=coffee_req
            money += coffee_cost
        if input("want to order again Type Y or N: ").lower() == 'n':
            break

       

