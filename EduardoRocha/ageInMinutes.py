def calculeYears(year):
    day = year * 365.25
    hour = day * 24
    minute = hour * 60

    print(day, hour, minute)


year = input('[+] Enter year:  ')
calculeYears(int(year))
