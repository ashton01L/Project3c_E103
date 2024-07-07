# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/7/2024

# Description: Write a program that prompts the user for an integer that the player
# (maybe the user, maybe someone else) will try to guess.
# If the player's guess is higher than the target integer,
# the program should display too high. If the user's guess is
# lower than the target integer, the program should display too low.
# The program should use a loop that repeats until the
# user correctly guesses the integer.
# Then the program should print how many guesses it took.

def main():
    try:
        # Prompt user to input the target integer
        target = int(input("Enter the integer for the player to guess. "))

        num_guesses = 0
        while True:
            # Prompt user for a guess
            guess = int(input("Enter your guess: "))
            num_guesses += 1

            # Check if guess is correct
            if guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print(f"You guessed it in {num_guesses} tries.")
                break

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
