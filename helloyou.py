#Print hello world n times
takingInput = True;
while(takingInput):
    n = input("How many times should I say hello? ")
    if n.isnumeric():
        n = int(n);
        takingInput = False;
    else:
        print("Input a number, stupid")

x = 0
while n > 0:
    x = x + 1
    print("Hello")
    n = n - 1
print("Done");
print(x)

