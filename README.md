## FastAPI ToDo application: simple task manager

### Used packages:
```commandline
fastapi
uvicorn
sqlalchemy
poetry         #  to manage dependency
```
How to run:
1. Install poetry package:
```commandline
python -m pip install --upgrade pip  #  if necessary
pip install poetry
poetry init
```
2. Install dependency from pyproject.toml:
```commandline
poetry install
```
3. Run uvicorn webserver:
```commandline
poetry run uvicorn app_fastapi.main:app --reload --port 8000
# or
uvicorn app_fastapi.main:app --reload --port 8000