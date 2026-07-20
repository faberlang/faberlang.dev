Faber 在值层面区分"空缺"与声明位置的"可选提供"。

## 可空值 — T ∪ nihil {#nullable-values}

当值可能缺失时，使用 `T ∪ nihil`：

<<<FENCE 0>>>

## 可选声明槽 — sponte {#optional-declaration-slots}

当参数或字段可由调用者或构造函数省略时，在名称之后使用 `sponte`：

<<<FENCE 1>>>

借用标记可与可选参数组合使用：

<<<FENCE 2>>>

## 非空断言 — ! {#non-null-assertion}

使用 `!.`, `![`, `!(` 来断言某个可空值不是 `nihil`：

<<<FENCE 3>>>

对 `nihil` 进行非空断言会在运行时中止。

## 空值合并 — vel {#nullish-coalescing}

<<<FENCE 4>>>

## ignotum {#ignotum}

`ignotum` 是用于应急通道和不完整知识的顶层未知类型。它不是一种可空性机制。
