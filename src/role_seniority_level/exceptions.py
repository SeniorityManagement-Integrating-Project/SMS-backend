from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class RoleSeniorityLevelNotFound(Exception):
    def __init__(self, role_seniority_level_id=None):
        self.role_seniority_level_id = role_seniority_level_id
        if role_seniority_level_id:
            self.message = f"Seniority level with id {role_seniority_level_id} does not exist"
        else:
            self.message = "Seniority level does not exist"
        super().__init__(self.message)


class RoleSeniorityLevelAlreadyExist(Exception):
    def __init__(self, seniority_level_id, role_id):
        self.seniority_level_id = seniority_level_id
        self.role_id = role_id
        self.message = (
            f"Role with id {role_id} already has the seniority level with id {seniority_level_id}"
        )
        super().__init__(self.message)


class SeniorityLevelSkillAlreadyExists(Exception):
    def __init__(self, seniority_level_id=None, skill_id=None):
        self.seniority_level_id = seniority_level_id
        self.skill_id = skill_id
        if seniority_level_id and skill_id:
            self.message = f"The Role associated with Seniority level with id {seniority_level_id} already has the skill with id {skill_id}"
        else:
            self.message = "Seniority level already has the skill"
        super().__init__(self.message)


class SeniorityLevelSkillNotFound(Exception):
    def __init__(self, seniority_level_id=None, skill_id=None):
        self.seniority_level_id = seniority_level_id
        self.skill_id = skill_id
        if seniority_level_id and skill_id:
            self.message = f"Seniority level with id {seniority_level_id} does not have the skill with id {skill_id}"
        else:
            self.message = "Seniority level does not have the skill"
        super().__init__(self.message)


async def seniority_level_skill_not_found_exception_handler(
    _: Request, exc: SeniorityLevelSkillNotFound
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.message},
    )


async def seniority_level_skill_already_exists_exception_handler(
    _: Request, exc: SeniorityLevelSkillAlreadyExists
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exc.message},
    )


async def role_seniority_level_not_found_exception_handler(
    _: Request, exc: RoleSeniorityLevelNotFound
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.message},
    )


async def role_seniority_level_already_exists_exception_handler(
    _: Request, exc: RoleSeniorityLevelAlreadyExist
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exc.message},
    )


def add_role_seniority_level_exception_handlers(app: FastAPI):
    app.add_exception_handler(
        RoleSeniorityLevelNotFound, role_seniority_level_not_found_exception_handler
    )
    app.add_exception_handler(
        RoleSeniorityLevelAlreadyExist, role_seniority_level_already_exists_exception_handler
    )
    app.add_exception_handler(
        SeniorityLevelSkillNotFound, seniority_level_skill_not_found_exception_handler
    )
    app.add_exception_handler(
        SeniorityLevelSkillAlreadyExists, seniority_level_skill_already_exists_exception_handler
    )
