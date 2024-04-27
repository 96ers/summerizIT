from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """Đại học Quốc gia Hà Nội (ĐHQGHN - tên giao dịch bằng tiếng Anh: Vietnam National University, Hanoi; viết tắt là VNU) là trung tâm đào tạo, nghiên cứu khoa học, chuyển giao tri thức và công nghệ đa ngành, đa lĩnh vực, chất lượng cao; ngang tầm khu vực, dần đạt trình độ quốc tế; đáp ứng yêu cầu phát triển của đất nước, phù hợp với xu hướng phát triển giáo dục đại học tiên tiến.

ĐHQGHN có 3 cấp quản lý hành chính:

1) ĐHQGHN là đầu mối được Chính phủ giao các chỉ tiêu, kế hoạch hàng năm; có tư cách pháp nhân, có con dấu mang hình Quốc huy. Giám đốc, các Phó Giám đốc và Chủ tịch Hội đồng ĐHQGHN do Thủ tướng Chính phủ bổ nhiệm, miễn nhiệm.  

2) Các trường đại học, viện nghiên cứu khoa học thành viên; các trường, khoa, trung tâm đào tạo, nghiên cứu khoa học và công nghệ trực thuộc; các đơn vị dịch vụ, phục vụ công tác đào tạo, nghiên cứu khoa học trực thuộc ĐHQGHN là các đơn vị cơ sở có tư cách pháp nhân, có con dấu và tài khoản riêng.

3) Các khoa, phòng nghiên cứu và tương đương thuộc trường đại học, viện nghiên cứu khoa học thành viên và các đơn vị trực thuộc.

"""
print(summarizer(ARTICLE, max_length=200, min_length=200, do_sample=False))
