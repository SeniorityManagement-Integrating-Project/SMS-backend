from typing import List

from fastapi import APIRouter, status, HTTPException
from src.seniority_level.exceptions import SeniorityLevelAlreadyExist, SeniorityLevelNotFound

import src.seniority_level.service as seniority_level_service
from src.seniority_level.models import SeniorityLevel
# from src.role.schemas import RoleCreate, RoleEmployees, RoleSeniorityLevels, RoleUpdate
from src.seniority_level.schemas import SeniorityLevelCreate, SeniorityLevelUpdate

router = APIRouter()


@router.get("/")
def get_all() -> List[SeniorityLevel]:
    return seniority_level_service.get_all()


@router.get("/{seniority_level_id}")
def get(seniority_level_id: int) -> SeniorityLevel:
    try:
        seniority_level = seniority_level_service.get(seniority_level_id)
        return seniority_level
    except SeniorityLevelNotFound as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post("/")
def create(seniority_level: SeniorityLevelCreate) -> SeniorityLevel:

    return seniority_level_service.create(seniority_level)


@router.patch("/{seniority_level_id}", status_code=status.HTTP_200_OK, response_model=SeniorityLevel)
def update(seniority_level_id: int, seniority_level: SeniorityLevelUpdate):
    try:
        return seniority_level_service.update(seniority_level_id, seniority_level)
    except SeniorityLevelNotFound as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


"""
@router.delete("/{role_id}", status_code=status.HTTP_200_OK)
def delete(role_id: int) -> Role:
    try:
        return role_service.delete(role_id)
    except RoleNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("/employees/{role_id}")
def get_with_employees(role_id: int) -> RoleEmployees:
    try:
        return role_service.get_with_employees(role_id)
    except RoleNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("/seniority_levels/{role_id}")
def get_with_seniority_levels(role_id: int) -> RoleSeniorityLevels:
    try:
        return role_service.get_with_seniority_levels(role_id)
    except RoleNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
"""
