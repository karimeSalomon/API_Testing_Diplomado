# practice #14

# implement the class Person and the subclass employee considering that
# Person will have:
#     Name
#     Last Name
#     Age
#     CI
#
# Employee will have:
#     Employee_Id
#     Department
#
# Define both classes into different modules.

from module05 import Person
from module06 import Employee

person = Person('Carlos','Caballero',34,'45934556')
print(person)

employee = Employee('CF04','ADM','Jose Luis','Perez',37,'95349956')
print(employee)

