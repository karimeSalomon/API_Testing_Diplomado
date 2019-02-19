import Person
class Employee(Person):

    def __init__(self, first, last, age, ci, e_id, e_department):
        # Person.__init__(self,first, last, age, ci)
        super().__init__(first, last, age, ci)
        self.employee_id = e_id
        self.employee_department = e_department

    def GetEmployee(self):
        return self.Name() + ", " +  str(self.employee_id)

person = Person("Juan", "Sejas", 40, 53697521)

employee = Employee("Raul", "Orellana", 40, 435982355, 1007, "HHRR")

print(person.Name())
print(employee.GetEmployee())