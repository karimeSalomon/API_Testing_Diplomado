# practice #6

# write a function days_in_month which takes the name of a month, and returns
# the number of days in the month. Ignore leap years:
#   days_in_month("February") == 28
#   days_in_month("December") == 31
# if the function is given invalid arguments, it should return None.

import sys

def days_in_month(month):
    dict={
        'january': 31,
        'february': 28,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31
    }

    return dict.get(month.lower())

if len(sys.argv) < 2:
    print('no value was provided')
    exit()

month = sys.argv[1]

print('days_in_month("{0}") == {1}'.format(month,days_in_month(month)))

