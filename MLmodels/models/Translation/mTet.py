from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


model_name = "VietAI/envit5-translation"
tokenizer = AutoTokenizer.from_pretrained(model_name)  
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.cuda()

inputs = [
    "en: In the serene tranquility of the morning, birds chirped melodiously as sunlight filtered through the lush green canopy, casting playful shadows on the dew-kissed grass, while a gentle breeze whispered secrets among the swaying branches, painting a picturesque scene that danced gracefully in the eyes of nature's silent admirers."
    ]

outputs = model.generate(tokenizer(inputs, return_tensors="pt", padding=True).input_ids.to('cuda'), max_length=512)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])

