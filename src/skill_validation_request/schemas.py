from typing import Optional, List
from datetime import datetime

from sqlmodel import SQLModel

from src.skill_validation_request.models import SkillValidationRequestComment


class RequestCreate(SQLModel):
    support_file: Optional[str]


class RequestUpdate(SQLModel):
    validator: int
    approved: bool


class RequestComment(SQLModel):
    id: int
    employee_id: int
    skill_id: int
    request_date: datetime
    support_file: str
    validator: int
    approved: bool
    validated: bool
    comments: List[SkillValidationRequestComment]


class RequestCommentCreate(SQLModel):
    comment: str
