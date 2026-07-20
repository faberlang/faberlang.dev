+++
translation_kind = "translated"

title = "Inline testing"
section = "features"
order = 7
sources = []


prose_hash = "sha256:85bf7bf8e3bbf81859e9163f3f1898d0a41aa347101b4ea5a299599abf47f756"
code_hash = "sha256:5c17d1f1d1850fa59128bd6e4a57dce82f2b3ef4be816ff3f5d7275481335af9"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
Faber 將一流的測試框架內建於語言中，提供三個關鍵字：`probandum` 宣告測試套件，`proba` 宣告單一測試案例，而 `adfirma` 則斷言條件。測試與其所測試的程式碼位於同一檔案中，透過 `faber test` 執行，並支援與正式程式碼相同的編譯器流程——具備地區設定感知、型別檢查及多目標支援。

## 三個關鍵字 {#keywords}

| 關鍵字 | 作用 | 約略對應 |
|---------|------|--------|
| `probandum` | 宣告具名測試套件 | `describe`、`#[cfg(test)] mod` |
| `proba` | 宣告單一測試案例 | `it`、`#[test]` |
| `adfirma` | 在執行時斷言條件 | `assert!`、`assert_eq!` |

### probandum — 測試套件 {#probandum-test-suite}

`probandum` 區塊會將相關的測試案例分組。套件可以巢狀，以階層方式組織測試：

```faber
probandum "arithmetica" {
    proba "unum plus unum" {
        adfirma 1 + 1 ≡ 2
    }

    proba "multiplicatio" {
        adfirma 3 * 4 ≡ 12
    }

    probandum "implicata" {
        proba "comparatio" {
            fixum _ x ← 10
            adfirma x ≥ 10
        }
    }
}
```

### proba — 測試案例 {#proba-test-case}

`proba` 區塊包含測試邏輯。它可以使用任何 Faber 程式碼——變數繫結、函式呼叫、控制流程——並以一個或多個 `adfirma` 斷言結束。測試可以使用選用的 `tag` 標記，以便選擇性執行：

```text
proba "echo formats operands with one space" tag "coreutils" {
    adfirma echo_textus(["hello", "world"]) ≡ "hello world"
}
```

### adfirma — 斷言 {#adfirma-assertion}

`adfirma` 會評估布林運算式；如果結果為假，便回報失敗。選用的訊息字串可在失敗時提供上下文：

```faber
incipit {
    fixum _ x ← 10

    # Simple assertion
    adfirma x > 0

    # With custom message
    adfirma x ≡ 10, "x decem esse debet"

    # Multiple assertions in sequence
    fixum _ nomen ← "Marcus"
    adfirma nomen ≡ "Marcus"
    adfirma nomen ≠ "", "nomen vacuum non sit"
}
```

## 工作流程 {#workflow}

測試透過 `faber test` 指令執行：

```text
faber test                        # run all tests in the current package
faber test examples/coreutils/packages/echo  # run tests for a specific package
```

由於測試與原始碼位於同一個 `.fab` 檔案中，因此不需要獨立的測試目錄結構、不需要測試模組宣告，也不需要在測試建置與正式建置之間區分建置指令碼。編譯器會根據所使用的關鍵字，辨識哪些區塊是測試程式碼、哪些區塊是正式程式碼——`probandum` 和 `proba` 會被解析，但會從正式建置中排除。

## 實際範例 {#real-world}

coreutils 的 `echo` 套件展示了測試框架的實際應用。測試與實作位於同一個檔案中，涵蓋選項解析、跳脫展開及邊界情況：

```text
probandum "echo formatting" tag "coreutils" {
    proba "empty operands format as empty text" {
        fixum lista<textus> words ← vacua
        adfirma echo_textus(words) ≡ ""
    }

    proba "single operand is unchanged" {
        adfirma echo_textus(["hello"]) ≡ "hello"
    }

    proba "-E is a leading no-op option" {
        adfirma echo_textus(["-E", "hello", "world"]) ≡ "hello world"
    }

    proba "-n suppresses the trailing newline flag" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }

    proba "-e expands the declared escape subset" {
        adfirma echo_textus(["-e", "a\\nb"]) ≡ "a\nb"
        adfirma echo_textus(["-e", "a\\tb"]) ≡ "a\tb"
    }
}
```

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
