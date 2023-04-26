from src.skill.models import Skill
from src.skill.schemas import SkillCreate, SkillUpdate, SkillEmployees, SkillSeniorityLevels, SkillRequests, SkillAll


def to_skill(skill: SkillCreate) -> Skill:
    return Skill(**skill.dict())


def update_skill(skill_db: Skill, skill: SkillUpdate) -> Skill:
    skill_data = skill.dict(exclude_unset=True)
    for key, value in skill_data.items():
        setattr(skill_db, key, value)
    return skill_db


def to_skill_employees(skill: Skill) -> SkillEmployees:
    skill_data = skill.dict()
    skill_data["employees"] = []
    return SkillEmployees(**skill_data)


def to_skill_seniority_levels(skill: Skill) -> SkillSeniorityLevels:
    skill_data = skill.dict()
    skill_data["seniority_levels"] = skill.seniority_levels
    return SkillSeniorityLevels(**skill_data)


def to_skill_requests(skill: Skill) -> SkillRequests:
    skill_data = skill.dict()
    skill_data["requests"] = skill.requests
    return SkillRequests(**skill_data)

