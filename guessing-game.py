#Variables & Functions
def title():
    print("Python Guessing Game!")
    print("Type any word starting with 'q' to quit.")

def end():
    print("Congrats! You guessed correctly.")

def thanks():
    print("Thanks for Playing!")

a = "elephant"

#Script
title()
    
while True:
    answer = input("I am thinking of an animal...: ").lower()
    if answer == a:
        end()
        answer = input("Do you like elephants? Enter yes (y) or no (n): ").lower()
        if answer.startswith("y"):
            print("I do too! That's why I picked them for this game.")
            thanks()
            break
        if answer.startswith("n"):
            print("I'm sorry to hear that...")
            thanks()
            break
    elif answer.startswith("q"):
        print("You quit the game. Thanks for playing!")
        break
    else:
        print("That's not it... try again!")
        continue


