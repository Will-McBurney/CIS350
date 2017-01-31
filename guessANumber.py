#guess a number
import random

#functions
def get_number_input():
    while True:
        x = input("Guess a number 1-10: ")
        if x.isnumeric():
            return int(x);
        else:
            print("You didn't type a number. Try again");

#initial variables
number = random.randint(1,10)
correct = False
guessesLeft = 3

while (guessesLeft > 0) and (not correct):
    #Get a guess
    guess = get_number_input();

    #decriment guesses
    guessesLeft = guessesLeft - 1;
    
    #Check guess
    if guess == number: #You found it!
        correct = True
    elif guess > number: #too high
        print("Your guess is too large")
    else: #too low
        print("Your guess is too small")

if correct:
    print("You win! Congratulations")
else:
    print("You lost. The correct number was", number);
        
