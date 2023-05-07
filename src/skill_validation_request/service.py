from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select
from sqlalchemy import desc

from src.db import engine
from src.employee.exceptions import EmployeeNotFound
from src.employee.models import Employee
from src.skill.exceptions import SkillNotFound
from src.skill.models import Skill
from src.skill_validation_request.exceptions import (
    RequestNotFound,
    RequestAlreadyApproved,
    EmployeeWithoutRequests,
    RequestAlreadyValidated,
)
from src.skill_validation_request.models import (
    SkillValidationRequest,
)
from src.skill_validation_request.schemas import (
    EmployeeRequest,
    RequestCreate,
    RequestUpdate,
    SkillValidationRequestComments,
)
from src.skill_validation_request.mappers import (
    to_employee_request,
    to_skill_validation_request,
    update_skill_validation_request,
    to_skill_validation_request_comments,
)


def get_all() -> list[SkillValidationRequest]:
    with Session(engine) as session:
        statement = select(SkillValidationRequest)
        result = session.exec(statement)
        return result.all()


def create(employee_id: int, skill_id: int, skill_request: RequestCreate) -> SkillValidationRequest:
    request_db = to_skill_validation_request(employee_id, skill_id, skill_request)
    with Session(engine) as session:
        employee = session.get(Employee, employee_id)
        if not employee:
            raise EmployeeNotFound(employee_id)
        skill = session.get(Skill, skill_id)
        if not skill:
            raise SkillNotFound(skill_id)
        statement = select(SkillValidationRequest).where(
            SkillValidationRequest.employee_id == employee_id,
            SkillValidationRequest.skill_id == skill_id,
            SkillValidationRequest.approved == True,
        )
        result = session.exec(statement)
        if result.one_or_none():
            raise RequestAlreadyApproved(employee_id, skill_id)
        session.add(request_db)
        session.commit()
        session.refresh(request_db)
        return request_db


def get(skill_validation_request_id: int) -> SkillValidationRequest:
    with Session(engine) as session:
        statement = select(SkillValidationRequest).where(
            SkillValidationRequest.id == skill_validation_request_id
        )
        result = session.exec(statement)
        try:
            return result.one()
        except NoResultFound as exception:
            raise RequestNotFound(skill_validation_request_id) from exception


def get_by_employee(employee_id: int) -> list[EmployeeRequest]:
    with Session(engine) as session:
        statement = (
            select(SkillValidationRequest)
            .where(SkillValidationRequest.employee_id == employee_id)
            .order_by(
                SkillValidationRequest.request_date, desc(SkillValidationRequest.request_date)
            )
        )
        result = session.exec(statement).all()
        if not result:
            raise EmployeeWithoutRequests(employee_id)
        return [to_employee_request(request) for request in result]


def update(
    skill_validation_request_id: int, skill_request: RequestUpdate
) -> SkillValidationRequest:
    with Session(engine) as session:
        # TODO: check if the validator_account exists and if it really is an admin
        skill_request_db = session.get(SkillValidationRequest, skill_validation_request_id)
        if not skill_request_db:
            raise RequestNotFound(skill_validation_request_id)
        if skill_request_db.validated:
            raise RequestAlreadyValidated(skill_validation_request_id)
        skill_request_db.before_update()
        skill_request_db = update_skill_validation_request(skill_request_db, skill_request)
        session.add(skill_request_db)
        session.commit()
        session.refresh(skill_request_db)
        return skill_request_db


def get_with_comments(skill_validation_request_id: int) -> SkillValidationRequestComments:
    with Session(engine) as session:
        request = session.get(SkillValidationRequest, skill_validation_request_id)
        if not request:
            raise RequestNotFound(skill_validation_request_id)
        return to_skill_validation_request_comments(request)
