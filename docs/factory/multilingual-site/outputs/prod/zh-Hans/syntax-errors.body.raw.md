Faber 将许多语言合并为同一种形状的三个相关概念区分开来：

| 构造 | 含义 |
|-----------|---------|
| `→ T` | 正常的成功返回通道 |
| `T ∪ nihil` | 成功值域中的缺失 |
| `⇥ E` | 用于错误的可恢复备用退出通道 |

## 正常返回 {#normal-return}

<<<FENCE 0>>>

## 可失败函数 {#failable-functions}

当函数可以通过错误通道退出时，使用 `⇥`：

<<<FENCE 1>>>

## 抛出异常 — iace {#throwing--iace}

`iace` 在错误通道上发送一个值：

<<<FENCE 2>>>

## 恢复 — fac / cape {#recovery--fac--cape}

调用者使用 `fac` 块和 `cape` 处理程序进行局部恢复：

<<<FENCE 3>>>

直接的可失败调用不是普通表达式。请将 `→ T ⇥ E` 函数的调用放在活动的 `fac` / `cape` 边界内。

## 内联转换恢复 {#inline-conversion-recovery}

`⇥` 也可以在 `↦` 转换上指定内联恢复值：

<<<FENCE 4>>>

## 仅效果可失败 {#effectonly-failable}

对于会出错但不返回成功值的函数，省略 `→ T`：

<<<FENCE 5>>>

## 当前状态 {#current-status}

`→`、`redde`、`⇥`、`iace` 以及 `fac` / `cape` 是现行的语法和检查器接口。针对完整 `⇥` / `iace` / `cape` 运行时行为的 Rust 和 Go 降阶（lowering）仍存在后端缺口——这些能通过类型检查，但尚未向所有目标生成可失败的运行时代码。
