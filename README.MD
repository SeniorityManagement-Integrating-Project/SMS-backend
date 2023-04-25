# SMS-backend 

Project created with `Python 3.10.10`

## Dependency installation

`pip install -r requirements.txt`

**Note:** When a new dependency is installed you have to run the command: `pip freeze > requirements.txt`
to add it to the requirements file.

**Nota 2:** It is important to isolate the python virtual environment from the packages of the system’s global user
space, so as not to be injecting unnecessary dependencies into the project.

## Executing the project

At the root of the project we execute: `uvicorn src.main:app --reload`

**Note:** Dont forget to create the `.env` file with the environment variables.