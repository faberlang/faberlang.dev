Faber 有數種由編譯器擁有的集合型別。它們的標準方法定義於編譯器中，而非標準函式庫。

## Lista — 有序動態集合 {#lista}

<<<FENCE 0>>>

使用 `sparge` 展開：

<<<FENCE 1>>>

主要方法：`longitudo`、`accipe`、`appende`、`summa`、`primus`、`novissimus`。

## Tabula — 鍵值對映射 {#tabula}

<<<FENCE 2>>>

## Tensor — 密集固定形狀緩衝區 {#tensor}

<<<FENCE 3>>>

Tensor 語法糖（數值運算密集的程式碼）：

<<<FENCE 4>>>

主要方法：`forma`、`accipe`、`ponde`、`crea`、`structa`、`strue`，以及逐元素算術、矩陣乘法（`multiplicatio`）和歸約（`summa`、`productum`）。

## Sparsa — 稀疏固定形狀緩衝區 {#sparsa}

<<<FENCE 5>>>

在密集與稀疏格式之間轉換：

<<<FENCE 6>>>

## Cursors — 延遲串流 {#cursors}

`cursor<T>` 是延遲串流型別。它可以由集合迭代器、`tuus` 檢視或產生器函式建立。使用 `itera ex` 消費：

<<<FENCE 7>>>

## Intervallum — 範圍 {#intervallum}

<<<FENCE 8>>>

`‥` 表示不包含終點的範圍；`…` 表示包含終點的範圍。
