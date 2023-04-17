from src.seniority_level.models import SeniorityLevel
from src.seniority_level.schemas import SeniorityLevelCreate


# def to_seniority_level(seniority_level: SeniorityLevelCreate | RoleUpdate) -> Role:
def to_seniority_level(seniority_level: SeniorityLevelCreate) -> SeniorityLevel:
    return SeniorityLevel(**seniority_level.dict())


"""
def update_role(role_db: Role, role: RoleUpdate) -> Role:
    role_data = role.dict(exclude_unset=True)
    for key, value in role_data.items():
        setattr(role_db, key, value)
    return role_db


def to_role_employees(role: Role) -> RoleEmployees:
    role_data = role.dict()
    role_data["employees"] = role.employees
    return RoleEmployees(**role_data)

def to_role_employees_list(roles: list[Role]) -> list[RoleEmployees]:
    return [to_role_employees(role) for role in roles]

def to_role_seniority_levels(role: Role) -> RoleSeniorityLevels:
    role_data = role.dict()
    role_data["seniority_levels"] = role.seniority_levels
    return RoleSeniorityLevels(**role_data)

def to_role_seniority_levels_list(roles: list[Role]) -> list[RoleSeniorityLevels]:
    return [to_role_seniority_levels(role) for role in roles]
"""
