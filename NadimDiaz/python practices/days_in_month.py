
def days_in_month(month):
    month_days=[('January',[31]),('February',[28,29]),('March',[31]),('April',[30]),('May',[31]),('June',[30]),('July',[31]),('August',[31]),('September',[30]),('October',[31]),('November',[30]),('December',[31])]
    for i in month_days:
        if month==i[0]:
            return i[1]
    return "None"

def main():
    #days in month
    print("days in February:", days_in_month("February"))
    print("days in March:", days_in_month("March"))
main()