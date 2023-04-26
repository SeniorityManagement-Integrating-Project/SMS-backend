from datetime import datetime
from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def before_update(self):
        self.updated_at = datetime.now()


# TODO: ensure that before_update is called always on update services
