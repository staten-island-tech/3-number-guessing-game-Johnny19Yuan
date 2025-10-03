import random

number = random.randint(1, 10)

guess = input("Guess first number between 1 and 10")

guesses = []
while correct < 1:
    if guess == number:
        correct = 1
        print(f"You guessed right you guessed{guesses}")
    else:
        guesses.append(guess)
