entrada= input("Introduce un texto: ")
diccionario = {}

for letra in entrada:
  if letra in diccionario :
     diccionario[letra] = diccionario[letra] + 1
  else:
     diccionario[letra] = 1
print (diccionario)
