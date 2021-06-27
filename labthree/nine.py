
num = int(input("Enter a number:"))

for i in range(2, num-1):

    if num % 1 == 0 and num % num == 0 and num % i != 0:
        print("Prime number")
    elif num % 1 == 0 and num % num == 0 and num%i == 0:
        print("Not Prime number")
    break
#uhgcuhdciv
git fetch origin master
git merge origin master
git add two.py
git commit -m "marks"
git push origin master