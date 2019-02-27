from person import Person

class Employee(Person):
    def __init__(self, name, lastname, age, ci, employee_id, department):
        Person.__init__(self, name, lastname, age, ci)
        self.employee_id = employee_id
        self.department = department

    def get_name(self):
        return self.name