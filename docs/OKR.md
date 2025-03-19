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
```

# Tiến độ công việc

## Sprint 1 (19/03/2024)

### Đã hoàn thành:

1. Khởi tạo cấu trúc project

    - [x] Tạo repository GitHub
    - [x] Thiết lập cấu trúc thư mục
    - [x] Tạo file README và hướng dẫn đóng góp

2. Chuẩn hóa tài liệu tham khảo
    - [x] Cập nhật format APA 7th Edition
    - [x] Thêm DOI và URL cho các nguồn
    - [x] Phân loại tài liệu theo nhóm

### Đang thực hiện:

1. Chỉnh sửa nội dung chapter 2
    - [ ] Chuyển đổi format gạch đầu dòng thành văn học thuật
    - [ ] Thêm trích dẫn theo chuẩn APA
    - [ ] Bổ sung hình ảnh minh họa

### Kế hoạch tiếp theo:

1. Sprint 2 (20/03/2024 - 22/03/2024)
    - [ ] Hoàn thiện nội dung chapter 2
    - [ ] Review và chỉnh sửa
    - [ ] Thêm hình ảnh và biểu đồ minh họa

# Khởi tạo Git repository và kết nối với remote

git init
git add .
git commit -m "Initial commit: Project structure and documentation setup"
git branch -M main
git remote add origin https://github.com/limpaulfin/HUB-nhom-a-Ngan-masters-thesis-cnn-2025.git
git push -u origin main
