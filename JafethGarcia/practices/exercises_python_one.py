from datetime import datetime
from calendar import monthrange


def area_of_circle(r):
    """ Write a function area_of_circle(r) which returns the area of a circle
    of radius r only if the radius value is greater of 10. """
    radius = int(r)
    if radius <= 10:
        return print('radius must be greater than 10')
    return 3.14 * radius**2


def sum_to(n):
    """ Write a function sum_to(n) that returns the sum of all integer numbers
    up to and including only until any value lower than 35.
    So sum_to(10) would be 1+2+3...+10 which would return the value 55,
    but if n=40 only until sum to 35 need to be returned. """
    number = n + 1 if n <= 35 else 36
    sumto = 0
    for i in range(1, number):
        sumto += i
    return sumto


def days_in_moth(month):
    """
    Write a function days_in_month which takes the name of a month, and
    returns the number of days in the month. Ignore leap years:
    days_in_month("February") == 28
    days_in_month("December") == 31
    If the function is given invalid arguments, it should return None.
    """
    month = month.lower()
    months = {
      "unknown": 0,
      "january": 1,
      "february": 2,
      "march": 3,
      "april": 4,
      "may": 5,
      "june": 6,
      "july": 7,
      "august": 8,
      "september": 9,
      "october": 10,
      "november": 11,
      "december": 12
    }
    current = datetime.now()
    return monthrange(current.year, months.get(month))[1]


print('area_of_circle(10)', area_of_circle(10))
print('area_of_circle(15)', area_of_circle(15))

print('sum_to(10)', sum_to(10))
print('sum_to(40)', sum_to(40))
print('sum_to(35)', sum_to(35))
print('sum_to(80)', sum_to(80))

print('days_in_moth("February")', days_in_moth("February"))
print('days_in_moth("December")', days_in_moth("December"))
