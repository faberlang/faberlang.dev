+++
translation_kind = "translated"

title = "Canonical vs sugar surfaces"
section = "features"
order = 6
sources = []


prose_hash = "sha256:af0aea6696c347bf589234a18320a6d9b7f95f6fbaf8bc3d83979b40f4212a43"
code_hash = "sha256:2fcab63f1bda97519d332924a5675a802a8a06cc8b303b8eaec72c6196ea1a43"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
*Nhiều bề mặt có thể phân tích, một hình dạng ngữ nghĩa duy nhất.*

Một mẫu thiết kế lặp lại trong Faber: ngôn ngữ định nghĩa **một cách viết chuẩn**
cho mỗi cấu trúc, nhưng chấp nhận nhiều **cách viết đường tắt**
có ngữ nghĩa tương đương. Trình biên dịch không ưu tiên cách nào —
cả hai đều được phân tích thành cùng một nút AST. Bộ định dạng quyết định
cách viết nào sẽ được xuất ra dựa trên ngữ cảnh và chế độ.

> **Quy tắc:** Các cách viết đường tắt có ngữ nghĩa tương đương với dạng đầy đủ.
> Nhiều bề mặt được phân tích thành cùng một `HirAnnotation` hoặc nút kiểu.
> `faber format --canonical` ưu tiên cách viết chuẩn; chế độ tác giả
> giữ nguyên cách viết đường tắt mà tác giả đã dùng.

## Đường tắt kiểu số {#numeric-type-sugar}

Các kiểu số có cách viết chuẩn dạng đầy đủ và các dạng đường tắt nhỏ gọn.
Lựa chọn này áp dụng theo từng mô-đun, không phải theo từng kho mã — một
gói CLI có thể dùng dạng đầy đủ ở mọi nơi, trong khi một mô-đun nhân tensor
dùng dạng đường tắt:

| Đường tắt | Dạng chuẩn | Miền |
|-------|----------------|--------|
| `f32`, `f64`, `i32`, `u64` | `fractus<f32>`, `numerus<i32>` | Dấu độ rộng — kiểu số vô hướng |
| `tf32`, `tf32[4]`, `ti64[2, 3]` | `tensor<f32, _>`, `tensor<f32, [4]>` | Tensor dày — `t` + độ rộng + hình dạng tùy chọn |
| `sf32`, `sf32[2, 3]`, `si64[N]` | `sparsa<f32, _>`, `sparsa<f32, [2, 3]>` | Tensor thưa — `s` + độ rộng + hình dạng tùy chọn |
| `mf32[4, 4]`, `mu32[3, 3]` | `matrix<f32, [4, 4]>` | Ma trận lớp thanh ghi — `m` + độ rộng + hình dạng |
| `lf32`, `lu32`, `li64` | `lista<f32>`, `lista<u32>` | Danh sách — `l` + độ rộng |
| `f16` | `fractus<f16>` | Dấu độ rộng half-float (chỉ có ý nghĩa về ngữ nghĩa/bố cục) |

**Faber thông thường (ưu tiên dạng đầy đủ):**

```faber
fixum lista<f32> values ← vacua
fixum tensor<f32, [2, 3]> grid ← vacua
fixum numerus<i32> narrow ← 7
```

**Các mô-đun số (ưu tiên dạng đường tắt):**

```faber
fixum lf32 values ← vacua
fixum tf32[2, 3] grid ← vacua
fixum i32 narrow ← 7
```

Đường tắt **chỉ dùng ở vị trí kiểu**. Các định danh giá trị có tên
`f32`, `tf32` hoặc `mf32` vẫn giữ nguyên — trình biên dịch chỉ
diễn giải chúng là đường tắt khi chúng xuất hiện ở vị trí kiểu. Một tệp
sử dụng đường tắt nhất quán nên khai báo điều này một lần ở đầu tệp:

```faber
# STYLE: numeric sugar (tf32, mf32, sf32, lf32, lu32)
```

## Đường tắt chú thích {#annotation-sugar}

Chú thích Faber tuân theo cùng mô hình hai bề mặt như kiểu số.
Chú thích là siêu dữ liệu do trình biên dịch sở hữu, được gắn vào các khai báo —
chẳng hạn `@ optio` cho định nghĩa tùy chọn CLI hoặc `@ futura`
cho các hàm bất đồng bộ.

**Dạng chuẩn:** một bản ghi có ngoặc nhọn với tên trường rõ ràng:

```text
@ optio {
    binding = verbose,
    brevis = "v",
    longum = "verbose",
    typus = bivalens,
    ubique = verum,
    descriptio = "Enable verbose output"
}
```

**Dạng đường tắt:** các đối số theo vị trí và bí danh có tên:

```text
@ optio verbose brevis "v" longum "verbose" typus bivalens ubique descriptio "Enable verbose output"
```

Cả hai dạng đều tạo ra cùng một bản ghi `HirAnnotation`. Dạng chuẩn rõ ràng
và tự mô tả; dạng đường tắt ngắn gọn cho các chú thích được dùng thường xuyên,
khi thứ tự trường đã được quy ước rõ.
`faber format --canonical` ưu tiên các bản ghi có ngoặc nhọn; chế độ tác giả
giữ nguyên dạng mà tác giả đã chọn.

## Định dạng theo tác giả và dạng chuẩn {#author-vs-canonical-formatting}

Lệnh `faber format` hoạt động ở hai chế độ, phản ánh nguyên tắc
dạng chuẩn và dạng đường tắt:

| Chế độ | Lệnh | Đầu vào | Đầu ra |
|------|---------|-------|--------|
| Tác giả | `faber format` | AST đã phân tích + trivia đứng trước | Mã nguồn Faber giữ nguyên chú thích `#`, dòng trống và cách viết đường tắt |
| Chuẩn | `faber format --canonical` | HIR đã phân tích + `TypeTable` | Faber đã chuẩn hóa — không có chú thích, dùng cách viết chuẩn, không có đường tắt |

Cả hai chế độ đều đi qua toàn bộ phần đầu của trình biên dịch (phân tích từ vựng,
phân tích cú pháp, phân tích ngữ nghĩa đối với chế độ chuẩn). Mã nguồn không hợp lệ
sẽ tạo ra chẩn đoán của trình biên dịch — bộ định dạng không âm thầm định dạng
đầu vào bị lỗi.

Các quy tắc chính áp dụng cho cả hai chế độ:

- Thụt lề bốn khoảng trắng
- Dấu ngoặc Stroustrup: dấu `{` mở nằm trên cùng dòng với phần đầu điều khiển
- Chế độ tác giả giữ nguyên *sự hiện diện* của các dòng trống nhưng thu gọn các chuỗi dài hơn một dòng
- Chế độ tác giả không chèn các dòng trống mà mã nguồn không có
- Chế độ chuẩn chuẩn hóa cách viết kiểu về dạng đầy đủ, tensor đường tắt về dạng chuẩn, và chú thích về bản ghi có ngoặc nhọn
- Chế độ chuẩn xuất `T ∪ nihil` cho các hợp nullable, và `sponte` cho các tham số tùy chọn

## Nguyên tắc thiết kế {#design-principle}

Mẫu dạng chuẩn và dạng đường tắt xuất hiện ở nhiều nơi vì đây là một
nguyên tắc thiết kế có chủ ý, không phải tập hợp các tiện ích riêng lẻ:

| Miền | Dạng chuẩn | Đường tắt |
--------|-----------|-------|
| Kiểu số | `numerus<i32>` | `i32` |
| Kiểu tensor | `tensor<f32, [4]>` | `tf32[4]` |
| Chú thích | `@ optio { binding = verbose }` | `@ optio verbose ...` |
| Định dạng | `faber format --canonical` | `faber format` (chế độ tác giả) |
| Ngôn ngữ đọc | Latin (`la`) | Bất kỳ gói ngôn ngữ nào |

Mẫu này phục vụ hai mục tiêu. Thứ nhất, nó hạ thấp rào cản tiếp cận —
người dùng mới có thể viết `tf32[4]` mà không phải gõ
`tensor<fractus<f32>, [4]>`. Thứ hai, nó giữ cho ngôn ngữ chuẩn không mơ hồ —
khi độ chính xác quan trọng, dạng đầy đủ nói chính xác ý nghĩa của nó.
Bộ định dạng kết nối hai dạng này: tác giả viết dạng đường tắt,
người đánh giá có thể yêu cầu dạng chuẩn, và CI có thể thực thi một trong hai.

## Tham chiếu {#references}

1. `radix/docs/design/numeric-type-sugar.md` — các họ đường tắt đầy đủ, ưu tiên cách viết
2. `radix/docs/design/annotation-sugar.md` — mô hình chú thích hai bề mặt
3. `radix/docs/design/faber-canonical-surface.md` — chính sách định dạng theo tác giả và dạng chuẩn
4. `radix/EBNF.md` — các bảng ngữ pháp cho dạng đường tắt
