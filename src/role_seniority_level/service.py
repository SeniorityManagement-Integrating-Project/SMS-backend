from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select, subquery

from src.db import engine
from src.role_seniority_level.mappers import (
    to_role_seniority_level,
    to_role_seniority_level_skills,
    update_role_seniority_level,
)
from src.role_seniority_level.schemas import (
    RoleSeniorityLevelCreate,
    RoleSeniorityLevelSkills,
    RoleSeniorityLevelUpdate,
)
from src.role_seniority_level.exceptions import (
    RoleSeniorityLevelAlreadyExist,
    RoleSeniorityLevelNotFound,
    SeniorityLevelSkillAlreadyExists,
    SeniorityLevelSkillNotFound,
)
from src.role_seniority_level.models import RoleSeniorityLevel, SeniorityLevelSkill
from src.seniority_level.exceptions import SeniorityLevelNotFound
from src.seniority_level.models import SeniorityLevel
from src.skill.exceptions import SkillNotFound
from src.skill.models import Skill


def get_all() -> list[RoleSeniorityLevel]:
    with Session(engine) as session:
        statement = select(RoleSeniorityLevel)
        result = session.exec(statement)
        return result.all()


def get(seniority_level_id: int) -> RoleSeniorityLevel:
    with Session(engine) as session:
        statement = select(RoleSeniorityLevel).where(RoleSeniorityLevel.id == seniority_level_id)
        result = session.exec(statement)
        try:
            return result.one()
        except NoResultFound as exception:
            raise RoleSeniorityLevelNotFound(seniority_level_id) from exception


def delete(seniority_level_id: int) -> RoleSeniorityLevel:
    with Session(engine) as session:
        seniority_level = session.get(RoleSeniorityLevel, seniority_level_id)
        if not seniority_level:
            raise RoleSeniorityLevelNotFound(seniority_level_id)
        session.delete(seniority_level)
        session.commit()
        return seniority_level


def create(role_seniority_level: RoleSeniorityLevelCreate) -> RoleSeniorityLevel:
    with Session(engine) as session:
        statement = (
            select(RoleSeniorityLevel)
            .where(RoleSeniorityLevel.role_id == role_seniority_level.role_id)
            .where(RoleSeniorityLevel.seniority_level_id == role_seniority_level.seniority_level_id)
        )
        result = session.exec(statement)
        if result.one_or_none():
            raise RoleSeniorityLevelAlreadyExist(
                role_seniority_level.seniority_level_id, role_seniority_level.role_id
            )
        seniority_level_db = to_role_seniority_level(role_seniority_level)
        session.add(seniority_level_db)
        session.commit()
        session.refresh(seniority_level_db)
        return seniority_level_db


def update(
    seniority_level_id: int, role_id: int, role_seniority_level: RoleSeniorityLevelUpdate
) -> RoleSeniorityLevel:
    with Session(engine) as session:
        statement = (
            select(RoleSeniorityLevel)
            .where(RoleSeniorityLevel.seniority_level_id == seniority_level_id)
            .where(RoleSeniorityLevel.role_id == role_id)
        )
        result = session.exec(statement)
        try:
            role_seniority_level_db = result.one()
        except NoResultFound as exception:
            raise RoleSeniorityLevelNotFound(seniority_level_id) from exception
        role_seniority_level_db.before_update()
        update_role_seniority_level(role_seniority_level_db, role_seniority_level)
        session.commit()
        session.refresh(role_seniority_level_db)
        return role_seniority_level_db


def get_with_skills(role_seniority_level_id: int) -> RoleSeniorityLevelSkills:
    with Session(engine) as session:
        role_sl = session.get(RoleSeniorityLevel, role_seniority_level_id)
        if not role_sl:
            raise SeniorityLevelNotFound(role_seniority_level_id)
        return to_role_seniority_level_skills(role_sl)


def add_skill(role_seniority_level_id: int, skill_id: int) -> SeniorityLevelSkill:
    with Session(engine) as session:
        role_seniority_level = session.get(RoleSeniorityLevel, role_seniority_level_id)
        skill = session.get(Skill, skill_id)
        if not role_seniority_level:
            raise RoleSeniorityLevelNotFound(role_seniority_level_id)
        if not skill:
            raise SkillNotFound(skill_id)
        # statement = (
        #     select(SeniorityLevelSkill)
        #     .where(SeniorityLevelSkill.role_seniority_level_id == role_seniority_level_id)
        #     .where(SeniorityLevelSkill.skill_id == skill_id)
        # )
        statement = (
            select(SeniorityLevelSkill)
            .join(
                RoleSeniorityLevel,
                SeniorityLevelSkill.role_seniority_level_id == RoleSeniorityLevel.id,
            )
            .where(RoleSeniorityLevel.role_id == role_seniority_level.role_id)
            .where(SeniorityLevelSkill.skill_id == skill_id)
        )
        result = session.exec(statement).all()
        print(result)
        if len(result) > 0:
            raise SeniorityLevelSkillAlreadyExists(role_seniority_level.role_id, skill_id)
        sl_skill = SeniorityLevelSkill(
            role_seniority_level_id=role_seniority_level_id, skill_id=skill_id
        )
        session.add(sl_skill)
        session.commit()
        session.refresh(sl_skill)
        return sl_skill


def remove_skill(role_seniority_level_id: int, skill_id: int):
    with Session(engine) as session:
        role_sl = session.get(RoleSeniorityLevel, role_seniority_level_id)
        if not role_sl:
            raise SeniorityLevelNotFound(role_seniority_level_id)
        skill = session.get(Skill, skill_id)
        if not skill:
            raise SkillNotFound(skill_id)
        statement = (
            select(SeniorityLevelSkill)
            .where(SeniorityLevelSkill.role_seniority_level_id == role_seniority_level_id)
            .where(SeniorityLevelSkill.skill_id == skill_id)
        )
        seniority_level_skill = session.exec(statement).one_or_none()
        if not seniority_level_skill:
            raise SeniorityLevelSkillNotFound(role_seniority_level_id, skill_id)
        session.delete(seniority_level_skill)
        session.commit()
        session.refresh(seniority_level_skill)
        return seniority_level_skill
