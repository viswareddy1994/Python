from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def div(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

cal_operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": div
}

def calculator():
    print(logo)
    num1 = float(input("Enter the first number: \n"))
    for symbol in cal_operations:
        print(symbol)
    
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: \n")
        num2 = float(input("Enter the next number: \n"))
        cal_fun = cal_operations[operation_symbol]
        answer = cal_fun(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        continue_operation = input(f"Type 'yes' to continue with {answer}, or 'no' to start a new calculation, or 'exit' to quit: ").lower()
        if continue_operation == 'yes':
            num1 = answer
        elif continue_operation == 'no':
            should_continue = False
            calculator()
        elif continue_operation == 'exit':
            should_continue = False
            print("Goodbye!")

calculator()


