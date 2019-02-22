

def sentMessage (age):
    if age <= 12:
        print('You are a child,')
    elif 12 > age or age <= 17:
        print('Your are teenager')
    elif 17 > age or age <= 29:
        print('You are young')
    else:
        print('You are adult')

while True:
    age = input('[+] Enter your age:  ')
    sentMessage(int (age))



