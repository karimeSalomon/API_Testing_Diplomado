def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

def calculate_prim(num1, num2):
    # list = [i for i in range(num1, num2)]
    result = []
    for num in range(num1,num2):
        if is_prime_number(num):
            result.append(num)

    return result

num1 = input('[+] Enter min value: ')
num2 = input('[+] Enter max value: ')

num1 = 0 if  num1 == '' else int(num1)

prime_numbers = calculate_prim(num1, int(num2))

print(prime_numbers)
