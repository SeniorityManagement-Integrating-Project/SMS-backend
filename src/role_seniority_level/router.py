from typing import List
from fastapi import APIRouter
from src.role_seniority_level.schemas import RoleSeniorityLevelByRole, RoleSeniorityLevelCreate, RoleSeniorityLevelUpdate
import src.role_seniority_level.service as role_seniority_level_service
from src.role_seniority_level.models import RoleSeniorityLevel, SeniorityLevelSkill

router = APIRouter()


@router.get("")
async def get_all() -> list[RoleSeniorityLevel]:
    return role_seniority_level_service.get_all()


@router.get("/{seniority_level_id}")
def get(seniority_level_id: int) -> RoleSeniorityLevel:
    return role_seniority_level_service.get(seniority_level_id)


@router.get("/skills/{seniority_level_id}")
def get_with_skills(seniority_level_id: int):
    return role_seniority_level_service.get_with_skills(seniority_level_id)


@router.delete("/{seniority_level_id}")
def delete(seniority_level_id: int) -> RoleSeniorityLevel:
    return role_seniority_level_service.delete(seniority_level_id)


@router.post("")
def create(role_seniority_level: RoleSeniorityLevelCreate) -> RoleSeniorityLevel:
    return role_seniority_level_service.create(role_seniority_level)


@router.patch("/{role_id}/{seniority_level_id}")
def update(
    seniority_level_id: int, role_id: int, role_seniority_level: RoleSeniorityLevelUpdate
) -> RoleSeniorityLevel:
    return role_seniority_level_service.update(seniority_level_id, role_id, role_seniority_level)


@router.post("/{role_seniority_level_id}/{skill_id}")
def add_skill(role_seniority_level_id: int, skill_id: int) -> SeniorityLevelSkill:
    return role_seniority_level_service.add_skill(role_seniority_level_id, skill_id)


@router.delete("/{role_seniority_level_id}/{skill_id}")
def remove_skill(role_seniority_level_id: int, skill_id: int) -> SeniorityLevelSkill:
    return role_seniority_level_service.remove_skill(role_seniority_level_id, skill_id)


@router.get("/role/{role_id}")
def get_by_role(role_id: int) -> list[RoleSeniorityLevelByRole]:
    return role_seniority_level_service.get_by_role(role_id)
