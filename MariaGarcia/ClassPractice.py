# Arithmetic operations

integer_value = 2
another_integer_value = 17
positive_float_value = 7.5
negative_float_value = -7.5
print('values: ', positive_float_value, ', ', integer_value, ', ', another_integer_value, ', ', negative_float_value)

addition = integer_value + positive_float_value
print('addition: ', addition)

multi = integer_value * integer_value
print('multiplication: ', multi)

division = positive_float_value / integer_value
print('normal division: ' , division)

floor_division = positive_float_value // integer_value
print('floor division: ' , floor_division)

division_remainder = another_integer_value % integer_value
print('division remainder: ' , division_remainder)


# Membership operators
a = 1
b = 2
list = [1, 2, 3, 4, 5]

if(a in list):
    print('a exists in list')
else:
    print('a does not exists in list')

if(b not in list):
    print('b exists in list')
else:
    print('b does not exists in list')

# Identity operators
if(a is 1):
    print('a is 1')

value_1 = 20
value_2 = 20

if(value_1 is value_2):
    print('value_1 and value_2 have same identity')

print('id value_1: ', id(value_1))
print('id value_2: ', id(value_2))
print('id 20: ', id(20))

if(id(value_1) == id(value_2)):
    print('value_1 and value_2 have same identity')

# User-defined functions
def print_lyrics():
    'Function documentation'
    print('i am a dev and i am ok')
    print('i sleep all day and work all night')

print_lyrics()
