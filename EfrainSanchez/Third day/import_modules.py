import module_age
import module_messages

users = int(input("Ingrese la cantidad de Uusarios:"))
dic = {}
for i in range(users):
    nombre = input(f"Ingrese el nombre del usuario {i+1} :")
    edad = int(input(f"Ingrese la edad de {nombre} :"))
    dic[i] = {"nombre":nombre, "edad":edad}
for i in range(len(dic)):
    day = str(module_age.calculate_age_ondays(dic[i]["edad"]))
    mess = module_messages.message(dic[i]["edad"])
    print("* "+dic[i]["nombre"]+" Es : "+mess+" y de edad en dias tiene : "+day)


