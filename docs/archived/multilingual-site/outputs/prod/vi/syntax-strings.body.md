Faber sử dụng ngữ nghĩa của các dấu phân cách — mỗi dạng dấu nháy biểu thị một dạng mã nguồn khác nhau. Chúng không phải là các từ đồng nghĩa có thể thay thế cho nhau.

## Dạng literal {#literal-forms}

| Dạng | Kiểu | Vai trò |
|------|------|------|
| `'…'` | `ascii` | Token cố định dành cho máy; không có `§`; không có `(…)` |
| `"…"` | `textus` | Chuỗi Unicode một dòng ngắn; `(…)` được nội suy |
| `«…»` | `textus` | Unicode dạng khối/nhiều dòng; `(…)` được nội suy |
| `` `…` `` | `forma` | Template được thu giữ; `(…)` được thu giữ |
| `{ … }` | `json` | Tài liệu JSON tại thời điểm biên dịch |
| `|…|` | `octeti` | Dãy byte hex tại thời điểm biên dịch |
| `[ … ]` | `lista<T>` | Literal danh sách Faber |

## Áp dụng template chuỗi {#string-template-application}

Faber định dạng văn bản bằng phép áp dụng template chuỗi: một literal
`"…"` hoặc `«…»` có các vị trí trống `§`, theo sau là các đối số trong
ngoặc đơn:

<<<FENCE 0>>>

Các quy tắc chính:

- `§` (U+00A7) là vị trí trống của template
- Vị trí trống theo thứ tự: `§0`, `§1`, … để chỉ rõ thứ tự
- Dấu `!` ở cuối chọn cách định dạng hiển thị: `"Salve, §!"(nomen)`
- Hậu tố `(args)` là phép áp dụng template, không phải lời gọi hàm

## Chuỗi dạng khối {#block-strings}

Các khối nhiều dòng sử dụng dấu ngoặc kép kiểu guillemet `«…»`:

<<<FENCE 1>>>

## Template được thu giữ (forma) {#captured-templates}

Template dùng dấu backtick thu giữ văn bản và tham số mà không thực hiện
việc kết xuất.
Phù hợp cho payload SQL/URL có liên kết tham số:

<<<FENCE 2>>>

## JSON nội tuyến {#inline-json}

`{ … }` trần là JSON nội tuyến: một tài liệu `json` tại thời điểm biên dịch,
không phải là đối tượng Faber ẩn danh. Các khóa là chuỗi được đặt trong dấu
nháy và phân tách bằng `:`:

<<<FENCE 3>>>

Để tạo một `genus` có kiểu, hãy sử dụng tên kiểu và dạng trường với `=`:

<<<FENCE 4>>>
