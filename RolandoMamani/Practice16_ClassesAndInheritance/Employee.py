class Employee:

    employee_id = None
    employee_department = None

    def __init__(self, name, last_name, age, ci, employee_id, employee_department):
        self.employee_id = employee_id
        self.employee_department = employee_department
        super().__init__(firs_name, last_name, age, ci)