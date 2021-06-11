'''5. A school decided to replace the desks in three classrooms. Each desk sits two students. Given the
 number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the
 third group of 22 students. So, we need 32 desks in total.'''

num_studentsinA = int(input("Enter the number of students in class a:"))
num_studentsinB = int(input("Enter the number of students in class b:"))
num_studentsinC = int(input("Enter the numbers of students in class c:"))

num_desksinA = (num_studentsinA//2)
num_remstudentsinA = (num_studentsinA%2)
print(f"The number of desk required in A is: {num_desksinA}")

num_desksinB = (num_studentsinB//2)
num_remstudentsinB = (num_studentsinB%2)
print(f"The number of desks required in B is: {num_desksinB}")

num_desksinC = (num_studentsinC//2)
num_remstudentsinC = (num_studentsinC%2)
print(f"The number of desks required in C is: {num_desksinC}")

print(num_desksinA+num_desksinB+num_desksinC+num_remstudentsinA+num_remstudentsinB+num_remstudentsinC)

