def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def perform_operation(operator,a,b):
    dict={
        '+':add(a,b),
        '-':minus(a,b),
        '*':multiply(a,b)
    }
    return dict.get(operator)

print(perform_operation('*',5,6))

