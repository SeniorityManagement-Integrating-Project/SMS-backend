from sqlmodel import Session, select
from src.skill_request_comment.models import SkillValidationRequestComment
from src.skill_request_comment.schemas import RequestCommentCreate
from src.skill_request_comment.exceptions import CommentNotFound
from src.db import engine
from src.skill_validation_request.exceptions import RequestAlreadyValidated, RequestNotFound
from src.skill_validation_request.models import SkillValidationRequest


def create(request_id: int, comment: RequestCommentCreate) -> SkillValidationRequestComment:
    with Session(engine) as session:
        request_db = session.get(SkillValidationRequest, request_id)
        if not request_db:
            raise RequestNotFound(request_id)
        if request_db.validated:
            raise RequestAlreadyValidated(request_id)
        comment_db = SkillValidationRequestComment(
            request_id=request_id, **comment.dict(exclude_unset=True)
        )
        session.add(comment_db)
        session.commit()
        session.refresh(comment_db)
        return comment_db


def get_all() -> list[SkillValidationRequestComment]:
    with Session(engine) as session:
        statement = select(SkillValidationRequestComment)
        result = session.exec(statement)
        return result.all()


def get(comment_id: int) -> SkillValidationRequestComment:
    with Session(engine) as session:
        comment = session.get(SkillValidationRequestComment, comment_id)
        if not comment:
            raise CommentNotFound(comment_id)
        return comment


def get_by_request_id(request_id: int) -> list[SkillValidationRequestComment]:
    with Session(engine) as session:
        statement = select(SkillValidationRequestComment).where(
            SkillValidationRequestComment.request_id == request_id
        )
        result = session.exec(statement)
        return result.all()


def delete(comment_id: int) -> SkillValidationRequestComment:
    with Session(engine) as session:
        comment = session.get(SkillValidationRequestComment, comment_id)
        if not comment:
            raise CommentNotFound(comment_id)
        session.delete(comment)
        session.commit()
        return comment
