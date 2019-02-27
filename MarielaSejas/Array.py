#Array sin argumentos definidos
def list1():
    li=[] #variable local
    for x in range(5): #llamamos a un for que se repita 5 veces
        valor=int (input("Ingrese valor:"))
        li.append(valor)
    return li



def imprimir(li):
    print ("Los elementos ingresados al array son los siguientes")
    for x in range(len(li)):
        print (li[x])

lista=list1()
imprimir(lista)

#Imprimiendo la lista que se esta recibiendo
def lista(list):
    for l in list:
         print (l)

lista([1, 2, 3, "Ana", "Panama"])