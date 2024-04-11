from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, String

from src.database import Base
from src.database.mixins import TimestampMixin


class Key(Base, TimestampMixin):
    __tablename__ = "keys"
    userId = Column(String(36), ForeignKey("users.userId"))
    keyId = Column(Integer, primary_key=True, autoincrement=True)
    privateKey = Column(VARCHAR(255), nullable=False)
    publicKey = Column(VARCHAR(255), nullable=False)
