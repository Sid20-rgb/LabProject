'''Q.No.5 Write a function calledshow_stars(rows).Ifrowsis 5, it should print thefollowing:
*
**
***
****
*****'''

def calledshow_stars(rows):
    for i in range(rows):#012345 row
        for j in range(i+1): #0+1, 1+1, 2+1, 3+1, 4+1, 5+1, column
            print('*', end = " ")

        print()

calledshow_stars(6)
