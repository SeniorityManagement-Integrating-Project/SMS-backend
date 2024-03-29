from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship
from src.models import BaseModel

from src.role_seniority_level.models import SeniorityLevelSkill

if TYPE_CHECKING:
    from src.seniority_level.models import RoleSeniorityLevel
    from src.skill_validation_request.models import SkillValidationRequest


class Skill(BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    seniority_levels: List["RoleSeniorityLevel"] = Relationship(
        back_populates="skills",
        link_model=SeniorityLevelSkill,
        sa_relationship_kwargs={"viewonly": True},
    )
    requests: List["SkillValidationRequest"] = Relationship()
    role_seniority_levels: List["RoleSeniorityLevel"] = Relationship(
        back_populates="skills",
        link_model=SeniorityLevelSkill,
        sa_relationship_kwargs={"viewonly": True},
    )
    seniority_level_skills: List["SeniorityLevelSkill"] = Relationship(back_populates="skill")
