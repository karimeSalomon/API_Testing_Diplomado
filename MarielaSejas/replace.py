#Sin usar el metodo reemplazar

def replace(string, old, new):

    for x in string:
        if  x ==old:
            print(string)
        else:
            print("")
replace("This is a examzle with string that will be rezlace the old with new word", "z", "p")


#usando el metodo reemplazar
s="This is a examzle with string that will be rezlace the old with new word"
print (s.replace("z","p"))




