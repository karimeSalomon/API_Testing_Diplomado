a = 50
b = 50
c = "German"
d = "german"

print("valor de a = "+str(a))
print("valor de b = "+str(b))
print("Valor de c = "+c)
print("Valor de d = "+d)

if(a is b):
    print(" los valores de a y b son IDENTICOS")
else:
    print("Los valores de a y b son DIFERENTES")
print("--------------------------------")
if(id(c)==id(d)):
    print(" los valores de id(c) y id(d) son identicos")
else:
    print(" los valores de id(c) y id(d) son diferentes")