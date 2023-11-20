# Exercise 4 - Guess the Word Game

# Step 1: Set up the game
secret = 'water'
turns = 6
guesses = ''

# Display introduction
print("Let's play Guess the Word")
print(f"You have {turns} turns to guess the word!")

# Display the initial state of the word
for letter in secret:
    if letter in guesses:
        print('', letter, '', end='')
    else:
        print(' _ ', end='')
print()

# Step 2: Allow the player to guess multiple times
while turns > 0:
    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()  # Convert input to lowercase for case-insensitivity

    # Check if the guessed letter is in the secret word
    if guess.isalpha() and len(guess) == 1:  # Check if the input is a single letter
        guesses += guess
        found = False  # Flag to check if the guessed letter is in the secret word

        # Display the current state of the word
        for letter in secret:
            if letter in guesses:
                print('', letter, '', end='')
            else:
                print(' _ ', end='')
                found = True

        print()  # Move to the next line

        if not found:
            print("Congratulations! You guessed the word.")
            break

    else:
        print("Invalid input. Please enter a single letter.")

    turns -= 1  # Subtract one from turns

    # Display end of game message
    if turns == 0:
        print("End of Game. You're out of turns.")
    else:
        print(f"Turns left: {turns}")

# Additional Exercise 7: Player should win when the word is guessed
if turns > 0:
    print("Congratulations! You guessed the word.")
