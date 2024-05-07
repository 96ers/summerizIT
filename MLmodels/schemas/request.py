from pydantic import BaseModel


class TranslationRequest(BaseModel):
    text: str
    isEnglish: bool


class SummarizationRequest(BaseModel):
    text: str
    length: int


class TokenRequest(BaseModel):
    text: str
