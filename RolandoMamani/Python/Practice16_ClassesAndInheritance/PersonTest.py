
class Person:

    def __init__(self, first, last, age, ci):
        self.firstname = first
        self.lastname = last
        self.age = age
        self.ci = ci

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, age, ci, e_id, e_department):
        # Person.__init__(self,first, last, age, ci)
        super().__init__(first, last, age, ci)
        self.employee_id = e_id
        self.employee_department = e_department

    def GetEmployee(self):
        return self.Name() + ", " +  str(self.employee_id)

x = Person("Juan", "Sejas", 40, 53697521)
y = Employee("Raul", "Orellana", 40, 435982355, 1007, "HHRR")

print(x.Name())
print(y.GetEmployee())
