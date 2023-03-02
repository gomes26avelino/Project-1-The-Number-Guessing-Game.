import random


def start_game():
    print("Welcome to the Number Guessing Game!")

    high_score = get_high_score()
    print(f"The current high score is {high_score} attempts.")

    answer = random.randint(1, 100)
    num_attempts = 0

    while True:
        guess = input("Guess a number between 1 and 100: ")
        num_attempts += 1

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess > answer:
            print("It's lower")
        elif guess < answer:
            print("It's higher")
        else:
            print("Got it! It took you", num_attempts, "attempts.")

            high_score = update_high_score(num_attempts, high_score)
            print(f"The current high score is {high_score} attempts.")

            play_again = input("Would you like to play again? (y/n) ")
            if play_again.lower() == "y":
                start_game()
            else:
                break

    print("Thanks for playing!")


def get_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        # If the file doesn't exist or can't be read, set the high score to a high value
        return 100


def update_high_score(num_attempts, high_score):
    if num_attempts < high_score:
        with open("high_score.txt", "w") as file:
            file.write(str(num_attempts))
        return num_attempts
    else:
        return high_score


# Kick off the program by calling the start_game function.
start_game()
