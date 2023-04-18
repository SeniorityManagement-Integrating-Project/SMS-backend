from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from sqlmodel import Session, select

from src.db import engine
from src.skill_validation_request.exceptions import RequestNotFound, RequestAlreadyApproved, EmployeeWithoutRequests, \
    RequestAlreadyValidated
from src.skill_validation_request.models import SkillValidationRequest, SkillValidationRequestComment
from src.skill_validation_request.schemas import RequestCreate, RequestUpdate, RequestComment, RequestCommentCreate
from src.skill_validation_request.mappers import to_skill_validation_request, update_skill_validation_request, \
    to_skill_validation_request_with_comments, to_skill_validation_request_comment


def get_all() -> list[SkillValidationRequest]:
    with Session(engine) as session:
        statement = select(SkillValidationRequest)
        result = session.exec(statement)
        return result.all()


def create(employee_id: int, skill_id: int, skill_request: RequestCreate) -> SkillValidationRequest:
    request_db = to_skill_validation_request(employee_id, skill_id, skill_request)
    with Session(engine) as session:
        statement = select(SkillValidationRequest).where(
            SkillValidationRequest.employee_id == employee_id,
            SkillValidationRequest.skill_id == skill_id,
            SkillValidationRequest.approved == True
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
        statement = select(SkillValidationRequest).where(SkillValidationRequest.id == skill_validation_request_id)
        result = session.exec(statement)
        try:
            return result.one()
        except NoResultFound as exception:
            raise RequestNotFound(skill_validation_request_id) from exception


def get_by_employee(employee_id: int) -> list[SkillValidationRequest]:
    with Session(engine) as session:
        statement = select(SkillValidationRequest).where(SkillValidationRequest.employee_id == employee_id)
        result = session.exec(statement).all()
        if not result:
            raise EmployeeWithoutRequests(employee_id)
        return result


def update(skill_validation_request_id: int, skill_request: RequestUpdate) -> SkillValidationRequest:
    with Session(engine) as session:
        statement = select(SkillValidationRequest).where(SkillValidationRequest.id == skill_validation_request_id)
        result = session.exec(statement)
        try:
            skill_request_db = result.one()
        except NoResultFound as exception:
            raise RequestNotFound(skill_validation_request_id) from exception
        if skill_request_db.validated:
            raise HTTPException(status_code=400, detail="Skill Request already validated")
        skill_request_db = update_skill_validation_request(skill_request_db, skill_request)
        session.add(skill_request_db)
        session.commit()
        session.refresh(skill_request_db)
        return skill_request_db


def get_with_comments(skill_validation_request_id: int) -> RequestComment:
    with Session(engine) as session:
        statement = select(SkillValidationRequest).where(SkillValidationRequest.id == skill_validation_request_id)
        result = session.exec(statement)
        try:
            return to_skill_validation_request_with_comments(result.one())
        except NoResultFound as exception:
            raise RequestNotFound(skill_validation_request_id) from exception


def create_comment(skill_validation_request_id: int,
                   request_comment: RequestCommentCreate) -> SkillValidationRequestComment:
    with Session(engine) as session:
        statement = select(SkillValidationRequest).where(SkillValidationRequest.id == skill_validation_request_id)
        result = session.exec(statement)
        try:
            skill_request_db = result.one()
        except NoResultFound as exception:
            raise RequestNotFound(skill_validation_request_id) from exception
        if skill_request_db.validated:
            raise HTTPException(status_code=400, detail="Cannot comment an already validated skill request")
        session.commit() # Close the session to avoid a deadlock

        # But it doesnt work, the session is still open and the next lines fails
        # to insert the comment :c
        # TODO: Find a way to close the session and open a new one
        #       and then insert the comment
        # TODO: Set the validator id to the current admin user when add the comment
        new_comment = SkillValidationRequestComment(**request_comment.dict(),
                                                    request_id=skill_validation_request_id)
        session.add(new_comment)
        session.commit()
        session.refresh(new_comment)
        session.refresh(skill_request_db)
        return to_skill_validation_request_comment(skill_request_db, request_comment)