from typing import Optional

from sqlmodel import SQLModel


class RoleCreate(SQLModel):
    name: str
    description: Optional[str]


class RoleUpdate(SQLModel):
    name: Optional[str]
    description: Optional[str]
