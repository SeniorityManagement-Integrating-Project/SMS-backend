from typing import List

from fastapi import APIRouter, status

import src.skill_validation_request.service as request_service
from src.skill_validation_request.models import (
    SkillValidationRequest,
    SkillValidationRequestComment,
)
from src.skill_validation_request.schemas import (
    RequestCreate,
    RequestUpdate,
    RequestComment,
    RequestCommentCreate,
)

router = APIRouter()


@router.get("/")
def get_all() -> List[SkillValidationRequest]:
    return request_service.get_all()


@router.get("/{skill_validation_request_id}")
def get(skill_validation_request_id: int) -> SkillValidationRequest:
    return request_service.get(skill_validation_request_id)


@router.get("/employee/{employee_id}")
def get_by_employee(employee_id: int) -> List[SkillValidationRequest]:
    return request_service.get_by_employee(employee_id)


@router.post("/{employee_id}/{skill_id}")
def create(employee_id: int, skill_id: int, request: RequestCreate) -> SkillValidationRequest:
    return request_service.create(employee_id, skill_id, request)


@router.patch(
    "/{skill_validation_request_id}",
    status_code=status.HTTP_200_OK,
    response_model=SkillValidationRequest,
)
def update(skill_validation_request_id: int, request: RequestUpdate):
    return request_service.update(skill_validation_request_id, request)


@router.get(
    "/comments/{skill_validation_request_id}",
    description="Broke if any of the attributes of the request is null",
)
def get_with_comments(skill_validation_request_id: int) -> RequestComment:
    return request_service.get_with_comments(skill_validation_request_id)


@router.post(
    "/comments/{skill_validation_request_id}",
    description="Not working yet. Cannot create a comment after query a request. Maybe because the session.",
)
def create_comment(
    skill_validation_request_id: int, request_comment: RequestCommentCreate
) -> SkillValidationRequestComment:
    return request_service.create_comment(skill_validation_request_id, request_comment)
