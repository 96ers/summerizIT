import enum
from uuid import uuid4

from sqlalchemy import TEXT, Column, Enum, ForeignKey, String

from src.database import Base
from src.database.mixins import TimestampMixin


class Language(enum.Enum):
    EN = "english"
    VI = "vietnamese"


class TranslationRequest(Base, TimestampMixin):
    __tablename__ = "translationRequests"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    userId = Column(String(36), ForeignKey("users.id"))
    text = Column(TEXT, nullable=False)
    language = Column(Enum(Language), default=Language.EN)
    targetLanguage = Column(Enum(Language), default=Language.VI)


class SummaryRequest(Base, TimestampMixin):
    __tablename__ = "summaryRequests"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    userId = Column(String(36), ForeignKey("users.id"))
    text = Column(TEXT, nullable=False)
    language = Column(Enum(Language), default=Language.EN)
