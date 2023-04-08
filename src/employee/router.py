from typing import List

from fastapi import APIRouter, status, HTTPException

import src.employee.service as employee_service
from src.employee.models import Employee
from src.employee.schemas import EmployeeCreate, EmployeeUpdate

router = APIRouter()


@router.get("/", response_model=List[Employee], status_code=status.HTTP_200_OK)
def get_all():
    return employee_service.get_all()


@router.post("/", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create(employee: EmployeeCreate):
    try:
        return employee_service.create(employee)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def get(employee_id: int):
    try:
        return employee_service.get(employee_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch("/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def update(employee_id: int, employee: EmployeeUpdate):
    try:
        return employee_service.update(employee_id, employee)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def delete(employee_id: int):
    try:
        return employee_service.delete(employee_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
