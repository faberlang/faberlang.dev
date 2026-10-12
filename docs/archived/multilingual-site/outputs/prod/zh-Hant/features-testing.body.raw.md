Faber 將一流的測試框架內建於語言中，提供三個關鍵字：`probandum` 宣告測試套件，`proba` 宣告單一測試案例，而 `adfirma` 則斷言條件。測試與其所測試的程式碼位於同一檔案中，透過 `faber test` 執行，並支援與正式程式碼相同的編譯器流程——具備地區設定感知、型別檢查及多目標支援。

## 三個關鍵字 {#keywords}

| 關鍵字 | 作用 | 約略對應 |
|---------|------|--------|
| `probandum` | 宣告具名測試套件 | `describe`、`#[cfg(test)] mod` |
| `proba` | 宣告單一測試案例 | `it`、`#[test]` |
| `adfirma` | 在執行時斷言條件 | `assert!`、`assert_eq!` |

### probandum — 測試套件 {#probandum-test-suite}

`probandum` 區塊會將相關的測試案例分組。套件可以巢狀，以階層方式組織測試：

<<<FENCE 0>>>

### proba — 測試案例 {#proba-test-case}

`proba` 區塊包含測試邏輯。它可以使用任何 Faber 程式碼——變數繫結、函式呼叫、控制流程——並以一個或多個 `adfirma` 斷言結束。測試可以使用選用的 `tag` 標記，以便選擇性執行：

<<<FENCE 1>>>

### adfirma — 斷言 {#adfirma-assertion}

`adfirma` 會評估布林運算式；如果結果為假，便回報失敗。選用的訊息字串可在失敗時提供上下文：

<<<FENCE 2>>>

## 工作流程 {#workflow}

測試透過 `faber test` 指令執行：

<<<FENCE 3>>>

由於測試與原始碼位於同一個 `.fab` 檔案中，因此不需要獨立的測試目錄結構、不需要測試模組宣告，也不需要在測試建置與正式建置之間區分建置指令碼。編譯器會根據所使用的關鍵字，辨識哪些區塊是測試程式碼、哪些區塊是正式程式碼——`probandum` 和 `proba` 會被解析，但會從正式建置中排除。

## 實際範例 {#real-world}

coreutils 的 `echo` 套件展示了測試框架的實際應用。測試與實作位於同一個檔案中，涵蓋選項解析、跳脫展開及邊界情況：

<<<FENCE 4>>>

## 設計說明 {#design}

有數項設計選擇，使 Faber 的測試框架有別於傳統方法：

- **沒有獨立的測試二進位檔。** 測試是同一份原始碼中的宣告，而不是獨立的編譯目標。編譯器會將測試區塊從正式輸出中篩除。
- **使用標記，而不是目錄。** 測試透過 `tag` 標記組織，而不是目錄結構。測試可以同時屬於多個組織軸，不必為此搬移檔案。
- **完整的編譯器流程。** 測試會進行型別檢查、分析，並具備地區設定感知——相同的 `--reader-locale` 旗標也適用於測試輸出。
- **多目標。** 測試會透過套件所指定的後端執行——`faber test --interpret` 使用 MIR 逐步執行器，`faber test` 使用編譯後的 Rust。
- **巢狀套件。** `probandum` 區塊可以巢狀，反映其所測試程式碼的結構。

## 參考資料 {#references}

1. `examples/corpus/probandum/` — probandum 範例檔案
2. `examples/corpus/proba/` — proba 範例檔案
3. `examples/corpus/adfirma/` — adfirma 範例檔案
4. `examples/coreutils/packages/echo/src/main.fab` — 使用標記的實際範例
