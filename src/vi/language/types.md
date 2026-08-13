+++
translation_kind = "translated"

title = "Types and values"
section = "language"
order = 2
sources = [
  "radix/README.md (Core Type Surfaces, Numeric Widths, Tensors And Sparsa, GPU Core Types)",
  "radix/docs/design/numeric-type-sugar.md",
  "radix/docs/design/tensor-intrinsics.md",
  "radix/docs/design/lista-intrinsics.md",
  "radix/docs/design/comparison-operators.md",
  "faber/docs/EBNF.md",
  "examples/corpus/typi/",
  "examples/corpus/tensor/",
  "examples/corpus/lista/",
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "examples/corpus/fixum/",
  "examples/corpus/sit/",
  "radix/README.md (Tensors And Sparsa)",
  "radix/docs/design/tabula-intrinsics.md",
  "examples/corpus/tabula/",
  "examples/corpus/sparsa/",
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
  "radix/README.md (Nullability and Optionality)",
  "examples/corpus/nihil/",
  "examples/corpus/sponte/",
  "examples/corpus/nonnihil/",
  "radix/README.md (Conversion and Construction)",
  "radix/docs/design/conversio-valor.md",
  "radix/docs/design/failable-conversio.md",
]
+++

## Data types

Faber có hệ thống kiểu tĩnh, ưu tiên kiểu. Mọi khai báo đều đặt kiểu trước tên: `textus nomen`, không phải `nomen: textus`. Hệ thống kiểu bao phủ các kiểu nguyên thủy vô hướng, tập hợp tổng quát, kiểu số có kích thước, tensor và các kiểu thanh ghi hướng đến GPU.

### Các kiểu nguyên thủy {#primitive-types}

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

### Các kiểu số có kích thước {#sized-numeric-types}

`numerus` và `fractus` có độ rộng mặc định (i64 và f64) cùng các dạng chỉ rõ
độ rộng:

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

Có thể dùng cú pháp rút gọn độ rộng ở vị trí kiểu: `i8` … `u64`, `f16`, `f32`,
`f64` tương đương với `numerus<W>` / `fractus<W>`.

### Các kiểu nullable {#nullable-types}

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

### Bí danh kiểu {#type-aliases}

```faber
typus UserId = numerus
```

### Generics {#generics}

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

### Tập hợp {#collections}

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

### Các kiểu tensor {#tensor-types}

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

### Các kiểu lõi GPU {#gpu-core-types}

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

### Marker mượn trên kiểu {#borrow-markers}

Các marker mượn (`de`, `in`, `ex`) có thể xuất hiện trên kiểu ở vị trí tham số
để cho biết cách truyền một giá trị:

```faber locale=la
# shared borrow — caller retains ownership
functio imprime(de textus label) → vacuum { }

# mutable borrow — caller lends mutable access
functio duplica(in numerus value) → vacuum { }

# move — caller gives up ownership
functio consume(ex textus buffer) → textus {
    redde buffer
}
```

### Chính sách so sánh {#comparison-policy}

| Toán tử | Nhóm | Hành vi |
|----------|------|---------|
| `≡`, `≠` | Bằng chính xác | Bắt buộc các kiểu giống hệt nhau; `nihil` được bỏ qua |
| `≈`, `≉` | Bằng theo giá trị số | Chỉ áp dụng cho lattice số |
| `<`, `≤`, `>`, `≥` | Thứ tự | Số, thời điểm, văn bản vô hướng |
| `intra` | Chứa trong khoảng | Số nằm trong khoảng |
| `inter` | Thành viên tập hợp | Phần tử nằm trong tập hợp |

## Variables and binding

Faber có ba từ khóa biến và một ký hiệu gán riêng. Điểm khác biệt chính nằm giữa `fixum` (chỉ ghi một lần) và `varia` (có thể gán lại tự do), cũng như giữa `←` (luồng thực thi) và `=` (hình dạng trường mang tính cấu trúc).

### fixum — liên kết bất biến {#fixum-immutable-binding}

Các liên kết `fixum` chỉ được ghi một lần. Có thể khai báo chúng có hoặc không có trình khởi tạo; nếu khai báo mà không có trình khởi tạo, chúng phải được gán đúng một lần trước khi đọc. Lần gán thứ hai sẽ bị từ chối.

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

Khởi tạo trì hoãn:

```faber
incipit {
    fixum numerus factor
    si verum {
        factor ← 10
    } secus {
        factor ← 100
    }
    nota factor
}
```

### varia — liên kết khả biến {#varia-mutable-binding}

Các liên kết `varia` có thể được gán lại tự do:

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

### sit — cú pháp rút gọn cho liên kết bất biến suy luận kiểu {#sit-inferred-immutable-sugar}

`sit` là cú pháp rút gọn của `fixum _` — một liên kết bất biến với kiểu được suy luận:

```faber
incipit {
    sit salve ← "Salve"
    sit nomen ← "Marcus"
    sit x ← 42

    # Deferred form
    sit label
    label ← "deferred"
}
```

### Liên kết thời gian chạy và định nghĩa cấu trúc {#runtime-binding-vs-structural-definition}

Faber tách biệt hai vai trò mà hầu hết các ngôn ngữ gộp chung vào `=`:

| Ký hiệu | Vai trò | Dùng cho |
|---------|---------|----------|
| `←` | Luồng thời gian chạy | Liên kết ban đầu, gán lại, biến đổi |
| `=` | Hình dạng cấu trúc | Tên trường bên trong literal và siêu dữ liệu |

```faber
genus Point {
    numerus x
    numerus y
}

incipit {
    # Runtime: ← attaches a value to a name at execution time
    varia numerus count ← 0
    varia textus label ← "ready"
    count ← count + 1

    # Structural: = defines field values inside a type literal
    fixum _ p ← Point {
        x = 10,
        y = 20
    }
}
```

### Trích xuất trường bằng ex {#ex-field-extraction}

`ex` trích xuất các trường từ một giá trị vào các liên kết cục bộ:

```faber
genus Persona {
    textus nomen
    numerus aetas
}

incipit {
    fixum _ p ← Persona { nomen = "Marcus", aetas = 30 }
    ex p fixum nomen, aetas
    # prints "Marcus"
    nota nomen
}
```

### Tăng và giảm hậu tố {#postfix-increment-and-decrement}

`⊕` và `⊖` là các câu lệnh tăng/giảm hậu tố dành cho các vị trí `numerus` khả biến. Chúng chỉ được dùng như câu lệnh — không có giá trị biểu thức và không có dạng tiền tố:

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ⊕
    # i becomes 0
    i ⊖
}
```

## Collections

Faber có một số kiểu tập hợp do trình biên dịch sở hữu. Các phương thức chuẩn của chúng nằm trong trình biên dịch, không nằm trong thư viện chuẩn.

### Lista — tập hợp động có thứ tự {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

Trải phần tử bằng `sparge`:

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

Các phương thức chính: `longitudo`, `accipe`, `appende`, `summa`, `primus`, `novissimus`.

### Tabula — ánh xạ khóa–giá trị {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

### Tensor — bộ đệm dày có hình dạng cố định {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

Cú pháp rút gọn cho Tensor (mã thiên về số):

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

Các phương thức chính: `forma`, `accipe`, `ponde`, `crea`, `structa`, `strue`, cùng với phép tính theo từng phần tử, phép nhân ma trận (`multiplicatio`) và các phép rút gọn (`summa`, `productum`).

### Sparsa — bộ đệm thưa có hình dạng cố định {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

Chuyển đổi giữa dạng dày và dạng thưa:

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

### Cursors — luồng lười {#cursors}

`cursor<T>` là một kiểu luồng lười. Nó được tạo từ các bộ lặp của tập hợp, các view `tuus` hoặc các hàm sinh. Luồng được tiêu thụ bằng `itera ex`:

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

### Intervallum — các khoảng {#intervallum}

```faber
# exclusive range: 0, 1, 2, 3, 4
itera ab 0‥5 fixum i {
    nota i
}
# inclusive range: 0, 1, 2, 3, 4, 5
itera ab 0…5 fixum i {
    nota i
}
```

`‥` là điểm cuối khoảng loại trừ; `…` là điểm cuối khoảng bao gồm.

## String and template literals

Faber sử dụng ngữ nghĩa của các dấu phân cách — mỗi dạng dấu nháy biểu thị một dạng mã nguồn khác nhau. Chúng không phải là các từ đồng nghĩa có thể thay thế cho nhau.

### Dạng literal {#literal-forms}

| Dạng | Kiểu | Vai trò |
|------|------|------|
| `'…'` | `ascii` | Token cố định dành cho máy; không có `§`; không có `(…)` |
| `"…"` | `textus` | Chuỗi Unicode một dòng ngắn; `(…)` được nội suy |
| `«…»` | `textus` | Unicode dạng khối/nhiều dòng; `(…)` được nội suy |
| `` `…` `` | `forma` | Template được thu giữ; `(…)` được thu giữ |
| `{ … }` | `json` | Tài liệu JSON tại thời điểm biên dịch |
| `|…|` | `octeti` | Dãy byte hex tại thời điểm biên dịch |
| `[ … ]` | `lista<T>` | Literal danh sách Faber |

### Áp dụng template chuỗi {#string-template-application}

Faber định dạng văn bản bằng phép áp dụng template chuỗi: một literal
`"…"` hoặc `«…»` có các vị trí trống `§`, theo sau là các đối số trong
ngoặc đơn:

```faber
functio greet(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}

fixum numerus pagina ← 3
fixum numerus totum ← 10
fixum textus code ← "200"
fixum textus label ← "OK"

fixum _ msg ← "Page § of §"(pagina, totum)
fixum _ block ← «status: § (§)»(code, label)
```

Các quy tắc chính:

- `§` (U+00A7) là vị trí trống của template
- Vị trí trống theo thứ tự: `§0`, `§1`, … để chỉ rõ thứ tự
- Dấu `!` ở cuối chọn cách định dạng hiển thị: `"Salve, §!"(nomen)`
- Hậu tố `(args)` là phép áp dụng template, không phải lời gọi hàm

### Chuỗi dạng khối {#block-strings}

Các khối nhiều dòng sử dụng dấu ngoặc kép kiểu guillemet `«…»`:

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

### Template được thu giữ (forma) {#captured-templates}

Template dùng dấu backtick thu giữ văn bản và tham số mà không thực hiện
việc kết xuất.
Phù hợp cho payload SQL/URL có liên kết tham số:

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

### JSON nội tuyến {#inline-json}

`{ … }` trần là JSON nội tuyến: một tài liệu `json` tại thời điểm biên dịch,
không phải là đối tượng Faber ẩn danh. Các khóa là chuỗi được đặt trong dấu
nháy và phân tách bằng `:`:

```faber
fixum _ empty ← {}
fixum _ user ← { "name": "Marcus", "age": 30, "active": true }
fixum _ nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
```

Để tạo một `genus` có kiểu, hãy sử dụng tên kiểu và dạng trường với `=`:

```faber
genus Point {
    numerus x
    numerus y
}
fixum _ p ← Point { x = 10, y = 20 }
```

## Nullability and optionality

Faber phân biệt sự vắng mặt trong một giá trị với việc cung cấp tùy chọn tại vị trí khai báo.

### Giá trị nullable — T ∪ nihil {#nullable-values}

Dùng `T ∪ nihil` khi giá trị có thể vắng mặt:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### Vị trí khai báo tùy chọn — sponte {#optional-declaration-slots}

Đặt `sponte` sau tên khi tham số hoặc trường có thể được lược bỏ bởi bên gọi hoặc hàm khởi tạo:

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

Các dấu mượn có thể kết hợp với tham số tùy chọn:

```faber
functio process(de numerus depth sponte) → vacuum { }
```

### Khẳng định non-null — ! {#non-null-assertion}

Dùng `!.`, `![`, `!(` để khẳng định rằng một giá trị nullable không phải là `nihil`:

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

Khẳng định non-null trên `nihil` sẽ hủy thực thi tại thời điểm chạy.

### Kết hợp nullish — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

### ignotum {#ignotum}

`ignotum` là kiểu unknown cấp cao nhất dành cho các lối thoát tạm thời và tri thức chưa hoàn chỉnh. Đây không phải là cơ chế biểu diễn tính nullable.

## Conversion and construction

Hai toán tử chuyển đổi quan trọng, một toán tử dùng khi chạy chương trình và một toán tử dùng tại thời điểm biên dịch:

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus value ← 7
fixum _ text ← value ∷ textus
```

### Chuyển đổi khi chạy chương trình — ↦ {#runtime-conversion}

Dùng `↦` để chuyển đổi khi chạy chương trình, đặc biệt là khi phân tích cú pháp hoặc ép kiểu có thể thất bại. Cung cấp xử lý phục hồi nội tuyến bằng `⇥`:

```faber
fixum textus input ← "9"
fixum _ n ← "42" ↦ numerus
fixum _ safe ← input ↦ numerus ⇥ 0
```

Vật chất hóa theo kiểu:

```faber
fixum textus path ← "/etc/hosts"
fixum _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
fixum _ body ← ad 'solum:lege' (path) ↦ textus
```

### Gán kiểu tĩnh — ∷ {#static-ascription}

Dùng `∷` để gán kiểu tĩnh một cách tường minh. Toán tử này đặt ở hậu tố và được điều khiển bởi kiểu đích:

```faber
fixum numerus value ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

### Kết hợp giá trị null — vel {#nullish-coalescing}

Dùng `vel` để kết hợp giá trị null khi một giá trị là `nihil`:

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
