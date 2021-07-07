'''5.Write a Python program to remove an item from a set if it is present in the set.'''

item = set([1, 2, 3, 4, 5, 6])

r = int(input("Enter a item to remove:"))

if r in item:
    item.remove(r)
    print(item)

else:
    print("Not available in this set.")