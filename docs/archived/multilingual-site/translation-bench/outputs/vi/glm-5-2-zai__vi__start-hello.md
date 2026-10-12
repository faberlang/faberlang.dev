Viết chương trình Faber nhỏ nhất có ích: một điểm vào gói định dạng một chuỗi rồi in nó ra.

## Điều kiện tiên quyết {#prerequisites}

Hãy hoàn thành [Cài đặt và tải về](/start/install.html) trước. Bạn cần có tệp
nhị phân `faber` trên `PATH` và một shell trong thư mục làm việc nơi bạn có thể
tạo tệp.

## Tạo một gói {#create-package}

<<<FENCE 0>>>

## Kiểm tra nó {#check}

<<<FENCE 1>>>

`faber check` chạy front end: lexing, parsing, kiểm tra kiểu, và hạ đủ mức để
bắt các lỗi gói thông thường mà không cần dựng tệp nhị phân native. Nếu lệnh
thất bại, hãy đọc mã chẩn đoán trước; các chẩn đoán Faber được thiết kế làm tay
cầm tìm kiếm ổn định.

## Chạy nó {#run}

<<<FENCE 2>>>

Kết quả mong đợi:

<<<FENCE 3>>>

## Những gì bạn vừa dùng {#what-you-used}

| Nguồn | Ý nghĩa |
|---|---|
| `functio salve(textus nomen) → textus` | Hàm tên `salve`, tham số kiểu-trước, trả về text |
| `fixum textus msg ← ...` | Liên kết bất biến |
| `"Salve, §!"(nomen)` | Chuỗi định dạng với nội suy hiển thị |
| `redde msg` | Trả về |
| `incipit` | Điểm vào gói |
| `nota m` | In một ghi chú/giá trị xuất |

## Minh chứng locale {#locale-proof}

Chương trình trên là kết xuất Latin reader chuẩn. Các locale reader có thể kết
xuất cùng một chương trình ngữ nghĩa với các gói từ khóa khác nhau nhưng vẫn
giữ nguyên glyph và định danh. Hãy bắt đầu với minh chứng đầy đủ tại
[Locale reader](/features/reader-locale.html) trước khi viết các gói non-Latin.

## Tiếp theo {#next}

| Trước | Tiếp |
|---|---|
| [Cài đặt và tải về](/start/install.html) | [Các lệnh bạn sẽ dùng](/start/commands.html) |
