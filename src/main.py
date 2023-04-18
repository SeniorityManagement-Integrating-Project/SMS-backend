from fastapi import FastAPI

from src.employee import router as employee
from src.role import router as role
from src.interaction import router as interaction
from src.skill import router as skill
from src.skill_validation_request import router as request
from src.seniority_level import router as seniority_level

from src.employee.exceptions import add_employee_exception_handlers
from src.role.exceptions import add_role_exception_handlers
from src.interaction.exceptions import add_interaction_exception_handlers
from src.skill.exceptions import add_skill_exception_handlers


app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome": "Welcome to Seniority Management System REST API"}


app.include_router(employee.router, prefix="/employee", tags=["Employee"])
app.include_router(role.router, prefix="/role", tags=["Role"])
app.include_router(interaction.router, prefix="/interaction", tags=["Interaction"])
app.include_router(seniority_level.router,
                   prefix="/seniority_level", tags=["seniority_level"])
app.include_router(skill.router, prefix="/skill", tags=["Skill"])
app.include_router(request.router, prefix="/request", tags=["Request"])


add_employee_exception_handlers(app)
add_role_exception_handlers(app)
add_interaction_exception_handlers(app)
add_skill_exception_handlers(app)