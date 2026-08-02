+++
translation_kind = "translated"

title = "The language corpus"
section = "libraries"
order = 3
sources = [
  "examples/corpus/ (292 .fab files, 174 registry terms, index.toml)",
  "examples/corpus/README.md",
]
+++

Kho ngữ liệu ngôn ngữ Faber là từ điển ngôn ngữ công khai: mỗi từ khóa, nhóm toán tử hoặc bề mặt kiểu ngôn ngữ có một thư mục cấp cao nhất riêng. Đây là nguồn phát triển cho `faber explain` và đầu vào chính cho các ma trận biên dịch đa mục tiêu.

## Thống kê {#stats}

- 292 tệp exemplar `.fab`
- 174 thuật ngữ trong registry `index.toml`
- Khoảng 135 thư mục từ khóa và khái niệm

## Bố cục {#layout}

```
corpus/
  functio/           # function keyword exemplars
  genus/             # record type exemplars
  si/                # conditional branch exemplars
  itera/             # iteration exemplars
  lista/ tabula/     # collection type exemplars
  tensor/ sparsa/    # tensor exemplars
  ad/                # capability call exemplars
  operatores/        # glyph / operator groups
  ...
  index.toml         # generated explain manifest
```

## Định dạng tệp {#file-format}

Mỗi tệp `.fab` bắt đầu bằng phần frontmatter TOML mô tả thuật ngữ:

```toml
+++
term = "functio"
kind = "keyword"
category = "function"
canonical = true
summary = "Declares a named function or method."
syntax = "functio <name>(<params>) [modifiers] [→ <type>] [⇥ <error-type>] <block>"
aliases = ["function"]
related = ["→", "⇥", "redde", "sponte"]
+++

functio saluta() {
    nota "Salve, Mundus!"
}
```

## Cách sử dụng {#usage}

```bash
faber explain functio       # show keyword reference
faber explain ≡             # show glyph reference
faber explain --search query # search across corpus
faber explain --list         # list all terms
```

## Danh mục {#categories}

Các thuật ngữ được sắp xếp theo danh mục: `function`, `control-flow`, `type`,
`collection`, `transfer`, `annotation`, `iteration`, `destructuring`,
`testing`, `cli`, `concept`, `operator-group`, `existing-home`.
