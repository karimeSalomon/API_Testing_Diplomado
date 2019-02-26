import random

def pratice1functions(number1, number2, operator):
    operation = f'{number1}{operator}{number2}'
    result = eval(operation)
    print(f'{operation}={result}')
    
def practice2Assignment(number, operator):
    initial_value = random.randint(0, 50)
    print(f'Initial value is {initial_value}')
    assignment = f'a{operator}{number}'
    print(assignment)
    operation = f'a={initial_value}; {assignment}; print("Final value is " + str(a))'
    exec(operation)
    
def practice3memberships(number):
    list = [1, 10, 3, 100, 20, 7]
    print(f'List is {list}')
    membership = f'{number} in {list}'
    result = eval(membership)    
    print(f'{membership} result is {result}')
    membership = f'{number} not in {list}'
    result = eval(membership)    
    print(f'{membership} result is {result}')

def main():
    a = 20
    b = 10

    #Printing values first.
    print(f'a={a}')
    print(f'b={b}')

    pratice1functions(a, b, '==')
    pratice1functions(a, b, '>=')
    pratice1functions(a, b, '<=')
    pratice1functions(a, b, '!=')
    pratice1functions(a, b, '>')
    pratice1functions(a, b, '<')

    practice2Assignment(11, '=')
    practice2Assignment(11, '+=')
    practice2Assignment(11, '-=')
    practice2Assignment(11, '*=')
    practice2Assignment(11, '/=')
    practice2Assignment(11, '%=')

    practice3memberships(3)
    practice3memberships(1)
    practice3memberships(0)
    practice3memberships(77)
main()