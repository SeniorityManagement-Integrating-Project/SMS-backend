from src.role_seniority_level.models import RoleSeniorityLevel
from src.role_seniority_level.schemas import (
    RoleSeniorityLevelCreate,
    RoleSeniorityLevelSkills,
    RoleSeniorityLevelUpdate,
)


def to_role_seniority_level(role_seniority_level: RoleSeniorityLevelCreate) -> RoleSeniorityLevel:
    return RoleSeniorityLevel(**role_seniority_level.dict(exclude_unset=True))


def update_role_seniority_level(
    role_seniority_level_db: RoleSeniorityLevel, role_seniority_level: RoleSeniorityLevelUpdate
) -> RoleSeniorityLevel:
    role_seniority_level_data = role_seniority_level.dict(exclude_unset=True)
    for key, value in role_seniority_level_data.items():
        setattr(role_seniority_level_db, key, value)
    return role_seniority_level_db


def to_role_seniority_level_skills(
    role_seniority_level: RoleSeniorityLevel,
) -> RoleSeniorityLevelSkills:
    role_sl_data = role_seniority_level.dict()
    role_sl_data["skills"] = role_seniority_level.skills
    return RoleSeniorityLevelSkills(**role_sl_data)
