import math

def say_odd_or_even(number):
    result = 'even' if number % 2 == 0 else 'odd'
    print(f'{number} is {result}')
    
def is_prime(number):
    if number > 1:
       for i in range(2, int(math.sqrt(number)) + 1):
           if (number % i) == 0:
               return False
       else:
           return True
    else:
       return False

def generate_prime_numbers(min, max):
    prime_numbers = []
    for i in range(min, max):
        if is_prime(i):
            prime_numbers.append(i) 
            
    return prime_numbers
    
say_odd_or_even(33)
say_odd_or_even(22)
print(generate_prime_numbers(0, 100))