+++
translation_kind = "translated"

title = "Faber build tool"
section = "tooling"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
]


prose_hash = "sha256:5d8304941413ba003c019f0b1c43cd19e99ad0f25fa9b7a4ffadbc1327e8dfb6"
code_hash = "sha256:7657ec817fefbfb88c20a7b862970c668ebe2835de88c17eda584340fd2d6654"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
CLI `faber` là điểm vào chính để xây dựng, kiểm tra, chạy, định dạng và kiểm thử mã nguồn Faber. CLI này bao bọc trình biên dịch Radix thành một công cụ phát triển tiện dụng.

## Các lệnh cốt lõi {#core-commands}

| Lệnh | Mục đích |
|---|---|
| `faber build <path>` | Biên dịch một gói sang backend đích (mặc định: Rust) |
| `faber check <path>` | Kiểm tra kiểu mà không sinh mã |
| `faber run <path>` | Xây dựng và thực thi |
| `faber test <path>` | Chạy các bộ kiểm thử `proba` |
| `faber format <path>` | Áp dụng định dạng chuẩn |
| `faber explain <code>` | Giải thích một mã chẩn đoán |
| `faber emit <path>` | Xuất mã nguồn trên một bề mặt đích |

## Xây dựng một gói {#building}

```text
faber build my-package/ -t rust
```

Cờ `-t` chọn đích sinh mã. Các đích được hỗ trợ gồm `rust` (mặc định), `wasm`, `typescript` và `go`.

## Kiểm tra mà không sinh mã {#checking}

```text
faber check my-package/
```

Chạy toàn bộ front end (lex → parse → typecheck → hạ xuống MIR) mà không tạo ra các tạo phẩm đầu ra. Sử dụng lệnh này trong CI và các tích hợp với trình soạn thảo.

## Chạy kiểm thử {#testing-command}

```text
faber test my-package/
```

Biên dịch tất cả các bộ kiểm thử `probandum` trong gói thành các hàm Rust `#[test]` rồi chạy chúng thông qua Cargo. Kiểm thử nội tuyến nằm cùng mã nguồn — không cần tệp nhị phân kiểm thử riêng.

## Định dạng {#formatting}

```text
faber format my-package/
```

Áp dụng trình định dạng Faber chuẩn. Trình định dạng thực thi bố cục nhất quán: mỗi dòng một khai báo, khoảng cách chuẩn và bề mặt từ khóa thống nhất.

## Giải thích chẩn đoán {#explaining}

```text
faber explain SEM001
```

In ra phần giải thích dễ đọc cho mọi mã chẩn đoán mà trình biên dịch có thể phát ra. Tính năng này hữu ích để tìm hiểu ý nghĩa của lỗi và cách khắc phục.
