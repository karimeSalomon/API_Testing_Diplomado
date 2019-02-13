a = 10
b = 20
c = 4
d = 16
lista = [10,15,16,17,18]

value_1=20
value_2=20

print('Variables:', 'a=', a, 'b=', b, 'c=', c)
print('adding result (a+b):',  a+b)
print('subtraction result (a-b):', a-b)
print('Multiplication result (a*b):', a*b)
print('Division result:', 10/20)
print('Module:', b % a)
print('Exponent:', 10**c)


if d in lista:
    print('d exists in lista')
else:
    print('b does not exist in lista')


if b not in lista:
    print('b does not exist in lista')
else:
    print('b exist in lista')



if value_1 is value_2:
    print("Line 1-a and b have the same identity")
else:
    print("Line 1-a and b do not have the same value")


if id(value_1)==id(value_2):
    print("Line 2 -a and b have the same identity")
else:
    print("Line 2-a and b do not have same identity")




