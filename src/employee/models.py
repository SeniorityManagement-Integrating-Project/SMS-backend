from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Relationship
from sqlmodel import SQLModel, Field

if TYPE_CHECKING:
    from src.role.models import Role
    from src.skill.models import Skill
    from src.account.models import Account
    from src.skill_validation_request.models import SkillValidationRequest


class Interaction(SQLModel, table=True):
    employee_from_id: int = Field(foreign_key='employee.id', primary_key=True)
    employee_to_id: int = Field(foreign_key='employee.id', primary_key=True)
    date: datetime = Field(default_factory=datetime.now)


class EmployeeSkill(SQLModel, table=True):
    __tablename__ = 'employee_skill'  # type: ignore
    employee_id: int = Field(foreign_key='employee.id', primary_key=True)
    skill_id: int = Field(foreign_key='skill.id', primary_key=True)
    attainment_date: datetime = Field(default_factory=datetime.now)


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    biography: Optional[str]
    role_id: Optional[int] = Field(default=None, foreign_key='role.id')
    role: Optional["Role"] = Relationship(back_populates='employees')
    account: "Account" = Relationship(back_populates='employee')
    skills: List["Skill"] = Relationship(link_model=EmployeeSkill)
    requests: List["SkillValidationRequest"] = Relationship(
        back_populates='employee')
