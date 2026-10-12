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

<<<FENCE 0>>>

Cờ `-t` chọn đích sinh mã. Các đích được hỗ trợ gồm `rust` (mặc định), `wasm`, `typescript` và `go`.

## Kiểm tra mà không sinh mã {#checking}

<<<FENCE 1>>>

Chạy toàn bộ front end (lex → parse → typecheck → hạ xuống MIR) mà không tạo ra các tạo phẩm đầu ra. Sử dụng lệnh này trong CI và các tích hợp với trình soạn thảo.

## Chạy kiểm thử {#testing-command}

<<<FENCE 2>>>

Biên dịch tất cả các bộ kiểm thử `probandum` trong gói thành các hàm Rust `#[test]` rồi chạy chúng thông qua Cargo. Kiểm thử nội tuyến nằm cùng mã nguồn — không cần tệp nhị phân kiểm thử riêng.

## Định dạng {#formatting}

<<<FENCE 3>>>

Áp dụng trình định dạng Faber chuẩn. Trình định dạng thực thi bố cục nhất quán: mỗi dòng một khai báo, khoảng cách chuẩn và bề mặt từ khóa thống nhất.

## Giải thích chẩn đoán {#explaining}

<<<FENCE 4>>>

In ra phần giải thích dễ đọc cho mọi mã chẩn đoán mà trình biên dịch có thể phát ra. Tính năng này hữu ích để tìm hiểu ý nghĩa của lỗi và cách khắc phục.
