from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from src.db import engine
from src.seniority_level.exceptions import SeniorityLevelAlreadyExist, SeniorityLevelNotFound
from src.seniority_level.models import RoleSeniorityLevel
# from src.role.schemas import RoleCreate, RoleSeniorityLevels, RoleUpdate, RoleEmployees
from src.seniority_level.schemas import SeniorityLevelCreate, SeniorityLevelUpdate
# from src.role.mappers import to_role, to_role_seniority_levels, update_role, to_role_employees
from src.seniority_level.mappers import to_seniority_level, update_seniority_level


def get_all() -> list[RoleSeniorityLevel]:
    with Session(engine) as session:
        statement = select(RoleSeniorityLevel)
        result = session.exec(statement)
        return result.all()


def get(seniority_level_id: int) -> RoleSeniorityLevel:
    with Session(engine) as session:
        statement = select(RoleSeniorityLevel).where(
            RoleSeniorityLevel.id == seniority_level_id)
        result = session.exec(statement)
        try:
            return result.one()
        except NoResultFound as exception:
            raise SeniorityLevelNotFound(seniority_level_id) from exception


def create(seniority_level: SeniorityLevelCreate) -> RoleSeniorityLevel:
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


def update(seniority_level_id: int, seniority_level: SeniorityLevelUpdate) -> RoleSeniorityLevel:
    with Session(engine) as session:
        seniority_level_db = session.get(RoleSeniorityLevel, seniority_level_id)
        if not seniority_level_db:
            raise SeniorityLevelNotFound(seniority_level_id)
        update_seniority_level(seniority_level_db, seniority_level)
        session.commit()
        session.refresh(seniority_level_db)
        return seniority_level_db


def delete(seniority_level_id: int) -> RoleSeniorityLevel:
    with Session(engine) as session:
        seniority_level = session.get(RoleSeniorityLevel, seniority_level_id)
        if not seniority_level:
            raise SeniorityLevelNotFound(seniority_level_id)
        session.delete(seniority_level)
        session.commit()
        return seniority_level


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

"""
