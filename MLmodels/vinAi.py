# Trước khi chạy phải cài đặt các gói phần mềm sau:
#   - sentencepiece: Sử dụng cho việc tách từ (pip install sentencepiece)
#   - protobuf: Cần thiết cho một số mô hình của Hugging Face (pip install protobuf)
#   - pytorch với CUDA(xem hướng dẫn https://pytorch.org/get-started/locally/)
import torch
import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate_vi2en(vi_texts: str) -> str:
    tokenizer_vi2en = AutoTokenizer.from_pretrained("vinai/vinai-translate-vi2en-v2", src_lang="vi_VN")
    model_vi2en = AutoModelForSeq2SeqLM.from_pretrained("vinai/vinai-translate-vi2en-v2")

    if torch.cuda.is_available():  
        device_vi2en = torch.device("cuda")
    else:
        device_vi2en = torch.device("cpu")
    model_vi2en.to(device_vi2en)
    sentences = nltk.sent_tokenize(vi_texts)
    translated_sentences = []
    for sentence in sentences:
        input_ids = tokenizer_vi2en(sentence, padding=True, return_tensors="pt").to(device_vi2en)
        output_ids = model_vi2en.generate(
            **input_ids,
            decoder_start_token_id=tokenizer_vi2en.lang_code_to_id["en_XX"],
            num_return_sequences=1,
            num_beams=5,
            early_stopping=True
        )
        translated_sentences.append(tokenizer_vi2en.batch_decode(output_ids, skip_special_tokens=True)[0])
    en_texts = " ".join(translated_sentences)
    return en_texts

def translate_en2vi(en_texts: str) -> str:
    tokenizer_en2vi = AutoTokenizer.from_pretrained("vinai/vinai-translate-en2vi-v2", src_lang="en_XX")
    model_en2vi = AutoModelForSeq2SeqLM.from_pretrained("vinai/vinai-translate-en2vi-v2")

    if torch.cuda.is_available():
        device_en2vi = torch.device("cuda")
    else:
        device_en2vi = torch.device("cpu")
    model_en2vi.to(device_en2vi)

    sentences = nltk.sent_tokenize(en_texts)
    translated_sentences = []
    for sentence in sentences:
        input_ids = tokenizer_en2vi(sentence, padding=True, return_tensors="pt").to(device_en2vi)
        output_ids = model_en2vi.generate(
            **input_ids,
            decoder_start_token_id=tokenizer_en2vi.lang_code_to_id["vi_VN"],
            num_return_sequences=1,
            num_beams=5,
            early_stopping=True
        )
        translated_sentences.append(tokenizer_en2vi.batch_decode(output_ids, skip_special_tokens=True)[0])
    vi_texts = " ".join(translated_sentences)
    return vi_texts

def translate(text, EngToViet):
    
    if EngToViet:
        return translate_en2vi(text)
    else:
        return translate_vi2en(text)
    
    return ""

