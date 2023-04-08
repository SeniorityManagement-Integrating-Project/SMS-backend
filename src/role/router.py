from typing import List

from fastapi import APIRouter, status, HTTPException

import src.role.service as role_service
from src.role.models import Role
from src.role.schemas import RoleCreate, RoleUpdate

router = APIRouter()


@router.get("/employee/{role_id}", response_model=Role)
def get(role_id: int):
    try:
        return role_service.get(role_id)
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=str(exception)) from exception


@router.get("/employee", response_model=List[Role])
def get_all():
    return role_service.get_all()


@router.post("/employee", response_model=Role)
def create(role: RoleCreate):
    return role_service.create(role)


@router.patch("/employee/{role_id}", response_model=Role, status_code=status.HTTP_200_OK)
def update(role_id: int, role: RoleUpdate):
    try:
        return role_service.update(role_id, role)
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=str(exception)) from exception


@router.delete("/employee/{role_id}", response_model=Role, status_code=status.HTTP_200_OK)
def delete(role_id: int):
    try:
        return role_service.delete(role_id)
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=str(exception)) from exception
