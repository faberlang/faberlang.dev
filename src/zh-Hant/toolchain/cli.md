+++
translation_kind = "translated"

title = "The faber CLI"
section = "toolchain"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
  "radix/docs/design/faber-scripting.md",
]
+++

## Faber build tool

`faber` CLI 是建置、檢查、執行、格式化與測試 Faber 原始碼的主要入口。它將 Radix 編譯器包裝成符合人體工學的開發者工具。

### 核心指令 {#core-commands}

| 指令 | 用途 |
|---|---|
| `faber build <path>` | 將套件編譯至目標後端（預設：Rust） |
| `faber check <path>` | 進行型別檢查，但不輸出程式碼 |
| `faber run <path>` | 建置並執行 |
| `faber test <path>` | 執行 proba 測試套件 |
| `faber format <path>` | 套用標準格式 |
| `faber explain <code>` | 解釋診斷碼 |
| `faber emit <path>` | 將原始碼輸出至目標介面 |

### 建置套件 {#building}

```text
faber build my-package/ -t rust
```

`-t` 旗標選取程式碼產生目標。支援的目標包括 `rust`（預設）、`wasm`、`typescript` 與 `go`。

### 不輸出程式碼的檢查 {#checking}

```text
faber check my-package/
```

執行完整的前端流程（詞法分析 → 剖析 → 型別檢查 → MIR 降階），但不產生輸出成品。在 CI 與編輯器整合中使用此指令。

### 執行測試 {#testing-command}

```text
faber test my-package/
```

將套件中的所有 `probandum` 套件編譯為 Rust `#[test]` 函式，並透過 Cargo 執行。內嵌測試與原始碼並存，不需要額外的測試二進位檔。

### 格式化 {#formatting}

```text
faber format my-package/
```

套用標準的 Faber 格式化工具。格式化工具會強制採用一致的版面配置：每行一個宣告、標準間距，以及統一的關鍵字介面。

### 解釋診斷 {#explaining}

```text
faber explain SEM001
```

列印編譯器可能產生的任何診斷碼之人類可讀說明。這有助於瞭解錯誤的意義與修正方式。

## In-process scripting

除了編譯至 Rust 的路徑之外，Faber 也支援透過 MIR 步進器在程序內執行直譯。

### 使用方式 {#usage}

```bash
faber run --interpret script.fab
```

這會在編譯器完成正常的前半段流程（從剖析到型別檢查，再到 MIR 降級）後，在程序內執行 Faber 原始碼，而不會呼叫 `rustc` 或產生建置程序。

### 運作方式 {#how-it-works}

編譯器會產生已分析的 HIR、經驗證的 MIR，以及已解析的執行階段內建函式表。MIR 步進器會將 MIR 區塊直接分派至主機，略過 wasm 輸出與具現化的往返流程：

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck
                                                      ↓
                                                 MIR lowering
                                                      ↓
                                              MIR stepper + Host
```

### 延遲 {#latency}

腳本路徑會執行與編譯路徑相同的線性前端流程，另外加上與腳本實際執行內容成正比的步進器耗時：

| 階段 | 成本 |
|-------|------|
| 前端（100 行腳本） | 約 0.6 毫秒 |
| MIR 步進 | 與已執行的陳述式數量成正比 |

步進器絕不會呼叫 `rustc` 或產生程序，因此啟動速度足以讓人感覺像執行 shell 腳本。

### 限制 {#limitations}

- MIR 步進器不支援編譯路徑所支援的所有主機 I/O 路徑 — 部分 `norma:*` 包裝器仍然僅能透過編譯使用
- 步進器是原生 MIR 的診斷／參考執行器，不是供已部署應用程式使用的正式執行階段
- 透過 Cargo 進行套件編譯仍是主要產品路徑
