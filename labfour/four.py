'''4.Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*'''

for i in range(0, 5):
    for j in range(i+1):
        print("*", end =" ")
    print()
for x in range(0, 4):
    for y in range(4 - x):
        print("*", end = " ")
    print()