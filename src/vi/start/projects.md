+++
translation_kind = "translated"

title = "Projects and examples"
section = "projects"
order = 4
sources = []

prose_hash = "sha256:8a914c63394e5bd0bf08ccef737eb95ec4cfb7df1813f3475c78d6ef579fb14d"
code_hash = "sha256:08056868d41c8d2a2925beb910fea8adcf4ac708fa67559e5a160dd900429a06"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
Sau phần hello-world, hãy chuyển sang các gói thực tế. Faber được tổ chức theo gói; cách nhanh nhất để học là kiểm tra và đọc các gói hiện có sử dụng cùng bề mặt trình biên dịch mà bạn dự định dùng.

## Các kho mã công khai {#repositories}

| Kho mã | Bắt đầu từ đây | Lý do |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`, các gói ứng dụng, các track | Corpus công khai và các ví dụ ứng dụng |
| [`faberlang/norma`](https://github.com/faberlang/norma) | Các gói `norma:*` | Mã nguồn thư viện chuẩn |
| [`faberlang/faber`](https://github.com/faberlang/faber) | Lớp bao CLI | Công cụ build dành cho người dùng |
| [`faberlang/cista`](https://github.com/faberlang/cista) | CLI/lib của kho gói | Bề mặt quản lý gói |
| [`faberlang/triga`](https://github.com/faberlang/triga) | Mã nguồn `triga:*` | Thư viện đồ họa và hình học |

## Sao chép workspace học tập {#clone-workspace}

```bash
mkdir faber-learning
cd faber-learning
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

Các gói có import `norma:*` sẽ phân giải dependency từ kho gói Cista được ghi trong `faber.lock`. Chỉ sử dụng `FABER_LIBRARY_HOME` khi bạn cố ý muốn ghi đè bộ phân giải cục bộ để phát triển thư viện.

## Đọc ví dụ theo thứ tự này {#read-order}

1. [Tham quan nhanh](/start/) để làm quen với ngữ pháp bề mặt.
2. [Xin chào, Faber](/start/hello.html) cho một gói đơn.
3. [Corpus](/corpus/) với mỗi trang trình bày một từ khóa hoặc cấu trúc.
4. [Ví dụ](/start/examples.html) cho các ứng dụng lớn hơn.
5. [Công cụ build Faber](/tooling/faber-build-tool.html) để tìm hiểu chi tiết CLI.

## Quy trình làm việc cho tác nhân {#agent-workflow}

Tác nhân không nên suy ra cú pháp chỉ từ phần diễn giải. Hãy sử dụng các bề mặt máy và sau đó xác thực mã được tạo:

```bash
curl -fsSL https://faberlang.dev/llms.txt
faber check path/to/package
```

Đối với công việc trên gói, hãy ghi rõ kho mã, đường dẫn gói, lệnh và mã chẩn đoán trong báo cáo. Nếu bạn chỉnh sửa tài liệu có mã Faber được đặt trong fence trên trang này, hãy chạy bộ xác thực fence trước khi khẳng định rằng các ví dụ vẫn biên dịch được.

## Sau track khởi đầu {#after-start}

| Mục tiêu | Đọc |
|---|---|
| Học cú pháp | [Cú pháp](/syntax/) |
| Tìm hiểu locale | [Locale đọc](/features/reader-locale.html) |
| Sử dụng trình biên dịch | [Công cụ build Faber](/tooling/faber-build-tool.html) và [Trình biên dịch Radix](/tooling/radix-compiler.html) |
| Duyệt các cấu trúc | [Corpus](/corpus/) |
| Xây dựng với thư viện | [Hệ sinh thái](/ecosystem/) |

## Tiếp theo {#next}

| Trước | Tiếp theo |
|---|---|
| [Các lệnh bạn sẽ sử dụng](/start/commands.html) | [Ví dụ](/start/examples.html) |
