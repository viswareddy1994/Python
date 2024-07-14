# Write your code below this line 👇
def prime_checker(number):
    is_prime =True
    if number<1:
        print("It's Not a Prime number.")
    import math
    div_num = int(math.sqrt(number))+1
    for i in range(3,div_num,2):
        if number%i ==0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
n = int(input()) # Check this number
prime_checker(number=n)