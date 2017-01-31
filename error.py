import math

def create_a_name_err():
    return 3

def create_a_div_zero_err():
    return 5/0

def catch_sqrt_err(x):
    try:
        return math.sqrt(x)
    except:
        return (str(math.sqrt(-x)) + "i")

def get_int(prompt):
    """Gets an integer from the user.
    Ensures that the input is an integer."""
    try:
        age = int(input(prompt))
        return age
    except ValueError:
        print("That's not an integer!")
        return get_int(prompt)
    

#create_a_name_error()
#create_a_div_zero_err()
#print(catch_sqrt_err(4));
#print(catch_sqrt_err(-4));
get_int("Give me a number");
