username = input("Enter a username of 6 characters: ")

try:
    if len(username) == 6:
        print("You have entered a user with 6 characters.")
    else:
        print("Your username does not have 6 characters.")
except ValueError:
    print("Incorrect: please won't leave space")