Faber 拥有多种由编译器内置的集合类型。其规范方法位于编译器中，而非标准库中。

## Lista — 有序动态集合 {#lista}

<<<FENCE 0>>>

使用 `sparge` 展开：

<<<FENCE 1>>>

关键方法：`longitudo`、`accipe`、`appende`、`summa`、`primus`、`novissimus`。

## Tabula — 键值映射 {#tabula}

<<<FENCE 2>>>

## Tensor — 密集定形缓冲区 {#tensor}

<<<FENCE 3>>>

Tensor 语法糖（用于数值密集型代码）：

<<<FENCE 4>>>

关键方法：`forma`、`accipe`、`ponde`、`crea`、`structa`、`strue`，以及逐元素算术、矩阵乘法（`multiplicatio`）和归约（`summa`、`productum`）。

## Sparsa — 稀疏定形缓冲区 {#sparsa}

<<<FENCE 5>>>

密集与稀疏之间的转换：

<<<FENCE 6>>>

## 游标 — 惰性流 {#cursors}

`cursor<T>` 是一种惰性流类型。可由集合迭代器、tuus 视图或生成器函数创建。通过 `itera ex` 消费：

<<<FENCE 7>>>

## Intervallum — 范围 {#intervallum}

<<<FENCE 8>>>

`‥` 是排他范围的端点；`…` 是包含端点。
