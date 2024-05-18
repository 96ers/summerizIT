from openai import OpenAI
import tiktoken
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv

import bart
import mTet
import vinAi

load_dotenv()
class TranslationRequest(BaseModel):
    text: str
    EngToViet: bool


class SummarizationRequest(BaseModel):
    text: str
    length: int


class TokenRequest(BaseModel):
    text: str


app = FastAPI()


@app.post("/translate/mtet")
async def translate_by_mTet(Tr: TranslationRequest):
    """mTet translation api

    Args:
        Tr (TranslationRequest): translation request

    Returns:
        json response: {"translation" : str}
    """
    # call the mTet translate method
    translation = mTet.translate(Tr.text, Tr.EngToViet)
    return {"translation": translation}


@app.post("/translate/vinai")
async def translate_by_vinAi(Tr: TranslationRequest):
    """_summary_

    Args:
        Tr (TranslationRequest): translation request

    Returns:
       json response: {"translation" : str}
    """
    # call the vinAi translate method
    translation = vinAi.translate(Tr.text, Tr.EngToViet)
    return {"translation": translation}


@app.post("/summary/gpt")
async def summarize_by_gpt(Tr: SummarizationRequest):
    """chatGpt summarize api

    Args:
        Tr (SummarizationRequest): {"text": str, "length": int} (length is in tokens)

    Raises:
        HTTPException: status_code = 400 if tokens exceed limit

    Returns:
        json response body : {"summarization" : str}
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
    client = OpenAI(
        api_key= os.environ.get("OPENAI_API_KEY"),
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful text analyzer that knows how to summarize a text",
            },
            {
                "role": "user",
                "content": "Summarize this text denoted by backticks:"
                + str(Tr.length)
                + ". Summary should be"
                + str(Tr.text)
                + "words long."
            },
        ],
    )

    response = completion.choices[0].message.content
    return {"summarization": response}


@app.post("/translate/gpt")
async def translate_by_gpt(Tr: TranslationRequest):
    print(Tr)
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
        "english to vietnamese" if Tr.EngToViet else "vietnamese to english"
    )
    # check limit
    if text_length > 16000:
        raise HTTPException(
            status_code=400, detail="Text exceeds maximum token limit"
        )
    # make chatGpt call
    client = OpenAI(
        api_key= os.environ.get("OPENAI_API_KEY")
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

    return {"translation": completion.choices[0].message.content}


@app.post("/summary/bart")
async def summarize_by_bart(Sr: SummarizationRequest):
    """bart model summarize api
    Args:
        Tr (SummarizationRequest): {"text": str, "length": int} (length is in tokens)

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
        return_value = bart.summarize(input, Sr.length + 30, Sr.length)[0]["summary_text"]

    return {"summarization": return_value}


@app.post("/checktoken")
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
