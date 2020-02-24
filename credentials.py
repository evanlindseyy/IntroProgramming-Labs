# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Evan Lindsey
# Created: 2020-02-24
import string
fn = "Enter your first name: "
ln = "Enter your last name: "
error = "Fool of a Took! That password is feeble"
password = "Create a new password. It must contain more than 8 characters, and have one or more uppercase characters: "
letters_characters = set(string.ascii_letters)



def Name(f, l):
    global first
    global last
    first = input(f).lower()
    last = input(l).lower()
    print()
    print(first, last)
    print()
    return first, last

def Marist():
    global uname
    uname = first + "." + last + "1"
    print("Your username is", uname)
    print()
    

def Password():
    global passwd
    passwd = input(password)

#Tried to apply DRY to this function, but it cause a bug that infinitely repeated a message
def Strength():
    global passwd
    while True:
        if len(passwd) < 8:
            print(error)
            print()
            passwd = input(password)
            continue
        if not any(character in passwd for character in letters_characters):
            print(error)
            print()
            passwd = input(password)
            continue
        elif len(passwd) >= 8:
            print("The force is strong in this one…")
            print()
            print("Account configured. Your new email address is", uname + "@marist.edu")
            break

first,last = Name(fn, ln)
Marist()
Password()
Strength()




