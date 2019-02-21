def days_in_month(argument):
    switcher = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    return switcher.get(argument, "None")


# call days_in_month
print(days_in_month("January"))
print(days_in_month("February"))
print(days_in_month("TEST"))
