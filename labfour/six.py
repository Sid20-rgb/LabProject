'''6.Write a Python program to count the number of even and odd numbers from a series of numbers.'''

num = int(input("Enter a number:"))

even = 0
odd = 0

for i in range(0, num):
    print(i , end = " ")
    if i%2==0:
        even+=1
    else:
        odd+= 1

print(f"\n{even} even numbers.")
print(f"{odd} odd numbers.")

