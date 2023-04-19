from typing import List

from fastapi import APIRouter, status, HTTPException

import src.skill.service as skill_service
from src.skill.exceptions import SkillAlreadyExists, SkillNotFound
from src.skill.models import Skill
from src.skill.schemas import SkillCreate, SkillUpdate, SkillEmployees, SkillSeniorityLevels, SkillRequests, SkillAll

router = APIRouter()


@router.get("/")
def get_all() -> List[Skill]:
    return skill_service.get_all()


@router.get("/{skill_id}")
def get(skill_id: int) -> Skill:
    try:
        skill = skill_service.get(skill_id)
        return skill
    except SkillNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post("/")
def create(skill: SkillCreate) -> Skill:
    try:
        return skill_service.create(skill)
    except SkillAlreadyExists as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.patch("/{skill_id}", status_code=status.HTTP_200_OK, response_model=Skill)
def update(skill_id: int, skill: SkillUpdate):
    try:
        return skill_service.update(skill_id, skill)
    except SkillNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except SkillAlreadyExists as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

@router.delete("/{skill_id}", status_code=status.HTTP_200_OK)
def delete(skill_id: int) -> Skill:
    try:
        return skill_service.delete(skill_id)
    except SkillNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("/employees/{skill_id}")
def get_with_employees(skill_id: int) -> SkillEmployees:
    try:
        return skill_service.get_with_employees(skill_id)
    except SkillNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("/seniority_levels/{skill_id}")
def get_with_seniority_levels(skill_id: int) -> SkillSeniorityLevels:
    try:
        return skill_service.get_with_seniority_levels(skill_id)
    except SkillNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("/requests/{skill_id}")
def get_with_requests(skill_id: int) -> SkillRequests:
    try:
        return skill_service.get_with_requests(skill_id)
    except SkillNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("/all/{skill_id}")
def get_with_all(skill_id: int) -> SkillAll:
    try:
        return skill_service.get_with_all(skill_id)
    except SkillNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
