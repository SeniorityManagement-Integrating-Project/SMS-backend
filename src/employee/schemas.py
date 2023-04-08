from typing import Optional

from sqlmodel import SQLModel


class EmployeeCreate(SQLModel):
    name: str
    email: str
    biography: str
    role_id: int


class EmployeeUpdate(SQLModel):
    name: Optional[str]
    email: Optional[str]
    biography: Optional[str]
    role_id: Optional[int]
