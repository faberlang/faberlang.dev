+++
translation_kind = "translated"

title = "Errors and testing"
section = "language"
order = 4
sources = [
  "radix/README.md (Return and Error Channels)",
  "examples/corpus/iace/",
  "examples/corpus/fac/",
  "examples/corpus/cape/",
  "radix/docs/design/failable-conversio.md",
]
+++

## Error handling

Faber 將三個相關概念分開處理，而許多語言會將它們折疊成同一種形式：

| 構造 | 意義 |
|-----------|---------|
| `→ T` | 一般成功回傳通道 |
| `T ∪ nihil` | 成功值域中的缺值 |
| `⇥ E` | 錯誤的可復原替代退出通道 |

### 一般回傳 {#normal-return}

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

### 可失敗函式 {#failable-functions}

當函式可以透過錯誤通道離開時，使用 `⇥`：

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}
```

### 拋出 — iace {#throwing--iace}

`iace` 將值送入錯誤通道：

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

### 復原 — fac / cape {#recovery--fac--cape}

呼叫端使用 `fac` 區塊與 `cape` 處理常式在本地復原：

```faber
functio divide(numerus a, numerus b) → numerus {
    si b ≡ 0 {
        redde 0
    }
    redde a / b
}

functio tutum(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    }
    cape err {
        mone err
        redde 0
    }
}
```

直接呼叫可失敗函式並不是一般運算式。請將對
`→ T ⇥ E` 函式的呼叫放在作用中的 `fac` / `cape` 邊界內。

### 內嵌轉換復原 {#inline-conversion-recovery}

`⇥` 也可以在 `↦` 轉換上指定內嵌復原值：

```faber
fixum textus raw ← "42"
fixum _ n ← raw ↦ numerus ⇥ 0
```

### 僅效果的可失敗函式 {#effectonly-failable}

對於會發生錯誤但不回傳成功值的函式，省略 `→ T`：

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

### 目前狀態 {#current-status}

`→`、`redde`、`⇥`、`iace` 與 `fac` / `cape` 都是現行的文法與檢查器
介面。Rust 與 Go 對完整 `⇥` / `iace` / `cape` 執行時行為的降階處理
仍是後端缺口——這些內容可以通過型別檢查，但目前尚未對所有目標產生
可失敗的執行時程式碼。

## Inline testing

Faber 將一流的測試框架內建於語言中，提供三個關鍵字：`probandum` 宣告測試套件，`proba` 宣告單一測試案例，而 `adfirma` 則斷言條件。測試與其所測試的程式碼位於同一檔案中，透過 `faber test` 執行，並支援與正式程式碼相同的編譯器流程——具備地區設定感知、型別檢查及多目標支援。

### 三個關鍵字 {#keywords}

| 關鍵字 | 作用 | 約略對應 |
|---------|------|--------|
| `probandum` | 宣告具名測試套件 | `describe`、`#[cfg(test)] mod` |
| `proba` | 宣告單一測試案例 | `it`、`#[test]` |
| `adfirma` | 在執行時斷言條件 | `assert!`、`assert_eq!` |

#### probandum — 測試套件 {#probandum-test-suite}

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

#### proba — 測試案例 {#proba-test-case}

`proba` 區塊包含測試邏輯。它可以使用任何 Faber 程式碼——變數繫結、函式呼叫、控制流程——並以一個或多個 `adfirma` 斷言結束。測試可以使用選用的 `tag` 標記，以便選擇性執行：

```text
proba "echo formats operands with one space" tag "coreutils" {
    adfirma echo_textus(["hello", "world"]) ≡ "hello world"
}
```

#### adfirma — 斷言 {#adfirma-assertion}

`adfirma` 會評估布林運算式；如果結果為假，便回報失敗。選用的訊息字串可在失敗時提供上下文：

```faber
incipit {
    fixum _ x ← 10

    # Simple assertion
    adfirma x > 0

    # With custom message
    adfirma x ≡ 10 secus "x decem esse debet"

    # Multiple assertions in sequence
    fixum _ nomen ← "Marcus"
    adfirma nomen ≡ "Marcus"
    adfirma nomen ≠ "" secus "nomen vacuum non sit"
}
```

### 工作流程 {#workflow}

測試透過 `faber test` 指令執行：

```text
faber test                        # run all tests in the current package
faber test examples/coreutils/packages/echo  # run tests for a specific package
```

由於測試與原始碼位於同一個 `.fab` 檔案中，因此不需要獨立的測試目錄結構、不需要測試模組宣告，也不需要在測試建置與正式建置之間區分建置指令碼。編譯器會根據所使用的關鍵字，辨識哪些區塊是測試程式碼、哪些區塊是正式程式碼——`probandum` 和 `proba` 會被解析，但會從正式建置中排除。

### 實際範例 {#real-world}

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

### 設計說明 {#design}

有數項設計選擇，使 Faber 的測試框架有別於傳統方法：

- **沒有獨立的測試二進位檔。** 測試是同一份原始碼中的宣告，而不是獨立的編譯目標。編譯器會將測試區塊從正式輸出中篩除。
- **使用標記，而不是目錄。** 測試透過 `tag` 標記組織，而不是目錄結構。測試可以同時屬於多個組織軸，不必為此搬移檔案。
- **完整的編譯器流程。** 測試會進行型別檢查、分析，並具備地區設定感知——相同的 `--reader-locale` 旗標也適用於測試輸出。
- **多目標。** 測試會透過套件所指定的後端執行——`faber test --interpret` 使用 MIR 逐步執行器，`faber test` 使用編譯後的 Rust。
- **巢狀套件。** `probandum` 區塊可以巢狀，反映其所測試程式碼的結構。

### 參考資料 {#references}

1. `examples/corpus/probandum/` — probandum 範例檔案
2. `examples/corpus/proba/` — proba 範例檔案
3. `examples/corpus/adfirma/` — adfirma 範例檔案
4. `examples/coreutils/packages/echo/src/main.fab` — 使用標記的實際範例
