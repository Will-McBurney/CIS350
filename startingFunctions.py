def get_pi():
    """Returns pi.
    Note, this is just an example, but this is
    a bad way to do things"""
    return 3.1415926

def mult(a, b):
    """Returns a times b"""
    return a * b;

def get_max(a,b):
    """Returns the larger of a and b"""
    return (a + b + abs(a-b)) / 2

def is_prime(x):
    """return true if x is prime, otherwise false"""
    if (x < 2):
        return False;
    counter = 2;
    while counter < x:
        if x % counter == 0:
            return False;
        counter = counter + 1;
    return True;

def main():
    print(get_pi());
    print(mult(2,3));
    print(get_max(2,3));
