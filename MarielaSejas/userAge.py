import calculateAge
import messageAge

def user():
    nuser=0
    while nuser<=0:
        nuser=int(input("Ingresa la cantidad de usuarios que quieras añadir: "))

    duser = {}
    for i in range(nuser):
        nombre= input("Insert the name of user: ")
        edad  = int(input("Insert the age of user: "))
        duser[nombre] = edad
        duser[edad]=calculateAge.calculate_age(edad)
        duser['']=messageAge.message(edad)
    #print("Los datos de los usuarios ingresados son:"+ str(duser))
    #print ("Las edad calculada en dias, horas y minutos es:"+ str(calculateAge.calculate_age(edad)))
    #print(messageAge.message(edad))


user()