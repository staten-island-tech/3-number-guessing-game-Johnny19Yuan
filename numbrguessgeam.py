import random

number = random.randint(1, 10)
correct = 0
guesses = []
guess = int(input(f"Guess first number between 1 and 10: "))

while correct == 0:
    if guess == number:
        correct = 1
        print(f"You guessed right you guessed{guesses}")
    elif guess < number:
        print("It is greater")
        guesses.append(guess)
        guess = int(input(f"Guess first number between 1 and 10: "))
    elif guess > number:
        print("It is less")
        guesses.append(guess)
        guess = int(input(f"Guess first number between 1 and 10: "))

print(f"it is right, the answer is {number}")
print (f"your guesses were {guesses}")