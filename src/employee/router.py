from typing import List

from fastapi import APIRouter, status, HTTPException
from src.employee.exceptions import EmployeeNotFound

import src.employee.service as employee_service
from src.employee.models import Employee
from src.employee.schemas import EmployeeCreate, EmployeeUpdate

router = APIRouter()


@router.get("/", response_model=List[Employee], status_code=status.HTTP_200_OK)
def get_all():
    return employee_service.get_all()


@router.post("/", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create(employee: EmployeeCreate):
    return employee_service.create(employee)


@router.get("/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def get(employee_id: int):
    try:
        return employee_service.get(employee_id)
    except EmployeeNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.patch("/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def update(employee_id: int, employee: EmployeeUpdate):
    try:
        return employee_service.update(employee_id, employee)
    except EmployeeNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete("/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def delete(employee_id: int):
    try:
        return employee_service.delete(employee_id)
    except EmployeeNotFound as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("/seniority_levels/{employee_id}")
def get_with_seniority_levels(employee_id: int):
    return employee_service.get_employee_seniority_levels(employee_id)
