from uuid import uuid4

from sqlalchemy import VARCHAR, Column, String, Enum
from sqlalchemy.orm import relationship
from enum import Enum as enumClass

from src.database import Base
from src.database.mixins import TimestampMixin


class UserRole(enumClass):
    ADMIN = "admin"
    USER = "regular-user"


class User(Base, TimestampMixin):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    username = Column(VARCHAR(255), unique=True, index=True, nullable=False)
    email = Column(VARCHAR(255), unique=True, index=True, nullable=False)
    password = Column(VARCHAR(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER)
    key = relationship("Key", uselist=False, back_populates="user")
