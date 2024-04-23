import openai
import tiktoken
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import bart
import mTet

#run with uvicorn main:app --reload

class TranslationRequest(BaseModel):
    text: str
    isEnglish: bool


class SummarizationRequest(BaseModel):
    text: str
    length: int


class TokenRequest(BaseModel):
    text: str


app = FastAPI()


@app.get("/mTetTranslate")
async def translate(Tr: TranslationRequest):
    """mTet translation api

    Args:
        Tr (TranslationRequest): translation request

    Returns:
        json response: {"translation" : str}
    """
    # call the mTet translate method
    translation = mTet.translate(Tr.text, Tr.isEnglish)
    return {"translation": translation}


@app.get("/ChatGptSummarize")
async def summarize(Tr: SummarizationRequest):
    """chatGpt summarize api

    Args:
        Tr (SummarizationRequest): {"text": str, "length": int}

    Raises:
        HTTPException: status_code = 400 if tokens exceed limit

    Returns:
        json response body : {"Summarization" : str}
    """
    # encode the input to get tokens
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(Tr.text)
    text_length = len(tokens)

    # check token limit
    if text_length > 16000:
        raise HTTPException(
            status_code=400, detail="Text exceeds maximum token limit"
        )

    # make the chatGpt call
    client = openai.OpenAI(
        api_key="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"
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Please answer as if you are a natural language processing model made for text summarization",
            },
            {
                "role": "user",
                "content": "Please summarize the following text.The summarize text should shoud be "
                + Tr.length
                + " tokens : "
                + Tr.text,
            },
        ],
    )

    return {"Summarization": completion.choices[0].message}


@app.get("/ChatGptTransalate")
async def summarize(Tr: TranslationRequest):
    """chatGpt translate api

    Args:
        Tr (TranslationRequest):

    Raises:
        HTTPException: status_code = 400 if tokens exceed limit

    Returns:
        json response body : {"Translation" : str}
    """
    # encode the input to get tokens
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(Tr.text)
    text_length = len(tokens)

    Language = (
        "english to vietnamese" if Tr.isEnglish else "vietnamese to english"
    )
    # check limit
    if text_length > 16000:
        raise HTTPException(
            status_code=400, detail="Text exceeds maximum token limit"
        )
    # make chatGpt call
    client = openai.OpenAI(
        api_key="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"
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Please answer as if you are a natural language processing model made for "
                + Language
                + " translation",
            },
            {
                "role": "user",
                "content": "Please translate the following text : "
                + Tr.text,
            },
        ],
    )

    return {"Translation": completion.choices[0].message}


@app.get("/BartSummarize")
async def summarize(Sr: SummarizationRequest):
    """bart model summarize api
    Args:
        Tr (SummarizationRequest): {"text": str, "length": int}

    Raises:
        HTTPException: status_code = 400 if tokens exceed limit

    Returns:
        json response body : {"Summarization" : str}
    """
    # translate the input to english
    input = mTet.translate(Sr.text, False)
    # get input tokens
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(input)
    # check token limit and make according function calls

    if len(tokens) > 2048:
        raise HTTPException(
            status_code=400, detail="Text exceeds maximum token limit "
        )
    elif len(tokens) > 1024:
        return_value = bart.summarize_large_text(
            input, 2000, 800, 400, 300, Sr.length + 100, Sr.length
        )
    else:
        return_value = bart.summarize(input, 400, 200)[0]["summary_text"]

    return {"Summarization": return_value}


@app.get("/TokenCheck")
async def summarize(Tr: TokenRequest):
    """returns the token and token count of text

    Args:
        Tr (TokenRequest): {"text": str}

    Returns:
        json response body: {"token" : List[str] , "length" : int}
    """
    # get input tokens
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(Tr.text)
    return {
        "tokens": [
            encoding.decode_single_token_bytes(token) for token in tokens
        ],
        "length": len(tokens),
    }
