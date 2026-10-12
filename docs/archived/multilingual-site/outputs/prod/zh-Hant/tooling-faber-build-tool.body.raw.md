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

<<<FENCE 0>>>

`-t` 旗標選取程式碼產生目標。支援的目標包括 `rust`（預設）、`wasm`、`typescript` 與 `go`。

## 不輸出程式碼的檢查 {#checking}

<<<FENCE 1>>>

執行完整的前端流程（詞法分析 → 剖析 → 型別檢查 → MIR 降階），但不產生輸出成品。在 CI 與編輯器整合中使用此指令。

## 執行測試 {#testing-command}

<<<FENCE 2>>>

將套件中的所有 `probandum` 套件編譯為 Rust `#[test]` 函式，並透過 Cargo 執行。內嵌測試與原始碼並存，不需要額外的測試二進位檔。

## 格式化 {#formatting}

<<<FENCE 3>>>

套用標準的 Faber 格式化工具。格式化工具會強制採用一致的版面配置：每行一個宣告、標準間距，以及統一的關鍵字介面。

## 解釋診斷 {#explaining}

<<<FENCE 4>>>

列印編譯器可能產生的任何診斷碼之人類可讀說明。這有助於瞭解錯誤的意義與修正方式。
