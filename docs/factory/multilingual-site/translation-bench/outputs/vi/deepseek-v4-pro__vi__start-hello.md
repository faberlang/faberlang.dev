Viết chương trình Faber hữu ích nhỏ nhất: một điểm vào gói định dạng một
chuỗi và in nó ra.

## Điều kiện tiên quyết {#prerequisites}

Hoàn thành [Cài đặt và tải xuống](/start/install.html) trước. Bạn cần có tệp
nhị phân `faber` trong `PATH` và một shell trong thư mục làm việc nơi bạn có
thể tạo tệp.

## Tạo một gói {#create-package}

<<<FENCE 0>>>

## Kiểm tra nó {#check}

<<<FENCE 1>>>

`faber check` chạy front end: lexing, parsing, type checking, và lowering đủ để
bắt các lỗi gói thông thường mà không cần build tệp nhị phân native. Nếu lệnh
thất bại, hãy đọc mã chẩn đoán trước; chẩn đoán của Faber được thiết kế làm
handle tìm kiếm ổn định.

## Chạy nó {#run}

<<<FENCE 2>>>

Đầu ra mong đợi:

<<<FENCE 3>>>

## Bạn vừa dùng những gì {#what-you-used}

| Nguồn | Ý nghĩa |
|---|---|
| `functio salve(textus nomen) → textus` | Hàm tên `salve`, tham số kiểu-trước, trả về text |
| `fixum textus msg ← ...` | Ràng buộc bất biến |
| `"Salve, §!"(nomen)` | Chuỗi định dạng với nội suy hiển thị |
| `redde msg` | Trả về |
| `incipit` | Điểm vào gói |
| `nota m` | In một giá trị ghi chú/đầu ra |

## Chứng minh locale {#locale-proof}

Chương trình trên là bản kết xuất Latin reader chính tắc. Reader locale có thể
kết xuất cùng chương trình ngữ nghĩa với các bộ từ khóa khác nhau trong khi vẫn
giữ nguyên glyph và định danh. Bắt đầu với chứng minh đầy đủ tại
[Reader locale](/features/reader-locale.html) trước khi viết các gói không phải
Latin.

## Tiếp theo {#next}

| Trước | Tiếp theo |
|---|---|
| [Cài đặt và tải xuống](/start/install.html) | [Các lệnh bạn sẽ dùng](/start/commands.html) |
