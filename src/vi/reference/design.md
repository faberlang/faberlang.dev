+++
translation_kind = "translated"

title = "Design notes"
section = "reference"
order = 3
sources = [
  "radix/docs/design/README.md",
]
+++

## Commandments

*Chín quy tắc làm cho Faber mang đúng tinh thần Faber.*

Đây là những quy luật thiết kế định hình bản sắc của Faber. Cú pháp có thể
phát triển và tính năng có thể được bổ sung, nhưng các thay đổi phải giữ
được những nguyên tắc này. Một chương trình vi phạm chúng vẫn có thể là Faber
hợp lệ, nhưng không còn mang đúng tinh thần Faber.

Các điều răn này áp dụng ở mọi cấp độ — từ chính ngữ pháp cho đến cách đặt tên
API của thư viện chuẩn. Chúng là lý do người đọc có thể nhận ra mã nguồn Faber
chỉ qua một cái nhìn, bất kể từ khóa được hiển thị bằng ngôn ngữ tự nhiên nào
hay mã được biên dịch cho backend đích nào.

### I. Kiểu dữ liệu trước tên {#i-types-before-names}

Khai báo được đọc từ hình dạng đến liên kết. Kiểu dữ liệu đứng trước vì người
đọc cần biết *đây là loại thực thể nào* trước khi tên cho biết *đó là thực thể
nào*. Cách này phù hợp với những ngôn ngữ có trật tự ngữ pháp đi từ phạm trù
đến thể hiện — tiếng Trung, tiếng Hindi, tiếng Ả Rập — và tạo ra các khai báo
có hình thức nhất quán khi quét qua mã.

```text
# Type before name in every declaration
textus nomen
numerus aetas
functio salve(textus name) → textus
```

### II. Cơ học thay vì huyền bí {#ii-mechanical-over-magical}

Cùng một cấu trúc phải có cùng ý nghĩa ở mọi nơi. Nếu người đọc cần dựa vào
ngữ cảnh ở nơi xa để biết một ký hiệu thực hiện điều gì, thì cú pháp đó đáng
ngờ. Faber ưu tiên suy luận tường minh và cục bộ — vị trí khai báo phải mang
đủ thông tin để hiểu điều gì sẽ xảy ra tại vị trí sử dụng.

```faber
# The meaning of a call is determined by the function's signature,
# not by invisible trait resolution or implicit conversions.
functio duplica(numerus n) → numerus {
    redde n * 2
}
```

### III. Ký hiệu mang cấu trúc {#iii-glyphs-carry-structure}

Ý nghĩa cấu trúc và toán tử được biểu thị bằng ký hiệu, không phải bằng từ:
`←` cho liên kết, `→` cho kiểu trả về, `⇥` cho lối thoát khi có lỗi, `ergo` cho
thân nhánh rút gọn, `≡` cho phép bằng nhau, `∪` cho kiểu hợp. Ký hiệu mang
tính phổ quát — chúng không bao giờ được bản địa hóa và không bao giờ đổi
nghĩa giữa các cách hiển thị. Người đọc tiếng Thái và người đọc tiếng Pháp
nhìn thấy cùng một ký hiệu, ngay cả khi các từ khóa xung quanh khác nhau.

### IV. Latin mang hành vi {#iv-latin-carries-behaviour}

Từ ngữ dành cho khai báo, câu lệnh, vòng đời và ý định hành vi:
`functio`, `genus`, `fixum`, `varia`, `redde`, `cape`. Các từ này có thể được
liên kết thông qua các gói ngôn ngữ của người đọc — chúng là từ vựng, không
phải ngữ pháp. Việc chọn tiếng Latin không nhằm đề cao tiếng Latin; mục đích
là chọn *một* nguồn cổ điển nhất quán để mọi từ khóa cùng thuộc một văn phong
và không từ khóa nào được ưu tiên chỉ vì đó là ngôn ngữ dùng để viết phần cài
đặt.

### V. Biến cách mang thời gian và luồng thực thi {#v-conjugation-carries-time-and-flow}

Khi cùng một logic gốc có thể chạy đồng bộ, bất đồng bộ hoặc dưới dạng
generator, dạng biến cách của động từ phải biểu thị chế độ thực thi đó. Các
cặp liên quan đến quyền sở hữu — biến đổi so với sao chép và trả ra — dùng
những dạng liên quan của cùng một gốc từ. Đây là nguyên tắc morphologia. Thư
viện chuẩn (Norma) tuân theo quy ước này cho mọi tên phương thức:
`lege` (đọc đồng bộ) so với `leget` (đọc bất đồng bộ), `adde` (biến đổi tại
chỗ) so với `addita` (trả về một bản sao mới). Trình biên dịch không áp đặt
hay tự suy ra các dạng biến cách — đây là chính sách đặt tên, không phải tính
năng ngôn ngữ.

### VI. Một ký hiệu, một nhiệm vụ {#vi-one-sign-one-job}

Một ký hiệu hoặc từ khóa có thể có các bí danh hoàn toàn tương đương, nhưng
không nên mang những ý nghĩa không liên quan. Các bí danh phải quy về một
khái niệm chuẩn duy nhất. Đây là nguyên tắc dẫn đến sự phân tách giữa `←`
(liên kết thời gian chạy) và `=` (hình dạng trường mang tính cấu trúc) trong
Faber — hầu hết ngôn ngữ gộp cả hai vào `=`, nhưng cách nạp chồng đó che khuất
việc một dòng là thao tác luồng dữ liệu hay định nghĩa ở cấp kiểu.

```text
# ← is always runtime flow
fixum numerus count ← 0
count ← count + 1

# = is always structural shape inside Type { }
fixum _ p ← Point {
    x = 10,
    y = 20
}
```

### VII. Luồng thời gian chạy phải tường minh {#vii-runtime-flow-is-explicit}

Liên kết thời gian chạy, gán lại và biến đổi dùng `←`; định nghĩa cấu trúc
dùng `=`. Khi quét mã nguồn, người đọc có thể thấy ngay mọi thao tác luồng dữ
liệu: mỗi `←` là một sự kiện trong thời gian chạy. Không có sự mơ hồ cú pháp
về việc một `=` cụ thể có nghĩa là “lưu vào biến này” hay “định nghĩa trường
này”.

### VIII. Sự vắng mặt có kiểu {#viii-absence-is-typed}

Các kiểu giá trị có thể rỗng được viết dưới dạng hợp: `T ∪ nihil`. Các vị trí
khai báo tùy chọn dùng dấu đánh dấu sau tên: `sponte`. Đây là hai khái niệm
khác nhau — *một giá trị có thể vắng mặt* so với *một vị trí mà bên gọi có thể
bỏ qua* — và Faber giữ chúng tách biệt về mặt cú pháp thay vì gộp cả hai vào
`T?` hoặc `Option<T>`.

```text
# Absence in a value: T ∪ nihil
functio find(textus key) → numerus ∪ nihil

# Omission at declaration: sponte
functio connect(textus host, numerus port sponte) → vacuum
```

### IX. Trình biên dịch không đoán để che giấu thông tin còn thiếu {#ix-compiler-does-not-guess}

Thông tin kiểu còn thiếu là vấn đề phân tích cần được sửa từ thượng nguồn,
không phải chi tiết sinh mã cần được che đậy. Khi thông tin thực sự không có,
trình biên dịch không bao giờ âm thầm suy ra một kiểu mà lập trình viên chưa
cung cấp — nó báo phần thiếu và dừng lại. Đây là quy tắc giữ cho Faber trung
thực: nếu người đọc không thể xác định ý nghĩa của một ký hiệu từ mã nguồn
cục bộ, trình biên dịch cũng không được giả vờ rằng nó có thể.

### Mục đích {#purpose}

Các điều răn tồn tại để trả lời một câu hỏi xuất hiện trong mọi cuộc thảo
luận về thiết kế ngôn ngữ: “Thay đổi này có còn là Faber không?” Chúng là
phép kiểm tra các bất biến — không dựa trên danh sách tính năng, mà dựa trên
bản sắc. Một thay đổi vi phạm điều răn vẫn có thể là một ý tưởng tốt, nhưng
phải được nhìn nhận là sự rời khỏi bản sắc thiết kế của Faber, thay vì một
bổ sung thông thường.

Trong thực tế, các điều răn thường được dùng làm tiêu chí xem xét cho những đề
xuất cú pháp mới. Một đề xuất làm suy yếu “kiểu dữ liệu trước tên” bằng cách
thêm lựa chọn đặt tên trước, hoặc làm mờ “một ký hiệu, một nhiệm vụ” bằng cách
nạp chồng một ký hiệu, phải giải thích vì sao Faber nên uốn cong bản sắc của
mình cho tính năng đó.

## Design documents

Kho lưu trữ Radix chứa các tài liệu thiết kế có tính thẩm quyền về cách Faber hoạt động như một ngôn ngữ và trình biên dịch. Các tài liệu này nằm trong `radix/docs/design/`.

### Mục lục {#index}

| Phạm vi | Tệp |
|------|-------|
| Đích và hạ tầng hạ cấp | `target-capability-matrix.md`, `lowering-routes.md`, `semantic-ownership.md` |
| Kiểu và cú pháp rút gọn | `numeric-type-sugar.md`, `comparison-operators.md`, `annotation-sugar.md` |
| Nội tại bộ sưu tập | `lista-intrinsics.md`, `tabula-intrinsics.md`, `tensor-intrinsics.md`, `numerus-intrinsics.md`, `fractus-intrinsics.md`, `textus-intrinsics.md`, `intervallum-intrinsics.md`, `instans-intrinsics.md`, `copia-intrinsics.md` |
| Chuyển đổi | `conversio-valor.md`, `failable-conversio.md` |
| Frame và hiệu ứng | `frame-stream-types.md`, `host-provider-gateway.md` |
| Reader và định dạng | `reader-locale.md`, `faber-canonical-surface.md` |
| Hệ thống / AIR | `air-dialect.md`, `aiml-foundation.md`, `systems-shaped-values.md` |
| Bề mặt công cụ | `faber-scripting.md` |
| Khoản nợ đặt tên | `mixed-case-naming-debt.md` |

### Tài liệu thiết kế thư viện chuẩn {#stdlib-design-docs}

Thư mục `radix/docs/stdlib/` chứa:

| Tài liệu | Vai trò |
|-----|------|
| `morphologia.md` | Chính sách chia dạng cho mọi tên phương thức của thư viện chuẩn |
| `tensor-methods.md` | Tài liệu tham khảo phương thức nhận `tensor` |
| `chorda-methods.md` | Tài liệu tham khảo phương thức `chorda` (văn bản) |
| `mathesis-methods.md` | Tài liệu tham khảo phương thức toán học |
| `tempus-methods.md` | Tài liệu tham khảo phương thức thời gian |
| `stdlib-mechanical-verbs.md` | Chính sách bộ ba `pange`/`solve`/`tempta` |

## History

### Nguồn gốc {#origins}

Cam kết đầu tiên cho trình biên dịch Radix được thực hiện vào **ngày 20 tháng 12 năm 2025**
dưới dạng một dự án Bun + TypeScript với duy nhất tệp `docs/decisions.md`. Cam kết
thứ hai đã hệ thống hóa năm Hồ sơ Quyết định Kiến trúc vẫn định hình ngôn ngữ cho đến
ngày nay.

**ADR-003**, có tiêu đề "Đuôi cách mang ý nghĩa ngữ nghĩa", ngay từ đầu đã xác lập
rằng hình thái học Latin sẽ không chỉ là một lớp vỏ từ khóa — trình biên dịch sẽ hiểu
sự biến cách và chia động từ để suy luận ý định của chương trình. Các ánh xạ cách ban
đầu là:

```text
Nominative  (subject)       →  return value, caller
Accusative  (direct object)  →  primary argument
Dative      (indirect obj.)  →  recipient, callback, destination
Genitive    (possession)     →  property access, "of" relationships
Ablative    (instrument)     →  dependencies, context, "using X"
```

Tài liệu đó cũng ghi chú: *"Chia động từ là một câu hỏi tiếp nối tự nhiên
(thì tương lai → bất đồng bộ?)."* Hạt giống này đã phát triển thành quy ước đặt tên
**morphologia** hiện đại, trong đó thư viện chuẩn sử dụng các dạng động từ Latin đã
được chia để biểu thị chạy đồng bộ hay bất đồng bộ, cũng như biến đổi hay sao chép dữ
liệu ra — mà không yêu cầu bản thân trình biên dịch phải hiểu ngữ pháp Latin.

Dự án bắt đầu bằng TypeScript, sau đó được viết lại bằng Rust, và ngữ pháp đã được
đóng băng cho dòng 1.x với edition 2026. Năm ADR ban đầu (phần mở rộng tệp `.fab`,
gợi ý lỗi, đuôi cách, trình phân tích cú pháp đệ quy đi xuống, AST tùy chỉnh) vẫn có
thể xem trong lịch sử git.

### Các bản phát hành {#releases}

Các gói CLI dựng sẵn — bản phát hành Faber hiện tại ở trên cùng, sau đó là mọi thẻ
và tệp nhị phân đã được phát hành từ [faberlang/releases](https://github.com/faberlang/releases):

- **[Các bản phát hành](/releases/)** — liên kết tải xuống và danh mục lịch sử
- **[Cài đặt và tải xuống](/start/install.html)** — thiết lập PATH và chạy `faber check` lần đầu
