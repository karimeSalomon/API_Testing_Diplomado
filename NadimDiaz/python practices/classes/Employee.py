import Person

class Employee(Person.Person):

    def __init__(self, name, lastName, age, CI, employee_id, department):
        super(self,name, lastName, age, CI)
        self.employee_id = employee_id
        self.department = department
