import random

def guess_the_number():
    secret_number = random.randint(1, 20)

    attempts = 0

    while attempts < 5:
        try:
            guess = int(input("Guess the number (between 1 and 20): "))

            if guess < 1 or guess > 20:
                print("Please enter a number between 1 and 20.")
                continue

            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("The correct number is higher.")
            else:
                print("The correct number is lower.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if attempts >= 5:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
