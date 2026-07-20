+++
translation_kind = "translated"

title = "Triga graphics library"
section = "ecosystem"
order = 2
sources = [
  "sibling triga/ repository",
  "radix/README.md (mentions triga)",
]


prose_hash = "sha256:d2d83d9401309c449bba9b993db7ec74cdb97afc4e8cc1b2195e769c043f07a1"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Triga là một thư viện mã nguồn công khai tùy chọn dành cho hình học, cảnh và các hợp đồng kiểu hướng đến GPU. Trong các dự án thông thường, hãy khai báo Triga là một phần phụ thuộc gói Cista trong `faber.toml`; Cista ghi lại mã nguồn đã được phân giải trong `faber.lock`, còn trình biên dịch sẽ phân giải thư viện này từ kho gói.

Khi được thiết lập, `FABER_LIBRARY_HOME` là tùy chọn ghi đè bộ phân giải dành cho phát triển cục bộ. Đây không phải là đường dẫn sản phẩm chính để sử dụng Triga.

Triga cung cấp các kiểu và thao tác cho:

- Các kiểu nguyên thủy hình học (điểm, vectơ, ma trận, phép biến đổi)
- Các cấu trúc đồ thị cảnh
- Các hợp đồng kiểu hướng đến GPU, phù hợp với luồng hệ thống của Faber

Triga không thuộc Norma. Đây là một phần phụ thuộc tùy chọn mà các gói có thể đăng ký khi cần thực hiện công việc về đồ họa hoặc hình học.
