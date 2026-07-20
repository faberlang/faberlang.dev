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
Faber 語言語料庫是公開的語言字典：每個關鍵字、運算子群組或語言型別表面各有一個頂層目錄。它是 `faber explain` 的開發來源，也是多目標編譯矩陣的主要輸入。

## 統計 {#stats}

- 292 個 `.fab` 範例檔案
- `index.toml` 中有 174 個註冊術語
- 約 135 個關鍵字與概念目錄

## 目錄結構 {#layout}

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

## 檔案格式 {#file-format}

每個 `.fab` 檔案都以描述該術語的 TOML 前置資料開頭：

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

## 分類 {#categories}

術語依分類組織：`function`、`control-flow`、`type`、`collection`、`transfer`、`annotation`、`iteration`、`destructuring`、`testing`、`cli`、`concept`、`operator-group`、`existing-home`。
