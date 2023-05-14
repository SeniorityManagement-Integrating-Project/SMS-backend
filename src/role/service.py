from typing import List
from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from src.db import engine
from src.role.exceptions import RoleNotFound, RoleAlreadyExists
from src.role.models import Role
from src.role.schemas import RoleCreate, RoleSeniorityLevels, RoleUpdate, RoleEmployees
from src.role.mappers import to_role, to_role_seniority_levels, update_role, to_role_employees
from src.role_seniority_level.models import RoleSeniorityLevel, SeniorityLevelSkill
from src.skill.models import Skill


def get_all() -> list[Role]:
    with Session(engine) as session:
        statement = select(Role)
        result = session.exec(statement)
        return result.all()


def get(role_id: int) -> Role:
    with Session(engine) as session:
        statement = select(Role).where(Role.id == role_id)
        result = session.exec(statement)
        try:
            return result.one()
        except NoResultFound as exception:
            raise RoleNotFound(role_id) from exception


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


def create(role: RoleCreate) -> Role:
    role_db = to_role(role)
    with Session(engine) as session:
        statement = select(Role).where(Role.name == role.name)
        result = session.exec(statement)
        if result.one_or_none():
            raise RoleAlreadyExists(role.name)
        session.add(role_db)
        session.commit()
        session.refresh(role_db)
        return role_db


def update(role_id: int, role: RoleUpdate) -> Role:
    with Session(engine) as session:
        if role.name:
            statement = select(Role).where(Role.name == role.name)
            result = session.exec(statement)
            if result.one_or_none():
                raise RoleAlreadyExists(role.name)
        role_db = session.get(Role, role_id)
        if not role_db:
            raise RoleNotFound(role_id)
        role_db.before_update()
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


def get_available_skills(role_id: int) -> List[Skill]:
    with Session(engine) as session:
        role = session.get(Role, role_id)
        if not role:
            raise RoleNotFound(role_id)
        statement = select(Skill).except_(
            select(Skill)
            .join(SeniorityLevelSkill)
            .join(RoleSeniorityLevel)
            .where(RoleSeniorityLevel.role_id == role_id)
        )
        result = session.exec(statement) # type: ignore
        return result.all()
