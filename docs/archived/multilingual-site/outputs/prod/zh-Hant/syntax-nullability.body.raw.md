Faber 區分值中的缺失與宣告位置上的可選提供。

## 可為空值 — T ∪ nihil {#nullable-values}

當值可能缺失時，使用 `T ∪ nihil`：

<<<FENCE 0>>>

## 可選宣告槽位 — sponte {#optional-declaration-slots}

當參數或欄位可由呼叫者或建構函式省略時，在名稱後使用 `sponte`：

<<<FENCE 1>>>

借用標記可以與可選參數結合：

<<<FENCE 2>>>

## 非空值斷言 — ! {#non-null-assertion}

使用 `!.`、`![`、`!(` 來斷言可為空值不是 `nihil`：

<<<FENCE 3>>>

對 `nihil` 進行非空值斷言會在執行階段中止。

## 空值合併 — vel {#nullish-coalescing}

<<<FENCE 4>>>

## ignotum {#ignotum}

`ignotum` 是頂層未知型別，用於逃生閘道與不完整的知識。它不是可為空值的機制。
