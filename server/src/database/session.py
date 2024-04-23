from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.configs import config

engine = create_engine(config.mysql.URI, echo=config.mysql.DEBUG)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_session():
    """
    Get the database session
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
