#Create 1 script to determine is a number is odd or even (use single line statement if applies)
def is_odd_or_even(n):
    if (n % 2 == 0):
        print('is even')
    else:
        print('is odd')

is_odd_or_even(4)
is_odd_or_even(19)


#According a list of values between a Min and Max range, identify if the number is prime or not.

from math import pi as PI
#Write a function area_of_circle(r) which returns the area of a circle of radius r only if the radius value is greater of 10.
def area_of_circle(r):
    if(r > 10):
        return PI * r * r
    else:
        return -1

area_of_circle(5)
area_of_circle(20)

#Write a function sum_to(n) that returns the sum of all integer numbers up to and including only
# until any value lower than 35. So sum_to(10)wouldbe1+2+3...+10which would return the value 55,
# but if n=40 only until sum to 35 need to be returned.
def sum_to(n):
    sum = 0
    if(n > 35): n = 35
    for t in range(1, n+1):
        sum = sum + t
    print(sum)

sum_to(5)
sum_to(36)







