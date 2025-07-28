# Báo cáo cuối kỳ
## Hướng tiếp cận

## 1. Các bước xử ly chuyển doc vào file csv để dể xử lý
1. Đọc dữ liệu trong thư mục duc_text.
2. Dùng regex để lấy được thông tin: docid, num, wdcount, sentence
3. Lap lai voi tat cả các file trong thư mục để tạo 1 file csv duy nhất

## 2. Xây dựng lại các hàm if,idf, cosine, euclid để vector hóa văn bản.
1. Hàm làm sach du liệu văn bản tiếng anh.
2. Hàm tính tf-idf trên ma trận.
3. Hàm tính cosine trên ma trận.

## 3. Xây dựng đồ thị:
1. Duyệt từng document đã chuẩn bị trong file csv trong bước 1
2. Thực hiện tính tf-idf, cosine, của từng document, nếu độ tương quan giửa 2 câu < SIM_THRESHOLD tức là có liên kết giữa 2 câu ấy
3. Sau đó lưu kết quả bào file json với định dạng
  [
    // Tung dòng này ứng với từng đồ thị vô lương của một tập tài liệu
    [
      // Ma trận này thể hiện sự liên quan của một câu với một câu khác trong một document
      [0,0,1],
      [0,0,1],
      [1,1,0],
    ],
  ]

## 4. Tính toán pagerank
1. Hàm pagerank
2. Duyệt file json ở bước 3 để tính pagerage cho từng documnent.
3. Sắp xếp lại page rage & và map với các docid_num trong tập dữ liệu đã chuẩn bị ở bước 1
   - Tiêu chí: Số lượng của đoạn tóm tắt được tính bằng tỉ lệ (36%) so với document gốc.
4. Lưu kết quả vào file simarizes_sperate.csv

## 5. Đánh giá kết quả:
1. Precition:
2. Recall:
3. F1 score:

## 6. Tiêu chí tối thiểu:
1. Mục tiêu của bài toán là gì, input, output là gì.
2. Phương phép tiếp cận chính & mô tả ý tưởng chính của phương án tiếp cận
3. Mô tả chi tiết các bước tiếp cận đã chọn
4. Biểu diễn được văn bản dưới dạng đồ thị
5. Xếp hạn được đồ thị theo mức dộ quan trọng.
6. Lấy được tóm tắt văn bản
7. Nhận xét ưu nhược điểm của phương pháp đang áp dụng
8. Cải thiện: thêm tọng số vào đồ thị chẳn hạn
## 7. Phản biện:

1. Tại sao abc?
2. Nếu không a thì c ok?
3. So sánh giửa ....?


# Báo cáo cuối kỳ: (Không quá 20 trang nội dung)
1. Mở bài: Giới thiệu vấn đề: 
  + Vấn đề hienejt ại là gì?
  + Trên thế giới có ai đã làm chưa
  + Nếu có rồi thì làm sao họ không phát triển theo hướng đó nửa? có nhưng thách thức nafop dẻ họ khong làm nửa.
  + Đối thũ cảnh tranh la gi, giải pháp tương tyuj là gì
  => Mục tiêu cuối dùng là để biết ngườita đã làm được gì, còn xót lại những vấn đề gì chưa giải quyết
  NOte: Khi giải quyết thì có thể giải quyết được một phần thôi, nên mới đẽ ra phần kết luận & hướng phát triển
2. Giải quyết:
  + High level ides (ý tửng là gì, nêu một số ứng dụng)
  + Các bước thực hiện
  + Thực nghiêm & đánh giá
3. Kết luận & Hướng phát triển: (Thường là từ những đánh giá chưa được đem qua hướng phát triển)