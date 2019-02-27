from Person import Person

class Employee(Person):
    def __init__(self, firstname, lastname, age, ci, employee_id, department):
        Person.__init__(self, firstname, lastname, age, ci)
        self.employee_id = employee_id
        self.department = department

    def GetEmployee(self):
        return self.Name() + ", " + self.GetPersonAge() + "," + self.employee_id + "," + self.department


person_1 = Person("Naira", "Romero", "25", "2345678")
employee_1 = Employee("Maria", "Perez", "26", "123456", "id_e_123", "Ventas")

print(person_1.Name())
print(employee_1.GetEmployee())
