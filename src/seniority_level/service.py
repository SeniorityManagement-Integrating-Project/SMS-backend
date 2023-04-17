from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from src.db import engine
from src.seniority_level.exceptions import SeniorityLevelAlreadyExist, SeniorityLevelNotFound
from src.seniority_level.models import SeniorityLevel
# from src.role.schemas import RoleCreate, RoleSeniorityLevels, RoleUpdate, RoleEmployees
from src.seniority_level.schemas import SeniorityLevelCreate
# from src.role.mappers import to_role, to_role_seniority_levels, update_role, to_role_employees
from src.seniority_level.mappers import to_seniority_level


def get_all() -> list[SeniorityLevel]:
    with Session(engine) as session:
        statement = select(SeniorityLevel)
        result = session.exec(statement)
        return result.all()


def get(seniority_level_id: int) -> SeniorityLevel:
    with Session(engine) as session:
        statement = select(SeniorityLevel).where(
            SeniorityLevel.id == seniority_level_id)
        result = session.exec(statement)
        try:
            return result.one()
        except NoResultFound as exception:
            raise SeniorityLevelNotFound(seniority_level_id) from exception


def create(seniority_level: SeniorityLevelCreate) -> SeniorityLevel:
    seniority_level_db = to_seniority_level(seniority_level)
    with Session(engine) as session:
        # statement = select(SeniorityLevel).where(Role.name == role.name)
        # result = session.exec(statement)
        # if result.one_or_none():
        #     raise RoleAlreadyExists(role.name)
        session.add(seniority_level_db)
        session.commit()
        session.refresh(seniority_level_db)
        return seniority_level_db


"""
def get_with_employees(role_id: int) -> RoleEmployees:
    with Session(engine) as session:
        statement = select(Role).where(Role.id == role_id)
        result = session.exec(statement)
        try:
            return to_role_employees(result.one())
        except NoResultFound as exception:
            raise RoleNotFound(role_id) from exception
        

def get_with_seniority_levels(role_id: int) -> RoleSeniorityLevels:
    with Session(engine) as session:
        statement = select(Role).where(Role.id == role_id)
        result = session.exec(statement)
        try:
            return to_role_seniority_levels(result.one())
        except NoResultFound as exception:
            raise RoleNotFound(role_id) from exception





def update(role_id: int, role: RoleUpdate) -> Role:
    with Session(engine) as session:
        role_db = session.get(Role, role_id)
        if not role_db:
            raise RoleNotFound(role_id)
        update_role(role_db, role)
        session.commit()
        session.refresh(role_db)
        return role_db


def delete(role_id: int) -> Role:
    with Session(engine) as session:
        role = session.get(Role, role_id)
        if not role:
            raise RoleNotFound(role_id)
        session.delete(role)
        session.commit()
        return role
"""
