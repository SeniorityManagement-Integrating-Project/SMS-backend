from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class RoleNotFound(Exception):
    def __init__(self, role_id):
        self.role_id = role_id
        self.message = f"Role with id {role_id} does not exists"
        super().__init__(self.message)


class RoleAlreadyExists(Exception):
    def __init__(self, role_name):
        self.role_id = role_name
        self.message = f"Role with name '{role_name}' already exists"
        super().__init__(self.message)


async def role_not_found_exception_handler(_: Request, exc: RoleNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.message},
    )


async def role_already_exists_exception_handler(_: Request, exc: RoleAlreadyExists):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exc.message},
    )


def add_role_exception_handlers(app: FastAPI):
    app.add_exception_handler(RoleNotFound, role_not_found_exception_handler)
    app.add_exception_handler(RoleAlreadyExists, role_already_exists_exception_handler)
