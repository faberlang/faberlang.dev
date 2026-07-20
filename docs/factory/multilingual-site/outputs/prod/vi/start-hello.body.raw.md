Viết chương trình Faber hữu ích và ngắn gọn nhất: một điểm vào gói định dạng một chuỗi rồi in chuỗi đó.

## Điều kiện tiên quyết {#prerequisites}

Trước tiên, hãy hoàn tất [Cài đặt và tải xuống](/start/install.html). Bạn cần có tệp nhị phân `faber` trong `PATH` và một shell đang ở thư mục làm việc nơi bạn có thể tạo tệp.

## Tạo một gói {#create-package}

<<<FENCE 0>>>

## Kiểm tra gói {#check}

<<<FENCE 1>>>

`faber check` chạy phần đầu vào của trình biên dịch: phân tích từ vựng, phân tích cú pháp, kiểm tra kiểu và hạ cấp đủ xa để phát hiện các lỗi thông thường trong gói mà không cần xây dựng tệp nhị phân gốc. Nếu lệnh thất bại, trước tiên hãy đọc mã chẩn đoán; các chẩn đoán của Faber được thiết kế để làm mã tra cứu ổn định.

## Chạy chương trình {#run}

<<<FENCE 2>>>

Kết quả dự kiến:

<<<FENCE 3>>>

## Những gì bạn vừa sử dụng {#what-you-used}

| Mã nguồn | Ý nghĩa |
|---|---|
| `functio salve(textus nomen) → textus` | Hàm tên `salve`, tham số theo kiểu trước, trả về văn bản |
| `fixum textus msg ← ...` | Khai báo bất biến |
| `"Salve, §!"(nomen)` | Chuỗi định dạng có nội suy giá trị hiển thị |
| `redde msg` | Trả về |
| `incipit` | Điểm vào của gói |
| `nota m` | In một giá trị ghi chú/kết quả |

## Chứng minh bản địa hóa {#locale-proof}

Chương trình trên là cách hiển thị chuẩn theo locale đọc tiếng Latinh. Các locale đọc khác có thể hiển thị cùng một chương trình ngữ nghĩa bằng các bộ từ khóa khác nhau, đồng thời giữ nguyên glyph và mã định danh. Hãy bắt đầu với phần chứng minh đầy đủ tại [Locale đọc](/features/reader-locale.html) trước khi viết các gói không dùng chữ Latinh.

## Tiếp theo {#next}

| Trước | Tiếp theo |
|---|---|
| [Cài đặt và tải xuống](/start/install.html) | [Các lệnh bạn sẽ sử dụng](/start/commands.html) |
