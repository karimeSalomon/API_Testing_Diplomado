# Write a function days_in_month which takes the
# name of a month, and returns the number of days in
# the month. Ignore leap years:
#
# days_in_month("February") == 28
# days_in_month("December") == 31
#
# If the function is given invalid arguments, it should
# return None.

from datetime import datetime, date
import calendar

def days_in_month(monthName):
    """
    Prints the number of days given the name of a month
    :param monthName:
    :return:
    """

    try:
        year = date.today().year
        month = datetime.strptime(monthName, '%B').month
        print(calendar.monthrange(year, month)[1])

    except ValueError:
        print("None")


days_in_month('Pluton')

days_in_month('May')

days_in_month('September')