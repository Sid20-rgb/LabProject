'''8.Write a Python program to create the colon of a tuple.'''
from copy import deepcopy
tuple = 1, 2, [], "three"

print(tuple)
#making tuple copy by using deepcopy
tupleColon = deepcopy(tuple)

tupleColon[2].append(3)
print(tupleColon)