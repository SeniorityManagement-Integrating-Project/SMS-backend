from fastapi.responses import JSONResponse
from fastapi import Request, status


class RequestNotFound(Exception):
    def __init__(self, request_id):
        self.request_id = request_id
        self.message = f"Request with id {request_id} does not exists"
        super().__init__(self.message)


class RequestAlreadyApproved(Exception):
    def __init__(self, employee_id, skill_id):
        self.employee_id = employee_id
        self.skill_id = skill_id
        self.message = (
            f"Employee with id {employee_id} has the skill with id {skill_id} already approved"
        )
        super().__init__(self.message)


class EmployeeWithoutRequests(Exception):
    def __init__(self, employee_id):
        self.employee_id = employee_id
        self.message = f"Employee with id {employee_id} does not have any requests"
        super().__init__(self.message)


class RequestAlreadyValidated(Exception):
    def __init__(self, request_id):
        self.request_id = request_id
        self.message = f"Request with id {request_id} is already validated"
        super().__init__(self.message)


async def request_not_found_handler(_: Request, exception: RequestNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exception.message},
    )


async def request_already_approved_handler(_: Request, exception: RequestAlreadyApproved):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exception.message},
    )


async def employee_without_requests_handler(_: Request, exception: EmployeeWithoutRequests):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exception.message},
    )


async def request_already_validated_handler(_: Request, exception: RequestAlreadyValidated):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exception.message},
    )


def add_request_exception_handlers(app):
    app.add_exception_handler(RequestNotFound, request_not_found_handler)
    app.add_exception_handler(RequestAlreadyApproved, request_already_approved_handler)
    app.add_exception_handler(RequestAlreadyValidated, request_already_validated_handler)
    app.add_exception_handler(EmployeeWithoutRequests, employee_without_requests_handler)
