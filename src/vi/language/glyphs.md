+++
# This page discusses Latin keywords as Latin. Rendering them in
# the reader locale would turn its own examples into nonsense.
translate_spans = false
translation_kind = "translated"

title = "Glyphs and Latin"
section = "language"
order = 5
sources = [
  "radix/README.md (Glyphs and Words)",
  "examples/corpus/operatores/",
  "examples/corpus/assignatio/",
  "faber/docs/EBNF.md",
]
+++

## Glyphs and operators

Faber sử dụng các glyph, trong đó ký hiệu mang vai trò cấu trúc. Dưới đây là toàn bộ danh mục glyph nguồn được lexer nhận diện.

### Luồng giá trị {#value-flow}

| Glyph | Ý nghĩa |
|-------|---------|
| `←` | Liên kết, gán lại và biến đổi tại thời điểm chạy |
| `→` | Kiểu trả về của hàm |
| `⇥` | Lối thoát thay thế — kiểu kênh lỗi hoặc phục hồi chuyển đổi nội dòng |
| `∴` | Khớp nối đóng — nối thân hàm đóng với chữ ký (`(a, b) → T ∴ a + b`) |

### Hình dạng kiểu {#type-shape}

| Glyph | Ý nghĩa |
|-------|---------|
| `∷` | Gán kiểu tĩnh (ép kiểu tại thời điểm biên dịch) |
| `↦` | Chuyển đổi tại thời điểm chạy (phân tích hoặc ép kiểu có thể thất bại) |
| `∪` | Kiểu hợp nội dòng (`T ∪ nihil`) |

### So sánh {#comparison}

| Glyph | Ý nghĩa |
|-------|---------|
| `≡` `≠` | Bằng và khác chính xác |
| `<` `>` `≤` `≥` | Thứ tự |
| `≈` `≉` | Bằng nhau về giá trị số |

### Logic và thao tác bit {#logical-and-bitwise}

| Glyph | Ý nghĩa |
|-------|---------|
| `∧` `∨` `⊻` `¬` | Và, hoặc, xor, phủ định |
| `⇐` `⇒` | Dịch bit sang trái và sang phải |

### Cập nhật phép gán {#assignment-updates}

| Glyph | Ý nghĩa |
|-------|---------|
| `←` | Toán tử gán duy nhất trong biểu thức |
| `⊕` `⊖` | Câu lệnh tăng hoặc giảm hậu tố (chỉ áp dụng cho `numerus` có thể biến đổi) |

### Chuỗi tùy chọn và khẳng định khác `nihil` {#optional-chaining-and-non-null-assertion}

| Glyph | Ý nghĩa |
|-------|---------|
| `?` `?.` `?[` `?(` | Chuỗi tùy chọn |
| `!` `!.` `![` `!(` | Khẳng định giá trị không phải `nihil` |

### Khoảng {#ranges}

| Glyph | Ý nghĩa |
|-------|---------|
| `‥` | Điểm cuối khoảng không bao gồm |
| `…` | Điểm cuối khoảng có bao gồm |

### Dấu phân cách literal {#literal-delimiters}

| Glyph | Kiểu | Vai trò |
|-------|------|------|
| `'` | `ascii` | Token máy cố định |
| `"` | `textus` | Chuỗi một dòng |
| `«` `»` | `textus` | Chuỗi khối (dấu ngoặc kép kiểu guillemet) |
| `` ` `` | `forma` | Mẫu đã bắt giữ |
| `|` | `octeti` | Literal thập lục phân |
| `§` | lỗ mẫu | Phần giữ chỗ bên trong `"…"`, `«…»` và `` `…` `` |

### Dấu câu {#punctuation}

| Glyph | Vai trò |
|-------|---------|
| `(` `)` | Nhóm và lời gọi |
| `{` `}` | Khối, literal `genus` hoặc tài liệu JSON |
| `[` `]` | Literal danh sách và phép lập chỉ mục |
| `.` | Truy cập thành viên |
| `,` | Dấu phân cách |
| `;` | Dấu phân cách câu lệnh |
| `:` | Dấu phân cách trường JSON |
| `=` | Hình dạng trường cấu trúc (không phải phép gán tại thời điểm chạy) |
| `@` | Dấu chú thích |
| `#` | Chú thích dòng |

## Latin vocabulary and structural glyphs

*Ba lựa chọn tín hiệu giúp nhận ra mã nguồn Faber ngay từ cái nhìn đầu tiên.*

Faber đưa ra ba lựa chọn tín hiệu có chủ đích. Chúng phối hợp để tạo ra mã nguồn có hình thái ngữ pháp ổn định. Người đọc có thể nhận ra vai trò ngữ nghĩa của từng cấu trúc trước khi biết mã nguồn sẽ được biên dịch sang backend đích nào.

### Ba tín hiệu {#three}

| Tín hiệu | Ví dụ | Vai trò |
|----------|-------|---------|
| Khai báo đặt kiểu trước | `textus nomen`, `numerus aetas` | Hình dạng hướng về phép liên kết — kiểu, rồi đến tên. |
| Từ chỉ hành vi bằng tiếng Latin | `functio`, `genus`, `si`, `redde`, `fixum` | Khai báo, câu lệnh, vòng đời và chủ đích hành vi. |
| Ký hiệu cấu trúc | `← → ∴ ≡ ∪ ⇥` | Luồng giá trị, luồng kiểu và các mối nối cấu trúc — mang tính phổ quát, không bao giờ bản địa hoá. |

Ba tín hiệu này được thiết kế để củng cố lẫn nhau. Người đọc biết Faber ở một bản địa hoá có thể đọc nó ở bất kỳ bản địa hoá nào khác vì ký hiệu và cấu trúc không thay đổi. Người đọc biết backend Rust vẫn có thể nhận ra mã nguồn Faber vì các từ khoá Latin và thứ tự kiểu-trước tạo nên một diện mạo riêng biệt.

### Khai báo đặt kiểu trước {#type-first}

Faber đặt kiểu trước tên trong mọi khai báo. Đây là điều ngược lại với cú pháp họ C phổ biến, và đó là chủ ý:

| Cấu trúc | Thói quen của họ C | Faber |
|----------|--------------------|-------|
| Biến | `int count = 0` | `numerus count ← 0` |
| Hàm | `fn greet(name: String) → String` | `functio salve(textus nomen) → textus` |
| Tham số | `(String name)` | `(textus nomen)` |

Khai báo đặt kiểu trước có nghĩa là hình dạng của dữ liệu là điều đầu tiên người đọc nhìn thấy. Điều này tự nhiên phù hợp với các ngôn ngữ đọc từ trái sang phải theo độ bao quát ngữ nghĩa — khai báo trong tiếng Trung, tiếng Hindi và tiếng Ả Rập cũng theo cùng thứ tự.

```faber
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### Từ vựng hành vi bằng tiếng Latin {#latin}

Faber sử dụng các từ Latin cho mọi cấu trúc có hình dạng hành vi hoặc ngữ pháp. Từ vựng này nhỏ và đều đặn. Nó bắt nguồn từ một nguồn cổ điển duy nhất thay vì có nhiều nguồn từ nguyên pha trộn như trong hầu hết ngôn ngữ lập trình.

#### Khai báo {#declarations}

| Từ khoá | Vai trò | Tương đương gần đúng |
|---------|---------|----------------------|
| `functio` | Khai báo một hàm hoặc phương thức có tên | `fn`, `def`, `function` |
| `genus` | Khai báo một kiểu cụ thể có các trường | `class`, `struct` |
| `implendum` | Khai báo một hợp đồng hành vi | `interface`, `trait` |
| `typus` | Khai báo bí danh kiểu | `typedef`, `type` |
| `discretio` | Khai báo một hợp kiểu có thẻ | `enum`, `sum type` |

#### Liên kết và truyền giá trị {#bindings-and-transfer}

| Từ khoá | Vai trò | Tương đương gần đúng |
|---------|---------|----------------------|
| `fixum` | Liên kết bất biến (chỉ ghi một lần) | `let`, `const` |
| `varia` | Liên kết khả biến | `let mut`, `var` |
| `sit` | Liên kết bất biến suy luận ngắn gọn | `let` (suy luận) |
| `redde` | Trả về một giá trị từ hàm | `return` |
| `iace` | Ném lỗi qua kênh lỗi | `throw`, `raise` |
| `mori` | Trì hoãn — hành vi chưa thể biểu đạt | `unimplemented!`, `todo` |

#### Luồng điều khiển {#control-flow}

| Từ khoá | Vai trò | Tương đương gần đúng |
|---------|---------|----------------------|
| `si` | Nhánh điều kiện | `if` |
| `sin` | Nhánh ngược điều kiện | `else if` |
| `secus` | Nhánh còn lại | `else` |
| `dum` | Vòng lặp while | `while` |
| `itera` | Lặp qua giá trị, khoá hoặc khoảng | `for` |
| `elige` | So khớp mẫu (nhánh đầu tiên thắng) | `match`, `switch` |
| `fac` | Khối thử với phục hồi lỗi | `try`, `do` |
| `cape` | Bộ xử lý lỗi cho fac | `catch` |

> Từ vựng Latin có thể **liên kết** — nó được cung cấp trong gói chuẩn nhưng có thể ánh xạ lại thông qua bản địa hoá người đọc. Lập trình viên Thái thấy `ถ้า` thay cho `si`; lập trình viên Trung Quốc thấy `函数` thay cho `functio`. Từ vựng không có đặc quyền; chỉ ngữ pháp là cố định.

### Ký hiệu cấu trúc {#glyphs}

Trong khi từ vựng hành vi sử dụng các từ Latin, ý nghĩa cấu trúc sử dụng các ký hiệu phổ quát. Các ký hiệu này không bao giờ được bản địa hoá và không bao giờ thay đổi ý nghĩa giữa các lần kết xuất. Chúng là điểm neo trực quan giúp nhận ra mã nguồn Faber bất kể từ khoá được hiển thị bằng ngôn ngữ nào.

#### Luồng giá trị {#value-flow}

| Ký hiệu | Ý nghĩa |
|---------|---------|
| `←` | Liên kết thời gian chạy, gán lại và biến đổi — toán tử gán duy nhất |
| `→` | Khai báo kiểu giá trị trả về của hàm |
| `⇥` | Lối thoát thay thế: kiểu kênh lỗi hoặc phục hồi chuyển đổi nội tuyến |
| `∴` | Khớp nối đóng — nối thân hàm đóng với chữ ký |

#### Hình dạng kiểu {#type-shape}

| Ký hiệu | Ý nghĩa |
|---------|---------|
| `∷` | Ghi rõ kiểu tĩnh — khẳng định ở thời điểm biên dịch về kiểu của một giá trị |
| `↦` | Chuyển đổi thời gian chạy — phân tích hoặc ép kiểu có thể thất bại |
| `∪` | Kiểu hợp nội tuyến — nối hai kiểu (như `T ∪ nihil`) |

#### So sánh và logic {#comparison-and-logic}

| Ký hiệu | Nghĩa |
|-------|---------|
| `≡` `≠` | Bằng và khác tuyệt đối — yêu cầu khớp kiểu nghiêm ngặt |
| `<` `>` `≤` `≥` | So sánh thứ tự |
| `∧` `∨` `⊻` `¬` | Logic và bitwise: and, or, xor, not |


#### Quy ước liên kết rất quan trọng {#the-binding-convention-matters}

Một lựa chọn ký hiệu cần được chú ý đặc biệt vì đây là điểm gây nhầm lẫn phổ biến nhất đối với người đọc mới:

| Ký hiệu | Vai trò | Dùng cho |
|---------|---------|----------|
| `←` | **Luồng thời gian chạy** | Liên kết ban đầu, gán lại và biến đổi trong thời gian thực thi |
| `=` | **Hình dạng cấu trúc** | Tên trường bên trong literal và siêu dữ liệu khai báo — không dùng để lưu trữ thời gian chạy |

Hầu hết ngôn ngữ dùng `=` cho cả “định nghĩa trường này trong một kiểu” và “đặt một giá trị thời gian chạy vào biến này”. Faber tách hai nhiệm vụ đó. Mọi `←` đều là luồng dữ liệu đang hoạt động; mọi `=` bên trong `Type { … }` đều là bố cục trường của genus.

```text
# Runtime binding: ← attaches a value to a name
fixum numerus count ← 0
varia textus label ← "ready"
count ← count + 1

# Structural shape: = defines field values inside a literal
fixum _ p ← Point {
    x = 10,
    y = 20
}
```

### So với các ngôn ngữ phổ biến {#compare}

Bảng dưới đây cho thấy các mẫu lập trình phổ biến ánh xạ thế nào vào hệ thống ba tín hiệu của Faber. Cột Faber sử dụng một ký hiệu hoặc từ khoá khác nhau cho từng nhiệm vụ ngữ nghĩa riêng biệt — không nạp chồng.

| Nhiệm vụ ngữ nghĩa | Phổ biến trong các ngôn ngữ khác | Faber |
|--------------------|----------------------------------|-------|
| Khai báo kiểu tham số | `name: String` | `textus nomen` |
| Kiểu giá trị trả về | `→ String`, `: String` | `→` `textus` |
| Gán thời gian chạy | `x = value` | `←` |
| Kiểm tra bằng nhau | `==` | `≡` |
| Tính có thể rỗng | `T?`, `Option<T>` | `T ∪ nihil` |
| Nhánh + một câu lệnh | `if (cond) return x` | `si cond ergo redde x` |
| Ép kiểu | `(T)value`, `value as T` | `value ∷ T` |
| Chuyển đổi (có thể thất bại) | `try_into()` | `value ↦ T` |

### Tham khảo {#references}

1. Ngữ pháp EBNF — danh mục đầy đủ các ký hiệu và từ khoá
2. examples/corpus/ — kho ngôn ngữ với 292 tệp ví dụ bao phủ mọi từ khoá
3. examples/corpus/operatores/ — các ví dụ về toán tử và ký hiệu
4. Các điều răn — chín quy luật thiết kế bảo toàn các tín hiệu này

## Canonical vs sugar surfaces

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

### Đường tắt kiểu số {#numeric-type-sugar}

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

### Đường tắt chú thích {#annotation-sugar}

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

### Định dạng theo tác giả và dạng chuẩn {#author-vs-canonical-formatting}

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

### Nguyên tắc thiết kế {#design-principle}

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

### Tham chiếu {#references}

1. `radix/docs/design/numeric-type-sugar.md` — các họ đường tắt đầy đủ, ưu tiên cách viết
2. `radix/docs/design/annotation-sugar.md` — mô hình chú thích hai bề mặt
3. `radix/docs/design/faber-canonical-surface.md` — chính sách định dạng theo tác giả và dạng chuẩn
4. `faber/docs/EBNF.md` — các bảng ngữ pháp cho dạng đường tắt
