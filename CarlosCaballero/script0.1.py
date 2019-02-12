a = 10
b = 30

# Operators
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a%b=',a%b)
print('a**b=',a**b)
print('a//b=',a//b)

# Array and existence
c = [1,2,3,4,5]

if(a in c):
    print('a in list c')
else:
    print('a not in list c')

# Identificators
d = 10

if(a is d):
    print('a is d')
else:
    print('a is not d')

if(id(a) is id(d)):
    print('id(a) is id(d)')
else:
    print('id(a) is not id(d)')

# Comments
def print_lyrics():
    "this is"
    print('additional line')

print_lyrics()

