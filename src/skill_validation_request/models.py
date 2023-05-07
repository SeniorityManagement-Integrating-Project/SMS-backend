from typing import List, TYPE_CHECKING, Optional
from datetime import datetime
from sqlmodel import Field, Relationship

from src.models import BaseModel

if TYPE_CHECKING:
    from src.skill_request_comment.models import SkillValidationRequestComment
    from src.employee.models import Employee
    from src.skill.models import Skill


class SkillValidationRequest(BaseModel, table=True):
    __tablename__ = "skill_validation_request"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="employee.id")
    employee: "Employee" = Relationship(back_populates="requests")
    skill_id: int = Field(foreign_key="skill.id")
    skill: "Skill" = Relationship(back_populates="requests")
    request_date: datetime = Field(default_factory=datetime.now)
    support_file: Optional[str]
    validator: Optional[int] = Field(default=None, foreign_key="account.id")
    approved: bool = False
    validated: bool = False
    comments: List["SkillValidationRequestComment"] = Relationship(back_populates="request")
