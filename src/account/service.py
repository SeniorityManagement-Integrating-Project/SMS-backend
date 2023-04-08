from sqlmodel import Session, select

from src.account.models import Account


def get_all() -> list[Account]:
    with Session() as session:
        statement = select(Account)
        return session.exec(statement).all()


def create(account: Account) -> Account:
    with Session() as session:
        session.add(account)
        session.commit()
        session.refresh(account)
        return account
