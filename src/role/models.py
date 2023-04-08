from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from src.seniority_level.models import SeniorityLevel
    from src.employee.models import Employee


class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    description: Optional[str]
    seniority_levels: Optional["SeniorityLevel"] = Relationship(
        back_populates='role')
    employees: List["Employee"] = Relationship(back_populates='role')
