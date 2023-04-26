from src.employee.models import Employee
from src.employee.schemas import (
    EmployeeAccount,
    EmployeeCreate,
    EmployeeCurrentSeniorityLevel,
    EmployeeRole,
    EmployeeSeniorityLevel,
    EmployeeSeniorityLevels,
    EmployeeSkills,
    EmployeeUpdate,
    EmployeeRequests,
)


def to_employee_skills(employee: Employee) -> EmployeeSkills:
    role_data = employee.dict()
    role_data["skills"] = []
    return EmployeeSkills(**role_data)


def to_employee_role(employee: Employee) -> EmployeeRole:
    role_data = employee.dict()
    role_data["role"] = employee.role
    return EmployeeRole(**role_data)


def to_employee_requests(employee: Employee) -> EmployeeRequests:
    role_data = employee.dict()
    role_data["requests"] = employee.requests
    return EmployeeRequests(**role_data)


def to_employee_account(employee: Employee) -> EmployeeAccount:
    role_data = employee.dict()
    role_data["account"] = employee.account
    return EmployeeAccount(**role_data)


def tuple_to_employee_seniority_level(employee_seniority_level: tuple):
    attributes = [
        "role_seniority_level_id",
        "level",
        "seniority_level_name",
        "role_name",
        "description",
        "attainment_date",
    ]
    employee_seniority_level_dict = dict(zip(attributes, employee_seniority_level))
    return EmployeeSeniorityLevel(**employee_seniority_level_dict)


def to_employee_seniority_levels(employee: Employee) -> EmployeeSeniorityLevels:
    role_data = employee.dict()
    role_data["seniority_levels"] = []
    return EmployeeSeniorityLevels(**role_data)


def to_employee_current_seniority_level(employee: Employee) -> EmployeeCurrentSeniorityLevel:
    role_data = employee.dict()
    role_data["seniority_level"] = None
    return EmployeeCurrentSeniorityLevel(**role_data)


def to_employee(employee: EmployeeCreate) -> Employee:
    return Employee(**employee.dict(exclude_unset=True))


def update_employee(employee_db: Employee, employee_update: EmployeeUpdate) -> Employee:
    employee_data = employee_update.dict(exclude_unset=True)
    for key, value in employee_data.items():
        setattr(employee_db, key, value)
    return employee_db
