#CMPT 120 - Intro to Programming
#Lab 6- Control and Program Design
#Author: Evan Lindsey
#Date: 3/2/20

Strings = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "VIOLET"]

def showTitle():
    print("Color Preference Evaluator")
    print()

def promptForColor():
    global color_choice
    color_choice = input("Type in a Color: ".strip()).upper()
    return(color_choice)

def confirmColor():
    global color_choice
    while True:
        answer = input("You entered " + color_choice + "." + " Is this correct (Y/N)?").upper()
        if answer == "Y":
            print("Thank you for confirming.")
            break
        if answer == "N":
            promptForColor()
        else:
            print("That input is invalid. Try again")
            confirmColor()
            
def containsElement():
    global color_choice
    if color_choice == Strings[0]:
        praiseUser()
    if color_choice == Strings[1]:
        praiseUser()
    if color_choice == Strings[2]:
        praiseUser()
    if color_choice == Strings[3]:
        praiseUser()
    if color_choice == Strings[4]:
        praiseUser()
    if color_choice == Strings[5]:
        praiseUser()
    else:
        ridiculeUser()

def praiseUser():
    print("That color is in the list!\nTry and enter another one!")
    Main()

def ridiculeUser():
    print("That color is NOT on the list!\nTry again and think a little harder...")
    Main()

def Main():
    showTitle()
    promptForColor()
    confirmColor()
    containsElement()
    praiseUser()
    ridiculeUser()

Main()
    



