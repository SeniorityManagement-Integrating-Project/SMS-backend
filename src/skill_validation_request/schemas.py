from typing import List, Optional
from datetime import datetime

from sqlmodel import SQLModel
from src.employee.models import Employee
from src.skill.models import Skill

from src.skill_request_comment.models import SkillValidationRequestComment


class SkillValidationRequestBase(SQLModel):
    id: int
    employee_id: int
    skill_id: int
    request_date: Optional[datetime]
    support_file: Optional[str]
    validator: Optional[int]
    approved: bool
    validated: bool


class RequestCreate(SQLModel):
    support_file: Optional[str]


class RequestUpdate(SQLModel):
    validator: Optional[int]
    approved: bool


class SkillValidationRequestComments(SkillValidationRequestBase):
    comments: List["SkillValidationRequestComment"]


class EmployeeRequest(SQLModel):
    id: int
    employee_id: int
    skill_id: int
    skill: "Skill"
    created_at: datetime
    updated_at: datetime
    support_file: Optional[str]
    validator: Optional[int]
    approved: bool
    validated: bool
    comments: List["SkillValidationRequestComment"]


class SkillValidationRequestFull(SQLModel):
    id: int
    employee: Employee
    skill: Skill
    created_at: datetime
    updated_at: datetime
    support_file: Optional[str]
    validator: Optional[int]
    approved: bool = False
    validated: bool = False
    comments: List["SkillValidationRequestComment"]
