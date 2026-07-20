Các hàm trong Faber được khai báo bằng `functio`, sử dụng cú pháp tham số đặt kiểu trước và kiểu trả về bằng glyph.

## Cú pháp cơ bản {#basic-syntax}

<<<FENCE 0>>>

Với kênh lỗi:

<<<FENCE 1>>>

## Ví dụ {#examples}

<<<FENCE 2>>>

## Giá trị trả về {#return-values}

Sử dụng `redde` để trả về thông thường:

<<<FENCE 3>>>

Dùng `redde` không kèm giá trị cho kiểu trả về `vacuum`:

<<<FENCE 4>>>

## Mượn và tính khả biến (de, in, ex) {#borrowing-and-mutability}

Faber đánh dấu cách truyền một giá trị bằng các giới từ ngắn đặt trên tham số:

| Dấu | Ý nghĩa | Hạ cấp Rust điển hình |
|--------|---------|----------------------|
| *(không có)* | Giá trị sở hữu | `T` truyền theo giá trị |
| `de` | Mượn dùng chung (chỉ đọc) | `&T` |
| `in` | Mượn có thể thay đổi | `&mut T` |
| `ex` | Tiêu thụ (move vào hàm gọi) | `T` move |

<<<FENCE 5>>>

Các từ tương tự (`de`, `ex`) cũng được dùng lại trong những cấu trúc khác — không được hiểu mọi `ex` là “tiêu thụ”:

| Cú pháp | Vai trò |
|---------|---------|
| `de textus name` trên tham số | Mượn dùng chung |
| `in numerus count` trên tham số | Mượn có thể thay đổi |
| `ex textus buffer` trên tham số | Move vào hàm gọi |
| `itera ex items fixum item` | Lặp qua các giá trị |
| `itera de tabula fixum key` | Lặp qua các khóa |
| `ex source fixum x, ceteri rest` | Phân rã các trường |
| `importa ex "path"` | Nhập từ mô-đun |

## Điểm vào {#entry-point}

Điểm vào của chương trình là `incipit`:

<<<FENCE 6>>>

## Điểm vào CLI {#cli-entry-point}

Đối với các chương trình CLI, `incipit argumenta` nhận các đối số lệnh đã được phân tích:

<<<FENCE 7>>>

## Chế độ truyền — `sponte` {#passing-mode-sponte}

`sponte` đánh dấu một tham số có thể được lược bỏ bởi bên gọi:

<<<FENCE 8>>>
