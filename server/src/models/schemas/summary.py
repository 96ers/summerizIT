from pydantic import BaseModel
from datetime import datetime


class SummaryInput(BaseModel):
    source_text: str
    model: str = "gpt"
    length: int = 10


class SummaryOutput(BaseModel):
    summarized_text: str


class SummaryHistory(BaseModel):
    id: str
    source_text: str
    summarized_text: str
    time: datetime
