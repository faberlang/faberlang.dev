Faber 拥有三个变量关键字和一个专门的赋值符。核心区别在于 `fixum`（一次写入）与 `varia`（可自由重赋值），以及 `←`（运行时流）与 `=`（结构体字段形状）。

## fixum — 不可变绑定 {#fixum-immutable-binding}

`fixum` 绑定只能写入一次。声明时可带或不带初始化式；若声明时不带，则必须在读取之前精确赋值一次。第二次赋值会被拒绝。

<<<FENCE 0>>>

延迟初始化：

<<<FENCE 1>>>

## varia — 可变绑定 {#varia-mutable-binding}

`varia` 绑定可自由重赋值：

<<<FENCE 2>>>

## sit — 推断不可变语法糖 {#sit-inferred-immutable-sugar}

`sit` 是 `fixum _` 的语法糖——一种类型推断的不可变绑定：

<<<FENCE 3>>>

## 运行时绑定与结构体定义 {#runtime-binding-vs-structural-definition}

Faber 将大多数语言合并为 `=` 的语义拆分为两种：

| 符号 | 角色 | 用途 |
|-------|------|---------|
| `←` | 运行时流 | 初始绑定、重赋值、变更 |
| `=` | 结构形状 | 字面量与元数据内的字段名 |

<<<FENCE 4>>>

## ex 字段提取 {#ex-field-extraction}

`ex` 将值的字段提取为局部绑定：

<<<FENCE 5>>>

## 后缀自增与自减 {#postfix-increment-and-decrement}

`⊕` 和 `⊖` 是用于可变 `numerus` 位置的后缀自增/自减语句。它们仅作为语句使用——没有表达式值，也没有前缀形式：

<<<FENCE 6>>>
