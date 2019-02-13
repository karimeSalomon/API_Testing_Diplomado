# practice #5

# write a function sum_to(n) that returns the sum of all integer numbers up
# to and including only until any value lower than 35.
# So sum_to(10) would be 1+2+3...+10 which would return the value 55,
# but if n=40 only until sum to 35 need to be returned.

import sys

def sum_to(n):
    return int((n * (n + 1)) / 2)

n = sys.argv[1]

if not str.isdigit(n):
    print('argument is not a number')
    exit()

n = int(n)

if(n > 35):
    n = 35

print(sum_to(n))

