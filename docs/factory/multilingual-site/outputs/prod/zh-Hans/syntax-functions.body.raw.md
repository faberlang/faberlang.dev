Faber 中的函数使用 `functio` 声明，采用类型在前的参数语法，并使用字形标注返回类型。

## 基本语法 {#basic-syntax}

<<<FENCE 0>>>

带有错误通道时：

<<<FENCE 1>>>

## 示例 {#examples}

<<<FENCE 2>>>

## 返回值 {#return-values}

使用 `redde` 进行正常返回：

<<<FENCE 3>>>

当返回类型为 `vacuum` 时，使用裸 `redde`：

<<<FENCE 4>>>

## 借用与可变性（de、in、ex） {#borrowing-and-mutability}

Faber 通过参数上的短介词来标记值的传递方式：

| 标记 | 用途 | 典型的 Rust 降阶 |
|--------|--------|----------------------|
| *(无)* | 拥有的值 | 按值传递 `T` |
| `de` | 共享借用（只读） | `&T` |
| `in` | 可变借用 | `&mut T` |
| `ex` | 消耗（移动到被调用方） | 按移动传递 `T` |

<<<FENCE 5>>>

相同的词（`de`、`ex`）在其他构造中也会复用——不要把每个 `ex` 都解读为"消耗"：

| 用法 | 角色 |
|---------|------|
| 参数上的 `de textus name` | 共享借用 |
| 参数上的 `in numerus count` | 可变借用 |
| 参数上的 `ex textus buffer` | 移动到被调用方 |
| `itera ex items fixum item` | 遍历值 |
| `itera de tabula fixum key` | 遍历键 |
| `ex source fixum x, ceteri rest` | 解构字段 |
| `importa ex "path"` | 从模块导入 |

## 入口点 {#entry-point}

程序入口点是 `incipit`：

<<<FENCE 6>>>

## CLI 入口点 {#cli-entry-point}

对于 CLI 程序，`incipit argumenta` 接收解析后的命令参数：

<<<FENCE 7>>>

## 传递模式——`sponte` {#passing-mode-sponte}

`sponte` 标记调用方可省略的参数：

<<<FENCE 8>>>
