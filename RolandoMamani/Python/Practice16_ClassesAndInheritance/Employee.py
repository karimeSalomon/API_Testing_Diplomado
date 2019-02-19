import Person as Person

class Employee(Person):

    employee_id = None
    employee_department = None

    def __init__(self, first_name, last_name, age, ci, employee_id, employee_department):
        super().__init__(first_name, last_name, age, ci)
        self.employee_id = employee_id
        self.employee_department = employee_department

    def getEmployee(self):
        return self.name() + "," + self.employee_id


x = Person("rolando", "mamani", "45", "4578541")
print(x.name())
