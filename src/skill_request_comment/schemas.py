from sqlmodel import SQLModel


class RequestCommentCreate(SQLModel):
    comment: str