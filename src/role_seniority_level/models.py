from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import UniqueConstraint

from sqlmodel import Field, Relationship
from src.models import BaseModel

if TYPE_CHECKING:
    from src.role.models import Role
    from src.seniority_level.models import SeniorityLevel
    from src.skill.models import Skill


class SeniorityLevelSkill(BaseModel, table=True):
    __tablename__ = "seniority_level_skill"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    role_seniority_level_id: int = Field(foreign_key="role_seniority_level.id")
    skill_id: int = Field(foreign_key="skill.id")
    skill: "Skill" = Relationship(back_populates="seniority_level_skills")
    role_seniority_level: "RoleSeniorityLevel" = Relationship(
        back_populates="seniority_level_skills"
    )


class RoleSeniorityLevel(BaseModel, table=True):
    __tablename__ = "role_seniority_level"  # type: ignore
    __table_args__ = (UniqueConstraint("role_id", "seniority_level_id"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    description: Optional[str]
    role_id: int = Field(foreign_key="role.id")
    seniority_level_id: int = Field(foreign_key="seniority_level.id")
    skills: List["Skill"] = Relationship(
        back_populates="role_seniority_levels",
        link_model=SeniorityLevelSkill,
        sa_relationship_kwargs={"viewonly": True},
    )
    seniority_level_skills: List["SeniorityLevelSkill"] = Relationship(
        back_populates="role_seniority_level"
    )
    role: "Role" = Relationship(back_populates="role_seniority_levels")
    seniority_level: "SeniorityLevel" = Relationship(back_populates="role_seniority_levels")
