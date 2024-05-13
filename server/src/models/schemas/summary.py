from pydantic import BaseModel
from datetime import datetime


class SummaryInput(BaseModel):
    source_text: str
    model: str = "gpt"


class SummaryOutput(BaseModel):
    summarized_text: str


class SummaryHistory(BaseModel):
    id: str
    source_text: str
    summarized_text: str
    time: datetime
