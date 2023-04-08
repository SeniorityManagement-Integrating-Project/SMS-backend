from fastapi import APIRouter

import src.account.service as account_service
from src.account.models import Account

router = APIRouter()


@router.get("/", response_model=Account)
def get_all():
    return account_service.get_all()


@router.post("/", response_model=Account)
def create(account: Account):
    return account_service.create(account)
