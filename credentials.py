# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Evan Lindsey
# Created: 2020-02-24
fn = "Enter your first name: "
ln = "Enter your last name: "



def Name(f, l):
    global first
    global last
    first = input(f)
    last = input(l)
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
    passwd = input("Create a new password: ")
    while True:
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble")
            passwd = input("Create a new password: ")
            continue
        elif len(passwd) >= 8:
            print("The force is strong in this one…")
            print("Account configured. Your new email address is", uname + "@marist.edu")
            break
first,last = Name(fn, ln)
Marist()
Password()




