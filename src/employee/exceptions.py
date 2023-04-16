
class EmployeeNotFound(Exception):
    def __init__(self, employee_id: int):
        self.employee_id = employee_id
        self.message = f"Employee with id {employee_id} does not exists"
        super().__init__(self.message)
