from fastapi import Depends
from fastapi.security import OAuth2AuthorizationCodeBearer

from dotenv import load_dotenv
import os

# Load the environment variables from the file .env
load_dotenv()

oauth2_scheme_admin = OAuth2AuthorizationCodeBearer(
    authorizationUrl=os.environ.get("AUTH0_DOMAIN")+"/authorize",
    tokenUrl=os.environ.get("AUTH0_DOMAIN")+"/oauth/token",
    scopes={
        "openid": "OpenID Connect",
        "profile": "User profile",
        "email": "User email",
        "write:admin": "An admin can write to the database (Skills, roles, seniorities level)",
    }
)

oauth2_scheme_employee = OAuth2AuthorizationCodeBearer(
    authorizationUrl=os.environ.get("AUTH0_DOMAIN")+"/authorize",
    tokenUrl=os.environ.get("AUTH0_DOMAIN")+"/oauth/token",
    scopes={
        "openid": "OpenID Connect",
        "profile": "User profile",
        "email": "User email",
    }
)


async def get_token_bearer_admin(token: str = Depends(oauth2_scheme_admin)):
    return token


async def get_token_bearer_employee(token: str = Depends(oauth2_scheme_employee)):
    return token
