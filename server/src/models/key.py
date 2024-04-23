from uuid import uuid4

from sqlalchemy import VARCHAR, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.database import Base
from src.database.mixins import TimestampMixin


class Key(Base, TimestampMixin):
    __tablename__ = "keys"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    userId = Column(String(36), ForeignKey("users.id"))
    publicKey = Column(VARCHAR(255), nullable=False)
    privateKey = Column(VARCHAR(255), nullable=False)
    user = relationship("User", back_populates="key")
