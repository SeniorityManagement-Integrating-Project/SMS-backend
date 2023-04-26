from fastapi import APIRouter
from src.skill_request_comment.models import SkillValidationRequestComment

from src.skill_request_comment.schemas import RequestCommentCreate
import src.skill_request_comment.service as comment_service

router = APIRouter()

@router.post("/{skill_request_id}")
def create(skill_request_id: int, comment: RequestCommentCreate) -> SkillValidationRequestComment:
    return comment_service.create(skill_request_id, comment)

@router.get("/")
def get_all() -> list[SkillValidationRequestComment]:
    return comment_service.get_all()

@router.get("/{comment_id}")
def get(comment_id: int) -> SkillValidationRequestComment:
    return comment_service.get(comment_id)

@router.get("/request/{skill_request_id}")
def get_by_request_id(skill_request_id: int) -> list[SkillValidationRequestComment]:
    return comment_service.get_by_request_id(skill_request_id)

@router.delete("/{comment_id}")
def delete(comment_id: int) -> SkillValidationRequestComment:
    return comment_service.delete(comment_id)