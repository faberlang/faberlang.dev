+++
translation_kind = "translated"

title = "Language corpus"
section = "ecosystem"
order = 6
sources = [
  "examples/corpus/ (292 .fab files, 174 registry terms, index.toml)",
  "examples/corpus/README.md",
]


prose_hash = "sha256:6dab4295fafeea620e65bd30edcc6c810bc3f0b11cb8681aae63f79ecbe2be63"
code_hash = "sha256:fbdcbf8ce9cd3fdcb367022a7df1cdbd74fd62244d662a6a85229773e4910739"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
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
