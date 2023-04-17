from fastapi import Request, FastAPI, status
from fastapi.responses import JSONResponse


class InteractionAlreadyExists(Exception):
    def __init__(self, employee_from_id: int, employee_to_id: int):
        self.employee_from_id = employee_from_id
        self.employee_to_id = employee_to_id
        self.message = f"Interaction from employee with id {employee_from_id} to employee with id {employee_to_id} already exists"
        super().__init__(self.message)


class InteractionNotFound(Exception):
    def __init__(self, employee_from_id: int, employee_to_id: int):
        self.employee_from_id = employee_from_id
        self.employee_to_id = employee_to_id
        self.message = f"Interaction between employee with id {employee_from_id} and employee with id {employee_to_id} does not exists"
        super().__init__(self.message)


async def interaction_already_exists_exception_handler(_: Request, exc: InteractionAlreadyExists):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exc.message},
    )


async def interaction_not_found_exception_handler(_: Request, exc: InteractionNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.message},
    )


def add_interaction_exception_handlers(app: FastAPI):
    app.add_exception_handler(
        InteractionAlreadyExists, interaction_already_exists_exception_handler
    )
    app.add_exception_handler(InteractionNotFound, interaction_not_found_exception_handler)
