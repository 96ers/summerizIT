import torch
import tiktoken
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
if torch.cuda.is_available():       
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model = T5ForConditionalGeneration.from_pretrained("NlpHUST/t5-small-vi-summarization")
tokenizer = T5Tokenizer.from_pretrained("NlpHUST/t5-small-vi-summarization",legacy = False)
model.to(device)

src = """Điện ảnh đã và đang góp phần không nhỏ quảng bá danh lam thắng cảnh, giá trị văn hóa, di sản của các vùng miền đến với công chúng, giúp thu hút khách du lịch và thúc đẩy sự phát triển kinh tế-xã hội của địa phương. Thực tế cho thấy, nhiều địa điểm là bối cảnh trong tác phẩm điện ảnh đã trở thành địa chỉ thu hút đông đảo du khách tìm đến. Tiêu biểu thời gian qua có thể kể đến lượng khách ồ ạt đổ về “Nhà của Pao” ở xã Sủng Là, huyện Đồng Văn, tỉnh Hà Giang sau thành công của bộ phim “Chuyện của Pao”; hay việc gia tăng đột biến số lượng du khách đến với quần thể Di sản thế giới Tràng An (Ninh Bình) ngay khi phim “Kong Skull Island” ra mắt năm 2017. Tại các địa danh ít được biết đến như ngôi làng Đo Đo ở xã Bình Quế (Thăng Bình, Quảng Nam) cũng trở nên nổi tiếng, được nhiều người tìm đến trải nghiệm sau khi bộ phim “Mắt biếc” công chiếu. Mới đây, bối cảnh xuất hiện trong các bộ phim “Tết ở làng Địa Ngục”, “Kẻ ăn hồn” cũng được khán giả săn tìm và đến thăm, đó là làng Sảo Há, xã Vần Chải, huyện Đồng Văn, tỉnh Hà Giang.

Là quốc gia sở hữu nhiều cảnh quan thiên nhiên ấn tượng và bản sắc văn hóa độc đáo, đa dạng nhưng so với nhiều nước trong khu vực, Việt Nam chưa thật sự trở thành điểm đến hấp dẫn đối với các đoàn làm phim nước ngoài, thậm chí ngay chính các đoàn làm phim trong nước cũng vấp phải không ít rào cản. Tiềm năng du lịch của nhiều vùng chưa được các nhà làm phim “đánh thức” và khai thác một cách hiệu quả. Từ đây đặt ra vấn đề: Các địa phương đã sẵn sàng mời gọi, “trải thảm đỏ” đón các nhà làm phim trên tinh thần hợp tác đôi bên cùng có lợi? Không ít đoàn làm phim đi tìm bối cảnh tại các địa phương song gặp phải sự kém mặn mà của chính quyền địa phương cũng như cơ quan chức năng. Cùng với đó họ phải đối mặt với nhiều thủ tục phiền hà, chồng chéo và những quy định hành chính cứng nhắc, mất thời gian, làm gia tăng đáng kể chi phí, khiến dự án làm phim bị chậm tiến độ, đội vốn.

Từ đây, những kế hoạch vốn rất thiện chí của đoàn làm phim không thể thực hiện. Bên cạnh đó, theo các chuyên gia những giấy phép con hiện nay là một nguyên nhân khiến nhiều đoàn làm phim trong nước cũng như nước ngoài thấy nản, chấp nhận bỏ cuộc. Đây là điều rất đáng tiếc.

Tất nhiên, cũng cần thừa nhận một thực tế, đó là trong quá trình tác nghiệp tại địa phương, một số đoàn làm phim hành xử chưa phù hợp lối sống, văn hóa bản địa, không hoàn trả mặt bằng sau khi kết thúc cảnh quay, xâm hại cơ sở vật chất, cảnh quan tại di tích cũng như danh lam thắng cảnh,... Cách đây ít lâu, một đoàn làm phim tự ý tô vẽ giếng cổ trong khuôn viên ngôi đình Mông Phụ (Đường Lâm, Hà Nội) đã được xếp hạng di tích quốc gia khiến người dân bức xúc, chính quyền phải vào cuộc.

Một nguyên nhân khác dẫn đến sự thờ ơ của nhiều địa phương với đoàn làm phim là bởi suốt một thời gian dài, điện ảnh Việt Nam hoạt động theo hình thức bao cấp từ khâu sản xuất đến khâu phát hành. Do đó, các nhà làm phim cũng như các địa phương đều chưa quan tâm nhiều đến yếu tố thị trường, cũng như quảng bá du lịch thông qua tác phẩm điện ảnh. Song khi bước vào cơ chế thị trường, cùng với các hãng phim của Nhà nước (từng bước được cổ phần hóa), điện ảnh ngày càng có sự góp mặt đông đảo của giới làm phim tư nhân, mức độ cạnh tranh ngày càng gia tăng. Những bộ phim được thị trường đón nhận góp phần kích cầu du lịch, thúc đẩy kinh tế cho địa phương.

Nhằm tháo gỡ phần nào vướng mắc hiện nay liên quan vấn đề này, năm 2023 Hiệp hội Xúc tiến phát triển điện ảnh Việt Nam (VFDA) chính thức công bố Bộ chỉ số thu hút đoàn làm phim (Production Attraction Index-PAI) với mục tiêu đánh giá sự quan tâm của các tỉnh, thành phố, đồng thời nâng cao sức hấp dẫn của từng địa phương, mở cánh cửa mời đoàn làm phim tìm đến. PAI được xây dựng dựa trên 5 tiêu chí, gồm: Hỗ trợ tài chính, hỗ trợ thông tin, hỗ trợ thực địa, hỗ trợ thủ tục pháp lý và hạ tầng sẵn có. Nhà làm phim Ấn Độ-Rahul Sudesh Bali đánh giá cao Bộ chỉ số thu hút đoàn làm phim vì theo ông, “thông tin của PAI giúp chúng tôi hiểu thêm về những ưu đãi, hỗ trợ đoàn quay phim của các tỉnh, thành phố ở Việt Nam. Tôi nghĩ các thành phố khác của Việt Nam nên phối hợp VFDA tham gia PAI. Như vậy, điện ảnh của Việt Nam sẽ phát triển mạnh mẽ hơn”.

Ngay khi công bố PAI, 10 địa phương đã đăng ký tham gia, một trong số đó là Phú Yên - địa phương có sự tăng trưởng du lịch mạnh mẽ nhờ sự lan tỏa từ tác phẩm điện ảnh. Lượng du khách đến với Phú Yên tăng mạnh từ 750.000 lượt khách năm 2014 tăng lên 1,8 triệu lượt khách năm 2019, doanh thu 2.000 tỷ đồng, cao gấp 2,5 lần so với trước khi bộ phim “Tôi thấy hoa vàng trên cỏ xanh” của đạo diễn Victor Vũ ra mắt. Phú Yên cũng đang đứng đầu bảng xếp hạng PAI. 9 tỉnh, thành phố khác cũng nhiệt tình tham gia PAI là Tuyên Quang, Khánh Hòa, Nam Định, Đà Nẵng, Hà Nội, Thừa Thiên Huế, Ninh Bình, Bắc Kạn và Cần Thơ. Tuy chưa tham gia PAI nhưng Lâm Đồng cho thấy quyết tâm của lãnh đạo tỉnh trong việc xây dựng nơi đây như một phim trường hấp dẫn các đoàn làm phim, từ đó kích cầu du lịch, nâng cao đời sống văn hóa tinh thần cho nhân dân. Chỉ riêng năm 2022, địa phương này đã đón và tạo điều kiện cho 130 đoàn làm phim chọn bối cảnh. Việc cấp phép cho đoàn làm phim chỉ mất hai ngày; cảnh quay sử dụng bối cảnh tại địa phương hoàn toàn không bị thu phí.

Hàn Quốc, Thái Lan, Indonesia, Ấn Độ... đã phát huy rất tốt việc quảng bá thương hiệu quốc gia, phát triển du lịch thông qua phim ảnh, các show truyền hình. Đây là hướng đi hiệu quả cần học tập, nhất là với những tiềm năng sẵn có mà chúng ta chưa khai thác hết, nhưng cũng đòi hỏi sự thay đổi tư duy của các nhà quản lý, các đơn vị hoạt động trong lĩnh vực văn hóa, đặc biệt là ngành du lịch và điện ảnh. Chính quyền địa phương và các ngành chức năng cần tăng cường phối hợp đồng bộ, hiệu quả, hoạch định chiến lược quảng bá đến các đoàn làm phim mạnh mẽ hơn, từng bước đơn giản hóa thủ tục hành chính, hỗ trợ chính sách thuế và tài chính cho đoàn làm phim. Thậm chí, chính quyền có thể chủ động đặt hàng nhà làm phim thực hiện các cảnh quay tại địa phương mình với nội dung phù hợp, “khoe” được những nét đặc sắc của địa phương. Tạo điều kiện cho nhà làm phim nói riêng, hoạt động văn hóa nói chung sẽ mở cánh cửa để quảng bá cho địa phương, thu hút khách du lịch, từng bước xây dựng thương hiệu cho mỗi vùng, miền, từ đó góp phần xây dựng thành công thương hiệu của quốc gia
"""
tokenized_text = tokenizer.encode(src, return_tensors="pt").to(device)
model.eval()
summary_ids = model.generate(
                    tokenized_text,
                    max_length=256, 
                    num_beams=5,
                    repetition_penalty=2.5, 
                    length_penalty=1, 
                    early_stopping=True,

                )
encoding = tiktoken.get_encoding("cl100k_base")
tokens = encoding.encode(src)
print(len(tokens))
output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(output)
