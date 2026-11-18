import random

# ***********************************
# 1. HANGMAN ASCII ART
# ***********************************

HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    *********
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    *********
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    *********
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    *********
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    *********
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    *********
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    *********
    """
]


# ***********************************
# 2. WORD LIST
# ***********************************

WORDS = [
    "python",
    "computer",
    "programming",
    "software",
    "keyboard",
    "internet",
    "technology",
    "developer",
    "engineering",
    "database"
]


# ***********************************
# 3. SELECT A RANDOM WORD
# ***********************************

def choose_word():
    return random.choice(WORDS)


# ***********************************
# 4. DISPLAY THE GAME
# ***********************************

def display_game(secret_word, correct_guesses, wrong_guesses):

    print(HANGMAN_PICS[len(wrong_guesses)])

    print("\nWord: ", end="")

    for letter in secret_word:

        if letter in correct_guesses:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")

    print("\n")

    print("Incorrect guesses remaining:", 6 - len(wrong_guesses))

    print("Incorrect letters:", " ".join(sorted(wrong_guesses)))


# ***********************************
# 5. MAIN GAME FUNCTION
# ***********************************

def play_game():

    secret_word = choose_word()

    correct_guesses = set()
    wrong_guesses = set()

    guessed_letters = set()

    print("***********************************")
    print("      WELCOME TO HANGMAN!")
    print("***********************************")

    while True:

        display_game(secret_word, correct_guesses, wrong_guesses)

        guess = input("\nGuess a letter: ").lower().strip()

        # Check if input is valid

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter ONE valid letter.")
            continue

        # Check for repeated guesses

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
            continue

        guessed_letters.add(guess)

        # Check if the letter is correct

        if guess in secret_word:

            correct_guesses.add(guess)

            print("Correct guess! Well done.")

        else:

            wrong_guesses.add(guess)

            print("Wrong guess! Be careful.")

        # Check if the player has won

        if set(secret_word).issubset(correct_guesses):

            display_game(secret_word, correct_guesses, wrong_guesses)

            print("\nCONGRATULATIONS! YOU WON!")
            print("The secret word was:", secret_word.upper())

            break

        # Check if the player has lost

        if len(wrong_guesses) == 6:

            display_game(secret_word, correct_guesses, wrong_guesses)

            print("\nGAME OVER! YOU LOST!")

            print("The secret word was:", secret_word.upper())

            break


# ***********************************
# 6. START THE GAME
# ***********************************

if __name__ == "__main__":
    play_game()
