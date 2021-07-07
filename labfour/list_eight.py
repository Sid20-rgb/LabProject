'''8. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements'''

list = [1,2,3,4,5,6,7,8,9]


del list[5]
del list[4]
del list[0]
print(list)