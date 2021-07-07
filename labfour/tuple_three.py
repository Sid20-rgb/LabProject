'''3.Write a Python program to create a tuple with numbers and print one item.'''

tuple = 1, 2, 3, 4, 5

print(tuple)

choose = int(input("Enter one item:"))

if choose in tuple:

    print(choose)

else:
    print("It is not available.")
