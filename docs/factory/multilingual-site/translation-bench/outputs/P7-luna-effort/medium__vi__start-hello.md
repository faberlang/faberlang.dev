Viết chương trình Faber hữu ích nhỏ nhất: một điểm vào của gói định dạng một
chuỗi và in chuỗi đó.

## Điều kiện tiên quyết {#prerequisites}

Trước hết, hãy hoàn tất [Cài đặt và tải xuống](/start/install.html). Bạn cần có
bản nhị phân `faber` trên `PATH` và một shell trong thư mục làm việc nơi bạn có thể
tạo tệp.

## Tạo một gói {#create-package}

<<<FENCE 0>>>

## Kiểm tra {#check}

<<<FENCE 1>>>

`faber check` chạy phần front end: phân tích từ vựng, phân tích cú pháp, kiểm tra
kiểu và hạ cấp đủ xa để phát hiện các lỗi thông thường của gói mà không cần xây
dựng tệp nhị phân native. Nếu lệnh thất bại, trước tiên hãy đọc mã chẩn đoán;
các chẩn đoán của Faber được thiết kế để làm khóa tra cứu ổn định.

## Chạy {#run}

<<<FENCE 2>>>

Kết quả mong đợi:

<<<FENCE 3>>>

## Những gì bạn vừa sử dụng {#what-you-used}

| Mã nguồn | Ý nghĩa |
|---|---|
| `functio salve(textus nomen) → textus` | Hàm tên `salve`, tham số theo thứ tự kiểu trước, trả về văn bản |
| `fixum textus msg ← ...` | Liên kết bất biến |
| `"Salve, §!"(nomen)` | Chuỗi định dạng với phép nội suy hiển thị |
| `redde msg` | Trả về |
| `incipit` | Điểm vào của gói |
| `nota m` | In một giá trị ghi chú/kết quả |

## Minh chứng locale {#locale-proof}

Chương trình trên là bản hiển thị trình đọc Latin chuẩn. Các locale của trình đọc
có thể hiển thị cùng một chương trình ngữ nghĩa bằng những bộ từ khóa khác nhau,
đồng thời giữ nguyên glyph và mã định danh. Hãy bắt đầu với phần minh chứng đầy đủ
ở [Locale của trình đọc](/features/reader-locale.html) trước khi viết các gói
không dùng Latin.

## Tiếp theo {#next}

| Trước | Tiếp theo |
|---|---|
| [Cài đặt và tải xuống](/start/install.html) | [Các lệnh bạn sẽ sử dụng](/start/commands.html) |