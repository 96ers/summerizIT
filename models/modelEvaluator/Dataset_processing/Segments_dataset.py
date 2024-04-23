import pandas as pd
import nltk
import csv
from underthesea import word_tokenize
import numpy as np
#English segment dataset creation
file_path = "server\\src\\models\\modelEvaluator\\Testing_Dataset\\test.en"
sentences_to_read = 350
try:
    with open(file_path, "r") as file:
        lines = [file.readline().strip() for _ in range(sentences_to_read)]
        df = pd.DataFrame(lines, columns=["Sentences"])  
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except IOError:
    print(f"An error occurred while reading the file {file_path}.")
df['text'] = df['Sentences'].astype(str)
segments = []
segment = ''
threshold_token_count = 300  
segment_token_count = 0
for index, row in df.iterrows():
    sentence = row['text']
    tokens = nltk.word_tokenize(sentence)
    if (segment_token_count+len(tokens)) >= threshold_token_count:
        segments.append(segment)
        segment = sentence
        segment_token_count = len(tokens)
    else:
        segment_token_count += len(tokens)
        segment += ' ' +  sentence
en = pd.DataFrame(segments, columns=['segments'])
en.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\english_segments.csv')
#Vietnamese segment dataset creation
file_path = "server\\src\\models\\modelEvaluator\\Testing_Dataset\\test.vi"
sentences_to_read = 350
try:
    with open(file_path, "r",encoding="utf-8") as file:
        lines = [file.readline().strip() for _ in range(sentences_to_read)]
        df = pd.DataFrame(lines, columns=["Sentences"])  
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except IOError:
    print(f"An error occurred while reading the file {file_path}.")
df['text'] = df['Sentences'].astype(str)
segments = []
segment = ''
threshold_token_count = 300  
segment_token_count = 0
for index, row in df.iterrows():
    sentence = row['text']
    tokens = word_tokenize(sentence)
    if (segment_token_count+len(tokens)) >= threshold_token_count:
        segments.append(segment)
        segment = sentence
        segment_token_count = len(tokens)
    else:
        segment_token_count += len(tokens)
        segment += ' ' +  sentence
vi = pd.DataFrame(segments, columns=['segments'])
vi.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\vietnamese_segments.csv')
#Mixed segment dataset creation
file_path = "server\\src\\models\\modelEvaluator\\Testing_Dataset\\test.vi"
sentences_to_read = 125
with open(file_path, "r",encoding="utf-8") as file:
    lines = [file.readline().strip() for _ in range(sentences_to_read)]
    df_vi = pd.DataFrame(lines, columns=["Sentences"])  


with open(file_path, "r",encoding="utf-8") as file:
    lines = [file.readline().strip() for _ in range(sentences_to_read)]
    df_en = pd.DataFrame(lines, columns=["Sentences"])  

df_mixed = df_en + ' ' + df_vi
df_mixed.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\test_mixed_a.txt', sep='\n', index=False)

df_mixed['text'] = df_mixed['Sentences'].astype(str)
segments = []
segment = ''
threshold_token_count = 300  
segment_token_count = 0
for index, row in df_mixed.iterrows():
    sentence = row['text']
    tokens = word_tokenize(sentence)
    if (segment_token_count+len(tokens)) >= threshold_token_count:
        segments.append(segment)
        segment = sentence
        segment_token_count = len(tokens)
    else:
        segment_token_count += len(tokens)
        segment += ' ' +  sentence
mixed = pd.DataFrame(segments, columns=['segments'])
mixed.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\mixed_segments_a.csv')