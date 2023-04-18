from sqlmodel import Session, select
from src.db import engine
from src.employee.exceptions import EmployeeNotFound
from src.employee.models import Employee
from src.interaction.exceptions import InteractionAlreadyExists, InteractionNotFound
from src.interaction.models import Interaction
from sqlalchemy.exc import IntegrityError


def create(employee_from_id: int, employee_to_id: int):
    with Session(engine) as session:
        employee_from = session.get(Employee, employee_from_id)
        employee_to = session.get(Employee, employee_to_id)
        if not employee_from:
            raise EmployeeNotFound(employee_from_id)
        if not employee_to:
            raise EmployeeNotFound(employee_to_id)
        interaction = Interaction(employee_from_id=employee_from_id, employee_to_id=employee_to_id)
        try:
            session.add(interaction)
            session.commit()
        except IntegrityError as exc:
            raise InteractionAlreadyExists(employee_from_id, employee_to_id) from exc
        session.refresh(interaction)
        return interaction


def delete(employee_from_id: int, employee_to_id: int):
    with Session(engine) as session:
        employee_from = session.get(Employee, employee_from_id)
        employee_to = session.get(Employee, employee_to_id)
        interaction = session.get(Interaction, (employee_from_id, employee_to_id))
        if not employee_from:
            raise EmployeeNotFound(employee_from_id)
        if not employee_to:
            raise EmployeeNotFound(employee_to_id)
        if not interaction:
            raise InteractionNotFound(employee_from_id, employee_to_id)
        session.delete(interaction)
        session.commit()
        return interaction


def get_all():
    with Session(engine) as session:
        statement = select(Interaction)
        result = session.exec(statement)
        return result.all()


def get_by_employee_to(employee_to_id: int):
    with Session(engine) as session:
        employee = session.get(Employee, employee_to_id)
        if not employee:
            raise EmployeeNotFound(employee_to_id)
        statement = select(Interaction).where(Interaction.employee_to_id == employee_to_id)
        result = session.exec(statement)
        return result.all()


def get_by_employee_from(employee_from_id: int):
    with Session(engine) as session:
        employee = session.get(Employee, employee_from_id)
        if not employee:
            raise EmployeeNotFound(employee_from_id)
        statement = select(Interaction).where(Interaction.employee_from_id == employee_from_id)
        result = session.exec(statement)
        return result.all()
