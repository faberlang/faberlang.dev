+++
translation_kind = "translated"

title = "Data types"
section = "syntax"
order = 1
sources = [
  "radix/README.md (Core Type Surfaces, Numeric Widths, Tensors And Sparsa, GPU Core Types)",
  "radix/docs/design/numeric-type-sugar.md",
  "radix/docs/design/tensor-intrinsics.md",
  "radix/docs/design/lista-intrinsics.md",
  "radix/docs/design/comparison-operators.md",
  "radix/EBNF.md",
  "examples/corpus/typi/",
  "examples/corpus/tensor/",
  "examples/corpus/lista/",
]


prose_hash = "sha256:b3f22d05ed3eb8bbc5d3322fd71f7677a77ba9909b6c80f1cfa00455320e7de5"
code_hash = "sha256:c2351c4cdd58a84dd89c4adc956cce28ce5d7a3db572eae85b44d4a6dbb5d48a"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
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

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

Có thể dùng cú pháp rút gọn độ rộng ở vị trí kiểu: `i8` … `u64`, `f16`, `f32`,
`f64` tương đương với `numerus<W>` / `fractus<W>`.

## Các kiểu nullable {#nullable-types}

Giá trị nullable sử dụng cú pháp hợp `T ∪ nihil`:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio maybe() → textus ∪ nihil {
    redde nihil
}
```

Faber không có cú pháp `T?` hoặc `Option<T>`. Hợp kiểu phải được viết tường minh.

## Bí danh kiểu {#type-aliases}

```faber
typus UserId = numerus
```

## Generics {#generics}

Hàm, bí danh kiểu, `genus` và `implendum` chấp nhận tham số kiểu với cú pháp
`<T>`:

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

Có thể chỉ rõ đối số kiểu tại vị trí gọi:

```faber
functio identitas<T>(T valor) → T { redde valor }

fixum numerus value ← identitas<numerus>(7)
```

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

```faber
fixum lista<numerus> nums ← [1, 2, 3]
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## Các kiểu tensor {#tensor-types}

`tensor<T, Figura>` là bộ chứa dày có hình dạng cố định:

| Dạng | Ý nghĩa |
|------|---------|
| `tensor<T, Figura>` | Cách viết chuẩn |
| `tensor<T, []>` | Rank 0 (bộ chứa vô hướng) |
| `tensor<T, _>` | Vị trí để suy luận hình dạng |
| `tensor<T, [N]>` | Vector rank 1 |
| `tensor<T, [N, M]>` | Ma trận rank 2 |

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

## Các kiểu lõi GPU {#gpu-core-types}

Các kiểu này được lane hệ thống nhận diện để xử lý GPU và thanh ghi.
Các đích gói không hỗ trợ phần cứng sẽ từ chối chúng:

```faber
functio half(f16 x) → f16 { redde x }

functio add(matrix<f32, [2, 2]> a, matrix<f32, [2, 2]> b) → matrix<f32, [2, 2]> {
    redde a.addita(b)
}

functio swap(atomic<i32> cell, i32 value) → i32 {
    redde cell.exchange(value)
}
```

## Marker mượn trên kiểu {#borrow-markers}

Các marker mượn (`de`, `in`, `ex`) có thể xuất hiện trên kiểu ở vị trí tham số
để cho biết cách truyền một giá trị:

```faber
# shared borrow — caller retains ownership
functio imprime(de textus label) → vacuum { }

# mutable borrow — caller lends mutable access
functio duplica(in numerus value) → vacuum { }

# move — caller gives up ownership
functio consume(ex textus buffer) → textus {
    redde buffer
}
```

## Chính sách so sánh {#comparison-policy}

| Toán tử | Nhóm | Hành vi |
|----------|------|---------|
| `≡`, `≠` | Bằng chính xác | Bắt buộc các kiểu giống hệt nhau; `nihil` được bỏ qua |
| `≈`, `≉` | Bằng theo giá trị số | Chỉ áp dụng cho lattice số |
| `<`, `≤`, `>`, `≥` | Thứ tự | Số, thời điểm, văn bản vô hướng |
| `intra` | Chứa trong khoảng | Số nằm trong khoảng |
| `inter` | Thành viên tập hợp | Phần tử nằm trong tập hợp |
