import pandas as pd
import time
from nltk.translate.bleu_score import sentence_bleu
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
#Load the model
tokenizer_en2vi = AutoTokenizer.from_pretrained("vinai/vinai-translate-en2vi-v2", src_lang="en_XX")
model_en2vi = AutoModelForSeq2SeqLM.from_pretrained("vinai/vinai-translate-en2vi-v2")
device_en2vi = torch.device("cuda")
model_en2vi.to(device_en2vi)

def translate_en2vi(en_texts: str) -> str:
    input_ids = tokenizer_en2vi(en_texts, padding=True, return_tensors="pt").to(device_en2vi)
    output_ids = model_en2vi.generate(
        **input_ids,
        decoder_start_token_id=tokenizer_en2vi.lang_code_to_id["vi_VN"],
        num_return_sequences=1,
        num_beams=5,
        early_stopping=True
    )
    vi_texts = tokenizer_en2vi.batch_decode(output_ids, skip_special_tokens=True)
    return vi_texts

tokenizer_vi2en = AutoTokenizer.from_pretrained("vinai/vinai-translate-vi2en-v2", src_lang="vi_VN")
model_vi2en = AutoModelForSeq2SeqLM.from_pretrained("vinai/vinai-translate-vi2en-v2")
device_vi2en = torch.device("cuda")
model_vi2en.to(device_vi2en)


def translate_vi2en(vi_texts: str) -> str:
    input_ids = tokenizer_vi2en(vi_texts, padding=True, return_tensors="pt").to(device_vi2en)
    output_ids = model_vi2en.generate(
        **input_ids,
        decoder_start_token_id=tokenizer_vi2en.lang_code_to_id["en_XX"],
        num_return_sequences=1,
        num_beams=5,
        early_stopping=True
    )
    en_texts = tokenizer_vi2en.batch_decode(output_ids, skip_special_tokens=True)
    return en_texts
#Evaluate en2vi translation
df = pd.read_csv("C:\\Users\\ACER\\Công nghệ phần mềm\\summerizIT-1\\server\\src\\models\\modelEvaluator\\Testing_Dataset\\english_segments.csv")
translation_times = []
df['segments'] = df['segments'].astype(str)
translated_segments = []
for index, row in df.iterrows():
    if index == 2:
        break
    start_time = time.time()
    translated_segments.append(translate_en2vi(row['segments']))
    end_time = time.time()
    translation_time = end_time - start_time
    translation_times.append(translation_time)
    print(index)
results_df = pd.DataFrame({
    'Text': translated_segments,
    'Translation_Time': translation_times,
})
results_df['Size'] = results_df['Text'].apply(len)
results_df.to_csv('C:\\Users\\ACER\\Công nghệ phần mềm\\summerizIT-1\\server\\src\\models\\modelEvaluator\\Testing_Dataset\\VinAi\\VinAi_en2vi.csv', index=False)
results_df.to_csv('C:\\Users\\ACER\\Công nghệ phần mềm\\summerizIT-1\\server\\src\\models\\modelEvaluator\\Testing_Dataset\\VinAi\\VinAi_en2vi.txt', sep='\n', index=False)
#Evaluate vi2en translation
df = pd.read_csv("server\\src\\models\\modelEvaluator\\Testing_Dataset\\vietnamese_segments.csv")
translation_times = []
df['segments'] = df['segments'].astype(str)
translated_segments = []
for index, row in df.iterrows():
    if index == 2:
        break
    start_time = time.time()
    translated_segments.append(translate_vi2en(row['segments']))
    end_time = time.time()
    translation_time = end_time - start_time
    translation_times.append(translation_time)
    print(index)
results_df = pd.DataFrame({
    'Text': translated_segments,
    'Translation_Time': translation_times,
})
results_df['Size'] = results_df['Text'].apply(len)
results_df.to_csv('C:\\Users\\ACER\\Công nghệ phần mềm\\summerizIT-1\\server\\src\\models\\modelEvaluator\\Testing_Dataset\\VinAi\\VinAi_vi2en.csv', index=False)
results_df.to_csv('C:\\Users\\ACER\\Công nghệ phần mềm\\summerizIT-1\\server\\src\\models\\modelEvaluator\\Testing_Dataset\\VinAi\\VinAi_vi2en.txt', sep='\n', index=False)
#Evaluate mixed translation
df = pd.read_csv("C:\\Users\\ACER\\Công nghệ phần mềm\\summerizIT-1\\server\\src\\models\\modelEvaluator\\Testing_Dataset\\mixed_segments.csv")
translation_times = []
df['segments'] = df['segments'].astype(str)
translated_segments = []
for index, row in df.iterrows():
    if index == 2:
        break
    start_time = time.time()
    translated_segments.append(translate_en2vi(row['segments']))
    end_time = time.time()
    translation_time = end_time - start_time
    translation_times.append(translation_time)
    print(index)
results_df = pd.DataFrame({
    'Text': translated_segments,
    'Translation_Time': translation_times,
})
results_df['Size'] = results_df['Text'].apply(len)
results_df.to_csv('C:\\Users\\ACER\\Công nghệ phần mềm\\summerizIT-1\\server\\src\\models\\modelEvaluator\\Testing_Dataset\\VinAi\\mixed_vi2en.csv', index=False)
results_df.to_csv('C:\\Users\\ACER\\Công nghệ phần mềm\\summerizIT-1\\server\\src\\models\\modelEvaluator\\Testing_Dataset\\VinAi\\mixed_vi2en.txt', sep='\n', index=False)
translation_times = []
translated_segments = []
for index, row in df.iterrows():
    if index == 2:
        break
    start_time = time.time()
    translated_segments.append(translate_vi2en(row['segments']))
    end_time = time.time()
    translation_time = end_time - start_time
    translation_times.append(translation_time)
    print(index)
results_df = pd.DataFrame({
    'Text': translated_segments,
    'Translation_Time': translation_times,
})
results_df['Size'] = results_df['Text'].apply(len)
results_df.to_csv('C:\\Users\\ACER\\Công nghệ phần mềm\\summerizIT-1\\server\\src\\models\\modelEvaluator\\Testing_Dataset\\VinAi\\mixed_en2vi.csv', index=False)
results_df.to_csv('C:\\Users\\ACER\\Công nghệ phần mềm\\summerizIT-1\\server\\src\\models\\modelEvaluator\\Testing_Dataset\\VinAi\\mixed_en2vi.txt', sep='\n', index=False)
