'''10.Write a Python program that accepts a string and calculate the number of digits and letters'''

string = str(input("Enter a string:"))

d = 0
l = 0

for i in string:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1

print(f"Digits: {d}")
print(f"Letters: {l}")


