from fastapi import FastAPI

from src.employee import router as employee
from src.role import router as role
from src.skill import router as skill

app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome": "Welcome to Seniority Management System REST API"}


app.include_router(employee.router, prefix="/employee", tags=["employee"])
app.include_router(role.router, prefix="/role", tags=["role"])
app.include_router(skill.router, prefix="/skill", tags=["skill"])
