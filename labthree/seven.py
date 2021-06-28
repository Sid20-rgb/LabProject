'''Q.No.7 Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.'''

def up_low(s):
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( f"No. of Upper case characters : {u}\nNo. of Lower case characters : {l}")

up_low("Hello World")