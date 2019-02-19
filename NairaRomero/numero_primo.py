
def determinar_si_es_numero_primo(num):


    aux =2
    while aux<num:
        if num%(aux)!=0 or num == (aux+1):
            aux+=1
        else:
            print("No es un mumero primo: ", num)
            break
    else:
        print("Es un munero primo", num)


#determinar_si_es_numero_primo(num):


def econtrar_numeros_Primos(num):
    for i in range(1, num):
        determinar_si_es_numero_primo(i)


econtrar_numeros_Primos(56