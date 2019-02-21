import random

def explain_and_run(number1, number2, operator):
    operation = f'{number1}{operator}{number2}'
    result = eval(operation)
    print(f'{operation}={result}')
    
def explain_and_assign(number, operator):
    initial_value = random.randint(0, 50)
    print('========BEGIN==========')
    print(f'Initial value is {initial_value}')
    assignment = f'a{operator}{number}'
    print(assignment)
    operation = f'a={initial_value}; {assignment}; print("Final value is " + str(a))'
    exec(operation)
    print('========END==========')
    
def explain_and_check_membership(number):
    list = [3, 9, 0, 56, 18, 77]
    print('========BEGIN==========')
    print(f'List is {list}')
    membership = f'{number} in {list}'
    result = eval(membership)    
    print(f'{membership} result is {result}')
    membership = f'{number} not in {list}'
    result = eval(membership)    
    print(f'{membership} result is {result}')
    print('========END==========')    

def main():
    a = 53
    b = 11

    print(f'a={a}')
    print(f'b={b}')
    explain_and_run(a, b, '==')
    explain_and_run(a, b, '!=')
    explain_and_run(a, b, '>')
    explain_and_run(a, b, '<')
    explain_and_run(a, b, '>=')
    explain_and_run(a, b, '<=')
    explain_and_assign(41, '=')
    explain_and_assign(41, '+=')
    explain_and_assign(41, '-=')
    explain_and_assign(41, '*=')
    explain_and_assign(41, '/=')
    explain_and_assign(41, '%=')
    explain_and_check_membership(3)
    explain_and_check_membership(40)
    explain_and_check_membership(0)
    explain_and_check_membership(78)
    print(f'a={a}')
    print(f'b={b}')
    print('a is b result is', eval(f'{a} is {b}'))
    print('a is not b result is', eval(f'{a} is not {b}'))
    a = 13
    b = 13
    print(f'a={a}')
    print(f'b={b}')
    print('a is b result is', eval(f'{a} is {b}'))
    print('a is not b result is', eval(f'{a} is not {b}'))
    

main()