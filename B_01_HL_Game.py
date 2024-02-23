# Check that users have entered a valid integer

def int_check(question, low=None, high=None, exit_code=None):
    # sets up an error message
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / high number)
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to be between a low and a high
    else:
        error = (f"Please enter and integer that"
                 f"is between {low} and {high} (inclusive")

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


# Displays the title
print()
print("⬆⬆⬆ Welcome to the Higher Lower Game ⬇⬇⬇")
print()


want_instruction = yes_no("Do you want to read the instructions? (If so type yes or if not type no)")

# Checks whether the user entered yes or no
if want_instruction == "yes":
    instructions()

# Asks the user how many rounds they want to play
num_rounds = int_check("Rounds <enter for infinite>: ", low=1, exit_code="")

# Gets the game parameters
low_num = int_check("Low number: ")
high_num = int_check("High number:", low=low_num+1)




