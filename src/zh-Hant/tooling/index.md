+++
translation_kind = "translated"

title = "Tooling and compiler"
section = "tooling"
order = 0
sources = []


prose_hash = "sha256:23ae82d266e39d96b2059d2b97d4b03c5e6efcba389ab0bfb621d32a2e7caad2"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
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
