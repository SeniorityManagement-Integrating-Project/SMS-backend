from fastapi import FastAPI

from src.employee import router as employee
from src.interaction.exceptions import add_interaction_exception_handlers
from src.role import router as role
from src.interaction import router as interaction

from src.employee.exceptions import add_employee_exception_handlers
from src.role.exceptions import add_role_exception_handlers
from src.skill.exceptions import add_skill_exception_handlers

app = FastAPI()

app.include_router(employee.router, prefix="/employee", tags=["Employee"])
app.include_router(role.router, prefix="/role", tags=["Role"])
app.include_router(interaction.router, prefix="/interaction", tags=["Interaction"])

add_interaction_exception_handlers(app)
add_employee_exception_handlers(app)
add_skill_exception_handlers(app)
add_role_exception_handlers(app)
