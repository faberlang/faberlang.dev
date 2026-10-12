Viết chương trình Faber hữu ích nhỏ nhất: một điểm vào gói định dạng một
chuỗi và in ra.

## Điều kiện tiên quyết {#prerequisites}

Hoàn thành [Cài đặt và tải xuống](/start/install.html) trước. Bạn cần có
binary `faber` trên `PATH` và một shell trong thư mục làm việc nơi bạn có thể
tạo file.

## Tạo một gói {#create-package}

<<<FENCE 0>>>

## Kiểm tra {#check}

<<<FENCE 1>>>

`faber check` chạy front end: lexing, parsing, type checking, và lowering
đủ xa để bắt các lỗi gói thông thường mà không build binary native.
Nếu lệnh thất bại, hãy đọc mã chẩn đoán trước; diagnostics của Faber được
thiết kế làm handle tìm kiếm ổn định.

## Chạy {#run}

<<<FENCE 2>>>

Kết quả mong đợi:

<<<FENCE 3>>>

## Những gì bạn vừa dùng {#what-you-used}

| Nguồn | Ý nghĩa |
|---|---|
| `functio salve(textus nomen) → textus` | Hàm tên `salve`, tham số type-first, trả về text |
| `fixum textus msg ← ...` | Binding bất biến |
| `"Salve, §!"(nomen)` | Chuỗi định dạng với display interpolation |
| `redde msg` | Trả về |
| `incipit` | Điểm vào gói |
| `nota m` | In một giá trị note/output |

## Bằng chứng locale {#locale-proof}

Chương trình ở trên là bản render Latin reader chuẩn. Các locale reader có thể
render cùng một chương trình ngữ nghĩa với các bộ từ khóa khác nhau trong khi vẫn giữ
glyph và identifier. Bắt đầu với bằng chứng đầy đủ tại
[Locale reader](/features/reader-locale.html) trước khi viết các gói non-Latin.

## Tiếp theo {#next}

| Trước | Tiếp |
|---|---|
| [Cài đặt và tải xuống](/start/install.html) | [Các lệnh bạn sẽ dùng](/start/commands.html) |
