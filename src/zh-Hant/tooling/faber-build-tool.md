+++
translation_kind = "translated"

title = "Faber build tool"
section = "tooling"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
]


prose_hash = "sha256:5d8304941413ba003c019f0b1c43cd19e99ad0f25fa9b7a4ffadbc1327e8dfb6"
code_hash = "sha256:7657ec817fefbfb88c20a7b862970c668ebe2835de88c17eda584340fd2d6654"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
`faber` CLI 是建置、檢查、執行、格式化與測試 Faber 原始碼的主要入口。它將 Radix 編譯器包裝成符合人體工學的開發者工具。

## 核心指令 {#core-commands}

| 指令 | 用途 |
|---|---|
| `faber build <path>` | 將套件編譯至目標後端（預設：Rust） |
| `faber check <path>` | 進行型別檢查，但不輸出程式碼 |
| `faber run <path>` | 建置並執行 |
| `faber test <path>` | 執行 proba 測試套件 |
| `faber format <path>` | 套用標準格式 |
| `faber explain <code>` | 解釋診斷碼 |
| `faber emit <path>` | 將原始碼輸出至目標介面 |

## 建置套件 {#building}

```text
faber build my-package/ -t rust
```

`-t` 旗標選取程式碼產生目標。支援的目標包括 `rust`（預設）、`wasm`、`typescript` 與 `go`。

## 不輸出程式碼的檢查 {#checking}

```text
faber check my-package/
```

執行完整的前端流程（詞法分析 → 剖析 → 型別檢查 → MIR 降階），但不產生輸出成品。在 CI 與編輯器整合中使用此指令。

## 執行測試 {#testing-command}

```text
faber test my-package/
```

將套件中的所有 `probandum` 套件編譯為 Rust `#[test]` 函式，並透過 Cargo 執行。內嵌測試與原始碼並存，不需要額外的測試二進位檔。

## 格式化 {#formatting}

```text
faber format my-package/
```

套用標準的 Faber 格式化工具。格式化工具會強制採用一致的版面配置：每行一個宣告、標準間距，以及統一的關鍵字介面。

## 解釋診斷 {#explaining}

```text
faber explain SEM001
```

列印編譯器可能產生的任何診斷碼之人類可讀說明。這有助於瞭解錯誤的意義與修正方式。
