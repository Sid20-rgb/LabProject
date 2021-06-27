'''Q.No.4 Write a function that returns the sum of multiples of 3 and 5 between 0 and limit(parameter). For example, if
 limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20'''

def sum_of_multiples(limit):

    for i in range(0, limit):
        if i%3==0 or i%5==0:
            print(i, end=" ")

limit = int(input("Enter a limit:"))
sum_of_multiples(limit)




