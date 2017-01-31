def mult(a, b):
    """This function multiplies two numbers
    and returns the output.
    a - first number to be multiplied
    b - second number to be multiplied
    return the product of the two inputs"""
    return a * b;

def my_max(a, b):
    """returns the maximum value of a and b"""
    return (a + b + abs(a-b)) / 2

def factorial(x):
    """Returns the factorial of a number.
    Example: !3 = 3 * 2 * 1"""
    product = 1
    counter = 1
    while counter <= x:
        product = mult(product, counter)
        counter = counter + 1;
    return product

def fact(x):
    """Returns the factorial of a number.
    Is recursive.
    Example: !3 = 3 * 2 * 1"""
    if x == 0:
        return 1;
    else:
        y = x * fact(x - 1);
        return y;

print(fact(0), "should be 1");
print(fact(1),"should be 1");
print(fact(3),"should be 6");
print(fact(6),"should be 720");

