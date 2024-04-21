from sqlalchemy import Column, ForeignKey, String, TEXT, Enum
from uuid import uuid4

from src.database import Base
from src.database.mixins import TimestampMixin

from .request import Language


class TranslationResult(Base, TimestampMixin):
    __tablename__ = "translationResults"
    id = Column(String(36), primary_key=True, default=str(uuid4()))
    requestId = Column(String(36), ForeignKey("translationRequests.id"))
    text = Column(TEXT, nullable=False)
    language = Column(Enum(Language), default=Language.VI)


class SummaryResult(Base, TimestampMixin):
    __tablename__ = "summaryResults"
    id = Column(String(36), primary_key=True, default=str(uuid4()))
    requestId = Column(String(36), ForeignKey("summaryRequests.id"))
    text = Column(TEXT, nullable=False)
    language = Column(Enum(Language), default=Language.EN)
