'''.8 Write a Python function that takes a number as a parameter and check the number is prime or not.'''

def test_prime(n):
    if (n==1):
        return "Not prime number"
    elif (n==2):
        return "Prime number"
    else:
        for x in range(2,n):
            if(n % x==0):
                return "Not Prime number"
        return "Prime number"
print(test_prime(5))