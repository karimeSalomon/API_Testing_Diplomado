# practice #2

# Create 1 script to determinate is a number odd or even (use single line
# statement if applies)

import sys

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

if str.isdigit(sys.argv[1]):
    number = int(sys.argv[1])
    if isEven(number):
        print(str(number)+' is even')
    else:
        print(str(number)+' is odd')
else:
    print('argument is not a number')

