import math

#Quadratic Formula Script
print("ax^2 + bx + c = 0")

#get values a,b,c
a = float(input("a=?"))
b = float(input("b=?"))
c = float(input("c=?"))

#get the root
root = math.sqrt(b*b - 4 * a * c)
numerator1 = -b + root
numerator2 = -b - root
denominator = 2 * a
x1 = numerator1/denominator
x2 = numerator2/denominator

print("The roots are", x1,"and",str(x2))
