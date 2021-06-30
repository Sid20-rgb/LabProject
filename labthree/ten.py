'''10 Write a program to find the factorial of a number using functions.'''

def fact():


    factorial = 1
    for i in range(1, num+1):

        factorial = factorial * i

    return factorial

num = int(input("Enter a number:"))
ans = fact()

print(f"The factorial of {num} is {ans}.")