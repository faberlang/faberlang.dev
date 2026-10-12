Sau hello-world, hãy chuyển sang các gói thực tế. Faber được tổ chức theo gói; cách nhanh nhất để học là kiểm tra và đọc các gói hiện có, trong đó sử dụng cùng bề mặt trình biên dịch mà bạn dự định dùng.

## Các kho lưu trữ công khai {#repositories}

| Kho lưu trữ | Bắt đầu tại đây | Lý do |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`, các gói ứng dụng, tracks | Corpus công khai và các ví dụ ứng dụng |
| [`faberlang/norma`](https://github.com/faberlang/norma) | các gói `norma:*` | Mã nguồn thư viện chuẩn |
| [`faberlang/faber`](https://github.com/faberlang/faber) | Trình bao CLI | Công cụ xây dựng hướng tới người dùng |
| [`faberlang/cista`](https://github.com/faberlang/cista) | CLI/lib của kho gói | Bề mặt quản lý gói |
| [`faberlang/triga`](https://github.com/faberlang/triga) | mã nguồn `triga:*` | Thư viện đồ họa và hình học |

## Sao chép không gian làm việc học tập {#clone-workspace}

<<<FENCE 0>>>

Các gói có import `norma:*` sẽ phân giải các phần phụ thuộc từ kho gói Cista được ghi trong `faber.lock`. Chỉ sử dụng `FABER_LIBRARY_HOME` khi bạn cố ý muốn ghi đè trình phân giải cục bộ để phát triển thư viện.

## Đọc các ví dụ theo thứ tự này {#read-order}

1. [Tham quan nhanh](/start/) để làm quen với ngữ pháp bề mặt.
2. [Xin chào, Faber](/start/hello.html) cho một gói đơn.
3. [Corpus](/corpus/) để xem mỗi từ khóa hoặc cấu trúc trên một trang.
4. [Các ví dụ](/start/examples.html) cho những ứng dụng lớn hơn.
5. [Công cụ xây dựng Faber](/tooling/faber-build-tool.html) để biết chi tiết CLI.

## Quy trình làm việc của tác tử {#agent-workflow}

Tác tử không nên suy ra cú pháp chỉ từ văn xuôi. Hãy sử dụng các giao diện máy, sau đó xác thực mã được tạo:

<<<FENCE 1>>>

Đối với công việc trên gói, hãy ghi rõ kho lưu trữ, đường dẫn gói, lệnh và mã chẩn đoán trong báo cáo. Nếu bạn chỉnh sửa tài liệu có mã Faber được rào bằng fence trên trang này, hãy chạy trình xác thực fence trước khi tuyên bố rằng các ví dụ vẫn biên dịch được.

## Sau track start là gì {#after-start}

| Mục tiêu | Đọc |
|---|---|
| Học cú pháp | [Cú pháp](/syntax/) |
| Tìm hiểu locale | [Locale của người đọc](/features/reader-locale.html) |
| Sử dụng trình biên dịch | [Công cụ xây dựng Faber](/tooling/faber-build-tool.html) và [Trình biên dịch Radix](/tooling/radix-compiler.html) |
| Duyệt các cấu trúc | [Corpus](/corpus/) |
| Xây dựng với thư viện | [Hệ sinh thái](/ecosystem/) |

## Tiếp theo {#next}

| Trước | Tiếp theo |
|---|---|
| [Các lệnh bạn sẽ sử dụng](/start/commands.html) | [Các ví dụ](/start/examples.html) |
