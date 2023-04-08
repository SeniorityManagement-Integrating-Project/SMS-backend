from typing import TYPE_CHECKING, List

from sqlmodel import Relationship

if TYPE_CHECKING:
    from src.skill.models import Skill
    from src.role.models import Role

from sqlmodel import Field, SQLModel
from typing import Optional


class SeniorityLevelSkill(SQLModel, table=True):
    __tablename__ = 'seniority_level_skill'  # type: ignore
    seniority_level_id: Optional[int] = Field(
        foreign_key="seniority_level.id", primary_key=True)
    skill_id: Optional[int] = Field(foreign_key='skill.id', primary_key=True)


class SeniorityLevel(SQLModel, table=True):
    __tablename__ = 'seniority_level'  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    role_id: Optional[int] = Field(foreign_key='role.id')
    skills: List["Skill"] = Relationship(
        back_populates="seniority_levels", link_model=SeniorityLevelSkill)
    role: Optional["Role"] = Relationship(back_populates="seniority_levels")
