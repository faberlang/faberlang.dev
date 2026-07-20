+++
translation_kind = "translated"

title = "Functions"
section = "syntax"
order = 3
sources = [
  "radix/README.md (Language Orientation, Borrowing and Mutability, How Faber Feels)",
  "examples/corpus/functio/",
  "examples/corpus/de/",
  "examples/corpus/in/",
  "examples/corpus/ex/",
  "radix/docs/design/semantic-ownership.md",
]


prose_hash = "sha256:ccb89a2cbb2274f10a9cf14807cb355ac88f2a65ac03fb0a5d6cea62f999df28"
code_hash = "sha256:c87e3ad8847578d6410ecd0d2147894a502f9700487a2d53bf6e86334209d5ad"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber 中的函数使用 `functio` 声明，采用类型在前的参数语法，并使用字形标注返回类型。

## 基本语法 {#basic-syntax}

```faber
functio twice(numerus n) → numerus {
    redde n
}
```

带有错误通道时：

```faber
functio parse(textus input) → numerus ⇥ textus {
    redde 0
}
```

## 示例 {#examples}

```faber
# No parameters, no return
functio saluta() {
    nota "Salve, Mundus!"
}

# Parameter, no explicit return
functio dic(textus verbum) {
    nota verbum
}

# Parameter and return type
functio duplica(numerus n) → numerus {
    redde n * 2
}

# Multiple parameters
functio adde(numerus a, numerus b) → numerus {
    redde a + b
}
```

## 返回值 {#return-values}

使用 `redde` 进行正常返回：

```faber
functio porta(numerus x) → numerus {
    si x < 0 ∴ redde 0
    redde x * 2
}
```

当返回类型为 `vacuum` 时，使用裸 `redde`：

```faber
functio tace() → vacuum {
    redde
}
```

## 借用与可变性（de、in、ex） {#borrowing-and-mutability}

Faber 通过参数上的短介词来标记值的传递方式：

| 标记 | 用途 | 典型的 Rust 降阶 |
|--------|--------|----------------------|
| *(无)* | 拥有的值 | 按值传递 `T` |
| `de` | 共享借用（只读） | `&T` |
| `in` | 可变借用 | `&mut T` |
| `ex` | 消耗（移动到被调用方） | 按移动传递 `T` |

```faber locale=la
# Shared borrow
functio imprime(de textus label) → vacuum {
    nota label
}

# Mutable borrow
functio duplica(in numerus value) → vacuum {
    value ← value * 2
}

# Consume
functio consume(ex textus buffer) → textus {
    redde buffer
}

# Owned
functio salve(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}
```

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

```faber
incipit {
    nota "ingressus"
}
```

## CLI 入口点 {#cli-entry-point}

对于 CLI 程序，`incipit argumenta` 接收解析后的命令参数：

```faber locale=la
@ cli "echo"
@ descriptio "Prints text"
@ operandus ceteri textus words
incipit argumenta args {
    itera ex args.words fixum word {
        nota word
    }
}
```

## 传递模式——`sponte` {#passing-mode-sponte}

`sponte` 标记调用方可省略的参数：

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```
