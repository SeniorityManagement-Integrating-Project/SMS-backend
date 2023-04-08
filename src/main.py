from fastapi import FastAPI

from src.employee import router as employee
from src.role import router as role

app = FastAPI()

app.include_router(employee.router, prefix="/employee", tags=["employee"])
app.include_router(role.router, prefix="/role", tags=["role"])
