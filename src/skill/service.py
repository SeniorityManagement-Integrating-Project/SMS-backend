from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from src.db import engine
from src.employee.models import Employee
from src.skill.exceptions import SkillNotFound, SkillAlreadyExists
from src.employee.exceptions import EmployeeNotFound
from src.skill.mappers import (
    to_skill,
    to_skill_employee_requests,
    update_skill,
    to_skill_employees,
    to_skill_seniority_levels,
    to_skill_requests,
)
from src.skill.models import Skill
from src.skill.schemas import (
    SkillCreate,
    SkillUpdate,
    SkillEmployees,
    SkillSeniorityLevels,
    SkillRequests,
)
from src.skill_validation_request.models import SkillValidationRequest


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
        if skill.name:
            statement = select(Skill).where(Skill.name == skill.name)
            result = session.exec(statement)
            if result.one_or_none():
                raise SkillAlreadyExists(skill.name)
        skill_db = session.get(Skill, skill_id)
        if not skill_db:
            raise SkillNotFound(skill_id)
        skill_db.before_update()
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
        skill = session.get(Skill, skill_id)
        if not skill:
            raise SkillNotFound(skill_id)
        statement = (
            select(SkillValidationRequest)
            .where(SkillValidationRequest.skill_id == skill_id)
            .where(SkillValidationRequest.approved == True)
        )
        result = session.exec(statement)
        employees = [request.employee for request in result.all()]
        skill = to_skill_employees(skill)
        skill.employees = employees
        return skill


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


def get_with_employee_requests(skill_id: int, employee_id: int):
    with Session(engine) as session:
        skill = session.get(Skill, skill_id)
        if not skill:
            raise SkillNotFound(skill_id)
        employee = session.get(Employee, employee_id)
        if not employee:
            raise EmployeeNotFound(employee_id)
        statement = (
            select(SkillValidationRequest)
            .where(SkillValidationRequest.skill_id == skill_id)
            .where(SkillValidationRequest.employee_id == employee_id)
        )
        result = session.exec(statement)
        employee_requests = result.all()
        skill_employee_requests = to_skill_employee_requests(skill)
        skill_employee_requests.employee_requests = employee_requests
        return skill_employee_requests
