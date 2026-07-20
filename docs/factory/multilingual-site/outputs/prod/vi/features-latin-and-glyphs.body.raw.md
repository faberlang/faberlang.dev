*Ba lựa chọn tín hiệu giúp nhận ra mã nguồn Faber ngay từ cái nhìn đầu tiên.*

Faber đưa ra ba lựa chọn tín hiệu có chủ đích. Chúng phối hợp để tạo ra mã nguồn có hình thái ngữ pháp ổn định. Người đọc có thể nhận ra vai trò ngữ nghĩa của từng cấu trúc trước khi biết mã sẽ được biên dịch sang phần phụ trợ đích nào.

## Ba tín hiệu {#three}

| Tín hiệu | Ví dụ | Vai trò |
|--------|----------|------|
| Khai báo đặt kiểu trước | `textus nomen`, `numerus aetas` | Hình thức hướng về phép ràng buộc — kiểu, rồi đến tên. |
| Từ chỉ hành vi bằng tiếng Latinh | `functio`, `genus`, `si`, `redde`, `fixum` | Khai báo, câu lệnh, vòng đời và ý định hành vi. |
| Ký hiệu cấu trúc | `← → ∴ ≡ ∪ ⇥` | Luồng giá trị, luồng kiểu và các điểm nối cấu trúc — mang tính phổ quát, không bao giờ bản địa hoá. |

Ba tín hiệu này được thiết kế để củng cố lẫn nhau. Người đọc biết Faber ở một locale có thể đọc nó trong mọi locale khác vì các ký hiệu và cấu trúc không bao giờ thay đổi. Người đọc biết backend Rust vẫn có thể nhận ra mã nguồn Faber vì các từ khoá Latinh và thứ tự kiểu-trước tạo nên một diện mạo riêng biệt.

## Khai báo đặt kiểu trước {#type-first}

Faber đặt kiểu trước tên trong mọi khai báo. Đây là điều ngược lại với cú pháp phổ biến của họ C, và đó là chủ ý:

| Cấu trúc | Thói quen của họ C | Faber |
|-----------|----------------|-------|
| Biến | `int count = 0` | `numerus count ← 0` |
| Hàm | `fn greet(name: String) → String` | `functio salve(textus nomen) → textus` |
| Tham số | `(String name)` | `(textus nomen)` |

Khai báo đặt kiểu trước khiến hình dạng của dữ liệu là điều đầu tiên người đọc nhìn thấy. Cách này tự nhiên phù hợp với các ngôn ngữ đọc từ trái sang phải theo độ rộng ngữ nghĩa — khai báo trong tiếng Trung, Hindi và Ả Rập cũng theo cùng thứ tự.

<<<FENCE 0>>>

## Từ vựng hành vi bằng tiếng Latinh {#latin}

Faber sử dụng các từ Latinh cho mọi cấu trúc có hình thái hành vi hoặc ngữ pháp. Từ vựng này nhỏ và đều đặn, được lấy từ một nguồn cổ điển duy nhất thay vì các nguồn gốc từ pha trộn của hầu hết ngôn ngữ lập trình.

### Khai báo {#declarations}

| Từ khoá | Vai trò | Tương đương gần đúng |
|---------|------|------------------------|
| `functio` | Khai báo một hàm hoặc phương thức có tên | `fn`, `def`, `function` |
| `genus` | Khai báo một kiểu cụ thể có các trường | `class`, `struct` |
| `implendum` | Khai báo một hợp đồng hành vi | `interface`, `trait` |
| `typus` | Khai báo bí danh kiểu | `typedef`, `type` |
| `discretio` | Khai báo một hợp kiểu có thẻ | `enum`, `sum type` |

### Ràng buộc và truyền giá trị {#bindings-and-transfer}

| Từ khoá | Vai trò | Tương đương gần đúng |
|---------|------|------------------------|
| `fixum` | Ràng buộc bất biến (chỉ ghi một lần) | `let`, `const` |
| `varia` | Ràng buộc khả biến | `let mut`, `var` |
| `sit` | Ràng buộc bất biến suy luận ngắn gọn | `let` (suy luận) |
| `redde` | Trả về một giá trị từ hàm | `return` |
| `iace` | Ném lỗi qua kênh lỗi | `throw`, `raise` |
| `mori` | Trì hoãn — hành vi chưa thể biểu đạt | `unimplemented!`, `todo` |

### Luồng điều khiển {#control-flow}

| Từ khoá | Vai trò | Tương đương gần đúng |
|---------|------|------------------------|
| `si` | Nhánh điều kiện | `if` |
| `sin` | Nhánh else-if | `else if` |
| `secus` | Nhánh else | `else` |
| `dum` | Vòng lặp while | `while` |
| `itera` | Lặp qua các giá trị, khoá hoặc khoảng | `for` |
| `elige` | Đối sánh mẫu (nhánh đầu tiên thắng) | `match`, `switch` |
| `fac` | Khối thử với khôi phục lỗi | `try`, `do` |
| `cape` | Trình xử lý lỗi cho fac | `catch` |

> Từ vựng Latinh **có thể ràng buộc** — nó được phát hành cùng gói chuẩn nhưng có thể ánh xạ lại thông qua locale người đọc. Lập trình viên Thái thấy `ถ้า` thay cho `si`; lập trình viên Trung Quốc thấy `函数` thay cho `functio`. Từ vựng không có đặc quyền; chỉ ngữ pháp là bất biến.

## Ký hiệu cấu trúc {#glyphs}

Trong khi từ vựng hành vi sử dụng các từ Latinh, ý nghĩa cấu trúc sử dụng các ký hiệu phổ quát. Các ký hiệu này không bao giờ được bản địa hoá và không bao giờ thay đổi ý nghĩa giữa các bản kết xuất. Chúng là điểm neo trực quan giúp nhận ra mã nguồn Faber bất kể các từ khoá được hiển thị bằng ngôn ngữ nào.

### Luồng giá trị {#value-flow}

| Ký hiệu | Ý nghĩa |
|-------|---------|
| `←` | Ràng buộc thời gian chạy, gán lại và biến đổi — toán tử gán duy nhất |
| `→` | Khai báo kiểu trả về của hàm |
| `⇥` | Lối thoát thay thế: kiểu kênh lỗi hoặc khôi phục chuyển đổi nội dòng |
| `∴` | Thân lệnh do đó rút gọn — giới thiệu thân nhánh chỉ có một câu lệnh |

### Hình dạng kiểu {#type-shape}

| Ký hiệu | Ý nghĩa |
|-------|---------|
| `∷` | Ghi rõ kiểu tĩnh — khẳng định tại thời điểm biên dịch về kiểu của một giá trị |
| `↦` | Chuyển đổi thời gian chạy — phân tích hoặc cưỡng chế kiểu có thể thất bại |
| `∪` | Kiểu hợp nội dòng — nối hai kiểu (như `T ∪ nihil`) |

### Quy ước ràng buộc rất quan trọng {#the-binding-convention-matters}

Một lựa chọn ký hiệu đáng được chú ý đặc biệt vì đây là điểm gây nhầm lẫn phổ biến nhất đối với người đọc mới:

| Ký hiệu | Vai trò | Dùng cho |
|-------|------|---------|
| `←` | **Luồng thời gian chạy** | Ràng buộc ban đầu, gán lại và biến đổi tại thời điểm thực thi |
| `=` | **Hình dạng cấu trúc** | Tên trường bên trong literal và siêu dữ liệu khai báo — không dùng để lưu tại thời gian chạy |

Hầu hết ngôn ngữ dùng `=` cho cả việc “định nghĩa trường này trong một kiểu” và “đặt một giá trị thời gian chạy vào biến này”. Faber tách hai nhiệm vụ đó. Mọi `←` đều là luồng dữ liệu đang hoạt động; mọi `=` bên trong `Type { … }` là bố cục trường của genus.

<<<FENCE 1>>>

## So với các ngôn ngữ phổ biến {#compare}

Bảng dưới đây cho thấy các mẫu lập trình phổ biến ánh xạ vào hệ thống ba tín hiệu của Faber như thế nào. Cột Faber sử dụng một ký hiệu hoặc từ khoá khác nhau cho từng nhiệm vụ ngữ nghĩa riêng biệt — không chồng lấp ý nghĩa.

| Nhiệm vụ ngữ nghĩa | Phổ biến trong các ngôn ngữ khác | Faber |
|--------------|---------------------------|-------|
| Khai báo kiểu tham số | `name: String` | `textus nomen` |
| Kiểu trả về | `→ String`, `: String` | `→` `textus` |
| Gán thời gian chạy | `x = value` | `←` |
| Kiểm tra bằng nhau | `==` | `≡` |
| Khả năng rỗng | `T?`, `Option<T>` | `T ∪ nihil` |
| Nhánh + một câu lệnh | `if (cond) return x` | `si cond ergo redde x` |
| Ép kiểu | `(T)value`, `value as T` | `value ∷ T` |
| Chuyển đổi (có thể thất bại) | `try_into()` | `value ↦ T` |

## Tài liệu tham khảo {#references}

1. Ngữ pháp EBNF — danh mục đầy đủ các ký hiệu và từ khoá
2. examples/corpus/ — corpus ngôn ngữ với 292 tệp ví dụ trên toàn bộ các từ khoá
3. examples/corpus/operatores/ — các ví dụ về toán tử và ký hiệu
4. Các điều răn — chín quy luật thiết kế bảo toàn các tín hiệu này
