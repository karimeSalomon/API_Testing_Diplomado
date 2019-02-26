import math

def odd_or_even(number):
    result = 'even' if number % 2 == 0 else 'odd'
    print(f'{number} is {result}')
    
def is_prime(number):
    if number % 2 == 0 and number > 2: 
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))

def generate_prime_numbers(min, max):
    prime_numbers = []
    for i in range(min, max):
        if is_prime(i):
            prime_numbers.append(i) 
            
    return prime_numbers

def main():
    #odd or even? 
    odd_or_even(20)
    odd_or_even(3)

    #isPrime?? 
    result = is_prime(20)
    print(result)
    result = is_prime(15)
    print(result)

    #generating numbers
    print(generate_prime_numbers(0, 50))
main()