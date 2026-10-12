Faber 將三個相關概念分開處理，而許多語言會將它們折疊成同一種形式：

| 構造 | 意義 |
|-----------|---------|
| `→ T` | 一般成功回傳通道 |
| `T ∪ nihil` | 成功值域中的缺值 |
| `⇥ E` | 錯誤的可復原替代退出通道 |

## 一般回傳 {#normal-return}

<<<FENCE 0>>>

## 可失敗函式 {#failable-functions}

當函式可以透過錯誤通道離開時，使用 `⇥`：

<<<FENCE 1>>>

## 拋出 — iace {#throwing--iace}

`iace` 將值送入錯誤通道：

<<<FENCE 2>>>

## 復原 — fac / cape {#recovery--fac--cape}

呼叫端使用 `fac` 區塊與 `cape` 處理常式在本地復原：

<<<FENCE 3>>>

直接呼叫可失敗函式並不是一般運算式。請將對
`→ T ⇥ E` 函式的呼叫放在作用中的 `fac` / `cape` 邊界內。

## 內嵌轉換復原 {#inline-conversion-recovery}

`⇥` 也可以在 `↦` 轉換上指定內嵌復原值：

<<<FENCE 4>>>

## 僅效果的可失敗函式 {#effectonly-failable}

對於會發生錯誤但不回傳成功值的函式，省略 `→ T`：

<<<FENCE 5>>>

## 目前狀態 {#current-status}

`→`、`redde`、`⇥`、`iace` 與 `fac` / `cape` 都是現行的文法與檢查器
介面。Rust 與 Go 對完整 `⇥` / `iace` / `cape` 執行時行為的降階處理
仍是後端缺口——這些內容可以通過型別檢查，但目前尚未對所有目標產生
可失敗的執行時程式碼。
