from sqlmodel import Session, select

from src.db import engine
from src.employee.models import Employee
from src.employee.schemas import EmployeeCreate, EmployeeUpdate
from src.role.models import Role
from src.role.service import get as get_role


def get(employee_id: int):
    with Session(engine) as session:
        statement = select(Employee).where(Employee.id == employee_id)
        result = session.exec(statement)
        try:
            return result.one()
        except Exception:
            raise Exception(f"Employee with id {employee_id} does not exist")


def get_all():
    with Session(engine) as session:
        statement = select(Employee)
        result = session.exec(statement)
        return result.all()


def create(employee: EmployeeCreate):
    # TODO: use a mapper
    employee_db = Employee(**employee.dict(exclude_unset=True))
    with Session(engine) as session:
        get_role(employee.role_id)
        session.add(employee_db)
        session.commit()
        session.refresh(employee_db)
        return employee_db


def update(employee_id: int, employee: EmployeeUpdate):
    with Session(engine) as session:
        employee_db = session.get(Employee, employee_id)
        if not employee_db:
            raise Exception(f"Employee with id {employee_id} does not exist")
        get_role(employee.role_id)
        # TODO: move into a generic function (maybe a mapper)
        employee_data = employee.dict(exclude_unset=True)
        for key, value in employee_data.items():
            setattr(employee_db, key, value)

        session.commit()
        session.refresh(employee_db)
        return employee_db


def delete(employee_id: int):
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            raise Exception(f"Employee with id {employee_id} does not exist")
        session.delete(employee)
        session.commit()
        return employee
