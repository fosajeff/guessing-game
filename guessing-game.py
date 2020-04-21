import random

no_of_guesses = {"easy": 6, "medium": 4, "hard": 3}


def play_game(no_of_guesses, secret_number):
    user_guess = 0
    print("What is my secret number?\n")
    print(f"Number of guess = {no_of_guesses}")
    while no_of_guesses != 0:
        try:
            user_guess = int(input("> "))
        except ValueError:
            print("Error! enter an interger number")
        else:
            if user_guess == secret_number:
                return "You got it right!"
            no_of_guesses -= 1
            if no_of_guesses == 0:
                break
            print(f"You got it wrong, guess left: {no_of_guesses}")

    return "\nGame Over!"


def guess_my_secret_number(username):
    choice = ""
    print(f"Welcome {username}!")
    while choice != "N":
        try:
            diff_level = int(
                input("\nChoose your diffulty level\n1. Easy\t2. Medium 3. Hard\n: ")
            )
        except ValueError:
            print("Wrong input,try again")
        else:
            if diff_level > 3 or diff_level < 1: print("Wrong input"); continue
            if diff_level == 1:
                secret_number = random.randint(1, 10)
                print(play_game(no_of_guesses.get("easy"), secret_number))
            elif diff_level == 2:
                secret_number = random.randint(1, 20)
                print(play_game(no_of_guesses.get("medium"), secret_number))
            else:
                secret_number = random.randint(1, 50)
                print(play_game(no_of_guesses.get("hard"), secret_number))
            while True:
                choice = input("\nDo you want to play again? [Y/n]\n: ").upper()
                if choice == "N" or choice == "Y":
                    break
                print("Wrong input. Enter y for Yes, n for No")

    return f"\nThanks for playing {username}. We'd love to have you again."


def main():
    print(
        "Welcome to our guessing game!\nInstructions:\n\
1. You are required to guess my secret number.\n\
2. There are three levels to choose from.\n   \
- Easy: your guess range is from 1-10 and you have 6 guesses\n   \
- Medium: your guess range is from 1-20 and you have 4 guesses\n   \
- Hard: your guess range is from 1-50 and you have 3 guesses\n\
Let's Begin! This is going to be fun!"
    )
    username = input("Enter your username: ")
    print(guess_my_secret_number(username))

    exit()


main()
