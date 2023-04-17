from fastapi import FastAPI

from src.employee import router as employee
from src.role import router as role
from src.seniority_level import router as seniority_level

app = FastAPI()

app.include_router(employee.router, prefix="/employee", tags=["employee"])
app.include_router(role.router, prefix="/role", tags=["role"])
app.include_router(seniority_level.router,
                   prefix="/seniority_level", tags=["seniority_level"])
