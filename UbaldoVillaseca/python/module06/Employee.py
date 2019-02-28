from module05.Person import *

class Employee(Person):
  def __init__(self, first_name, last_name, age, ci, employee_id, department):
    super().__init__(first_name, last_name, age, ci)
    self.employee_id = employee_id
    self.department = department
    
  def GetEmployee(self):
    return f'{self.Name()}, {self.employee_id}'