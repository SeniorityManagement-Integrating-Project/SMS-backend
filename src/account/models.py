from enum import Enum
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship

from src.models import BaseModel

if TYPE_CHECKING:
    from src.employee.models import Employee


class AccountType(str, Enum):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'


class Account(BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: Optional[int] = Field(foreign_key='employee.id')
    employee: Optional["Employee"] = Relationship(back_populates='account')
    photo: Optional[str]
    username: str
    password: str
    account_type: AccountType
