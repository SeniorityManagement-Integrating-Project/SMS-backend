from typing import Any
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class EmployeeNotFound(Exception):
    def __init__(self, property_value: Any, property_name: str = "id"):
        self.property_value = property_value
        self.property_name = property_name
        self.message = f"Employee with {property_name} {property_value} does not exists"
        super().__init__(self.message)


class EmployeeSkillNotFound(Exception):
    def __init__(self, employee_id: int, skill_id: int):
        self.employee_id = employee_id
        self.skill_id = skill_id
        self.message = f"Employee with id {employee_id} does not have a skill with id {skill_id}"
        super().__init__(self.message)


class EmployeeSkillAlreadyExists(Exception):
    def __init__(self, employee_id: int, skill_id: int):
        self.employee_id = employee_id
        self.skill_id = skill_id
        self.message = f"Employee with id {employee_id} already has the skill with id {skill_id}"
        super().__init__(self.message)


async def employee_not_found_exception_handler(_: Request, exc: EmployeeNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.message},
    )


async def employee_skill_not_found_exception_handler(_: Request, exc: EmployeeSkillNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.message},
    )


async def employee_skill_already_exists_exception_handler(
    _: Request, exc: EmployeeSkillAlreadyExists
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exc.message},
    )


def add_employee_exception_handlers(app: FastAPI):
    app.add_exception_handler(EmployeeNotFound, employee_not_found_exception_handler)
    app.add_exception_handler(EmployeeSkillNotFound, employee_skill_not_found_exception_handler)
    app.add_exception_handler(
        EmployeeSkillAlreadyExists, employee_skill_already_exists_exception_handler
    )
