Sau hello-world, hãy chuyển sang các gói thực tế. Faber hướng theo gói; cách
nhanh nhất để học là kiểm tra và đọc các gói đã có, những gói này dùng cùng bề
mặt trình biên dịch mà bạn định dùng.

## Kho lưu trữ công khai {#repositories}

| Kho lưu trữ | Bắt đầu từ đây | Lý do |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`, các gói ứng dụng, các track | Kho ngữ liệu và ví dụ ứng dụng công khai |
| [`faberlang/norma`](https://github.com/faberlang/norma) | các gói `norma:*` | Mã nguồn thư viện chuẩn |
| [`faberlang/faber`](https://github.com/faberlang/faber) | bộ bao bọc CLI | Công cụ xây dựng dành cho người dùng |
| [`faberlang/cista`](https://github.com/faberlang/cista) | CLI/lib kho gói | Bề mặt quản lý gói |
| [`faberlang/triga`](https://github.com/faberlang/triga) | mã nguồn `triga:*` | Thư viện đồ họa và hình học |

## Nhân bản một không gian làm việc học tập {#clone-workspace}

<<<FENCE 0>>>

Các gói có lệnh import `norma:*` sẽ giải quyết phụ thuộc từ kho gói Cista được
ghi trong `faber.lock`. Chỉ dùng `FABER_LIBRARY_HOME` khi bạn cố ý muốn ghi đè
bộ giải quyết cục bộ để phát triển thư viện.

## Đọc ví dụ theo thứ tự này {#read-order}

1. [Hướng dẫn nhanh](/start/) cho ngữ pháp bề mặt.
2. [Hello, Faber](/start/hello.html) cho một gói đơn lẻ.
3. [Ngữ liệu](/corpus/) với mỗi trang cho một từ khóa hoặc cấu trúc.
4. [Ví dụ](/start/examples.html) cho các ứng dụng lớn hơn.
5. [Công cụ xây dựng Faber](/tooling/faber-build-tool.html) để biết chi tiết CLI.

## Quy trình tác tử {#agent-workflow}

Các tác tử không nên suy luận cú pháp chỉ từ văn xuôi. Hãy dùng các bề mặt máy,
sau đó kiểm chứng mã đã sinh:

<<<FENCE 1>>>

Khi làm việc với gói, hãy trích dẫn kho, đường dẫn gói, lệnh và mã chẩn đoán
trong báo cáo. Nếu bạn sửa tài liệu có khối Faber trong fencing tại trang này,
hãy chạy trình kiểm tra fence trước khi khẳng định các ví dụ vẫn biên dịch được.

## Nội dung sau track khởi động {#after-start}

| Mục tiêu | Đọc |
|---|---|
| Học cú pháp | [Cú pháp](/syntax/) |
| Hiểu vùng địa phương | [Vùng địa phương người đọc](/features/reader-locale.html) |
| Dùng trình biên dịch | [Công cụ xây dựng Faber](/tooling/faber-build-tool.html) và [Trình biên dịch Radix](/tooling/radix-compiler.html) |
| Duyệt các cấu trúc | [Ngữ liệu](/corpus/) |
| Xây dựng với thư viện | [Hệ sinh thái](/ecosystem/) |

## Tiếp theo {#next}

| Trước đó | Tiếp theo |
|---|---|
| [Các lệnh bạn sẽ dùng](/start/commands.html) | [Ví dụ](/start/examples.html) |
