## 條件分支 {#conditional-branching}

### si / sin / secus {#si-sin-secus}

<<<FENCE 0>>>

包含 else-if 與 else：

<<<FENCE 1>>>

### 使用 ∴ 的精簡分支 {#compact-branch-with}

單一敘述的分支主體使用 `∴`（或其別名 `ergo`）：

<<<FENCE 2>>>

## 迭代 {#iteration}

### 值 — itera ex {#values-itera-ex}

<<<FENCE 3>>>

### 鍵 — itera de {#keys-itera-de}

<<<FENCE 4>>>

### 範圍 — itera ab {#range-itera-ab}

<<<FENCE 5>>>

## While 迴圈 {#while-loops}

<<<FENCE 6>>>

## 保護區段 — custodi {#guard-sections-custodi}

`custodi` 會在函式的主要主體之前，集中處理提早退出的檢查。
每個 `si` 子句都是依序執行的保護條件：

<<<FENCE 7>>>

在 v1 中，`custodi` 不可中斷——它是防護欄，而不是迴圈。

## 模式比對 — elige {#pattern-matching-elige}

`elige` 會選取第一個符合的分支：

<<<FENCE 8>>>

## 標記聯集比對 — discerne {#tagged-union-matching-discerne}

`discerne` 會完整比對 `discretio` 的各個變體：

<<<FENCE 9>>>

## Try 區塊 — fac / cape {#try-blocks-fac-cape}

`fac` 開啟一個可能拋出例外的區塊，而 `cape` 負責復原：

<<<FENCE 10>>>
