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

        except ValueError or response == "":
            if response == "":
                response = "infinite"
                return response
            else:
                print(error)


# Main routine goes here

# rounds = "test"
# while rounds != "":
#     rounds = int_check("Rounds <enter for infinite>: ", low=1, exit_code="xxx")
#     print(f"You asked for {rounds}")

low_num = int_check("Low number: ")
print(f"You chose {low_num} as your low number")

high_num = int_check("High number:", low=1)
print(f"You chose {high_num} as your high number")

guess = ""
while guess != "xxx":
    guess = int_check("Guess:", low=0, high=10, exit_code="xxx")
    print(f"You guessed {guess}")
    print()
