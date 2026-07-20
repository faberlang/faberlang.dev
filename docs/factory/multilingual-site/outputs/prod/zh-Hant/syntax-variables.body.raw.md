Faber 有三個變數關鍵字，以及專用的指派字元。關鍵差異在於 `fixum`（只能寫入一次）與 `varia`（可自由重新指派），以及 `←`（執行期流程）與 `=`（結構欄位形狀）之間的區別。

## fixum — 不可變繫結 {#fixum-immutable-binding}

`fixum` 繫結只能寫入一次。宣告時可以提供初始值，也可以不提供；若未提供初始值，則必須在讀取前恰好指派一次。第二次指派會被拒絕。

<<<FENCE 0>>>

延遲初始化：

<<<FENCE 1>>>

## varia — 可變繫結 {#varia-mutable-binding}

`varia` 繫結可以自由重新指派：

<<<FENCE 2>>>

## sit — 推導的不可變語法糖 {#sit-inferred-immutable-sugar}

`sit` 是 `fixum _` 的語法糖——具有推導型別的不可變繫結：

<<<FENCE 3>>>

## 執行期繫結與結構定義 {#runtime-binding-vs-structural-definition}

Faber 將多數語言合併在 `=` 中的概念分開：

| 字元 | 作用 | 用於 |
|-------|------|---------|
| `←` | 執行期流程 | 初始繫結、重新指派、變更 |
| `=` | 結構形狀 | 常值與中繼資料中的欄位名稱 |

<<<FENCE 4>>>

## ex 欄位擷取 {#ex-field-extraction}

`ex` 將值中的欄位擷取至區域繫結：

<<<FENCE 5>>>

## 後置遞增與遞減 {#postfix-increment-and-decrement}

`⊕` 與 `⊖` 是可變 `numerus` 儲存處的後置遞增／遞減陳述式。它們只能作為陳述式使用——沒有運算式值，也沒有前置形式：

<<<FENCE 6>>>
