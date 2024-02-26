import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app_fastapi.config import settings


DB_DIR = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(DB_DIR, 'database', 'DB')
if not os.path.exists(db_path):
    os.makedirs(db_path)

engine = create_engine(
    settings.db_url, connect_args={"check_same_thread": False}, echo=True
)


def get_db():
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

