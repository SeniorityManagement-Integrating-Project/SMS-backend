from typing import List, Optional
from sqlmodel import SQLModel

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
