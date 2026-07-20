## 条件分支 {#conditional-branching}

### si / sin / secus {#si-sin-secus}

<<<FENCE 0>>>

包含 else-if 与 else：

<<<FENCE 1>>>

### 使用 ∴ 的紧凑分支 {#compact-branch-with}

单语句分支体使用 `∴`（或其别名 `ergo`）：

<<<FENCE 2>>>

## 迭代 {#iteration}

### 值 —— itera ex {#values-itera-ex}

<<<FENCE 3>>>

### 键 —— itera de {#keys-itera-de}

<<<FENCE 4>>>

### 范围 —— itera ab {#range-itera-ab}

<<<FENCE 5>>>

## while 循环 {#while-loops}

<<<FENCE 6>>>

## 守卫段 —— custodi {#guard-sections-custodi}

`custodi` 用于在函数主体之前组织提前退出检查。
每一条 `si` 子句都是一个顺序守卫：

<<<FENCE 7>>>

`custodi` 在 v1 中不可被 break —— 它是护栏，不是循环。

## 模式匹配 —— elige {#pattern-matching-elige}

`elige` 选择第一个匹配的分支：

<<<FENCE 8>>>

## 标签联合匹配 —— discerne {#tagged-union-matching-discerne}

`discerne` 对 `discretio` 变体进行穷尽匹配：

<<<FENCE 9>>>

## try 块 —— fac / cape {#try-blocks-fac-cape}

`fac` 开启一个可能抛出的块，`cape` 负责恢复：

<<<FENCE 10>>>
