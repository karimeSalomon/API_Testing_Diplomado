import operator
texto = input("ingregese un parrafo por favor: ")
midic = {}
for char in texto:
    if char in midic: midic[char]=midic[char]+1
    else: midic[char]=1
print(sorted(midic.items(),key=operator.itemgetter(0)))