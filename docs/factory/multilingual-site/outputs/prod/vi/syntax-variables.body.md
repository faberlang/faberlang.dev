Faber có ba từ khóa biến và một ký hiệu gán riêng. Điểm khác biệt chính nằm giữa `fixum` (chỉ ghi một lần) và `varia` (có thể gán lại tự do), cũng như giữa `←` (luồng thực thi) và `=` (hình dạng trường mang tính cấu trúc).

## fixum — liên kết bất biến {#fixum-immutable-binding}

Các liên kết `fixum` chỉ được ghi một lần. Có thể khai báo chúng có hoặc không có trình khởi tạo; nếu khai báo mà không có trình khởi tạo, chúng phải được gán đúng một lần trước khi đọc. Lần gán thứ hai sẽ bị từ chối.

<<<FENCE 0>>>

Khởi tạo trì hoãn:

<<<FENCE 1>>>

## varia — liên kết khả biến {#varia-mutable-binding}

Các liên kết `varia` có thể được gán lại tự do:

<<<FENCE 2>>>

## sit — cú pháp rút gọn cho liên kết bất biến suy luận kiểu {#sit-inferred-immutable-sugar}

`sit` là cú pháp rút gọn của `fixum _` — một liên kết bất biến với kiểu được suy luận:

<<<FENCE 3>>>

## Liên kết thời gian chạy và định nghĩa cấu trúc {#runtime-binding-vs-structural-definition}

Faber tách biệt hai vai trò mà hầu hết các ngôn ngữ gộp chung vào `=`:

| Ký hiệu | Vai trò | Dùng cho |
|---------|---------|----------|
| `←` | Luồng thời gian chạy | Liên kết ban đầu, gán lại, biến đổi |
| `=` | Hình dạng cấu trúc | Tên trường bên trong literal và siêu dữ liệu |

<<<FENCE 4>>>

## Trích xuất trường bằng ex {#ex-field-extraction}

`ex` trích xuất các trường từ một giá trị vào các liên kết cục bộ:

<<<FENCE 5>>>

## Tăng và giảm hậu tố {#postfix-increment-and-decrement}

`⊕` và `⊖` là các câu lệnh tăng/giảm hậu tố dành cho các vị trí `numerus` khả biến. Chúng chỉ được dùng như câu lệnh — không có giá trị biểu thức và không có dạng tiền tố:

<<<FENCE 6>>>
