import random

hidden = 6

while True:
    try:
        guess = int(input("Enter your guess(between 1 and 20): "))

        if guess < 1 or guess > 20:
            print("Please enter a number between 1 and 20.")
        else:

            if guess < hidden:
                print("Your guess is too low.")
            elif guess > hidden:
                print("Your guess is too high.")
            else:
                print("Congratulations! Your guess is correct.")
                break

    except ValueError:
        print("Invaild Input. Please enetr a vaild answer!.")