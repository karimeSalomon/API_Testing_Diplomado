
def days_in_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    months_length = len(months)
    aux = 1
    aux2 = 0
    while aux <= months_length:
        if aux == 8:
            aux2 = 1

        if aux == 2:
            print("The month {0} has  {1} days".format(months[aux-1], 28))
        elif (aux + aux2) % 2 == 0:
            print("The month {0} has  {1} days".format(months[aux-1], 30))
        else:
            print("The month {0} has {1} days".format(months[aux-1], 31))

        aux += 1


days_in_month()
