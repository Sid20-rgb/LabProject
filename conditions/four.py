'''Task -----------------condition------------------------------
Weight converter:
Input the weight of a person in either kg or lbs. If the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.
'''

weight = int(input("Enter the weight:"))
kg_lbs = int(input("1.kg or 2.lbs:"))

if kg_lbs == 1:
    convertedWeight = weight * 2.20462
    print(f"The weight in lbs is {convertedWeight}.")
elif kg_lbs == 2:
    convertedWeight = weight//2.20462
    print(f"The weight in kg is {convertedWeight}.")
else:
    print("Invalid input.")
