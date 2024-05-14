from datetime import datetime

from pydantic import BaseModel


class TranslateInput(BaseModel):
    source_text: str
    model: str = "gpt"


class TranslateOutput(BaseModel):
    translated_text: str


class TranslateHistory(BaseModel):
    id: str
    source_text: str
    translated_text: str
    time: datetime
