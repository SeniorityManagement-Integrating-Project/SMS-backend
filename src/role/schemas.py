from typing import Optional, List

from sqlmodel import SQLModel
from src.employee.models import Employee
from src.role_seniority_level.models import RoleSeniorityLevel

class RoleCreate(SQLModel):
    name: str
    description: Optional[str]


class RoleUpdate(SQLModel):
    name: Optional[str]
    description: Optional[str]

class RoleEmployees(SQLModel):
    id: int
    name: str
    description: str
    employees: List[Employee]

class RoleSeniorityLevels(SQLModel):
    id: int
    name: str
    description: str
    seniority_levels: List[RoleSeniorityLevel]
