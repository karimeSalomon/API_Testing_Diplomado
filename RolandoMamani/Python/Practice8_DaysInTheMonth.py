"""
Practice 8:
    - Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore leap years:
            * days_in_month("February") == 28
            * days_in_month("December") == 31

    - If the function is given invalid arguments, it should return None.
"""

monthsWith31Days = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
monthsWith30Days = ['April', 'June', 'September', 'November']

def days_in_month(month):

    if(month == 'February'):
        return "28"
    else:
        if(month in monthsWith30Days):
            return "30"
        else:
            if(month in monthsWith31Days):
                return "31"
            else:
                return


def inputMonth():
    month_entered = input("Enter the name of month. E.g. January:  ")
    result = days_in_month(month_entered)
    if(result != None): print("Days in " + month_entered + " = " + days_in_month(month_entered))
    else: print("Wrong month name entered, please it should be a valid name of month")

inputMonth()
