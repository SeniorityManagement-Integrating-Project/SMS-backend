from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.seniority_level.models import RoleSeniorityLevel


if TYPE_CHECKING:
    from src.seniority_level.models import SeniorityLevel
    from src.employee.models import Employee


class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    description: Optional[str]
    seniority_levels: List["SeniorityLevel"] = Relationship(
        back_populates="roles",
        link_model=RoleSeniorityLevel,
        sa_relationship_kwargs={"viewonly": True},
    )
    employees: List["Employee"] = Relationship(back_populates="role")
    role_seniority_levels: List["RoleSeniorityLevel"] = Relationship(back_populates="role")
