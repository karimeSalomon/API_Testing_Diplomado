value_1 = [20]
value_2 = [20]

print(value_2)

if value_1 is value_2:
    print("Line 1- a and b have same identity")
else:
    print("Line 1- a and b do not have same identity")

if value_1 == value_2:
    print("Line 2- a and b have same identity")
else:
    print("Line 2- a and b do not have same identity")

if id(value_1) == id(value_2):
    print("Line 3- a and b have same identity")
else:
    print("Line 3- a and b do not have same identity")
