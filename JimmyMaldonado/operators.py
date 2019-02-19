#
# Operators
#

a = 50
b = 20

sum = a + b
print("a + b =", sum)

subs = a - b
print("a - b =", subs)

multi = a * b
print("a * b =", multi)

div = a / b
print("a / b =", div)

mod = a % b
print("a % b =", mod)

exp = a ** b
print("a ** b =", exp)

floor_div = a // b
print("a // b =", floor_div)

#
# Membership Operators
#

list = [10, 20, 30, 40, 50, 60, 70]

if a in list:
    print("a exists in list")
else:
    print("a does not exist in list")

if b not in list:
    print("b does not exist in list")
else:
    print("b exists in list")

#
# Identity Operators
#

value_1 = 20
value_2 = 20

if value_1 is value_2:
    print("is: value_1 and value_2 have the same identity")
else:
    print("is: value_1 and value_2 do not have the same identity")

if id(value_1) == id(value_2):
    print("id(): value_1 and value_2 have the same identity")
else:
    print("id(): value_1 and value_2 do not have the same identity")
