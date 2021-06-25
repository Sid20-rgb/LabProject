'''Task -----------------condition------------------------------
Weight converter:
Input the weight of a person in either kg or lbs. If the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.
'''

weight = int(input("Enter the weight:"))
kg_lbs = input("(K)g or (L)bs:").lower()

if kg_lbs == "k":
    convertedWeight = weight * 2.20462
    print(f"The weight in lbs is {convertedWeight}.")
elif kg_lbs == "l":
    convertedWeight = weight//2.20462
    print(f"The weight in kg is {convertedWeight}.")
else:
    print("Invalid input.")
