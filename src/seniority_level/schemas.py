from typing import Optional, List

from sqlmodel import SQLModel
from src.employee.models import Employee
from src.seniority_level.models import SeniorityLevel


class SeniorityLevelCreate(SQLModel):
    name: str
    description: Optional[str]
    role_id: int


class SeniorityLevelUpdate(SQLModel):
    name: Optional[str]
    description: Optional[str]
    role_id: Optional[int]


class RoleEmployees(SQLModel):
    id: int
    name: str
    description: str
    employees: List[Employee]


class RoleSeniorityLevels(SQLModel):
    id: int
    name: str
    description: str
    seniority_levels: List[SeniorityLevel]
