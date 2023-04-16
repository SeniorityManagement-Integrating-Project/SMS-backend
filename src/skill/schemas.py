from typing import Optional, List

from sqlmodel import SQLModel

from src.employee.models import Employee
from src.seniority_level.models import SeniorityLevel
from src.skill_validation_request.models import SkillValidationRequest


class SkillCreate(SQLModel):
    name: str
    description: Optional[str]


class SkillUpdate(SQLModel):
    name: Optional[str]
    description: Optional[str]


class SkillEmployees(SQLModel):
    id: int
    name: str
    description: str
    employees: List[Employee] = []


class SkillSeniorityLevels(SQLModel):
    id: int
    name: str
    description: str
    seniority_levels: List[SeniorityLevel] = []


class SkillRequests(SQLModel):
    id: int
    name: str
    description: str
    requests: List[SkillValidationRequest] = []


class SkillAll(SQLModel):
    id: int
    name: str
    description: str
    employees: List[Employee] = []
    seniority_levels: List[SeniorityLevel] = []
    requests: List[SkillValidationRequest] = []