first_var = 10
second_var = 20


print("Result of {} + {} is {}".format(first_var, second_var, first_var + second_var))
print(first_var - second_var)
print(first_var * second_var)
print(second_var / first_var)
print(second_var % first_var)
print(first_var ** second_var)
print(second_var // first_var)


a = 1
b = 2

list_example = [1, 2, 3, 4, 5]

if a in list_example:
    print("{} exists list".format(a))
else:
    print("{} does not exists list".format(a))

if b in list_example:
    print("{} exists list".format(b))
else:
    print("{} does not exists list".format(b))

value_1 = 20
value_2 = 20
value_3 = 50

if value_1 is value_3:
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")
value_3 = 20
if id(value_1) == id(value_3):
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")


def print_lyrics():
    """This is documentation"""
    print("I'm a tester")


print_lyrics()
