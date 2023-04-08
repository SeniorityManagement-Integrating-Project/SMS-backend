from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from src.employee.models import Employee
    from src.skill.models import Skill

from sqlmodel import Field, Relationship, SQLModel
from typing import Optional
from datetime import datetime


class SkillValidationRequestComment(SQLModel, table=True):
    __tablename__ = 'skill_validation_request_comment'  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    request_id: int = Field(foreign_key='skill_validation_request.id')
    request: "SkillValidationRequest" = Relationship(back_populates='comments')
    comment: str
    date: datetime = Field(default_factory=datetime.now)


class SkillValidationRequest(SQLModel, table=True):
    __tablename__ = 'skill_validation_request'  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: Optional[int] = Field(foreign_key='employee.id')
    employee: "Employee" = Relationship(back_populates='requests')
    skill_id: Optional[int] = Field(foreign_key='skill.id')
    skill: "Skill" = Relationship(back_populates='requests')
    request_date: datetime = Field(default_factory=datetime.now)
    support_file: Optional[str]
    validator: Optional[int] = Field(foreign_key='account.id')
    approved: bool = False
    validated: bool = False
    comments: List["SkillValidationRequestComment"] = Relationship(
        back_populates='request')
