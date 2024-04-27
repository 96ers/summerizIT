# Trước khi chạy phải cài đặt các gói phần mềm sau:
#   - sentencepiece: Sử dụng cho việc tách từ (pip install sentencepiece)
#   - protobuf: Cần thiết cho một số mô hình của Hugging Face (pip install protobuf)
#   - pytorch với CUDA(xem hướng dẫn https://pytorch.org/get-started/locally/)
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

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

# The input may consist of multiple text sequences, with the number of text sequences in the input ranging from 1 up to 8, 16, 32, or even higher, depending on the GPU memory.
vi_texts = ["Cô cho biết: trước giờ tôi không đến phòng tập công cộng, mà tập cùng giáo viên Yoga riêng hoặc tự tập ở nhà.",
            "Khi tập thể dục trong không gian riêng tư, tôi thoải mái dễ chịu hơn.",
            "cô cho biết trước giờ tôi không đến phòng tập công cộng mà tập cùng giáo viên yoga riêng hoặc tự tập ở nhà khi tập thể dục trong không gian riêng tư tôi thoải mái dễ chịu hơn"]
print(translate_vi2en(vi_texts))
