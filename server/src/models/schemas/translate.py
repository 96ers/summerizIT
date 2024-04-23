from pydantic import BaseModel


class TranslateInput(BaseModel):
    source_text: str


class TranslateOutput(BaseModel):
    translated_text: str
