import os
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel

from src.account.models import Account
from src.employee.models import Employee
from src.role.models import Role
from src.seniority_level.models import SeniorityLevelSkill, SeniorityLevel
from src.skill.models import Skill
from src.skill_validation_request.models import SkillValidationRequest

load_dotenv(dotenv_path='.env')

db_url = os.getenv('DATABASE_URL')
engine = None
if db_url:
  engine = create_engine(db_url, echo=True)
  SQLModel.metadata.create_all(engine)
else:
  raise Exception('DATABASE_URL not found')
