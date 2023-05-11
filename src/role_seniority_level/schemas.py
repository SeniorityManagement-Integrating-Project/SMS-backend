from typing import List, Optional
from sqlmodel import SQLModel
from src.role.models import Role
from src.seniority_level.models import SeniorityLevel

from src.skill.models import Skill


class RoleSeniorityLevelCreate(SQLModel):
    description: Optional[str]
    role_id: int
    seniority_level_id: int


class RoleSeniorityLevelUpdate(SQLModel):
    description: Optional[str]
    role_id: Optional[int]
    seniority_level_id: Optional[int]


class RoleSeniorityLevelSkills(SQLModel):
    id: int
    description: Optional[str]
    role_id: int
    seniority_level_id: int
    skills: List["Skill"]


class RoleSeniorityLevelByRole(SQLModel):
    id: int
    description: Optional[str]
    skills: List[Skill]
    role: Role
    seniority_level: SeniorityLevel
