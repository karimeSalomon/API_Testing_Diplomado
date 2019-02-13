# practice #1

# create a function that receive 3 arguments:
# 2 numbers and 1 operation
# according the operation defined the expected result need to be printed.

def perform_operation(operator,a,b):
    dict={
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b,
        '%': a % b,
        '**': a ** b,
        '//': a // b
    }

    return dict.get(operator)

print('perform_operation(\'+\',1,2)    => ',perform_operation('+',1,2))
print('perform_operation(\'-\',5,9)    => ',perform_operation('-',5,9))
print('perform_operation(\'*\',-1,2)   => ',perform_operation('*',-1,2))
print('perform_operation(\'/\',0,22)   => ',perform_operation('/',0,22))
print('perform_operation(\'%\',111,4)  => ',perform_operation('%',111,4))
print('perform_operation(\'**+\',2,32) => ',perform_operation('**',2,32))
print('perform_operation(\'//\',10,3)  => ',perform_operation('//',10,3))
print('perform_operation(\'\',10,10)   => ',perform_operation('',10,10))

