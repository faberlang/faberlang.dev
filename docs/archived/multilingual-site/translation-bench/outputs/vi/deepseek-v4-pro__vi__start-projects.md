Sau hello-world, hãy chuyển sang các package thực tế. Faber thiên về package;
cách học nhanh nhất là kiểm tra và đọc các package hiện có — những package
sử dụng cùng bề mặt trình biên dịch mà bạn định dùng.

## Kho lưu trữ công khai {#repositories}

| Kho lưu trữ | Bắt đầu từ đây | Lý do |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`, package ứng dụng, tracks | Tập corpus công khai và ví dụ ứng dụng |
| [`faberlang/norma`](https://github.com/faberlang/norma) | package `norma:*` | Mã nguồn thư viện chuẩn |
| [`faberlang/faber`](https://github.com/faberlang/faber) | Trình bao CLI | Công cụ build cho người dùng |
| [`faberlang/cista`](https://github.com/faberlang/cista) | CLI/lib kho package | Bề mặt quản lý package |
| [`faberlang/triga`](https://github.com/faberlang/triga) | Mã nguồn `triga:*` | Thư viện đồ họa và hình học |

## Clone workspace học tập {#clone-workspace}

<<<FENCE 0>>>

Các package có import `norma:*` phân giải phụ thuộc từ kho package Cista
được ghi trong `faber.lock`. Chỉ dùng `FABER_LIBRARY_HOME` khi bạn chủ ý
ghi đè bộ phân giải cục bộ để phát triển thư viện.

## Đọc ví dụ theo thứ tự này {#read-order}

1. [Tham quan nhanh](/start/) để nắm ngữ pháp bề mặt.
2. [Hello, Faber](/start/hello.html) cho package đơn.
3. [Corpus](/corpus/) — mỗi từ khóa hoặc cấu trúc một trang.
4. [Examples](/start/examples.html) cho ứng dụng lớn hơn.
5. [Công cụ build Faber](/tooling/faber-build-tool.html) để biết chi tiết CLI.

## Quy trình làm việc của agent {#agent-workflow}

Agent không nên suy luận cú pháp chỉ từ văn xuôi. Hãy dùng bề mặt máy và
sau đó xác thực mã đã sinh:

<<<FENCE 1>>>

Khi làm việc với package, hãy trích dẫn repo, đường dẫn package, lệnh, và
mã chẩn đoán trong báo cáo. Nếu bạn sửa tài liệu có mã Faber trong fence
trên site này, hãy chạy trình xác thực fence trước khi tuyên bố ví dụ vẫn
biên dịch được.

## Tiếp theo sau lộ trình bắt đầu {#after-start}

| Mục tiêu | Đọc |
|---|---|
| Học cú pháp | [Syntax](/syntax/) |
| Hiểu locale | [Reader locale](/features/reader-locale.html) |
| Dùng trình biên dịch | [Công cụ build Faber](/tooling/faber-build-tool.html) và [Radix compiler](/tooling/radix-compiler.html) |
| Duyệt cấu trúc | [Corpus](/corpus/) |
| Xây dựng với thư viện | [Ecosystem](/ecosystem/) |

## Tiếp theo {#next}

| Trước | Tiếp |
|---|---|
| [Các lệnh bạn sẽ dùng](/start/commands.html) | [Examples](/start/examples.html) |
