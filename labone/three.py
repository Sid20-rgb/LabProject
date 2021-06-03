'''
N students take K apples and distributed them among each other evenly. The remaining(the undivisible)
part remains in the basket. How many apples will each single student get? How many apples will remain in
the basket? The program reads the number N and K. It should print the two answers for the questions above.'''
n = int(input("Enter the number of students:"))

k = int(input("Enter the number of apples:"))

divided= n//k

remaining = n%k


print(divided)

print(remaining)