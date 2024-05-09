import nltk
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def translate(text, isEnglish):
    """_summary_

    Args:
        text (str): text input
        isEnglish (bool): boolean value

    Returns:
        str : translation
    """
    # load model
    model_name = "VietAI/envit5-translation"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    # select language
    Language = "en: " if isEnglish else "vi: "

    # splits the text into  segments to translate
    sentences = nltk.sent_tokenize(text)
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

    # check if cuda is available with code:
    if torch.cuda.is_available():
        model.cuda()
        translated_segments = []
        for segment in segments:
            outputs = model.generate(
                tokenizer(
                    Language + segment, return_tensors="pt", padding=True
                ).input_ids.to("cuda"),
                max_length=512,
            )
            translated_segments.append(
                tokenizer.batch_decode(outputs, skip_special_tokens=True)[0][4:]
            )
        answer = " ".join(translated_segments)
    else:
        print("CUDA is not available. Only CPU will be used.")
        translated_segments = []
        for segment in segments:
            outputs = model.generate(
                tokenizer(
                    Language + segment, return_tensors="pt", padding=True
                ).input_ids,
                max_length=512,
            )
            translated_segments.append(
                tokenizer.batch_decode(outputs, skip_special_tokens=True)[0][4:]
            )
        answer = " ".join(translated_segments)
    final = answer
    return final
