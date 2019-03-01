text = "qe  WQQW SDFGhttps://medium.com/@eddydecena/validando-si-un-n%C3%BAmero-es-primo-en-python-a622cf6b4363 "

len = len(text)
print len
print (text[len-1])
print (text[0:8])
print (text.find("http"))

if(" " in text):
    print ("hay espacio url no valida")
if("http" in text):
    print ("hay http")




