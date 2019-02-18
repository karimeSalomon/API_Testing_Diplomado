def function1():
    array = [None]*int(input("Ingrese El Tamaño del array Principal:"))
    for a in range(len(array)):
        array[a] = [None]*int(input(f"Ingrese El Tamaño del Array en la Posicion {a+1} :"))
    return array
def function2(array):
    for i in range(len(array)):
        print(array[i])
function2(function1())