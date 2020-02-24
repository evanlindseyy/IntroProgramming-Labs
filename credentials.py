# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Evan Lindsey
# Created: 2020-02-24
def main():
# get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
# TODO modify this to generate a Marist-style username
    uname = first + "." + last + "1@marist.edu"
# ask user to create a new password
    passwd = input("Create a new password: ")
    if len(passwd) < 8:
        print("Fool of a Took! That password is feeble")
        passwd = input("Create a new password: ")
    elif len(passwd) >= 8:
        print("The force is strong in this one…")
        print("Account configured. Your new email address is", uname)
main()
