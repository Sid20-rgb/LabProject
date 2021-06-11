'''6. Solve each of the following problems using Python Scripts. Make sure you use appropriate variable names
and comments. When there is a final answer have Python print it to the screen.
A person’s body mass index (BMI) is defined as:
BMI=mass in kg / (height in m)2.'''

mass = int(input("Enter the mass of a body in kg:"))
height = int(input("Enter the height of a body in m:"))

BMI = mass/(height**2)

print(BMI)