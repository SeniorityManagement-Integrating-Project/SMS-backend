from fastapi.responses import JSONResponse
from fastapi import Request, status, FastAPI


class SeniorityLevelNotFound(Exception):
    def __init__(self, seniority_level_id: int):
        self.seniority_level_id = seniority_level_id
        self.message = f"Seniority level with id {seniority_level_id} does not exist."
        super().__init__(self.message)


class SeniorityLevelAlreadyExist(Exception):
    def __init__(self, property_value=None, property_name="id"):
        self.property_name = property_name
        self.property_name = property_value
        self.message = f"Seniority level with {property_name} {property_value} already exist."
        super().__init__(self.message)


async def seniority_level_not_found_exception_handler(_: Request, exc: SeniorityLevelNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.message},
    )


async def seniority_level_already_exist_exception_handler(
    _: Request, exc: SeniorityLevelAlreadyExist
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exc.message},
    )


def add_seniority_level_exception_handlers(app: FastAPI):
    app.add_exception_handler(SeniorityLevelNotFound, seniority_level_not_found_exception_handler)
    app.add_exception_handler(
        SeniorityLevelAlreadyExist, seniority_level_already_exist_exception_handler
    )
