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
Faber 语言语料库是公开的语言词典：每个关键字、运算符组或语言类型表面各占一个顶级目录。它是 `faber explain` 的开发来源，也是多目标编译矩阵的主要输入。

## 统计 {#stats}

- 292 个 `.fab` 示例文件
- `index.toml` 中有 174 个注册条目
- 约 135 个关键字和概念目录

## 布局 {#layout}

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

## 文件格式 {#file-format}

每个 `.fab` 文件以 TOML frontmatter 开头，用于描述该条目：

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

## 用法 {#usage}

```bash
faber explain functio       # show keyword reference
faber explain ≡             # show glyph reference
faber explain --search query # search across corpus
faber explain --list         # list all terms
```

## 类别 {#categories}

条目按类别组织：`function`、`control-flow`、`type`、`collection`、`transfer`、`annotation`、`iteration`、`destructuring`、`testing`、`cli`、`concept`、`operator-group`、`existing-home`。
