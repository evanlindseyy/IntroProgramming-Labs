def title():
    print("Python Guessing Game!")

def end():
    print("Congrats! You guessed correctly.")


a = "elephant"






title()
    
while True:
    answer = input("I am thinking of an animal...: ")
    if answer == a:
        break
    else:
        print("That's not it... try again!")
        continue

end()
