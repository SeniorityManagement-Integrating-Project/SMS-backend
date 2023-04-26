from typing import Optional

from sqlmodel import SQLModel


class SeniorityLevelCreate(SQLModel):
    name: str
    level: int


class SeniorityLevelUpdate(SQLModel):
    name: str
