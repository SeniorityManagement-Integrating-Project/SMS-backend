from typing import Optional

from sqlmodel import SQLModel

from src.seniority_level.models import SeniorityLevel


class SeniorityLevelCreate(SQLModel):
    name: str
    level: int


class SeniorityLevelUpdate(SQLModel):
    name: str


class SeniorityLevelByRole(SeniorityLevel):
    description: Optional[str]
