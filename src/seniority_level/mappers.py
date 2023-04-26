from src.seniority_level.models import SeniorityLevel
from src.seniority_level.schemas import SeniorityLevelCreate, SeniorityLevelUpdate


def to_seniority_level(
    seniority_level: SeniorityLevelCreate | SeniorityLevelUpdate,
) -> SeniorityLevel:
    return SeniorityLevel(**seniority_level.dict(exclude_unset=True))


def update_seniority_level(
    seniority_level_db: SeniorityLevel, seniority_level: SeniorityLevelUpdate
) -> SeniorityLevel:
    seniority_level_data = seniority_level.dict(exclude_unset=True)
    for key, value in seniority_level_data.items():
        setattr(seniority_level_db, key, value)
    return seniority_level_db
