from person import Person


class Employee(Person):
    def __init__(self, name, last_name, age, ci, employee_id, department):
        self.Employee_Id = employee_id
        self.Department = department
        Person.__init__(self, name, last_name, age, ci)
