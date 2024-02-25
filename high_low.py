while True:
    guess_num = 10
    num_chose = input()
    num_chose = int(num_chose)

    if num_chose > guess_num:
        print("The number you have chosen is higher than the secret number")
    elif num_chose < guess_num:
        print("The number you have chose is lower than the secret number")
    else:
        print("You have chosen the correct number!")
