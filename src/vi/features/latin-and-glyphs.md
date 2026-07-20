+++
translation_kind = "translated"


title = "Latin vocabulary and structural glyphs"
section = "features"
order = 4
sources = []



prose_hash = "sha256:e460f8b157e7a98e6ecfc93d025078296877a974b90af1780945825df87741e5"
code_hash = "sha256:af40f7de992982b8319f9aed102017b00ded01ddee4d3d48ecb75d1b7b746b92"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
*Ba lựa chọn tín hiệu giúp nhận ra mã nguồn Faber ngay từ cái nhìn đầu tiên.*

Faber đưa ra ba lựa chọn tín hiệu có chủ đích. Chúng phối hợp để tạo ra mã nguồn có hình thái ngữ pháp ổn định. Người đọc có thể nhận ra vai trò ngữ nghĩa của từng cấu trúc trước khi biết mã nguồn sẽ được biên dịch sang backend đích nào.

## Ba tín hiệu {#three}

| Tín hiệu | Ví dụ | Vai trò |
|----------|-------|---------|
| Khai báo đặt kiểu trước | `textus nomen`, `numerus aetas` | Hình dạng hướng về phép liên kết — kiểu, rồi đến tên. |
| Từ chỉ hành vi bằng tiếng Latin | `functio`, `genus`, `si`, `redde`, `fixum` | Khai báo, câu lệnh, vòng đời và chủ đích hành vi. |
| Ký hiệu cấu trúc | `← → ∴ ≡ ∪ ⇥` | Luồng giá trị, luồng kiểu và các mối nối cấu trúc — mang tính phổ quát, không bao giờ bản địa hoá. |

Ba tín hiệu này được thiết kế để củng cố lẫn nhau. Người đọc biết Faber ở một bản địa hoá có thể đọc nó ở bất kỳ bản địa hoá nào khác vì ký hiệu và cấu trúc không thay đổi. Người đọc biết backend Rust vẫn có thể nhận ra mã nguồn Faber vì các từ khoá Latin và thứ tự kiểu-trước tạo nên một diện mạo riêng biệt.

## Khai báo đặt kiểu trước {#type-first}

Faber đặt kiểu trước tên trong mọi khai báo. Đây là điều ngược lại với cú pháp họ C phổ biến, và đó là chủ ý:

| Cấu trúc | Thói quen của họ C | Faber |
|----------|--------------------|-------|
| Biến | `int count = 0` | `numerus count ← 0` |
| Hàm | `fn greet(name: String) → String` | `functio salve(textus nomen) → textus` |
| Tham số | `(String name)` | `(textus nomen)` |

Khai báo đặt kiểu trước có nghĩa là hình dạng của dữ liệu là điều đầu tiên người đọc nhìn thấy. Điều này tự nhiên phù hợp với các ngôn ngữ đọc từ trái sang phải theo độ bao quát ngữ nghĩa — khai báo trong tiếng Trung, tiếng Hindi và tiếng Ả Rập cũng theo cùng thứ tự.

```faber
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## Từ vựng hành vi bằng tiếng Latin {#latin}

Faber sử dụng các từ Latin cho mọi cấu trúc có hình dạng hành vi hoặc ngữ pháp. Từ vựng này nhỏ và đều đặn. Nó bắt nguồn từ một nguồn cổ điển duy nhất thay vì có nhiều nguồn từ nguyên pha trộn như trong hầu hết ngôn ngữ lập trình.

### Khai báo {#declarations}

| Từ khoá | Vai trò | Tương đương gần đúng |
|---------|---------|----------------------|
| `functio` | Khai báo một hàm hoặc phương thức có tên | `fn`, `def`, `function` |
| `genus` | Khai báo một kiểu cụ thể có các trường | `class`, `struct` |
| `implendum` | Khai báo một hợp đồng hành vi | `interface`, `trait` |
| `typus` | Khai báo bí danh kiểu | `typedef`, `type` |
| `discretio` | Khai báo một hợp kiểu có thẻ | `enum`, `sum type` |

### Liên kết và truyền giá trị {#bindings-and-transfer}

| Từ khoá | Vai trò | Tương đương gần đúng |
|---------|---------|----------------------|
| `fixum` | Liên kết bất biến (chỉ ghi một lần) | `let`, `const` |
| `varia` | Liên kết khả biến | `let mut`, `var` |
| `sit` | Liên kết bất biến suy luận ngắn gọn | `let` (suy luận) |
| `redde` | Trả về một giá trị từ hàm | `return` |
| `iace` | Ném lỗi qua kênh lỗi | `throw`, `raise` |
| `mori` | Trì hoãn — hành vi chưa thể biểu đạt | `unimplemented!`, `todo` |

### Luồng điều khiển {#control-flow}

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

## Ký hiệu cấu trúc {#glyphs}

Trong khi từ vựng hành vi sử dụng các từ Latin, ý nghĩa cấu trúc sử dụng các ký hiệu phổ quát. Các ký hiệu này không bao giờ được bản địa hoá và không bao giờ thay đổi ý nghĩa giữa các lần kết xuất. Chúng là điểm neo trực quan giúp nhận ra mã nguồn Faber bất kể từ khoá được hiển thị bằng ngôn ngữ nào.

### Luồng giá trị {#value-flow}

| Ký hiệu | Ý nghĩa |
|---------|---------|
| `←` | Liên kết thời gian chạy, gán lại và biến đổi — toán tử gán duy nhất |
| `→` | Khai báo kiểu giá trị trả về của hàm |
| `⇥` | Lối thoát thay thế: kiểu kênh lỗi hoặc phục hồi chuyển đổi nội tuyến |
| `∴` | Thân lệnh compact bắt đầu bằng therefore — giới thiệu thân nhánh chỉ có một câu lệnh |

### Hình dạng kiểu {#type-shape}

| Ký hiệu | Ý nghĩa |
|---------|---------|
| `∷` | Ghi rõ kiểu tĩnh — khẳng định ở thời điểm biên dịch về kiểu của một giá trị |
| `↦` | Chuyển đổi thời gian chạy — phân tích hoặc ép kiểu có thể thất bại |
| `∪` | Kiểu hợp nội tuyến — nối hai kiểu (như `T ∪ nihil`) |

### So sánh và logic {#comparison-and-logic}

| Ký hiệu | Nghĩa |
|-------|---------|
| `≡` `≠` | Bằng và khác tuyệt đối — yêu cầu khớp kiểu nghiêm ngặt |
| `<` `>` `≤` `≥` | So sánh thứ tự |
| `∧` `∨` `⊻` `¬` | Logic và bitwise: and, or, xor, not |


### Quy ước liên kết rất quan trọng {#the-binding-convention-matters}

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

## So với các ngôn ngữ phổ biến {#compare}

Bảng dưới đây cho thấy các mẫu lập trình phổ biến ánh xạ thế nào vào hệ thống ba tín hiệu của Faber. Cột Faber sử dụng một ký hiệu hoặc từ khoá khác nhau cho từng nhiệm vụ ngữ nghĩa riêng biệt — không nạp chồng.

| Nhiệm vụ ngữ nghĩa | Phổ biến trong các ngôn ngữ khác | Faber |
|--------------------|----------------------------------|-------|
| Khai báo kiểu tham số | `name: String` | `textus nomen` |
| Kiểu giá trị trả về | `→ String`, `: String` | `→` `textus` |
| Gán thời gian chạy | `x = value` | `←` |
| Kiểm tra bằng nhau | `==` | `≡` |
| Tính có thể rỗng | `T?`, `Option<T>` | `T ∪ nihil` |
| Nhánh + một câu lệnh | `if (cond) return x` | `si cond ∴ redde x` |
| Ép kiểu | `(T)value`, `value as T` | `value ∷ T` |
| Chuyển đổi (có thể thất bại) | `try_into()` | `value ↦ T` |

## Tham khảo {#references}

1. Ngữ pháp EBNF — danh mục đầy đủ các ký hiệu và từ khoá
2. examples/corpus/ — kho ngôn ngữ với 292 tệp ví dụ bao phủ mọi từ khoá
3. examples/corpus/operatores/ — các ví dụ về toán tử và ký hiệu
4. Các điều răn — chín quy luật thiết kế bảo toàn các tín hiệu này
