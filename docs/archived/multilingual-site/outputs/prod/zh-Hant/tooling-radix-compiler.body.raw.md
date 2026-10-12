Radix 是 Faber 編譯器。它是一個私有 crate（`radix/`），負責實作從原始文字到目標後端的完整編譯流程。

## 流程 {#pipeline}

Radix 會將 Faber 原始碼降低為三種中間表示：

1. **HIR**（高階 IR）— 語意核心。讀者語系整合、型別檢查，以及直接以 HIR 為基礎的後端都在此階段運作。
2. **MIR**（中階 IR）— 以執行為形狀的 IR。這是語意所有權邊界，借用分析與效果分析會在此執行。
3. **AIR**（自動微分 IR）— 用於自動微分與融合的純函數轉換，供 GPU 目標通道使用。

## 目標通道 {#target-lanes}

| 通道 | IR | 輸出 | 狀態 |
|---|---|---|---|
| CPU 執行階段 | MIR | FMIR（Rust 執行階段） | 已發布 |
| LLVM | MIR | LLVM 文字 | 實驗性 |
| WASM | MIR | WebAssembly 文字 | 實驗性 |
| TypeScript | HIR | TypeScript 原始碼 | 實驗性 |
| Go | HIR | Go 原始碼 | 實驗性 |
| GPU/WGSL | AIR | 透過 WGPU 產生 WGSL | 實驗性 |

## 架構 {#architecture}

Radix 採用文字發射方式，而不是嵌入 LLVM。目標後端會以各自的語言產生文字，之後再由目標語言本身的工具鏈進行編譯。這讓編譯器保持自給自足，也使目標輸出易於人類閱讀。

## 診斷 {#diagnostics}

Radix 會產生帶有穩定識別碼的結構化診斷碼：

- `LEX0xx` — 詞法分析錯誤
- `PARSE0xx` — 剖析錯誤
- `SEM0xx` — 語意分析錯誤
- `DEFER0xx` — 延後功能（語法有效，但尚未實作）

每個診斷都可以透過 `faber explain <code>` 取得說明。
