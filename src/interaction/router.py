from fastapi import APIRouter
import src.interaction.service as interaction_service


router = APIRouter()


@router.post("/{employee_to_id}")
def create(employee_to_id: int, employee_from_id: int):
    return interaction_service.create(employee_from_id, employee_to_id)


@router.get("/")
def get_all():
    return interaction_service.get_all()


@router.get("/employee_to/{employee_to_id}")
def get_by_employee_to(employee_to_id: int):
    return interaction_service.get_by_employee_to(employee_to_id)


@router.get("/employee_from/{employee_from_id}")
def get_by_employee_from(employee_from_id: int):
    return interaction_service.get_by_employee_from(employee_from_id)


@router.delete("/interaction/{employee_to_id}")
def delete(employee_to_id: int, employee_from_id: int):
    return interaction_service.delete(employee_from_id, employee_to_id)
