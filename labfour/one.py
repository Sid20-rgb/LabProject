'''1.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
 (both included).'''

num = []
for x in range(1500, 2701):
    if x%7== 0 and x%5 == 0:

        print(x, end= " ")

        '''can be written in this way as well
        num.append(str(x))
print(','. join(num))''' 
