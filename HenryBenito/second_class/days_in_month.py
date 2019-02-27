month_days = {"january": 31, "march": 31, "may": 31, "july": 31, "august": 31, "october": 31,
              "december": 31, "april": 30, "june": 30, "september": 30, "november": 30, "february": 28}


def days_in_month(month_name):
    return month_days.get(month_name.lower())


print(days_in_month("january"))
print(days_in_month("february"))
print(days_in_month("november"))
print(days_in_month("another"))
