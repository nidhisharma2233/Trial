import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts <= max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try guessing higher.")
            elif guess > secret_number:
                print("Too high! Try guessing lower.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break

        except ValueError:
            print("Please enter a valid number!")

    else:
        print(f"\nSorry, you've used all {max_attempts} attempts. The number was {secret_number}.")


guessing_game()
