'''6.Write a Python program to convert a tuple to a string.'''

tuple = 'a', 'b', 'c', 'd'

str = ''.join(tuple)

print(str)

#OR
'''for i in tuple:
    str += i

print(str)'''