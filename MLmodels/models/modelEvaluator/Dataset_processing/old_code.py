import pandas as pd
import nltk
import csv
df = pd.read_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\articles_final.csv')
df['text'] = df['text'].astype(str)
segments = []

threshold_token_count = 300  
t=0
for i in range(6):
    sentences = nltk.sent_tokenize(df.at[i,'text'])
    segment_token_count = 0
    segment = []
    
    for sentence in sentences:
        
        tokens = nltk.word_tokenize(sentence)
        
        segment_token_count += len(tokens)
        
        if segment_token_count >= threshold_token_count:
            t+=1
            segments.append(segment)
            segment = []
            segment_token_count = len(tokens)
        
        segment.append(sentence)

    if segment:
        t+=1
        segments.append(segment)

segments_as_strings = [' '.join(segment) for segment in segments]

df = pd.DataFrame(segments_as_strings, columns=['segments'])
df.to_csv('server\\src\\models\\modelEvaluator\\Testing_Dataset\\segments.csv')