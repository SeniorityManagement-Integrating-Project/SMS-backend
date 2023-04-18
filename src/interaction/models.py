from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Interaction(SQLModel, table=True):
    employee_from_id: int = Field(foreign_key="employee.id", primary_key=True)
    employee_to_id: int = Field(foreign_key="employee.id", primary_key=True)
    date: Optional[datetime] = Field(default_factory=datetime.now)
