import requests

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.middleware.cors import CORSMiddleware

from fastapi_auth0 import Auth0, Auth0User
from dotenv import load_dotenv
import os

from src.employee import router as employee
from src.role import router as role
from src.interaction import router as interaction
from src.role_seniority_level.exceptions import add_role_seniority_level_exception_handlers
from src.seniority_level.exceptions import add_seniority_level_exception_handlers
from src.skill import router as skill
from src.skill_request_comment.exceptions import add_comment_exception_handlers
from src.skill_validation_request import router as request
from src.seniority_level import router as seniority_level
from src.skill_request_comment import router as comment
from src.role_seniority_level import router as role_seniority_level

from src.employee.exceptions import add_employee_exception_handlers
from src.role.exceptions import add_role_exception_handlers
from src.interaction.exceptions import add_interaction_exception_handlers
from src.skill.exceptions import add_skill_exception_handlers
from src.skill_validation_request.exceptions import add_request_exception_handlers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=os.environ.get("AUTH0_DOMAIN")+"/authorize",
    tokenUrl=os.environ.get("AUTH0_DOMAIN")+"/oauth/token",
    scopes={
        "openid": "OpenID Connect",
        "profile": "User profile",
        "email": "User email",
        "read:skills": "Read user skills",
    }

)

# Configurar Auth0 utilizando las variables de entorno
auth = Auth0(
    domain=os.environ.get("AUTH0_DOMAIN"),
    api_audience=os.environ.get("AUTH0_API_AUDIENCE"),
    # scopes={"read:users": "Read Users"},
)

# Protección de rutas con Auth0


@app.get("/protected")
async def protected_route(user: Auth0User = Depends(auth.get_user), token: str = Depends(oauth2_scheme)):
    # Aquí puedes acceder a los datos del usuario autenticado
    print("*****************************", user)
    # Make a request to the Auth0 userinfo endpoint to retrieve the user's profile
    userinfo_url = os.environ.get("ISSUER")+'/userinfo'
    headers = {'Authorization': f'Bearer {token}'}
    userinfo_response = requests.get(userinfo_url, headers=headers)

    # Extract the user's email from the response
    email = userinfo_response.json()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", email)
    return {"message": f"Hola, {email}!"}
    # return {"message": f"Hola, {user.email}!"}


@app.get("/")
def read_root():
    return {"Welcome": "Welcome to Seniority Management System REST API"}


app.include_router(role.router, prefix="/role", tags=["Role"])
app.include_router(skill.router, prefix="/skill", tags=["Skill"])
app.include_router(employee.router, prefix="/employee", tags=["Employee"])
app.include_router(request.router, prefix="/request", tags=["Request"])
app.include_router(comment.router, prefix="/comment", tags=["Request Comment"])
app.include_router(seniority_level.router,
                   prefix="/seniority_level", tags=["Seniority Level"])
app.include_router(
    role_seniority_level.router, prefix="/role_seniority_level", tags=["Role Seniority Level"]
)
app.include_router(interaction.router,
                   prefix="/interaction", tags=["Interaction"])


add_role_exception_handlers(app)
add_skill_exception_handlers(app)
add_comment_exception_handlers(app)
add_request_exception_handlers(app)
add_employee_exception_handlers(app)
add_interaction_exception_handlers(app)
add_seniority_level_exception_handlers(app)
add_role_seniority_level_exception_handlers(app)
