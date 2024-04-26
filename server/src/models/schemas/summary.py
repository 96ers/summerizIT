from pydantic import BaseModel


class SummaryInput(BaseModel):
    source_text: str


class SummaryOutput(BaseModel):
    summarized_text: str
