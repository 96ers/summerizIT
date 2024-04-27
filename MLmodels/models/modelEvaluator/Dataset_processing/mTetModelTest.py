import pandas as pd
import time
from nltk.translate.bleu_score import sentence_bleu
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
#Load the model
model_name = "VietAI/envit5-translation"
tokenizer = AutoTokenizer.from_pretrained(model_name)  
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.cuda()
#Evaluate en2vi translation

df = pd.read_csv("server\\src\\models\\modelEvaluator\\Testing_Dataset\\english_segments.csv")
translation_times = []
df['segments'] = df['segments'].astype(str)
translated_segments = []
for index, row in df.iterrows():
    if index == 10:
        break
    start_time = time.time()
    outputs = model.generate(tokenizer("en : " + row['segments'], return_tensors="pt", padding=True).input_ids.to('cuda'), max_length=512)
    translated_segments.append(tokenizer.batch_decode(outputs, skip_special_tokens=True))
    end_time = time.time()
    translation_time = end_time - start_time
    translation_times.append(translation_time)
    print(index)
results_df = pd.DataFrame({
    'Text': translated_segments,
    'Translation_Time': translation_times,
})
results_df['Size'] = results_df['Text'].apply(len)
results_df.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\mTet\\mTet_en2vi.csv', index=False)
results_df.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\mTet\\mTet_en2vi.txt', sep='\n', index=False)
#Evaluate vi2en translation
df = pd.read_csv("server\\src\\models\\modelEvaluator\\Testing_Dataset\\vietnamese_segments.csv")
translation_times = []
df['segments'] = df['segments'].astype(str)
translated_segments = []
for index, row in df.iterrows():
    if index == 10:
        break
    start_time = time.time()
    outputs = model.generate(tokenizer("vi : " + row['segments'], return_tensors="pt", padding=True).input_ids.to('cuda'), max_length=512)
    translated_segments.append(tokenizer.batch_decode(outputs, skip_special_tokens=True))
    end_time = time.time()
    translation_time = end_time - start_time
    translation_times.append(translation_time)
    print(index)
results_df = pd.DataFrame({
    'Text': translated_segments,
    'Translation_Time': translation_times,
})
results_df['Size'] = results_df['Text'].apply(len)
results_df.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\mTet\\mTet_vi2en.csv', index=False)
results_df.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\mTet\\mTet_vi2en.txt', sep='\n', index=False)
#Evaluate mixed translation
df = pd.read_csv("server\\src\\models\\modelEvaluator\\Testing_Dataset\\mixed_segments.csv")
translation_times = []
df['segments'] = df['segments'].astype(str)
translated_segments = []
for index, row in df.iterrows():
    if index == 10:
        break
    start_time = time.time()
    outputs = model.generate(tokenizer("vi : " + row['segments'], return_tensors="pt", padding=True).input_ids.to('cuda'), max_length=512)
    translated_segments.append(tokenizer.batch_decode(outputs, skip_special_tokens=True))
    end_time = time.time()
    translation_time = end_time - start_time
    translation_times.append(translation_time)
    print(index)
results_df = pd.DataFrame({
    'Text': translated_segments,
    'Translation_Time': translation_times,
})
results_df['Size'] = results_df['Text'].apply(len)
results_df.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\mTet\\mixed_vi2en.csv', index=False)
results_df.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\mTet\\mixed_vi2en.txt', sep='\n', index=False)
translation_times = []
translated_segments = []
for index, row in df.iterrows():
    if index == 10:
        break
    start_time = time.time()
    outputs = model.generate(tokenizer("en : " + row['segments'], return_tensors="pt", padding=True).input_ids.to('cuda'), max_length=512)
    translated_segments.append(tokenizer.batch_decode(outputs, skip_special_tokens=True))
    end_time = time.time()
    translation_time = end_time - start_time
    translation_times.append(translation_time)
    print(index)
results_df = pd.DataFrame({
    'Text': translated_segments,
    'Translation_Time': translation_times,
})
results_df['Size'] = results_df['Text'].apply(len)
results_df.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\mTet\\mixed_en2vi.csv', index=False)
results_df.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\mTet\\mixed_en2vi.txt', sep='\n', index=False)