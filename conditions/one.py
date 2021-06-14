'''Price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise they need to put down 20%.
Print the down payment.'''

credit = bool(input("Enter a credit:"))

if credit == True:
    down_payment = 1000000*10//100
    print(f"The down payment is ${down_payment}.")
else:
    down_payment = 1000000*20//100
    print(f"The down payment is ${down_payment}.")