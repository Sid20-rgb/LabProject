'''10. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.'''

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 != num2 and num1 != num3 and num2 != num3:
    print(num1+num2+num3)
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("0")