#Demonstration of pass by value vs. pass by reference


#ints, floats, strings, and booleans are pass by value
def inc_z(z):
    """Add 1 to x, but this function ends up not doing anything"""
    z = z + 1

x = 123
print(x)
inc_z(x)
print(x)

lst = [1,2,3]

#lists, along with other collcetions are pass by reference
def addtoA(a,x):
    """Append x to the end of list a"""
    a.append(x);

print(lst)
addtoA(lst,4);
print(lst)
