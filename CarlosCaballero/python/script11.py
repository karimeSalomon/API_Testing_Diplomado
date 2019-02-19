# practice #9

# function 1:
# no arguments defined
# should ask to the user the number of elements in the list
# according the value inserted ask for each value of the array 
# and push it in a new array
# return the array
#
# function 2
# should receive 1 argument (the array returned in method 1)
# Should print the array

def function1():
    print('Ingrese el tamaño de la lista')
    count = input()
    list = []

    if str.isdigit(count):
        count = int(count)

        for i in range(count):
            value = ''
            while not str.isdigit(value):
                print('=> Ingrese el valor numero',i+1)
                value = input()
            list.append(value)
    else:
        print('Numero invalido')
    return list

def function2(array):
    for i,value in enumerate(array):
        print(i,' => ',value)

function2(function1())

