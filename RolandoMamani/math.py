"""
Practice 3
"""

value_1 = 5
value_2 = 9
if (value_1 is value_2):
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")

if(id(value_1)==id(value_2)):
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")
print(id(value_1))
print(id(value_2))


"""
Practice 2
"""
a = "a"
b = "b"
list = ["z", "g", "aa", "c", "k"]; listb = ["q", "a", "l", "r", "x"]

if(a in listb):
    print("a exist in the list")
else:
    print("a is not in the list")
if(b not in list):
    print("b does not exist in the list")
else:
    print("b exist in the list")


"""
Practice 1
"""

number1_longNameOfVariable_longNameOfVariable = 20
number2_longNameOfVariable_longNameOfVariable = 2
print(number1_longNameOfVariable_longNameOfVariable+number2_longNameOfVariable_longNameOfVariable)
print(number1_longNameOfVariable_longNameOfVariable-number2_longNameOfVariable_longNameOfVariable)
print(number1_longNameOfVariable_longNameOfVariable*number2_longNameOfVariable_longNameOfVariable)
print(number1_longNameOfVariable_longNameOfVariable/number2_longNameOfVariable_longNameOfVariable)
print(number1_longNameOfVariable_longNameOfVariable%number2_longNameOfVariable_longNameOfVariable)
print(number1_longNameOfVariable_longNameOfVariable**number2_longNameOfVariable_longNameOfVariable)
print(number1_longNameOfVariable_longNameOfVariable//number2_longNameOfVariable_longNameOfVariable)

