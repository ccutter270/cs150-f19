"""
CS150 number guessing game examples
"""

import random

def number_guessing_game():
    """
    Play a number guessing game where the user tries to guess a number
    between 1 and MAX_GUESS and is given hints for lower and higher
    """

    # To keep the functions self-contained, and independent, I am creating the constant
    # inside the function. Normally I would do so at the top of the file
    MAX_GUESS = 20

    number = random.randint(1, MAX_GUESS)

    correct = False

    while not correct:
        # input returns a string, so we need to convert it to an integer for
        # comparison
        guess = int(input("Guess a number between 1 and " + str(MAX_GUESS) + ": "))

        if guess == number:
            print("Good job!")
            correct = True
        elif guess < number:
            print("A bit higher")
        else:
            print("A bit lower")


# Here is an alternate implementation that doesn't use a
# bool variable. The trade-off is duplicating the input code.
def number_guessing_game2():
    """
    Play a number guessing game where the user tries to guess a number
    between 1 and MAX_GUESS and is given hints for lower and higher
    """

    MAX_GUESS = 20

    number = random.randint(1, MAX_GUESS)
    guess = int(input("Guess a number between 1 and " + str(MAX_GUESS) + ": "))

    while guess != number:
        if guess < number:
            print("A bit higher")
        else:
            print("A bit lower")

        guess = int(input("Guess a number between 1 and " + str(MAX_GUESS) + ": "))

    # when we exit the loop, we know the user got it right
    print("Good job!")


# Here is a third implementation that doesn't use a bool variable and
# instead breaks out of the loop
def number_guessing_game3():
    """
    Play a number guessing game where the user tries to guess a number
    between 1 and MAX_GUESS and is given hints for lower and higher
    """

    MAX_GUESS = 20

    number = random.randint(1, MAX_GUESS)

    while True:
        guess = int(input("Guess a number between 1 and " + str(MAX_GUESS) + ": "))

        if guess == number:
            print("Good job!")
            break
        elif guess < number:
            print("A bit higher")
        else:
            print("A bit lower")
