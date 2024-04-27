import tiktoken
from langchain.text_splitter import NLTKTextSplitter
from transformers import pipeline

# load model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def summarize(text, max_value, min_value):
    """Summarize method called when input length <= 1024 tokens

    Args:
        text (str): input text
        max_value (int): max output token length
        min_value (int): min output token length

    Returns:
        List[Dict[str, str]]: list of a dict containing the summary
    """
    return summarizer(
        text, max_length=max_value, min_length=min_value, do_sample=False
    )


def split_chunk(text, chunk_size, overlap_size):
    """sliding window chunking method using .split()

    Args:
        text (str): input text
        chunk_length (int): length of chunks
        overlap_size (int): the overlap size of chunks

    Returns:
        List[str]: list of chunks of type str
    """
    chunks = []
    words = text.split()
    start = 0
    ncoding = tiktoken.get_encoding("cl100k_base")
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        start += chunk_size - overlap_size
    return chunks


def nltk_chunk(text, chunk_length, overlap_size):
    """sliding window chunking method using using NLTKTextSplitter

    Args:
        text (str): input text
        chunk_length (int): length of chunks
        overlap_size (int): the overlap size of chunks

    Returns:
        List[str]: list of chunks of type str
    """

    # 2000,1000
    nltk_splitter = NLTKTextSplitter(
        separator=" ", chunk_size=chunk_length, chunk_overlap=overlap_size
    )
    splits = nltk_splitter.split_text(text)
    return splits


def summarize_chunks(chunks, chunk_size, max_value, min_value):
    """Summarize each chunk, returns combined chunk summaries

    Args:
        chunks (_type_): list of chunk strings
        chunk_size (int): size of chunks in length
        max_value (int): max output token length
        min_value (int): min output token length

    Returns:
        str: the combined chunk summaries
    """
    summarized_chunks = []
    encoding = tiktoken.get_encoding("cl100k_base")
    for chunk in chunks:
        if len(chunk) < chunk_size:
            continue
        summarized_chunk = summarizer(
            chunk, max_length=max_value, min_length=min_value, do_sample=False
        )
        summarized_chunks.append(summarized_chunk[0]["summary_text"])
    return " ".join(summarized_chunks)


def summarize_large_text(
    text,
    chunk_size,
    overlap_size,
    max_chunk_value,
    min_chunk_value,
    max_value,
    min_value,
):
    """summarize method when 1024 tokens < input token length < 2048 tokens

    Args:
        text (str): text input
        chunk_size (int): size of the chunk in terms of length
        overlap_size (int): the chunks overlap size in terms of length
        max_chunk_value (int): max chunk summary output token length
        min_chunk_value (int): min chunk summary output token length
        max_value (int): max output token length
        min_value (int): min output token length

    Returns:
        str : the summary
    """
    # chunks = split_chunk(text, chunk_size, overlap_size)
    chunks = nltk_chunk(text, chunk_size, overlap_size)

    combined_summary = summarize_chunks(
        chunks, chunk_size, max_chunk_value, min_chunk_value
    )

    # run a final summary on combined summarize chunks text
    final_summary = summarizer(
        combined_summary,
        max_length=max_value,
        min_length=min_value,
        do_sample=False,
    )

    return final_summary[0]["summary_text"]
