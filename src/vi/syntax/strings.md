+++
translation_kind = "translated"

title = "String and template literals"
section = "syntax"
order = 8
sources = [
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
]


prose_hash = "sha256:61bc93552e4a6ccc2a3a51453c146c31eee8331c6e82a3b17de5bc70f4ce24b0"
code_hash = "sha256:e7cba6e75a702466f92ecdbaa2c9d777b027a09a7f1b0414387cc746376d3075"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
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

## Chuỗi dạng khối {#block-strings}

Các khối nhiều dòng sử dụng dấu ngoặc kép kiểu guillemet `«…»`:

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

## Template được thu giữ (forma) {#captured-templates}

Template dùng dấu backtick thu giữ văn bản và tham số mà không thực hiện
việc kết xuất.
Phù hợp cho payload SQL/URL có liên kết tham số:

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

## JSON nội tuyến {#inline-json}

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
