from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship
from src.models import BaseModel

if TYPE_CHECKING:  
    from src.skill_validation_request.models import SkillValidationRequest



class SkillValidationRequestComment(BaseModel, table=True):
    __tablename__ = "skill_validation_request_comment"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    request_id: int = Field(foreign_key="skill_validation_request.id")
    request: Optional["SkillValidationRequest"] = Relationship(back_populates="comments")
    comment: str