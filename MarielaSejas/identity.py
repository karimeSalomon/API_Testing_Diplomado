value_1 = 40
value_2 = 30

if ( value_1 is value_2 ):
   print("Line 1 - a and b have same identity")
   print(id(value_1))
else:
   print('Line 1 - a and b do not have same identity')
   print(id(value_1))

if ( id(value_1) == id(value_2) ):
   print("Line 2 - a and b have same identity")
   print (id(value_2))
else:
   print("Line 2 - a and b do not have same identity")
   print(id(value_2))

