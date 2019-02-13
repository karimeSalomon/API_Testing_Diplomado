a = 2
b = 10
nombre = "Carlos"
lista =[2,5,6,9,1,100,9,20]
nombres = ["carlos", "efra", "Liz"]

print("a = "+str(a))
print("b = "+str(b))
print("nombre = "+nombre)
print(lista)
print(nombres)
if(a in lista):
    print("a existe en la lista")
else:
    print("a no existe en la lista")

if(nombre in nombres):
    print("Carlos existe en la lista")
else:
    print(nombre+ " no existe en la lista")