Faber 工具鏈涵蓋三項工具：用於建置與測試的 `faber` CLI、用於程式碼生成的 Radix 編譯器，以及用於相依性解析的 Cista 套件管理器。

## Faber 建置工具 {#faber-cli}

主要的開發者介面。透過單一指令完成建置、檢查、執行、測試、格式化與說明。[深入瞭解 →](/tooling/faber-build-tool.html)

## Radix 編譯器 {#radix}

編譯器後端。將 Faber 原始碼經由 HIR → MIR → AIR 降階至多個目標通道。[深入瞭解 →](/tooling/radix-compiler.html)

## Cista 套件管理器 {#cista}

套件解析與公開套件儲存庫。管理 `faber.toml` 資訊清單與相依性鎖定檔。[深入瞭解 →](/tooling/cista-package-manager.html)

## 程式碼生成目標 {#codegen-targets}

Faber 可編譯至 Rust（預設）、WASM、TypeScript、Go 與 GPU/WGSL。每個目標通道都有自己的 IR 路徑與執行階段繫結。[深入瞭解 →](/tooling/codegen-targets.html)

## 效能 {#performance}

跨目標通道測量的編譯與執行效能。[深入瞭解 →](/tooling/performance.html)

## 指令碼編寫 {#scripting}

搭配 `faber run` 指令將 Faber 作為指令碼語言使用。[深入瞭解 →](/tooling/scripting.html)
