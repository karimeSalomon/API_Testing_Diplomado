def text_url():
    texto = input("Ingrese un texto que contenga url : ")
    begin = texto.find("http")
    size = len(texto)
    texto2 = texto[begin:size]
    end = texto2.find(" ")
    print(texto[begin:begin+end])

text_url()