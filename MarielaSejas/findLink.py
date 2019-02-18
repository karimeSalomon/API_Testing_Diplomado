import re

myString = "My primer ejemplo buscando el siguiente link  http://example.com/blah"
print(re.search("(?P<url>https?://[^\s]+)", myString).group("url"))


#Otro ejemplo para buscar un link en la cadena

string = "My primer ejemplo buscando el siguiente link  http://example.com/blah"
buscarLink = "htt://example.com/blah"
if string.find(buscarLink) is not -1:
	print("El link fue encontrado " +buscarLink )
else:
	print("El link no fue encontrado")