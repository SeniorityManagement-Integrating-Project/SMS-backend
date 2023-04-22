from typing import List
from sqlmodel import Session, col, select
from sqlalchemy.exc import IntegrityError
from src.employee.queries import employee_seniority_levels_query

from src.db import engine
from src.employee.exceptions import EmployeeNotFound
from src.employee.models import Employee
from src.employee.schemas import (
    EmployeeAccount,
    EmployeeCreate,
    EmployeeCurrentSeniorityLevel,
    EmployeeRequests,
    EmployeeRole,
    EmployeeSeniorityLevels,
    EmployeeSkills,
    EmployeeUpdate,
)
from src.role.exceptions import RoleNotFound
from src.employee.mappers import (
    to_employee,
    to_employee_account,
    to_employee_current_seniority_level,
    to_employee_requests,
    to_employee_role,
    to_employee_seniority_levels,
    to_employee_skills,
    tuple_to_employee_seniority_level,
    update_employee,
)
from src.role.models import Role


def get_all() -> List[Employee]:
    with Session(engine) as session:
        statement = select(Employee)
        result = session.exec(statement)
        return result.all()


def get(employee_id: int) -> Employee:
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            raise EmployeeNotFound(employee_id)
        return employee


def get_by_email(email: str) -> Employee:
    with Session(engine) as session:
        statement = select(Employee).where(Employee.email == email)
        result = session.exec(statement)
        employee = result.first()
        if not employee:
            raise EmployeeNotFound(email, "email")
        return employee


def get_by_role_id(role_id: int) -> List[Employee]:
    with Session(engine) as session:
        role = session.get(Role, role_id)
        if not role:
            raise RoleNotFound(role_id)
        statement = select(Employee).where(Employee.role_id == role_id)
        result = session.exec(statement)
        employees = result.all()
        return employees


def search_by_name(name: str) -> List[Employee]:
    with Session(engine) as session:
        statement = select(Employee).where(col(Employee.name).ilike(f"%{name}%"))
        result = session.exec(statement)
        employees = result.all()
        return employees


def create(employee: EmployeeCreate) -> Employee:
    employee_db = to_employee(employee)
    with Session(engine) as session:
        try:
            session.add(employee_db)
            session.commit()
            session.refresh(employee_db)
            return employee_db
        except IntegrityError as exc:
            raise RoleNotFound(employee.role_id) from exc


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


def get_employee_seniority_levels(employee_id: int):
    with Session(engine) as session:
        statement = employee_seniority_levels_query(employee_id)
        result = session.execute(statement).all()  # type: ignore
        return result


def get_employee_current_seniority_level(employee_id: int):
    with Session(engine) as session:
        statement = employee_seniority_levels_query(employee_id)
        result = session.execute(statement)  # type: ignore
        seniority_level = result.first()
        return seniority_level


def get_with_seniority_levels(employee_id: int) -> EmployeeSeniorityLevels:
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            raise EmployeeNotFound(employee_id)
        employee = to_employee_seniority_levels(employee)
        seniority_levels = get_employee_seniority_levels(employee_id)
        print(seniority_levels)
        employee.seniority_levels = [
            tuple_to_employee_seniority_level(seniority_level)
            for seniority_level in seniority_levels
        ]
        return employee


def get_with_current_seniority_level(employee_id: int) -> EmployeeCurrentSeniorityLevel:
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            raise EmployeeNotFound(employee_id)
        employee = to_employee_current_seniority_level(employee)
        seniority_level = get_employee_current_seniority_level(employee_id)
        if seniority_level:
            employee.seniority_level = tuple_to_employee_seniority_level(seniority_level)
        return employee


def get_with_account(employee_id: int) -> EmployeeAccount:
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            raise EmployeeNotFound(employee_id)
        return to_employee_account(employee)


def get_with_role(employee_id: int) -> EmployeeRole:
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            raise EmployeeNotFound(employee_id)
        return to_employee_role(employee)


def get_with_requests(employee_id: int) -> EmployeeRequests:
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            raise EmployeeNotFound(employee_id)
        return to_employee_requests(employee)


def get_with_skills(employee_id: int) -> EmployeeSkills:
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            raise EmployeeNotFound(employee_id)
        employee_with_skills = to_employee_skills(employee)
        approved_requests = filter(lambda request: request.approved == True, employee.requests)
        skills = [request.skill for request in approved_requests]
        employee_with_skills.skills = skills
        return employee_with_skills
