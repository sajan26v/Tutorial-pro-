while True:
    response = input("Do you like Python? (yes/no): ").lower()

    try:
        if response in ["yes", "y"]:
            print("You are on the right course.")
            break
        elif response in ["no", "n"]:
            print("You might change your mind.")
            break
        else:
            raise ValueError("Invalid response")
    except ValueError:
        print("I did not understand. Please enter 'yes' or 'no'.")
