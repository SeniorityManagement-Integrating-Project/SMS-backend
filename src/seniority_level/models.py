from typing import TYPE_CHECKING, List

from sqlmodel import Relationship

if TYPE_CHECKING:
    from src.skill.models import Skill
    from src.role.models import Role

from sqlmodel import Field, SQLModel
from typing import Optional


class SeniorityLevelSkill(SQLModel, table=True):
    __tablename__ = "seniority_level_skill"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    role_seniority_level_id: int = Field(foreign_key="role_seniority_level.id")
    skill_id: int = Field(foreign_key="skill.id")
    skill: "Skill" = Relationship(back_populates="seniority_level_skills")
    role_seniority_level: "RoleSeniorityLevel" = Relationship(
        back_populates="seniority_level_skills"
    )


class RoleSeniorityLevel(SQLModel, table=True):
    __tablename__ = "role_seniority_level"  # type: ignore
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


class SeniorityLevel(SQLModel, table=True):
    __tablename__ = "seniority_level"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    level: int
    roles: List["Role"] = Relationship(
        back_populates="seniority_levels",
        link_model=RoleSeniorityLevel,
        sa_relationship_kwargs={"viewonly": True},
    )
    role_seniority_levels: List["RoleSeniorityLevel"] = Relationship(
        back_populates="seniority_level"
    )
