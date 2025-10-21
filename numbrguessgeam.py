import random
number = random.randint(1, 10)
correct = 0
guesses = []
guess = int(input(f"Guess first number between 1 and 10: "))
while correct == 0:
    if guess == number:
        correct = 1
    elif guess < number:
        print(f"It is greater you used{guesses}")
        guesses.append(guess)
        guess = int(input(f"Guess first number between 1 and 10: "))
    elif guess > number:
        print(f"It is less you used{guesses}")
        guesses.append(guess)
        guess = int(input(f"Guess first number between 1 and 10: "))
print(f"it is right, the answer is {number}, your guesses were {guesses}")