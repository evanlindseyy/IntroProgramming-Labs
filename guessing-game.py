#Variables & Functions
def title():
    print("Python Guessing Game!")
    print("Type 'quit' at any point to exit.")

def end():
    print("Congrats! You guessed correctly.")

a = "elephant"

#Script
title()
    
while True:
    answer = input("I am thinking of an animal...: ").lower()
    if answer == a:
        end()
        break
        end()
    elif answer == "quit":
        print("Thanks for playing!")
        break
    else:
        print("That's not it... try again!")
        continue


