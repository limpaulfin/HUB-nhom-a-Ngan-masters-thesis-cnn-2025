# Cấu trúc thư mục tiểu luận

```
docs/
├── chapter2/
│   ├── 2.0-README.md
│   ├── 2.1-cnn.md
│   ├── 2.1.1-dinh-nghia-ung-dung.md
│   ├── 2.1.2-kien-truc-co-ban.md
│   ├── 2.1.3-ham-kich-hoat.md
│   ├── 2.1.4-uu-nhuoc-diem.md
│   ├── 2.2-so-sanh.md
│   └── references.md
└── OKR.md

# Ghi chú về format tài liệu tham khảo

1. Định dạng APA 7th Edition cho tài liệu tham khảo:

## Sách:
Tác giả, A. A. (Năm). *Tên sách* (Ấn bản nếu có). Nhà xuất bản.

Ví dụ:
Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press.

## Bài báo khoa học:
Tác giả, A. A., & Tác giả, B. B. (Năm). Tên bài báo. *Tên tạp chí*, *Tập*(Số), Trang-Trang. DOI hoặc URL

Ví dụ:
LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature*, *521*(7553), 436-444. https://doi.org/10.1038/nature14539

## Tài liệu trực tuyến:
Tác giả, A. A. (Năm). Tên tài liệu. *Tên website*. URL đầy đủ [Ngày truy cập]

2. Yêu cầu về nội dung:
- Viết theo phong cách học thuật, tránh liệt kê dạng gạch đầu dòng
- Sử dụng câu văn hoàn chỉnh, có tính logic và liên kết
- Trích dẫn nguồn đầy đủ theo chuẩn APA
- Đảm bảo tính nhất quán trong cách trình bày

# Đề xuất tên repository GitHub

Dựa trên nội dung và tính chất học thuật của dự án, tôi đề xuất các tên repository sau:

1. `cnn-image-analysis-thesis`
   - Ngắn gọn, rõ ràng
   - Phản ánh đúng nội dung về CNN và phân tích hình ảnh
   - Dễ tìm kiếm và nhận diện

2. `deep-learning-image-processing-research`
   - Bao quát hơn, phù hợp nếu mở rộng nghiên cứu
   - Thể hiện tính học thuật

3. `masters-thesis-cnn-2024`
   - Thể hiện rõ đây là luận văn thạc sĩ
   - Có năm thực hiện
   - Dễ quản lý nếu có nhiều dự án khác

# Objectives and Key Results (OKR)

## Tiến độ công việc

### Sprint 1 (19/03/2024)
- [x] Khởi tạo cấu trúc dự án
- [x] Chuẩn hóa tài liệu tham khảo theo APA 7th Edition
- [x] Hoàn thiện cấu trúc Chapter 2
- [x] Chỉnh sửa nội dung các file markdown thành văn học thuật

### Sprint 2 (20/03/2024)
- [x] Bổ sung tài liệu tham khảo mới về:
  - ELU và PReLU
  - Ứng dụng CNN trong y tế và công nghiệp
  - Các nghiên cứu về tối ưu hóa CNN
- [x] Cập nhật đường dẫn trong các file markdown
- [x] Kiểm tra và xác thực tất cả các đường dẫn
- [ ] Thêm hình ảnh minh họa cho các phần
- [ ] Bổ sung chú thích cho hình ảnh

### Sprint 3 (21/03/2024 - 22/03/2024)
- [ ] Review và chỉnh sửa nội dung
- [ ] Thêm ví dụ cụ thể cho từng phần
- [ ] Hoàn thiện format và trình bày

## Cấu trúc thư mục

```

docs/
├── chapter2/
│ ├── 2.0-README.md
│ ├── 2.1.1-dinh-nghia-ung-dung.md
│ ├── 2.1.2-kien-truc-co-ban.md
│ ├── 2.1.3-ham-kich-hoat.md
│ ├── 2.1.4-uu-nhuoc-diem.md
│ ├── 2.2-so-sanh.md
│ └── references.md

```

## Quy chuẩn tài liệu tham khảo

1. Tuân thủ APA 7th Edition
2. Phân loại theo:
   - Sách và Giáo trình
   - Bài Báo Khoa Học
   - Tài Liệu Trực Tuyến và Khóa Học
   - Ứng dụng và Nghiên cứu Thực Nghiệm
   - Luận Văn và Báo Cáo Kỹ Thuật
3. Đường dẫn:
   - Sử dụng đường dẫn tương đối cho file nội bộ
   - Kiểm tra tính hợp lệ của URL
   - Thêm ngày truy cập cho tài liệu trực tuyến

## Yêu cầu nội dung

1. Văn phong học thuật, chuyên nghiệp
2. Trích dẫn đầy đủ và chính xác
3. Cấu trúc rõ ràng, logic
4. Ví dụ minh họa cụ thể
5. Hình ảnh và biểu đồ chất lượng cao

# Khởi tạo Git repository và kết nối với remote

git init
git add .
git commit -m "Initial commit: Project structure and documentation setup"
git branch -M main
git remote add origin https://github.com/limpaulfin/HUB-nhom-a-Ngan-masters-thesis-cnn-2025.git
git push -u origin main
```
