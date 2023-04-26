from fastapi import FastAPI

from src.employee import router as employee
from src.role import router as role
from src.interaction import router as interaction
from src.role_seniority_level.exceptions import add_role_seniority_level_exception_handlers
from src.seniority_level.exceptions import add_seniority_level_exception_handlers
from src.skill import router as skill
from src.skill_request_comment.exceptions import add_comment_exception_handlers
from src.skill_validation_request import router as request
from src.seniority_level import router as seniority_level
from src.skill_request_comment import router as comment
from src.role_seniority_level import router as role_seniority_level

from src.employee.exceptions import add_employee_exception_handlers
from src.role.exceptions import add_role_exception_handlers
from src.interaction.exceptions import add_interaction_exception_handlers
from src.skill.exceptions import add_skill_exception_handlers
from src.skill_validation_request.exceptions import add_request_exception_handlers


app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome": "Welcome to Seniority Management System REST API"}


app.include_router(role.router, prefix="/role", tags=["Role"])
app.include_router(skill.router, prefix="/skill", tags=["Skill"])
app.include_router(employee.router, prefix="/employee", tags=["Employee"])
app.include_router(request.router, prefix="/request", tags=["Request"])
app.include_router(comment.router, prefix="/comment", tags=["Request Comment"])
app.include_router(seniority_level.router, prefix="/seniority_level", tags=["Seniority Level"])
app.include_router(
    role_seniority_level.router, prefix="/role_seniority_level", tags=["Role Seniority Level"]
)
app.include_router(interaction.router, prefix="/interaction", tags=["Interaction"])


add_role_exception_handlers(app)
add_skill_exception_handlers(app)
add_comment_exception_handlers(app)
add_request_exception_handlers(app)
add_employee_exception_handlers(app)
add_interaction_exception_handlers(app)
add_seniority_level_exception_handlers(app)
add_role_seniority_level_exception_handlers(app)
