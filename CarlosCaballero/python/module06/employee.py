from module05 import Person

class Employee(Person):
    def __init__(self,id,deparment,name,lastname,age,ci):
        Person.__init__(self,name,lastname,age,ci)
        self.Employee_Id = id
        self.Deparment = deparment
        self.type = 'EMPLOYEE'


