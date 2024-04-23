from sqlalchemy import Column, VARCHAR, ForeignKey, String
from uuid import uuid4

from src.database import Base
from src.database.mixins import TimestampMixin


class Key(Base, TimestampMixin):
    __tablename__ = "keys"
    userId = Column(String(36), ForeignKey("users.userId"))
    keyId = Column(String(36), primary_key=True, default=str(uuid4()))
    privateKey = Column(VARCHAR(255), nullable=False)
    publicKey = Column(VARCHAR(255), nullable=False)
