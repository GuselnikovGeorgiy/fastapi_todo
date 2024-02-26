## My first app using web-framework FastAPI.

### Simple toDo app to track your tasks.

### Steps:
1. Making & setting a virtual env for a project:

```commandline
python -m venv venv
venv/Scripts/activate.bat
python -m pip install pip --upgrade  #  if nessecary
```
I used poetry lib to configuring my dependencies, so u need to install it first:
```commandline
pip install -U pip setuptools
pip install poetry
```
You also can check poetry config if you need to:
```commandline
poetry config --list
```
configure venv in project:
```commandline
poetry config virtualenvs.in-project true
poetry init
```
Adding packages:
```
poetry add fastapi[all]
poetry add uvicorn
poetry add sqlalchemy
```
2. Run project:
```commandline
poetry run uvicorn app_fastapi.main:app --reload --port 8000
# or
uvicorn app_fastapi.main:app --reload --port 8000
```
