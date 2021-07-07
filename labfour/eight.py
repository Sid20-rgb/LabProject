'''8.Write a Python program to get the Fibonacci series between 0 to 50.Note : The Fibonacci Sequence is the series of
numbers :0, 1, 1, 2, 3, 5, 8, 13, 21, ....Every next number is found by adding up the two numbers before it'''


a = 0
b = 1                  #0, 1, 1, 2, 3, 5, 8, .......
print(a)               #a, b, c
                       #c = a + b     a and b and c will just keep shifting  by a = b, b = c
print(b)

for i in range(0, 51):

    c = a+b
    a = b
    b = c

    print(c)