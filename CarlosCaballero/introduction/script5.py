# practice #3

# According a list of values between a Min and Max range, identify if the number
# is prime or not

import math
import sys

def isprime(number):
    if number < 2:
        return False
    else:
        for value in range(2,math.floor(math.sqrt(number))+1):
            if number % value == 0:
                return False
        return True

# input: two positive integers
# output: set of primes in range
min = sys.argv[1]
max = sys.argv[2]
valid = True

if not str.isdigit(min):
    print('argument1 is not a number')
    valid = False

if not str.isdigit(max):
    print('argument2 is not a number')
    valid = False

if not valid:
    exit()

min = int(min)
max = int(max)
result = []

for value in range(min,max):
    if isprime(value):
        result.append(value)

print('primes in range [{0},{1}] are:'.format(min,max))
print(result)

