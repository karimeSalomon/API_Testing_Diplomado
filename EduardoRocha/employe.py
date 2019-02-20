from API_Testing_Diplomado.EduardoRocha.person import Person


class Employee(Person):
    def __init__(self, Name, LastName, Age, CI, Employee_Id, Department):
        self.EmployeeId = Employee_Id
        self.Department = Department
        Person.__init__(self, Name, LastName, Age, CI)

