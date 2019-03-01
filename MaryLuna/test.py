a=10
b=5
print(a+b)
print (a-b)
print (a/b)
print (a*b)
print (a%b)
print (a**b)
print (a==b)


list=[1,2,3,4,5,6,7,8,9]
a=1
if a in list:
    print ("exist a")
else:
    print ("no exist a")

b=44
if (b is not list):
    print ("no exist b")
else:
    print ("exist b")


value1 = 10
value2 = 10

if(value1 is value2):
    print (" value 1 y value 2  same identity")
else:
    print (" value 1 y value 2  not same identity")


value1 =40
if( id(value1) == id(value2)):
    print (" value 1 y value 2  same identity")
else:
    print (" value 1 y value 2  not same identity")



