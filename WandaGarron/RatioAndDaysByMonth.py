import math

def area_of_circle(r):
    if r > 10:
        return math.pi * r**2


months = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

def days_by_month(month):
    print("The number of days for {0} is {1}".format(month, months.get(month.lower(), None)))

days_by_month("JULY")