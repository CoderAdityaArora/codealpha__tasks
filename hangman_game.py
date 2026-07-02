import random

words = [
    "python", "hangman", "computer", "programming",
    "keyboard", "developer", "challenge", "function"
]

word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0
max_wrong_guesses = 6

hangman_pictures = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

print("Welcome to Hangman!")

while wrong_guesses < max_wrong_guesses:
    print(hangman_pictures[wrong_guesses])

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Good guess!\n")
    else:
        print("Wrong guess!\n")
        wrong_guesses += 1

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break
else:
    print(hangman_pictures[wrong_guesses])
    print("Game over! The word was:", word)