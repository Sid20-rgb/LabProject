'''.8 Write a Python function that takes a number as a parameter and check the number is prime or not.'''

def function(number):
    if num > 1:
        for i in range(1, num):

            if num%i==0:
                print("Not Prime number")
                

            elif num%1==0 and num%num== 0:
                print("Prime number")
                break


    else:
        print("Invalid input.")

num = int(input("Enter a number:"))
function(num)