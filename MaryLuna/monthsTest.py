

months = {
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


def days_month(month):
    return months.get(month, None)

def test():
    month = "February"
    print("Days in", month, days_month(month))
    month = "June"
    print("Days in", month, days_month(month))
    month = "Wednesday"
    print("Days in", month, days_month(month))
    month = "January"
    print("Days in", month, days_month(month))
    month = "May"
    print("Days in", month, days_month(month))
    month = "Saturday"
    print("Days in", month, days_month(month))
    month = "August"
    print("Days in", month, days_month(month))


test()