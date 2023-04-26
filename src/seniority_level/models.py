from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Relationship, Field


from src.models import BaseModel
from src.role_seniority_level.models import RoleSeniorityLevel

if TYPE_CHECKING:
    from src.skill.models import Skill
    from src.role.models import Role


class SeniorityLevel(BaseModel, table=True):
    __tablename__ = "seniority_level"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    level: int = Field(unique=True)
    roles: List["Role"] = Relationship(
        back_populates="seniority_levels",
        link_model=RoleSeniorityLevel,
        sa_relationship_kwargs={"viewonly": True},
    )
    role_seniority_levels: List["RoleSeniorityLevel"] = Relationship(
        back_populates="seniority_level"
    )
 