from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd
import nltk
from enum import Enum
import openai


class TranslationRequest(BaseModel):
    text: str
    isEnglish: bool


class Length(str, Enum):
    long = "long"
    short = "short"
    medium = "medium length"


class SummarizationRequest(BaseModel):
    text: str
    length: Length


app = FastAPI()


@app.get("/Translate")
async def translate(Tr: TranslationRequest):
    # defining translation mode
    Language = "en: " if Tr.isEnglish else "vi: "

    # create list of text segments of 300 tokens each
    sentences = nltk.sent_tokenize(Tr.text)
    segments = []
    segment_token_count = 0
    segment = []
    threshold_token_count = 300
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        segment_token_count += len(tokens)
        if segment_token_count >= threshold_token_count:
            segments.append(" ".join(segment))
            segment = []
            segment_token_count = len(tokens)
        segment.append(sentence)
    if segment:
        segments.append(" ".join(segment))
    # load model
    model_name = "VietAI/envit5-translation"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.cuda()
    # translate the models and then merge them into return string
    translated_segments = []
    for segment in segments:
        outputs = model.generate(
            tokenizer(
                Language + segment, return_tensors="pt", padding=True
            ).input_ids.to("cuda"),
            max_length=512,
        )
        translated_segments.append(
            tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
        )
    final = " ".join(translated_segments)

    return {"translation": final}


@app.get("/Summarize")
async def summarize(Tr: SummarizationRequest):
    client = openai.OpenAI()
    openai.api_key = "openai key here"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Please answer as if you are a natural language processing model made for text summarization",
            },
            {
                "role": "user",
                "content": "Please summarize the following text.The summarize text should be "
                + Tr.length
                + " :"
                + Tr.text,
            },
        ],
    )

    return {"Summarization": completion.choices[0].message}
