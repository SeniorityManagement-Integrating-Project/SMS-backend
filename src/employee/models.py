from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Relationship
from sqlmodel import SQLModel, Field

if TYPE_CHECKING:
    from src.role.models import Role
    from src.skill.models import Skill
    from src.account.models import Account
    from src.skill_validation_request.models import SkillValidationRequest

class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    biography: Optional[str]
    role_id: Optional[int] = Field(default=None, foreign_key="role.id")
    role: Optional["Role"] = Relationship(back_populates="employees")
    account: List["Account"] = Relationship(
        back_populates="employee",
        sa_relationship_kwargs={"uselist": False},
    )
    requests: List["SkillValidationRequest"] = Relationship(back_populates="employee")
