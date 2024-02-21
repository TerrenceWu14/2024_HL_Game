# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid answer from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            # Checks if the user response is a word in the list
            if item == user_response:
                return item
            # Checks if the user response
            # is the as the first letter of an item in the list

            elif user_response == item[0]:
                return item

        # Print error if the user does not enter something that is valid
        print(error)
        print()


# Asks the user how many rounds they want to play or infinite mode
def num_rounds():
    while True:
        num_round = input("How many rounds do you want to play (press <enter> for infinite): ")

        # Returns infinite if the user pressed <enter>
        if num_round == "":
            return "infinite"
        # Returns the number of rounds the user chose
        elif num_round == int(num_round) > 0:
            return int(num_round)
        # Anything else gets sent back to the start of the loop
        else:
            print("Please either press <enter> for infinite mode "
                  "or type the number (greater than 0) of rounds you want to play")
            print()


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

# Loops the code
while True:
    want_instruction = string_checker("Do you want to read the instructions? (If so type yes or if not type no)")

    # Checks whether the user entered yes or no
    if want_instruction == "yes" or want_instruction == "y":
        instructions()
    print("program continues")
    print()

    rounds = num_rounds()
