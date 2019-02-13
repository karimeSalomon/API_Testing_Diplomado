def numeroParImpar(numero):
    if (numero%2 == 0):
        print(numero, 'es un numero par')
    else:
        print(numero, 'es un numero impar')


while True:
    numero1=input('[+] Enter a number')

    numeroParImpar(int(numero1))





