+++
translation_kind = "translated"

title = "The faber CLI"
section = "toolchain"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
  "radix/docs/design/faber-scripting.md",
]
+++

## Faber build tool

CLI `faber` là điểm vào chính để xây dựng, kiểm tra, chạy, định dạng và kiểm thử mã nguồn Faber. CLI này bao bọc trình biên dịch Radix thành một công cụ phát triển tiện dụng.

### Các lệnh cốt lõi {#core-commands}

| Lệnh | Mục đích |
|---|---|
| `faber build <path>` | Biên dịch một gói sang backend đích (mặc định: Rust) |
| `faber check <path>` | Kiểm tra kiểu mà không sinh mã |
| `faber run <path>` | Xây dựng và thực thi |
| `faber test <path>` | Chạy các bộ kiểm thử `proba` |
| `faber format <path>` | Áp dụng định dạng chuẩn |
| `faber explain <code>` | Giải thích một mã chẩn đoán |
| `faber emit <path>` | Xuất mã nguồn trên một bề mặt đích |

### Xây dựng một gói {#building}

```text
faber build my-package/ -t rust
```

Cờ `-t` chọn đích sinh mã. Các đích được hỗ trợ gồm `rust` (mặc định), `wasm`, `typescript` và `go`.

### Kiểm tra mà không sinh mã {#checking}

```text
faber check my-package/
```

Chạy toàn bộ front end (lex → parse → typecheck → hạ xuống MIR) mà không tạo ra các tạo phẩm đầu ra. Sử dụng lệnh này trong CI và các tích hợp với trình soạn thảo.

### Chạy kiểm thử {#testing-command}

```text
faber test my-package/
```

Biên dịch tất cả các bộ kiểm thử `probandum` trong gói thành các hàm Rust `#[test]` rồi chạy chúng thông qua Cargo. Kiểm thử nội tuyến nằm cùng mã nguồn — không cần tệp nhị phân kiểm thử riêng.

### Định dạng {#formatting}

```text
faber format my-package/
```

Áp dụng trình định dạng Faber chuẩn. Trình định dạng thực thi bố cục nhất quán: mỗi dòng một khai báo, khoảng cách chuẩn và bề mặt từ khóa thống nhất.

### Giải thích chẩn đoán {#explaining}

```text
faber explain SEM001
```

In ra phần giải thích dễ đọc cho mọi mã chẩn đoán mà trình biên dịch có thể phát ra. Tính năng này hữu ích để tìm hiểu ý nghĩa của lỗi và cách khắc phục.

## In-process scripting

Bên cạnh đường dẫn Rust đã biên dịch, Faber hỗ trợ thực thi thông dịch trong tiến trình thông qua bộ tiến từng bước MIR.

### Cách sử dụng {#usage}

```bash
faber run --interpret script.fab
```

Lệnh này chạy mã nguồn Faber trong cùng tiến trình sau phần đầu thông thường của trình biên dịch (từ phân tích cú pháp đến kiểm tra kiểu và hạ cấp MIR), mà không gọi `rustc` hoặc tạo một tiến trình xây dựng.

### Cách hoạt động {#how-it-works}

Trình biên dịch tạo ra HIR đã được phân tích, MIR đã được kiểm tra hợp lệ và bảng nội tại thời gian chạy đã được phân giải. Bộ tiến từng bước MIR chuyển trực tiếp các khối MIR đến máy chủ, bỏ qua vòng chuyển đổi phát sinh/khởi tạo wasm:

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck
                                                      ↓
                                                 MIR lowering
                                                      ↓
                                              MIR stepper + Host
```

### Độ trễ {#latency}

Đường dẫn kịch bản chạy cùng frontend tuyến tính với đường dẫn biên dịch, cộng thêm thời gian tiến từng bước tỉ lệ với phần mã mà kịch bản thực sự thực thi:

| Giai đoạn | Chi phí |
|-------|------|
| Frontend (kịch bản 100 dòng) | ~0.6 ms |
| Tiến từng bước MIR | Tỉ lệ với số câu lệnh được thực thi |

Bộ tiến từng bước không bao giờ gọi `rustc` hoặc tạo tiến trình, vì vậy thời gian khởi động đủ nhanh để tạo cảm giác như chạy một shell script.

### Hạn chế {#limitations}

- Bộ tiến từng bước MIR không hỗ trợ mọi tuyến I/O của máy chủ như đường dẫn đã biên dịch — một số wrapper `norma:*` chỉ hoạt động khi biên dịch
- Bộ tiến từng bước là trình thực thi chẩn đoán/tham chiếu thuần MIR, không phải runtime sản xuất cho các ứng dụng đã triển khai
- Việc biên dịch gói thông qua Cargo vẫn là đường dẫn sản phẩm chính
