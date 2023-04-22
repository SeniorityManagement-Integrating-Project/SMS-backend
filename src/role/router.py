from typing import List

from fastapi import APIRouter, status

import src.role.service as role_service
from src.role.models import Role
from src.role.schemas import RoleCreate, RoleEmployees, RoleSeniorityLevels, RoleUpdate

router = APIRouter()


@router.get("/")
def get_all() -> List[Role]:
    return role_service.get_all()


@router.get("/{role_id}")
def get(role_id: int) -> Role:
    return role_service.get(role_id)


@router.post("/")
def create(role: RoleCreate) -> Role:
    return role_service.create(role)


@router.patch("/{role_id}", status_code=status.HTTP_200_OK, response_model=Role)
def update(role_id: int, role: RoleUpdate):
    return role_service.update(role_id, role)


@router.delete("/{role_id}", status_code=status.HTTP_200_OK)
def delete(role_id: int) -> Role:
    return role_service.delete(role_id)


@router.get("/employees/{role_id}")
def get_with_employees(role_id: int) -> RoleEmployees:
    return role_service.get_with_employees(role_id)


@router.get("/seniority_levels/{role_id}")
def get_with_seniority_levels(role_id: int) -> RoleSeniorityLevels:
    return role_service.get_with_seniority_levels(role_id)
