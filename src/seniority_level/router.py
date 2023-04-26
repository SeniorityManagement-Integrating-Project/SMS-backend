from typing import List

from fastapi import APIRouter, status

import src.seniority_level.service as seniority_level_service
from src.seniority_level.models import SeniorityLevel
from src.seniority_level.schemas import SeniorityLevelCreate, SeniorityLevelUpdate

router = APIRouter()


@router.get("/")
def get_all() -> List[SeniorityLevel]:
    return seniority_level_service.get_all()


@router.get("/{seniority_level_id}")
def get(seniority_level_id: int) -> SeniorityLevel:
    seniority_level = seniority_level_service.get(seniority_level_id)
    return seniority_level


@router.post("/")
def create(seniority_level: SeniorityLevelCreate) -> SeniorityLevel:
    return seniority_level_service.create(seniority_level)


@router.patch(
    "/{seniority_level_id}", status_code=status.HTTP_200_OK, response_model=SeniorityLevel
)
def update(seniority_level_id: int, seniority_level: SeniorityLevelUpdate):
    return seniority_level_service.update(seniority_level_id, seniority_level)


@router.delete("/{seniority_level_id}", status_code=status.HTTP_200_OK)
def delete(seniority_level_id: int) -> SeniorityLevel:
    return seniority_level_service.delete(seniority_level_id)
