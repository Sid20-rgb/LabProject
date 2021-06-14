'''Write a Python program to convert seconds to day, hour, minutes and seconds.'''

second = int(input("Enter a second:"))

minute = second / 60


print(f"It is {minute} minutes.")

hour = second / 3600

print(f"It is {hour} hours.")

day = second / 86400


print(f"It is {day} day.")