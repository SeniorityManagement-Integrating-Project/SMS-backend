from src.employee.models import Employee
from src.employee.schemas import EmployeeCreate, EmployeeUpdate


def to_employee(employee: EmployeeCreate) -> Employee:
    return Employee(**employee.dict(exclude_unset=True))


def update_employee(employee_db: Employee, employee: EmployeeUpdate) -> Employee:
    employee_data = employee.dict(exclude_unset=True)
    for key, value in employee_data.items():
        setattr(employee_db, key, value)
    return employee_db
