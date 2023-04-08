from sqlmodel import Session, select

from src.db import engine
from src.role.models import Role
from src.role.schemas import RoleCreate, RoleUpdate


def get_all():
    with Session(engine) as session:
        statement = select(Role)
        result = session.exec(statement)
        return result.all()


def get(role_id: int):
    with Session(engine) as session:
        statement = select(Role).where(Role.id == role_id)
        result = session.exec(statement)
        try:
            return result.one()
        except Exception as exception:
            raise Exception(
                f"Role with id {role_id} does not exist") from exception


def create(role: RoleCreate):
    # TODO: use a mapper
    role_db = Role(**role.dict())
    with Session(engine) as session:
        # TODO: check if a role with the same name already exists
        session.add(role_db)
        session.commit()
        session.refresh(role_db)
        return role_db


def update(role_id: int, role: RoleUpdate):
    with Session(engine) as session:
        role_db = session.get(Role, role_id)
        if not role_db:
            raise Exception(f"Role with id {role_id} does not exist")

        # TODO: move into a generic function (maybe a mapper)
        role_data = role.dict(exclude_unset=True)
        for key, value in role_data.items():
            setattr(role_db, key, value)

        session.commit()
        session.refresh(role_db)
        return role_db


def delete(role_id: int):
    with Session(engine) as session:
        role = session.get(Role, role_id)
        if not role:
            raise Exception(f"Role with id {role_id} does not exist")
        session.delete(role)
        session.commit()
        return role
