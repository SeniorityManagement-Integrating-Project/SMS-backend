import os
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel


# pylint: disable=unused-import
from src.account.models import Account
from src.employee.models import Employee
from src.interaction.models import Interaction
from src.role.models import Role
from src.seniority_level.models import SeniorityLevel, RoleSeniorityLevel, SeniorityLevelSkill
from src.skill.models import Skill
from src.skill_validation_request.models import SkillValidationRequest

load_dotenv(dotenv_path=".env")

db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise ValueError("No database URL found")
engine = create_engine(url=db_url)
SQLModel.metadata.create_all(engine)
