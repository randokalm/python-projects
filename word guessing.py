import random

name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the guessing game.")

words = ["python", "java", "ruby", "javascript", "swift"]
word = random.choice(words)

guesses = ""
turns = 12

while turns > 0:
    failed = 0  

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print()  

    if failed == 0:
        print(f"Congratulations, {name}! You've guessed the word '{word}'.")
        break

    guess = input("Guess a character: ").lower()
    guesses += guess  

    if guess not in word:
        turns -= 1  # Decrease turns by 1
        print(f"Wrong! You have {turns} turns left.")

if turns == 0:
    print(f"You lose! The correct word was '{word}'.")
