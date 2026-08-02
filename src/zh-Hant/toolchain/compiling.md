+++
translation_kind = "translated"

title = "Compiling and targets"
section = "toolchain"
order = 2
sources = [
  "radix/docs/design/target-capability-matrix.md (40 KB)",
  "radix/README.md (Codegen Targets and HIR/MIR Split)",
  "faber targets CLI output",
  "radix/README.md (Compiler Performance section)",
]
+++

## Codegen targets

Faber 只有一種語言，卻有許多編譯契約。並非每項功能都必須降階至每個目標。本頁說明各目標支援、消除、警告或拒絕哪些功能。

### 政策動詞 {#policy-verbs}

| 動詞 | 意義 |
|------|---------|
| **Support** | 以預期語意進行降階 |
| **Erase** | 通過型別檢查；程式碼生成會捨棄目標特定語意 |
| **Warn** | 合法的 Faber；在該目標上沒有作用，或行為有所降級 |
| **Reject** | 檢查或輸出會失敗，並提供明確診斷 |
| **Defer** | 可解析／繫結；尚未為任何目標實作降階 |
| **Limited** | 具有明確子集閘門的穩定契約 |

### 目標表 {#target-table}

| 目標 | 途徑 | 建置 | 執行 | 套件 | 政策 |
|--------|------|-------|-----|---------|--------|
| `rust` | HIR | yes | yes | yes | **Support** |
| `fmir-text` | MIR | yes | yes | yes | **Support** |
| `fmir` | MIR | yes | yes | yes | **Support** |
| `fmir-bin` | MIR | yes | yes | yes | **Support** |
| `faber` | HIR | yes | no | no | **Support** |
| `ts` | HIR | yes | no | no | **Probe** |
| `go` | HIR | yes | no | no | **Erase** |
| `wasm` | MIR | yes | no | no | **Limited** |
| `wasm-text` | MIR | yes | no | no | **Limited** |
| `llvm-text` | MIR | yes | no | no | **Limited** |
| `metal-text` | MIR | yes | no | no | **Limited** |
| `wgsl-text` | MIR | yes | no | no | **Limited** |
| `sexp` | MIR | yes | no | no | **Limited** |

### 管線路由 {#pipeline-routing}

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck → Analysis
                                                              ↓
                                    ┌─────────────────────────┴──────────┐
                                    │                                    │
                              HIR backends                        MIR backends
                                    │                                    │
            Rust · Faber · TS · Go            fmir · wasm · llvm · metal · wgsl · sexp
```

### 應用程式途徑（HIR） {#application-lane-hir}

| 目標 | 實測下限 |
|--------|---------------|
| Rust | 生產路徑。借用模式、CLI 生成、可失敗的 Result 降階。 |
| Faber | 標準來源檢視／往返轉換。不是執行後端。 |
| TypeScript | 已分析 288/318 · 型別檢查有效 268/318 · 可執行 262/318 |
| Go | 通過 146/216。借用模式會被消除；`ad` 會被拒絕。 |

### 系統途徑（MIR） {#systems-lane-mir}

| 目標 | 實測下限 |
|--------|---------------|
| fmir* | 套件 MIR 映像；執行器證明來源獨立性。 |
| wasm | 已輸出 200/289 · 驗證通過 195/289 · 樣板主機可執行 171/289 |
| llvm-text | 已輸出 249/289 · 驗證器有效 232/289 · 可執行 65/289 |
| metal-text | 裝置安全的核心子集；88 項聚焦測試。活動已暫停。 |
| wgsl-text | 使用 naga 30.x 驗證。87 項聚焦測試。反射旁載檔。 |
| sexp | 已輸出 193 · Racket 編譯 190 · Racket 執行 190。驗證目標。 |

如需即時能力旗標，請執行 `faber targets`。

## Compilation lanes

Faber 具備單一共用前端：詞法分析、剖析、型別檢查，接著依據目標的需求分流至多條降低路徑。中間表示形成一條管線：原始碼先分析為 HIR，可選擇再降低為 MIR，也可選擇繞道經過 AIR，最後才產生輸出。每種 IR 都有明確用途，而每個目標都會從符合其需求的 IR 取用資料。

### 管線總覽 {#overview}

```text
Source (.fab)  →  Lex  →  Parse  →  Collect  →  Resolve  →  Lower  →  Typecheck  →  Analysis
                                                              │
                                                    HIR (semantic core)
                                                    ┌─────┴─────┐
                                                    │           │
                                              Reader locale    MIR lowering
                                              (input/output)    │
                                                                │
                                                      ┌─────────┴─────────┐
                                                      │                   │
                                                CPU lanes           GPU lanes
                                                      │                   │
                                            ┌────┬────┼────┬────┐     ┌───┴───┐
                                            │    │    │    │    │     │       │
                                          FMIR LLVM WASM  TS  Go   WGSL   Metal
                                                                          (hold)
```

相同的前端服務於所有目標。語意分析產生 HIR 後，編譯器會依據目標選擇路徑：

- **HIR 直出** — 直接從具型別的 HIR 產生輸出，適用於語言形狀的後端（Rust、Faber、TypeScript、Go）
- **HIR → MIR** — 降低為以執行為形狀的 MIR，再為系統與低階目標產生輸出
- **HIR → MIR → AIR → MIR** — 繞道經過純函數式 AIR，以進行自動微分與融合轉換，然後重新接回 MIR

### HIR — 高階中間表示 {#hir}

HIR 是真實來源。它是一種具型別、以語言為形狀的 IR，保留宣告、型別資訊與結構關係。每個 Faber 程式，不論原始語系或目標目的地為何，都會經過此表示。

#### 讀者語系整合 {#reader-locale-integration}

讀者語系透過 HIR 運作。以泰文關鍵字撰寫的 Faber 原始檔，會被剖析並降低為與等價拉丁文原始碼相同的 HIR。語系是 HIR 的表面呈現，不是語意核心的分支。

- **輸入：** 在地化原始碼（泰文、中文、阿拉伯文等）→ 正規化 HIR — **已提供**
- **輸出：** HIR → 重新產生在地化原始碼 — **進行中**（正在實作）

輸出方向完成後，`faber format --reader-locale=th-TH` 將能讓任何 Faber 原始碼經由 HIR 往返轉換，並以泰文關鍵字輸出，完成對稱性：同一個 HIR 可以產生任何語系表面，正如它也可以產生任何目標後端。

#### HIR 直出後端 {#hir-direct-backends}

這些目標直接從具型別的 HIR 產生輸出，不降低至 MIR。它們會更長時間保留原始碼層級的結構，適合語言形狀的輸出：

| 目標 | 狀態 | 角色 |
|---|---|---|
| `Rust` | **主要** | 生產路徑。套件、建置、執行、測試。使用 Cargo + rustc 產生原生二進位檔。 |
| `Faber` | **支援** | 透過 `forma` 格式化工具提供標準原始碼檢視。確保往返穩定性。 |
| `TypeScript` | 探測 | 僅產生檔案。驗證跨目標形狀的語意。 |
| `Go` | 抹除 | 僅產生檔案。借用模式會被抹除；拒絕 `ad`。 |

### MIR — 中階中間表示 {#mir}

MIR 是以執行為形狀的 IR。它表示控制流程、區域變數、執行期呼叫、位置、分支與錯誤邊界，這些都是低階目標所需的資訊。HIR 保留原始碼結構，而 MIR 則將其扁平化為控制流程圖。

HIR → MIR 降低會將語言形狀的結構轉換為執行步驟。降低後會驗證 MIR，以便在任何後端嘗試產生輸出前，先捕捉結構問題。

> **語意責任。** Faber 在 HIR/MIR 中強制執行的規則（型別檢查、確定賦值、借用模式 lint）與交由目標工具鏈處理的規則（Rust 生命週期分析、Go 型別安全）之間維持清楚的邊界。如此可避免編譯器重複處理目標編譯器已能正確完成的工作。

### AIR 繞道路徑 {#air}

AIR（自動微分／AI 表示）是從 HIR → MIR 路徑分出的純函數式轉換繞道路徑。只有個別函式上的明確註記，才能進入此路徑：

```faber locale=la
@ radix lane "air"
functio loss(numerus predicted, numerus expected) → numerus {
    fixum numerus delta ← predicted - expected
    redde delta * delta
}
```

AIR 路徑函式必須符合純性政策：不得有變異、效果或迴圈。違反規則的函式會在 AIR 降低開始前，以診斷訊息拒絕。程式的其餘部分仍可使用具有變異、效果與迴圈的標準 Faber。

AIR 轉換完成其工作後（未來包括自動微分與融合），結果會重新降低為 MIR，並重新加入一般的 MIR 後端管線。AIR 不擁有任何後端，也沒有獨立的型別檢查器；它是轉換檢查點，不是平行的 IR。

```text
HIR  →  AIR purity check  →  HIR to AIR lowering  →  AIR validation  →  AIR to MIR re-lowering  →  MIR backend
```

此架構反映 JAX 的方法：保留純函數式表示以進行轉換，直到最後才降低為命令式 IR。AIR 存在的原因，是對已降低為變異形式的命令式 MIR 執行自動微分時，必須重新從程式碼重建純性。

### CPU 目標路徑 {#cpu}

CPU 目標會取用 MIR，並產生可執行成品或供外部工具鏈使用的文字。Faber 會在可行時產生文字，並依賴低階工具鏈完成最後的編譯步驟，這類似於 C 編譯器為組譯器與連結器產生組合語言。

#### FMIR — Faber 自有的 MIR 執行期 {#fmir}

FMIR 是原生支援 MIR 的套件執行器。編譯器會將 MIR 擷取為二進位承載資料，並以簡短的 Rust 核心載入器包裝。這會產生一個自包含的可執行檔，透過 Faber 的程序內步進器執行 MIR，不需要另外安裝執行期。

| 格式 | 說明 |
|---|---|
| `fmir-text` | 可檢視的 FMIR 文字映像，位於 `target/faber-mir/image.fmir.txt` |
| `fmir` | 精簡的 FMIR 二進位映像，位於 `target/faber-mir/image.fmir` |
| `fmir-bin` | 自包含執行器，位於 `target/faber-mir/exe/run` — 內嵌 FMIR 位元組 |

#### LLVM 文字 {#llvm}

Faber 會以文字形式產生 LLVM IR（`.ll`），而不是整合 LLVM 程式碼產生器。產生的 IR 是供外部工具鏈步驟使用；驗證、最佳化與原生程式碼產生由下游 LLVM 工具處理。這是暫存與驗證目標，不是嵌入編譯器的原生程式碼產生路徑。

#### WASM {#wasm}

Faber 會產生 WebAssembly 文字（`.wat`）與二進位（`.wasm`）格式。產生的 Wasm 使用外部主機匯入（`faber_*` 執行期符號），並透過 `wasm-tools validate` 驗證。Wasm 是一個受支援但有限制的目標：它以開放標準格式驗證 MIR 降低管線，但不是套件交付執行期。

| 格式 | CLI 目標 | 輸出 |
|---|---|---|
| `wasm-text` | `-t wasm-text`（別名 `wat`） | WAT 文字格式 |
| `wasm` | `-t wasm` | 二進位 Wasm 模組 |

#### TypeScript 與 Go（HIR 直出） {#typescript-go}

TypeScript 與 Go 通常用於應用程式層級的檔案產生，也可作為驗證目標：它們驗證 Faber 的語意能否轉換至廣泛使用的型別系統，即使目前套件編譯與執行期執行仍僅支援 Rust。

### GPU 目標路徑 {#gpu}

#### WGSL（透過 WGPU） {#wgsl}

Faber 透過 MIR 管線產生 WGSL 計算著色器原始碼。產生的 WGSL 會透過 `naga`（30.x）驗證，並包含用於繫結群組中繼資料的反射附屬檔案。這涵蓋裝置安全的核心子集：支援 rank-1 `f32` 裝置檢視；拒絕 rank-2 檢視。WGSL 不是 GPU 啟動執行期；Faber 會產生著色器原始碼，但執行需要外部 WebGPU 執行期。

#### Metal（暫緩） {#metal}

Metal 計算著色器文字產生已完成設計並部分實作，但目前暫緩。其架構遵循與 WGSL 相同的模式：Faber 為裝置安全的核心子集產生 Metal Shading Language 原始碼，由外部工具鏈處理編譯與執行。預計將恢復相關工作。

### 架構說明 {#comparison}

Faber 的編譯架構在理念上類似 Rust 編譯器的運作方式。Rust 會經過 HIR → MIR → LLVM IR 的降低流程，並直接嵌入 LLVM 工具鏈以完成最終原生程式碼產生。Faber 採取較柔性的方式：為外部工具鏈產生文字（LLVM 文字、WGSL、Metal、WAT），而不是嵌入這些工具鏈；同時保留直接程式碼產生給自有執行期（FMIR）與主要套件目標（Rust，其中 Cargo 與 rustc 處理下游管線）。

文字產生方式表示 Faber 永遠不需要附帶 LLVM、Wasm 執行期或 GPU 驅動程式；這些都保留為由使用者選擇的外部相依項。取捨是 Faber 無法為每個目標提供單一命令建置；使用者必須為所選後端安裝適當的工具鏈。

### 目標摘要 {#matrix}

| 目標 | IR | 系列 | 建置 | 執行 | 套件 |
|---|---|---|---|---|---|
| `Rust` | HIR | CPU | 是 | 是 | 是 |
| `fmir` / `fmir-bin` | MIR | CPU | 是 | 是 | 是 |
| `Faber`（格式化） | HIR | — | 否 | 否 | 否 |
| `TypeScript` | HIR | CPU | 否 | 否 | 否 |
| `Go` | HIR | CPU | 否 | 否 | 否 |
| `LLVM text` | MIR | CPU | 否 | 否 | 否 |
| `WASM` / `WAT` | MIR | CPU | 否 | 否 | 否 |
| `WGSL` | MIR | GPU | 否 | 否 | 否 |
| `Metal`（暫緩） | MIR | GPU | 否 | 否 | 否 |

*`build`、`run` 與 `package` 描述 Faber 工作流程。外部工具鏈（rustc、wasm-tools、naga）會為文字產生目標處理最終編譯。*

## Compiler performance

Radix 的前端處理效能大致會隨來源大小呈線性成長，並且在程序內以單執行緒執行。

### 前端編譯時間 {#frontend-compile-times}

| 程式大小 | 原始碼 | 編譯中位數 |
|-------------|--------|---------------|
| 100 個函式 / 約 650 行 | 約 10 KB | 約 0.6 毫秒 |
| 500 個函式 / 約 3.3K 行 | 約 52 KB | 約 3 毫秒 |
| 1,000 個函式 / 約 6.5K 行 | 約 105 KB | 約 6 毫秒 |
| 5,000 個函式 / 約 32K 行 | 約 530 KB | 約 37 毫秒 |

目前最大的實際範例約為 140 行，遠低於雜訊底線。

### 後端成本（Rust 目標） {#backend-costs-rust-target}

對於 `faber build` 而言，使用者感受到的時間主要由 Cargo/rustc
所決定，而不是 Faber 的前端：

| 階段 | 成本 |
|-------|------|
| 冷啟動 `faber` 相依項編譯（每個目標目錄一次） | 約 2.8 秒 |
| 冷啟動 `tokio` 相依項編譯（僅在需要時） | 約 2.3 秒 |
| 每個程式的暖啟動建置（相依項已快取） | 約 30–110 毫秒 |
| 每次程式的 Cargo 呼叫額外開銷 | 約 400 毫秒 |

### 增量編譯 {#incremental-compilation}

`faber-runtime` crate 會在每個目標目錄中編譯一次，並以 `.rlib` 成品的形式快取：

| 你變更的內容 | faber-runtime crate | 你的程式 |
|-----------|-------------------|-------------|
| 你的程式原始碼 | 已快取 | 重新編譯 |
| `norma/src/*.fab`（Faber 原始碼） | 已快取 | 重新編譯 |
| `faber-runtime/src/*.rs` | 重新編譯一次 | 重新編譯 |

應避免的陷阱，是將每個程式建置到全新的 `target/`。
重複使用共用的 `--target-dir`，讓快取的 `.rlib` 保持暖狀態。
