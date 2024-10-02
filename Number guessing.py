import random
import math

def number_guessing_game():
    # Step 1: User inputs range
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

    # Step 2: Generate random number
    random_number = random.randint(lower_bound, upper_bound)
    
    # Calculate minimum guesses
    min_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))
    
    # Step 3: Initialize guessing loop
    guesses = 0
    while True:
        guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
        guesses += 1

        # Step 4: User guess logic
        if guess > random_number:
            print("Try Again! You guessed too high.")
        elif guess < random_number:
            print("Try Again! You guessed too small.")
        else:
            print("Congratulations! You've guessed the right number.")
            break

    # Step 5: Check minimum guesses
    if guesses <= min_guesses:
        print(f"You guessed it in {guesses} tries, which is within the minimum {min_guesses}.")
    else:
        print(f"You guessed it in {guesses} tries, but the minimum was {min_guesses}. Better Luck Next Time!")

# Start the game
number_guessing_game()
