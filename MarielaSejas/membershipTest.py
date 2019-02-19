a = 1
b = 2
list = [1, 2, 3, 4, 5 ]

if ( a in list ):
   print("a exists list")
   a=7
   print("Ahora 'a' tiene el siguiente valor")
   print (a)
else:
   print("a does not exist list")

if ( b not in list ):
    print("b does not exist list")
else:
    print("b exists list")
