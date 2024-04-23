from sqlalchemy import Column, VARCHAR, String
from uuid import uuid4

from src.database import Base
from src.database.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"
    userId = Column(String(36), primary_key=True, default=str(uuid4()))
    username = Column(VARCHAR(255), unique=True, index=True, nullable=False)
    email = Column(VARCHAR(255), unique=True, index=True, nullable=False)
    password = Column(VARCHAR(255), nullable=False)
