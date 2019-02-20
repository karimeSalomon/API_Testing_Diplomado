# Implement the class Person and the subclass employee considering that person will have:
#   Name
#   Last Name
#   Age
#   CI
# 
# Employee will have:
#   Employee_Id
#   Department
# 
# Define both classes into different modules.

from person import Person

class Employee (Person):

    def __init__(self, name, last_name, age, ci, employee_id, department):
        super().__init__(name, last_name, age, ci)
        self.employee_id = employee_id
        self.department = department

