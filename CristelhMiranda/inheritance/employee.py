from API_Testing_Diplomado.CristelhMiranda.inheritance.person import Person


class Employee(Person):
    def __init__(self, name, last_name, age, ci, employee_id, department):
        super().__init__(name, last_name, age, ci)
        self.department = department
        self.employee_id = employee_id

    def __str__(self):
        employee_str = super().__str__()
        employee_str += f", employee_id {self.employee_id}, " \
            f"Department: {self.department}"
        return employee_str


person1 = Person("Juan", "Perez", 25, 123455)
employee1 = Employee("Pedro", "Paredes", 23, 98765, 4567, "Testing")

print(person1)
print(employee1)
