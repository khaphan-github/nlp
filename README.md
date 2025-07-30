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
https://docs.google.com/document/d/1EQ6KwcZgtv-mcD_bffiORRZcKOqFe06DAwTdwiS7z-U/edit?tab=t.0
1. Mở bài: Giới thiệu vấn đề: (5)
Tóm tắt văn bản là quá trình: cô đọng văn bản thành văn bản có độ dài nhỏ hơn.
Việc tóm tắt văn bản mang lại nhiều lợi ích trong cả công việc và học tập, việc này có những lợi ích sau:
1. Tiết kiệm thời gian: Giúp người đọc nắm bắt nhanh chóng nội dung chính mà không cần đọc toàn bộ văn bản dài.
2. Tăng hiệu quả học tập và nghiên cứu: trong thời cùng một thời gian có thể tiếp cận được nhiều thông tin hơn.

Vấn đề tóm tắt văn bản này trên thế giới có rất nhiều công trình nghiên cứu & sử dụng nhiều thuận toán khác nhau như:
+ PageRank: Pagerank là thuật toán phân tích các liên kết được dùng trong Google Search để xếp hạng các trang web. Thuật toán này chỉ định giá trị nhất định cho mỗi thành phần của một tập hợp các văn bản liên kết với nhau, ví dụ như World Wide Web.
Mục đích "đo" tầm quan trọng tương đối của các liên kết trong tập hợp đó.
Áp dụng cho bất kỳ tập hợp văn bản nào có trích dẫn đối ứng và liên kết cụ thể.
giá trị (weight) mà nó gán cho bất kỳ thành phần E được gọi là PageRank của E và ký hiệu là 
PR(E)
+ TextRank: 
TextRank là một biến thể của thuật toán PageRank, được áp dụng cho xử lý ngôn ngữ tự nhiên, đặc biệt là trong tóm tắt văn bản và trích xuất từ khóa.

Chọn ra các câu có điểm cao nhất để tạo thành bản tóm tắt.
+ SumBasic: SumBasic là một thuật toán tạo tóm tắt văn bản đa tài liệu. Ý tưởng cơ bản là sử dụng các từ thường xuyên xuất hiện trong một tài liệu hơn các từ ít xuất hiện hơn để tạo ra một bản tóm tắt có khả năng tương đồng với bản tóm tắt của con người.

Thuật toán này tạo ra các bản tóm tắt có độ dài n, trong đó n là số câu do người dùng chỉ định.
  - SumBasic có các ưu điểm sau:
      + Được sử dụng để dễ dàng hiểu mục đích của một tài liệu.
      + Mang lại sự tiện lợi và linh hoạt hơn cho người đọc.
      + Tạo ra hình thức ngắn gọn và súc tích từ nhiều tài liệu.

    + Nếu có rồi thì làm sao họ không phát triển theo hướng đó nửa? có nhưng thách thức nào dẻ họ khong làm nửa.

  + Đối thũ cảnh tranh la gi, giải pháp tương tyuj là gì
  => Mục tiêu cuối dùng là để biết ngườita đã làm được gì, còn xót lại những vấn đề gì chưa giải quyết.

  NOte: Khi giải quyết thì có thể giải quyết được một phần thôi, nên mới đẽ ra phần kết luận & hướng phát triển

2. Giải quyết:(11)
  + High level ides (ý tửng là gì, nêu một số ứng dụng)
  + Các bước thực hiện
  + Vẽ lưu đồ.
  + Thực nghiêm & đánh giá & Phân tich & Huong xu ly loi..

3. Kết luận & Hướng phát triển: (Thường là từ những đánh giá chưa được đem qua hướng phát triển)

