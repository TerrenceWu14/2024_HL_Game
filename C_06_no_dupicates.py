already_guessed = []

secret = 8
guesses_used = 0
guesses_allowed = 5


guess = ""
while guess != secret:
    guess = int(input("Guess: "))


    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've still used"
              f"{guesses_used} out of {guesses_allowed}")
