from typing import List

from fastapi import APIRouter, status, HTTPException

import src.skill_validation_request.service as request_service
from src.skill_validation_request.exceptions import RequestNotFound, RequestAlreadyApproved, EmployeeWithoutRequests
from src.skill_validation_request.models import SkillValidationRequest, SkillValidationRequestComment
from src.skill_validation_request.schemas import RequestCreate, RequestUpdate, RequestComment, RequestCommentCreate

router = APIRouter()


@router.get("/")
def get_all() -> List[SkillValidationRequest]:
    return request_service.get_all()


@router.get("/{skill_validation_request_id}")
def get(skill_validation_request_id: int) -> SkillValidationRequest:
    try:
        request = request_service.get(skill_validation_request_id)
        return request
    except RequestNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("/employee/{employee_id}")
def get_by_employee(employee_id: int) -> List[SkillValidationRequest]:
    try:
        return request_service.get_by_employee(employee_id)
    except EmployeeWithoutRequests as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post("/{employee_id}/{skill_id}")
def create(employee_id: int, skill_id: int, request: RequestCreate) -> SkillValidationRequest:
    try:
        return request_service.create(employee_id, skill_id, request)
    except RequestAlreadyApproved as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.patch("/{skill_validation_request_id}", status_code=status.HTTP_200_OK, response_model=SkillValidationRequest)
def update(skill_validation_request_id: int, request: RequestUpdate):
    try:
        return request_service.update(skill_validation_request_id, request)
    except RequestNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("/comments/{skill_validation_request_id}",
            description="Broke if any of the attributes of the request is null")
def get_with_comments(skill_validation_request_id: int) -> RequestComment:
    try:
        return request_service.get_with_comments(skill_validation_request_id)
    except RequestNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post("/comments/{skill_validation_request_id}",
             description="Not working yet. Cannot create a comment after query a request. Maybe because the session.")
def create_comment(skill_validation_request_id: int,
                   request_comment: RequestCommentCreate) -> SkillValidationRequestComment:
    try:
        return request_service.create_comment(skill_validation_request_id, request_comment)
    except RequestNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
