'''WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction,
 more than 60% –> first division, more than 40% –> pass, less than 40% –> fail'''

maths = float(input("Enter the mark of maths:"))
science = float(input("Enter the mark of science:"))
social = float(input("Enter the mark of social:"))
computer = float(input("Enter the marks of computer:"))

totalMarks = maths + science + social + computer
print(f"The total marks is {totalMarks}.")
percentage = totalMarks/400*100
print(f"The percentage is {percentage}%.")

if percentage > 70:
    print("Distinction")

elif percentage > 60:
    print("First division")

elif percentage > 40:
    print("Pass")

else:
    print("Fail")
