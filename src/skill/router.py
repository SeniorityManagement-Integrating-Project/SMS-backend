from typing import List

from fastapi import APIRouter, status, Depends

import src.skill.service as skill_service
from src.skill.models import Skill
from src.skill.schemas import (
    SkillCreate,
    SkillEmployeeRequests,
    SkillUpdate,
    SkillEmployees,
    SkillSeniorityLevels,
    SkillRequests,
    SkillAll,
)
from src.utils.auth import oauth2_scheme_admin, get_token_bearer_admin

router = APIRouter()


@router.get("/")
def get_all() -> List[Skill]:
    return skill_service.get_all()


@router.get("/{skill_id}")
def get(skill_id: int) -> Skill:
    return skill_service.get(skill_id)


@router.post("/")
def create(skill: SkillCreate, token: str = Depends(get_token_bearer_admin)) -> Skill:
    return skill_service.create(skill)


@router.patch("/{skill_id}", status_code=status.HTTP_200_OK, response_model=Skill)
def update(skill_id: int, skill: SkillUpdate):
    return skill_service.update(skill_id, skill)


@router.delete("/{skill_id}", status_code=status.HTTP_200_OK)
def delete(skill_id: int) -> Skill:
    return skill_service.delete(skill_id)


@router.get("/employees/{skill_id}")
def get_with_employees(skill_id: int) -> SkillEmployees:
    return skill_service.get_with_employees(skill_id)


@router.get("/seniority_levels/{skill_id}")
def get_with_seniority_levels(skill_id: int) -> SkillSeniorityLevels:
    return skill_service.get_with_seniority_levels(skill_id)


@router.get("/requests/{skill_id}")
def get_with_requests(skill_id: int) -> SkillRequests:
    return skill_service.get_with_requests(skill_id)


@router.get("/employee_request/{skill_id}/{employee_id}")
def get_with_employee_requests(skill_id: int, employee_id: int) -> SkillEmployeeRequests:
    return skill_service.get_with_employee_requests(skill_id, employee_id)
