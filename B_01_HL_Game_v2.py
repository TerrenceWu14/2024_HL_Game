import math

import random


# Check that users have entered a valid integer

def int_check(question, low=None, high=None, exit_code=None):
    # sets up an error message
    if low is None and high is None:
        error = "Please enter an integer"
        print()

    # if the number needs to be more than an
    # integer (ie: rounds / high number)
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
        print()

    # if the number needs to be between a low and a high
    else:
        error = (f"Please enter and integer that"
                 f"is between {low} and {high} (inclusive")
        print()

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            # checks that the integer is not lower than the low num
            if low is not None and response < low:
                print(error)

            # checks that the integer is not higher than the high num
            elif high is not None and response > high:
                print(error)

            # returns the response if the response entered meets the criteria
            else:
                return response

        except ValueError:
            print(error)


# calculate the number of guesses allowed

def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped
    return max_guesses


# Checks whether the user entered yes or no
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you didn't choose a valid option (yes/no)")


# Asks the user how many rounds they want to play
def num_rounds():
    while True:
        print()
        num_round = input("How many rounds do you want to play (press <enter> for infinite) or type secret for us to "
                          "choose for you?")
        if num_round == "":
            return "infinite"

        elif num_round == "secret" or num_round == "s" or num_round == "sec":
            return "secret"

        # Checks that the integer is higher than 0
        try:
            num_round = int(num_round)
            if num_round > 0:
                return num_round

            else:
                print("Please enter a number greater than 0 or press <enter> for infinite mode or choose secret mode")
        # prints an error message if the user didn't enter an integer or a valid option
        except ValueError:
            print("Please enter a valid number or press <enter> for infinite mode or choose secret mode")


# Displays instructions
def instructions():
    print('''

*** Instructions ***

To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where 
the secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for 
infinite mode.

Your goal is to try to guess the secret number without 
running out of guesses

Good luck!

    ''')


# Main routine

round_num = 0
secret = 0
already_guessed = []

# Displays the title
print()
print("⬆⬆⬆ Welcome to the Higher Lower Game ⬇⬇⬇")
print()

want_instruction = yes_no("Do you want to read the instructions? (If so type yes or if not type no)")

# Checks whether the user entered yes or no
if want_instruction == "yes":
    instructions()

# Asks the user how many rounds they want to play
total_rounds = num_rounds()

while total_rounds == "infinite" or "secret" or round_num < total_rounds or guesses_allowed > 0:

    # adds 1 to the num of rounds
    round_num += 1

    print(f"--- Round {round_num} ---")
    if total_rounds == "secret":
        # Generates the random secret number from 1 to 100
        secret_number = random.randint(1, 100)
        guesses_allowed = 6
        guess_num = secret_number

    else:
        # Gets the game parameters
        print()
        low_num = int_check("Low number: ")
        high_num = int_check("High number:", low=low_num + 1)
        print()
        guesses_allowed = calc_guesses(low_num, high_num)
        # Generates the random number, between the low num and high num
        guess_num = random.randint(low_num, high_num)

    # Loops while guesses remaining are above 0 or
    # if they have not guessed the number yet
    while guesses_allowed > 0:

        # if guesses = 1 it prints "This is your final guess"
        if guesses_allowed == 1:
            print()
            print("This is your final guess!")
            print()
        # prints the amount of guesses you have left
        elif guesses_allowed > 1:
            print(f"You have {guesses_allowed} guesses")
            print()

        guess = int_check("Guess a number (or type xxx to exit): ")

        # exits the code if the user types "xxx"
        if guess == "xxx":
            print("Thanks for playing!")
            exit()

        # check that guess is not duplicate
        if guess in already_guessed:
            print(f"You've already guessed {guess}. You've still got"
                  f" {guesses_allowed} left")
            continue

        # if guess is not a duplicate, add it to the already guessed list
        else:
            already_guessed.append(guess)

        if guess > guess_num or guess > secret_number:
            print("The number you have chosen is higher than the secret number")
        elif guess < guess_num or guess < secret_number:
            print("The number you have chose is lower than the secret number")
        elif guess == guess_num or guess == guess_num:
            break
        # Removes 1 guess every loop
        guesses_allowed -= 1

    print(f"Congratulations 🥳🥳🥳 You have chosen the correct number which was {guess_num}")
    print()
