'''3.Write a Python program to guess a number between 1 to 9.Note :User is prompted to enter a guess. If the user
guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a
"Well guessed!" message, and the program will exit.'''

import random

random = random.randint(1, 10)

print(random)

guess = int(input("Enter a number:"))

while guess > 0:
    if guess != random:
        print("That's incorrect")
        again = int(input("Guess again:"))
        if again == random:
            print("That's correct guess.")
            break

    elif guess == random:
        print("That's the correct guess.")
        break



