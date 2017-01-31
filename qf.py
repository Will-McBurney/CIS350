#Quadratic Formula Solver
import math

print("ax^2 + bx + c")
a = float(input("What is a? "))
b = float(input("What is b? "))
c = float(input("What is c? "))

root = math.sqrt(b * b - 4 * a * c)
x1 = (-b + root) / (2 * a)
x2 = (-b - root) / (2 * a)
print("x=",x1,"or",x2);
