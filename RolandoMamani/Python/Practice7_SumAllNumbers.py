"""
Practice 7:     Write a function sum_to(n) that returns the sum of all integer numbers up to and including only until
                any value lower than 35. So sum_to(10)wouldbe1+2+3...+10which would return the value 55,
                but if n=40 only until sum to 35 need to be returned.  .
"""

def sum_to(n):
    result = 0
    iterator = 35
    if (n <= 35): iterator = n
    for i in range(1, iterator+1):
        result += i
    return result

print(sum_to(int(input("The sum of the numbers will be done, from 1 to the number that you enter \n"
                 "Note: the entered value should be less than or equal to 35, in the other hand it will applied the sum just until 35\n"
                 "Please enter the number:  "))))