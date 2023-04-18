from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from src.db import engine
from src.skill.exceptions import SkillNotFound, SkillAlreadyExists
from src.skill.mappers import to_skill, update_skill, to_skill_employees, to_skill_seniority_levels, to_skill_requests, \
    to_skill_all
from src.skill.models import Skill
from src.skill.schemas import SkillCreate, SkillUpdate, SkillEmployees, SkillSeniorityLevels, SkillRequests, SkillAll


def get_all() -> list[Skill]:
    with Session(engine) as session:
        statement = select(Skill)
        result = session.exec(statement)
        return result.all()


def get(skill_id: int) -> Skill:
    with Session(engine) as session:
        statement = select(Skill).where(Skill.id == skill_id)
        result = session.exec(statement)
        try:
            return result.one()
        except NoResultFound as exception:
            raise SkillNotFound(skill_id) from exception


def create(skill: SkillCreate) -> Skill:
    skill_db = to_skill(skill)
    with Session(engine) as session:
        statement = select(Skill).where(Skill.name == skill.name)
        result = session.exec(statement)
        if result.one_or_none():
            raise SkillAlreadyExists(skill.name)
        session.add(skill_db)
        session.commit()
        session.refresh(skill_db)
        return skill_db


def update(skill_id: int, skill: SkillUpdate) -> Skill:
    with Session(engine) as session:
        skill_db = session.get(Skill, skill_id)
        if not skill_db:
            raise SkillNotFound(skill_id)
        update_skill(skill_db, skill)
        session.commit()
        session.refresh(skill_db)
        return skill_db


def delete(skill_id: int):
    with Session(engine) as session:
        skill_db = session.get(Skill, skill_id)
        if not skill_db:
            raise SkillNotFound(skill_id)
        session.delete(skill_db)
        session.commit()
        return skill_db


def get_with_employees(skill_id: int) -> SkillEmployees:
    with Session(engine) as session:
        statement = select(Skill).where(Skill.id == skill_id)
        result = session.exec(statement)
        try:
            return to_skill_employees(result.one())
        except NoResultFound as exception:
            raise SkillNotFound(skill_id) from exception


def get_with_seniority_levels(skill_id: int) -> SkillSeniorityLevels:
    with Session(engine) as session:
        statement = select(Skill).where(Skill.id == skill_id)
        result = session.exec(statement)
        try:
            return to_skill_seniority_levels(result.one())
        except NoResultFound as exception:
            raise SkillNotFound(skill_id) from exception


def get_with_requests(skill_id: int) -> SkillRequests:
    with Session(engine) as session:
        statement = select(Skill).where(Skill.id == skill_id)
        result = session.exec(statement)
        try:
            return to_skill_requests(result.one())
        except NoResultFound as exception:
            raise SkillNotFound(skill_id) from exception


def get_with_all(skill_id: int) -> SkillAll:
    with Session(engine) as session:
        statement = select(Skill).where(Skill.id == skill_id)
        result = session.exec(statement)
        try:
            return to_skill_all(result.one())
        except NoResultFound as exception:
            raise SkillNotFound(skill_id) from exception
