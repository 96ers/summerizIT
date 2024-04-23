import nltk
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

    # check if cuda is available with code:
    # if torch.cuda.is_available():
    # Get the number of available GPUs
    # num_gpus = torch.cuda.device_count()
    # print(f"Number of GPUs available: {num_gpus}")
    # Get the name of each GPU
    # for i in range(num_gpus):
    # print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
    # else:
    # print("CUDA is not available. Only CPU will be used.")

    # remove the line below if cuda not available and change input_ids.to('cuda') to just input_ids
    model.cuda()
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

    # translate the segments and then join them
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
    final = " ".join(translated_segments)

    return final
