'''game finding a secret number within 3 attempts using while loop'''
import random

randomnum = random.randrange(1, 5)

print(randomnum)

guess = int(input("Enter your guess:"))

i = 1
while i < 3:
    if guess != randomnum:
        again = int(input("Try Again:"))

    i+= 1
while i > 3:

    print("Time out.")
    break

if guess == randomnum:
    print("Congrats.")


import random

random_num = random.randint(1,5)
print(random_num)

guess = int(input("Guess:"))

i = 1
while i < 3:
    if guess == random_num:
        print("Congrats")
    break
    else:
        guess_again= int(input("Guess again."))
        


