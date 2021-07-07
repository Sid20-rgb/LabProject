'''4.Write a Python program to remove item(s) from set.'''

def remove(item):

    item.remove(1)

    return item

item = set([1, 2, 3, 4, 5])

print(remove(item))