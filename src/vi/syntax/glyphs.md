+++
translation_kind = "translated"

title = "Glyphs and operators"
section = "syntax"
order = 10
sources = [
  "radix/README.md (Glyphs and Words)",
  "examples/corpus/operatores/",
  "examples/corpus/assignatio/",
  "radix/EBNF.md",
]


prose_hash = "sha256:54e4eb805a45db166418f1022bedfd033e2bca91ee9938895587a767c9856463"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber sử dụng các glyph, trong đó ký hiệu mang vai trò cấu trúc. Dưới đây là toàn bộ danh mục glyph nguồn được lexer nhận diện.

## Luồng giá trị {#value-flow}

| Glyph | Ý nghĩa |
|-------|---------|
| `←` | Liên kết, gán lại và biến đổi tại thời điểm chạy |
| `→` | Kiểu trả về của hàm |
| `⇥` | Lối thoát thay thế — kiểu kênh lỗi hoặc phục hồi chuyển đổi nội dòng |
| `∴` | Khớp nối đóng — nối thân hàm đóng với chữ ký (`(a, b) → T ∴ a + b`) |

## Hình dạng kiểu {#type-shape}

| Glyph | Ý nghĩa |
|-------|---------|
| `∷` | Gán kiểu tĩnh (ép kiểu tại thời điểm biên dịch) |
| `↦` | Chuyển đổi tại thời điểm chạy (phân tích hoặc ép kiểu có thể thất bại) |
| `∪` | Kiểu hợp nội dòng (`T ∪ nihil`) |

## So sánh {#comparison}

| Glyph | Ý nghĩa |
|-------|---------|
| `≡` `≠` | Bằng và khác chính xác |
| `<` `>` `≤` `≥` | Thứ tự |
| `≈` `≉` | Bằng nhau về giá trị số |

## Logic và thao tác bit {#logical-and-bitwise}

| Glyph | Ý nghĩa |
|-------|---------|
| `∧` `∨` `⊻` `¬` | Và, hoặc, xor, phủ định |
| `⇐` `⇒` | Dịch bit sang trái và sang phải |

## Cập nhật phép gán {#assignment-updates}

| Glyph | Ý nghĩa |
|-------|---------|
| `←` | Toán tử gán duy nhất trong biểu thức |
| `⊕` `⊖` | Câu lệnh tăng hoặc giảm hậu tố (chỉ áp dụng cho `numerus` có thể biến đổi) |

## Chuỗi tùy chọn và khẳng định khác `nihil` {#optional-chaining-and-non-null-assertion}

| Glyph | Ý nghĩa |
|-------|---------|
| `?` `?.` `?[` `?(` | Chuỗi tùy chọn |
| `!` `!.` `![` `!(` | Khẳng định giá trị không phải `nihil` |

## Khoảng {#ranges}

| Glyph | Ý nghĩa |
|-------|---------|
| `‥` | Điểm cuối khoảng không bao gồm |
| `…` | Điểm cuối khoảng có bao gồm |

## Dấu phân cách literal {#literal-delimiters}

| Glyph | Kiểu | Vai trò |
|-------|------|------|
| `'` | `ascii` | Token máy cố định |
| `"` | `textus` | Chuỗi một dòng |
| `«` `»` | `textus` | Chuỗi khối (dấu ngoặc kép kiểu guillemet) |
| `` ` `` | `forma` | Mẫu đã bắt giữ |
| `|` | `octeti` | Literal thập lục phân |
| `§` | lỗ mẫu | Phần giữ chỗ bên trong `"…"`, `«…»` và `` `…` `` |

## Dấu câu {#punctuation}

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
