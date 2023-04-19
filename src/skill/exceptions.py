from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class SkillNotFound(Exception):
    def __init__(self, skill_id: int):
        self.skill_id = skill_id
        self.message = f"Skill with id {skill_id} does not exists"
        super().__init__(self.message)


class SkillAlreadyExists(Exception):
    def __init__(self, skill_name):
        self.skill_name = skill_name
        self.message = f"Skill with name '{skill_name}' already exists"
        super().__init__(self.message)


async def skill_not_found_exception_handler(_: Request, exc: SkillNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.message},
    )


async def skill_already_exists_exception_handler(_: Request, exc: SkillAlreadyExists):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exc.message},
    )


def add_skill_exception_handlers(app: FastAPI):
    app.add_exception_handler(SkillNotFound, skill_not_found_exception_handler)
    app.add_exception_handler(SkillAlreadyExists, skill_already_exists_exception_handler)
