from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from src.employee.models import Employee


class AccountType(str, Enum):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'


class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: Optional[int] = Field(foreign_key='employee.id')
    employee: Optional["Employee"] = Relationship(back_populates='account')
    creation_date: Optional[datetime] = Field(default_factory=datetime.now)
    photo: Optional[str]
    username: str
    password: str
    account_type: AccountType
