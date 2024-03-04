import math

import random


# Check that users have entered a valid integer

def int_check(question, low=None, high=None, exit_code="xxx"):
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

# Initializes game variables
round_num = 0
secret = 0
game_history = []
correct_guess = ""
history_item = ""

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

while total_rounds == "infinite" or total_rounds == "secret" or round_num < total_rounds:

    # Resets the list of guesses each round
    already_guessed = []

    # adds 1 to the num of rounds
    round_num += 1

    # displays the round number
    print(f"--- Round {round_num} ---")

    # randomly generates a number from 1 to 100 if its secret mode
    if total_rounds == "secret":
        print("The secret number is between 1 and 100!")
        # Generates the random secret number from 1 to 100
        secret_number = random.randint(1, 100)
        guesses_allowed = 6
        guess_num = secret_number

    # else it's the normal game mode
    else:
        # Gets the game parameters
        print()
        low_num = int_check("Low number: ")
        high_num = int_check("High number:", low=low_num + 1)
        print()
        guesses_allowed = calc_guesses(low_num, high_num)
        initial_guesses = guesses_allowed
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
            print(f"You have {guesses_allowed} guesses left")
            print()

        # The user guesses a number
        guess = int_check("Guess a number (or type xxx to exit): ")

        # displays message depending on whether the user guessed the number or not
        if correct_guess == "yes":
            print()
            print(f"Congratulations 🥳🥳🥳 You have chosen the correct number which was {guess_num}")
            print()
            history_item = f"Round {round_num}: You have won this round by guessing {guess_num}"
            break

        # exits the code if the user types "xxx"
        if guess == "xxx":
            print("Thanks for playing!")
            correct_guess = "no"
            break

        # check that guess is not duplicate
        elif guess in already_guessed:
            print(f"You've already guessed {guess}. You've still got"
                  f" {guesses_allowed} left")
            continue

        # if guess is not a duplicate, add it to the already guessed list
        else:
            already_guessed.append(guess)

        if guess > guess_num:
            print()
            print("The number you have chosen is higher than the secret number")
        elif guess < guess_num:
            print()
            print("The number you have chose is lower than the secret number")
        elif guess == guess_num or guess == guess_num:
            correct_guess = "yes"
            break

        guesses_allowed -= 1

        # if the user runs out of guesses it exits the while loop and displays one of 2 end messages
        if guesses_allowed == 0:
            correct_guess = "no"

    if correct_guess == "yes" and guesses_allowed == 1:
        print()
        print(f"Phew! It was close, you managed to guess {guess_num} correctly on your last guess!")
        print()
        history_item = f"Round {round_num}: You were super close from losing! Luckily you had guessed {guess_num}!"

    elif correct_guess == "no":
        print()
        print(
            f"Round {round_num}: Sadly, you ran out of guesses and you have not guessed the number which was {guess_num}.")
        print()
        history_item = f"Round {round_num}: Sadly you lost, you didn't manage to guess {guess_num}."

    elif correct_guess == "yes" and initial_guesses == guesses_allowed:
        print()
        print(f"Round {round_num}: Lucky! You managed to guess it on your first guess! You guessed {guess_num}.")
        print()
        history_item = f"Round {round_num}: Lucky! You had managed to guess it on your first guess! You guessed {guess_num}."

    game_history.append(history_item)

    # If the game mode chosen was secret mode, it asks if the user wants to play again
    if total_rounds == "secret":
        play_again = yes_no("Do you want to play again?")

        if play_again == "yes":
            continue

        elif play_again == "no":
            break

if correct_guess == "no" and guesses_allowed > 0:
    print()
    print("Sorry, you have not finished a single round thus we have no history to show you")
    exit()

# asks the user whether they would want to see the game history
view_history = yes_no("Do you want to view the game history?")
print()

# displays the game history if the user wants to see it
if view_history == "yes":
    print("\n⌛⌛⌛ Game History ⌛⌛⌛ ")
    print()
    # Outputs the game history
    for item in game_history:
        print(item)
