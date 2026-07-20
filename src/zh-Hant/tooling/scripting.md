+++
translation_kind = "translated"

title = "In-process scripting"
section = "tooling"
order = 3
sources = [
  "radix/docs/design/faber-scripting.md",
]


prose_hash = "sha256:0a78a5f2ec00dd6ec6d024631c78979f8b92ea90caed72c43a20785002145e14"
code_hash = "sha256:49d88b2d9c376e533ab8e397f53f2c4f96d2aeb99771c4ca89350b6fe05bb93d"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
除了編譯至 Rust 的路徑之外，Faber 也支援透過 MIR 步進器在程序內執行直譯。

## 使用方式 {#usage}

```bash
faber run --interpret script.fab
```

這會在編譯器完成正常的前半段流程（從剖析到型別檢查，再到 MIR 降級）後，在程序內執行 Faber 原始碼，而不會呼叫 `rustc` 或產生建置程序。

## 運作方式 {#how-it-works}

編譯器會產生已分析的 HIR、經驗證的 MIR，以及已解析的執行階段內建函式表。MIR 步進器會將 MIR 區塊直接分派至主機，略過 wasm 輸出與具現化的往返流程：

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck
                                                      ↓
                                                 MIR lowering
                                                      ↓
                                              MIR stepper + Host
```

## 延遲 {#latency}

腳本路徑會執行與編譯路徑相同的線性前端流程，另外加上與腳本實際執行內容成正比的步進器耗時：

| 階段 | 成本 |
|-------|------|
| 前端（100 行腳本） | 約 0.6 毫秒 |
| MIR 步進 | 與已執行的陳述式數量成正比 |

步進器絕不會呼叫 `rustc` 或產生程序，因此啟動速度足以讓人感覺像執行 shell 腳本。

## 限制 {#limitations}

- MIR 步進器不支援編譯路徑所支援的所有主機 I/O 路徑 — 部分 `norma:*` 包裝器仍然僅能透過編譯使用
- 步進器是原生 MIR 的診斷／參考執行器，不是供已部署應用程式使用的正式執行階段
- 透過 Cargo 進行套件編譯仍是主要產品路徑
