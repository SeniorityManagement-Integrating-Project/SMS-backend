from typing import List

from fastapi import APIRouter, status, Query

import src.employee.service as employee_service
from src.employee.models import Employee
from src.employee.schemas import EmployeeAccount, EmployeeCreate, EmployeeUpdate

router = APIRouter()


@router.get("/", response_model=List[Employee], status_code=status.HTTP_200_OK)
def get_all():
    return employee_service.get_all()


@router.get("/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def get(employee_id: int):
    return employee_service.get(employee_id)


@router.get("/email/{email}", response_model=Employee, status_code=status.HTTP_200_OK)
def get_by_email(email: str):
    return employee_service.get_by_email(email)


@router.get("/role_id/{role_id}", response_model=List[Employee], status_code=status.HTTP_200_OK)
def get_by_role_id(role_id: int):
    return employee_service.get_by_role_id(role_id)


@router.get("", response_model=List[Employee], status_code=status.HTTP_200_OK)
def search_by_name(name: str = Query(min_length=3)):
    return employee_service.search_by_name(name)


@router.post("/", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create(employee: EmployeeCreate):
    return employee_service.create(employee)


@router.patch("/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def update(employee_id: int, employee: EmployeeUpdate):
    return employee_service.update(employee_id, employee)


@router.delete("/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def delete(employee_id: int):
    return employee_service.delete(employee_id)


@router.post("/skills/{employee_id}/{skill_id}", tags=["Employee Skills"])
def add_skill(employee_id: int, skill_id: int):
    return employee_service.add_skill(employee_id, skill_id)


@router.delete("/skills/{employee_id}", tags=["Employee Skills"])
def remove_skill(employee_id: int, skill_id: int):
    return employee_service.remove_skill(employee_id, skill_id)


@router.get("/skills/{employee_id}", tags=["Employee Skills"])
def get_with_skills(employee_id: int):
    return employee_service.get_with_skills(employee_id)


@router.get("/seniority_levels/{employee_id}")
def get_with_seniority_levels(employee_id: int):
    return employee_service.get_with_seniority_levels(employee_id)


@router.get("/current_seniority_level/{employee_id}")
def get_with_current_seniority_level(employee_id: int):
    return employee_service.get_with_current_seniority_level(employee_id)


@router.get("/role/{employee_id}")
def get_with_role(employee_id: int):
    return employee_service.get_with_role(employee_id)


@router.get("/skill_validation_requests/{employee_id}")
def get_with_requests(employee_id: int):
    return employee_service.get_with_requests(employee_id)


@router.get(
    "/account/{employee_id}", response_model=EmployeeAccount, status_code=status.HTTP_200_OK
)
def get_account(employee_id: int):
    return employee_service.get_with_account(employee_id)
