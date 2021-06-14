'''7. You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops
 on the way. How long will the bus journey take? Alternatively, you could run to university. You jog the first mile
 at 7mph; then run the next two at15mph; before jogging the last at 7mph again. Will this be quicker or slower than
 the bus?'''
#by bus
print("By Bus")
distance = int(input("Enter a distance in miles:"))
speed = int(input("Enter the speed in mph:"))
stops = int(input("Enter the number of stops:"))
timespent = int(input("Enter the number of time spends at each stops:"))

totaltimespent = stops * timespent

timerate = distance/speed

timetaken = distance/timerate

totaltimetaken = timetaken - totaltimespent

print(f"The total time taken by bus is {totaltimetaken}.")

#by jogging
print("By Jogging")
distance1 = int(input("Enter the 1st distance travel:"))
speed1 = int(input("Enter the speed used in 1st distance:"))
timerate1 = distance1/speed1

distance2 = int(input("Enter the 2nd distance:"))
speed2 = int(input("Enter the speed used in 2nd distance:"))
timerate2 = distance2/speed2

distance3 = int(input("Enter the 3rd distance:"))
speed3 = int(input("Enter the speed used in 3rd distance:"))
timerate3 = distance3/speed3

totaltimerate= timerate1 + timerate2 + timerate3

totaltimetaken1 = (distance1 + distance2 + distance3)//totaltimerate

print(f"The total time taken by jogging is {totaltimetaken1}.")

if totaltimetaken > totaltimetaken1:
    print("It will be slower by jogging.")
elif totaltimetaken1 > totaltimetaken:
    print("It will be slower by bus.")