'''
Write a program that reads the length of the base and the height of a right-angled triangle and prints the area.
Every number is given on a seperate line.'''

l = int(input("Enter length:"))
h = int(input("Enter height:"))

area = (l*h)//2

print(area)

print(f"The area is {area}")