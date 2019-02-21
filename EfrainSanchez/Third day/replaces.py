texto = input("Ingrese un texto porfavor:")
char = input("Ingrese un caracter a reemplazar:")
char_new = input("Ingrese el  nuevo Caracter que reemplazara  a "+char+" :")
def replace(texto,char,char_new):
    print(texto.replace(char,char_new))
replace(texto,char,char_new)
