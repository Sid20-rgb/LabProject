'''4. Given three integers, print the smallest one. (Three integers should be user input)'''

int1 = int(input("Enter first integer:"))
int2 = int(input("Enter second integer:"))
int3 = int(input("Enter third integer:"))

if int1 < int2 and int1 < int3:
    print(f"{int1} is smallest.")
elif int2 < int3 and int2 < int1:
    print(f"{int2} is smallest.")
else:
    print(f"{int3} is smallest.")