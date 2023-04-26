from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from src.db import engine
from src.role_seniority_level.exceptions import SeniorityLevelSkillNotFound
from src.role_seniority_level.models import RoleSeniorityLevel, SeniorityLevelSkill
from src.seniority_level.exceptions import SeniorityLevelAlreadyExist, SeniorityLevelNotFound
from src.seniority_level.models import SeniorityLevel
from src.seniority_level.schemas import SeniorityLevelCreate, SeniorityLevelUpdate
from src.seniority_level.mappers import to_seniority_level, update_seniority_level
from src.skill.exceptions import SkillNotFound
from src.skill.models import Skill


def get_all() -> list[SeniorityLevel]:
    with Session(engine) as session:
        statement = select(SeniorityLevel)
        result = session.exec(statement)
        return result.all()


def get(seniority_level_id: int) -> SeniorityLevel:
    with Session(engine) as session:
        seniority_level = session.get(SeniorityLevel, seniority_level_id)
        if not seniority_level:
            raise SeniorityLevelNotFound(seniority_level_id)
        return seniority_level


def create(seniority_level: SeniorityLevelCreate) -> SeniorityLevel:
    seniority_level_db = to_seniority_level(seniority_level)
    with Session(engine) as session:
        statement1 = select(SeniorityLevel).where(SeniorityLevel.name == seniority_level.name)
        result1 = session.exec(statement1).one_or_none()
        if result1:
            raise SeniorityLevelAlreadyExist(seniority_level.name, "name")
        statement2 = select(SeniorityLevel).where(SeniorityLevel.level >= seniority_level.level)
        result2 = session.exec(statement2).all()
        if len(result2) != 0:
            for seniority_level_ in result2:
                seniority_level_.level += 1
        session.add(seniority_level_db)
        session.commit()
        session.refresh(seniority_level_db)
        return seniority_level_db


def update(seniority_level_id: int, seniority_level: SeniorityLevelUpdate) -> SeniorityLevel:
    with Session(engine) as session:
        statement1 = select(SeniorityLevel).where(SeniorityLevel.name == seniority_level.name)
        result1 = session.exec(statement1).one_or_none()
        if result1:
            raise SeniorityLevelAlreadyExist(seniority_level.name, "name")
        seniority_level_db = session.get(SeniorityLevel, seniority_level_id)
        if not seniority_level_db:
            raise SeniorityLevelNotFound(seniority_level_id)
        seniority_level_db.before_update()
        update_seniority_level(seniority_level_db, seniority_level)
        session.commit()
        session.refresh(seniority_level_db)
        return seniority_level_db


def delete(seniority_level_id: int) -> SeniorityLevel:
    with Session(engine) as session:
        seniority_level = session.get(SeniorityLevel, seniority_level_id)
        if not seniority_level:
            raise SeniorityLevelNotFound(seniority_level_id)
        statement = select(SeniorityLevel).where(SeniorityLevel.level >= seniority_level.level)
        result = session.exec(statement).all()
        if len(result) != 0:
            for seniority_level in result:
                seniority_level.level -= 1
        session.delete(seniority_level)
        session.commit()
        return seniority_level
