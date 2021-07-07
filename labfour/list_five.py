'''5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last
character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''

list = ['abc', 'xyz', 'aba', '1221']
ctrl = 0

for i in list:
    rev = i[::-1]

    if rev == i and len(rev)>=2:

        ctrl += 1
        print(rev, end = " ")
    print()

print(f"Ans: {ctrl}")







