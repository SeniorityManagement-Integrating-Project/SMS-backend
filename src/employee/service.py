from typing import List
from sqlmodel import Session, select
from sqlalchemy.exc import NoResultFound, IntegrityError
from src.employee.queries import employee_seniority_levels_query

from src.db import engine
from src.employee.exceptions import EmployeeNotFound
from src.employee.models import Employee
from src.employee.schemas import EmployeeCreate, EmployeeUpdate
from src.role.exceptions import RoleNotFound
from src.role.service import get as get_role
from src.employee.mappers import to_employee, update_employee
from src.seniority_level.models import SeniorityLevel


def get_all() -> List[Employee]:
    with Session(engine) as session:
        statement = select(Employee)
        result = session.exec(statement)
        return result.all()


def get(employee_id: int) -> Employee:
    with Session(engine) as session:
        statement = select(Employee).where(Employee.id == employee_id)
        result = session.exec(statement)
        try:
            return result.one()
        except NoResultFound as exception:
            raise EmployeeNotFound(employee_id) from exception


def create(employee: EmployeeCreate) -> Employee:
    employee_db = to_employee(employee)
    with Session(engine) as session:
        get_role(employee.role_id)
        session.add(employee_db)
        session.commit()
        session.refresh(employee_db)
        return employee_db


def update(employee_id: int, employee: EmployeeUpdate) -> Employee:
    with Session(engine) as session:
        employee_db = session.get(Employee, employee_id)
        if not employee_db:
            raise EmployeeNotFound(employee_id)
        update_employee(employee_db, employee)
        try:
            session.commit()
        except IntegrityError as exc:
            raise RoleNotFound(employee_id) from exc
        session.refresh(employee_db)
        return employee_db


def delete(employee_id: int) -> Employee:
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            raise EmployeeNotFound(employee_id)
        session.delete(employee)
        session.commit()
        return employee


def get_employee_seniority_levels(employee_id: int) -> List[SeniorityLevel]:
    with Session(engine) as session:
        statement = employee_seniority_levels_query(employee_id)
        result = session.execute(statement).all()  # type: ignore
        return result
