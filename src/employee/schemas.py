from datetime import datetime
from typing import List, Optional

from sqlmodel import SQLModel
from src.account.models import Account
from src.role.models import Role
from src.seniority_level.models import SeniorityLevel

from src.skill.models import Skill
from src.skill_validation_request.models import SkillValidationRequest


class EmployeeBase(SQLModel):
    name: str
    email: str
    biography: Optional[str]
    role_id: Optional[int]


class EmployeeCreate(SQLModel):
    name: str
    email: str
    biography: Optional[str]
    role_id: int


class EmployeeSkills(EmployeeBase):
    skills: List[Skill]


class EmployeeRequests(EmployeeBase):
    requests: List[SkillValidationRequest]


class EmployeeAccount(EmployeeBase):
    account: Account


class EmployeeRole(EmployeeBase):
    role: Role


class EmployeeUpdate(SQLModel):
    name: Optional[str]
    email: Optional[str]
    biography: Optional[str]
    role_id: Optional[int]


class EmployeeSeniorityLevel(SeniorityLevel):
    attainment_date: datetime
    role_name: str


class EmployeeCurrentSeniorityLevel(EmployeeBase):
    seniority_level: EmployeeSeniorityLevel | None


class EmployeeSeniorityLevels(EmployeeBase):
    seniority_levels: List[EmployeeSeniorityLevel] | None
