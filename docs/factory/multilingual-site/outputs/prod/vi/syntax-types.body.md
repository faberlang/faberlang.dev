Faber có hệ thống kiểu tĩnh, ưu tiên kiểu. Mọi khai báo đều đặt kiểu trước tên: `textus nomen`, không phải `nomen: textus`. Hệ thống kiểu bao phủ các kiểu nguyên thủy vô hướng, tập hợp tổng quát, kiểu số có kích thước, tensor và các kiểu thanh ghi hướng đến GPU.

## Các kiểu nguyên thủy {#primitive-types}

| Kiểu | Vai trò | Literal ví dụ |
|------|---------|---------------|
| `textus` | Chuỗi Unicode | `"Salve, munde"` |
| `ascii` | Token máy có độ dài cố định | `'solum:lege'` |
| `numerus` | Số nguyên có dấu (mặc định i64) | `42` |
| `fractus` | Số dấu phẩy động (mặc định f64) | `3.14` |
| `bivalens` | Boolean | `verum`, `falsum` |
| `vacuum` | Đơn vị / không có giá trị | — |
| `nihil` | Null / vắng mặt | `nihil` |
| `instans` | Khoảng thời gian / thời điểm | — |
| `json` | Giá trị JSON tại thời điểm biên dịch | `{ "key": "value" }` |
| `octeti` | Chuỗi byte dạng thập lục phân | \|00ff\| |

## Các kiểu số có kích thước {#sized-numeric-types}

`numerus` và `fractus` có độ rộng mặc định (i64 và f64) cùng các dạng chỉ rõ
độ rộng:

<<<FENCE 0>>>

Có thể dùng cú pháp rút gọn độ rộng ở vị trí kiểu: `i8` … `u64`, `f16`, `f32`,
`f64` tương đương với `numerus<W>` / `fractus<W>`.

## Các kiểu nullable {#nullable-types}

Giá trị nullable sử dụng cú pháp hợp `T ∪ nihil`:

<<<FENCE 1>>>

Faber không có cú pháp `T?` hoặc `Option<T>`. Hợp kiểu phải được viết tường minh.

## Bí danh kiểu {#type-aliases}

<<<FENCE 2>>>

## Generics {#generics}

Hàm, bí danh kiểu, `genus` và `implendum` chấp nhận tham số kiểu với cú pháp
`<T>`:

<<<FENCE 3>>>

Có thể chỉ rõ đối số kiểu tại vị trí gọi:

<<<FENCE 4>>>

## Tập hợp {#collections}

| Kiểu | Vai trò | Cú pháp rút gọn |
|------|---------|-----------------|
| `lista<T>` | Tập hợp động có thứ tự | `lf32`, `lu32` |
| `tabula<K, V>` | Bản đồ khóa-giá trị | — |
| `tensor<T, Figura>` | Bộ đệm dày có hình dạng cố định | `tf32[4]`, `ti64[2,3]` |
| `sparsa<T, Figura>` | Bộ đệm thưa có hình dạng cố định | `sf32[4]`, `si64[2,3]` |
| `intervallum` | Kiểu khoảng | — |
| `copia<T>` | Tập hợp không có thứ tự | — |
| `cursor<T>` | Luồng lười | — |

<<<FENCE 5>>>

## Các kiểu tensor {#tensor-types}

`tensor<T, Figura>` là bộ chứa dày có hình dạng cố định:

| Dạng | Ý nghĩa |
|------|---------|
| `tensor<T, Figura>` | Cách viết chuẩn |
| `tensor<T, []>` | Rank 0 (bộ chứa vô hướng) |
| `tensor<T, _>` | Vị trí để suy luận hình dạng |
| `tensor<T, [N]>` | Vector rank 1 |
| `tensor<T, [N, M]>` | Ma trận rank 2 |

<<<FENCE 6>>>

## Các kiểu lõi GPU {#gpu-core-types}

Các kiểu này được lane hệ thống nhận diện để xử lý GPU và thanh ghi.
Các đích gói không hỗ trợ phần cứng sẽ từ chối chúng:

<<<FENCE 7>>>

## Marker mượn trên kiểu {#borrow-markers}

Các marker mượn (`de`, `in`, `ex`) có thể xuất hiện trên kiểu ở vị trí tham số
để cho biết cách truyền một giá trị:

<<<FENCE 8>>>

## Chính sách so sánh {#comparison-policy}

| Toán tử | Nhóm | Hành vi |
|----------|------|---------|
| `≡`, `≠` | Bằng chính xác | Bắt buộc các kiểu giống hệt nhau; `nihil` được bỏ qua |
| `≈`, `≉` | Bằng theo giá trị số | Chỉ áp dụng cho lattice số |
| `<`, `≤`, `>`, `≥` | Thứ tự | Số, thời điểm, văn bản vô hướng |
| `intra` | Chứa trong khoảng | Số nằm trong khoảng |
| `inter` | Thành viên tập hợp | Phần tử nằm trong tập hợp |
