+++
translation_kind = "translated"

title = "Functions and control flow"
section = "language"
order = 3
sources = [
  "radix/README.md (Language Orientation, Borrowing and Mutability, How Faber Feels)",
  "examples/corpus/functio/",
  "examples/corpus/de/",
  "examples/corpus/in/",
  "examples/corpus/ex/",
  "radix/docs/design/semantic-ownership.md",
  "radix/README.md (Control Flow Shape, Canonical Surface)",
  "examples/corpus/si/",
  "examples/corpus/itera/",
  "examples/corpus/dum/",
  "examples/corpus/custodi/",
  "examples/corpus/discerne/",
  "examples/corpus/elige/",
  "radix/README.md (Type and Size Generics)",
  "examples/corpus/generic/",
  "examples/corpus/functio/generic-call-type-args.fab",
]
+++

## Functions

Faber 中的函数使用 `functio` 声明，采用类型在前的参数语法，并使用字形标注返回类型。

### 基本语法 {#basic-syntax}

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

### 示例 {#examples}

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

### 返回值 {#return-values}

使用 `redde` 进行正常返回：

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

当返回类型为 `vacuum` 时，使用裸 `redde`：

```faber
functio tace() → vacuum {
    redde
}
```

### 借用与可变性（de、in、ex） {#borrowing-and-mutability}

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

### 入口点 {#entry-point}

程序入口点是 `incipit`：

```faber
incipit {
    nota "ingressus"
}
```

### CLI 入口点 {#cli-entry-point}

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

### 传递模式——`sponte` {#passing-mode-sponte}

`sponte` 标记调用方可省略的参数：

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```

## Control flow

### 条件分支 {#conditional-branching}

#### si / sin / secus {#si-sin-secus}

```faber
incipit {
    fixum _ condition ← verum
    si condition {
        # truthy branch
        nota "matched"
    }
}
```

包含 else-if 与 else：

```faber
incipit {
    fixum _ score ← 85
    si score ≥ 90 {
        nota "A"
    } sin score ≥ 80 {
        nota "B"
    } secus {
        nota "C"
    }
}
```

#### 使用 ergo 的紧凑分支 {#compact-branch-with-ergo}

单语句分支体使用 `ergo`：

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    si ready ergo redde value
    redde nihil
}
```

### 迭代 {#iteration}

#### 值 —— itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ergo redde item
    }
    redde nihil
}
```

#### 键 —— itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

#### 范围 —— itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

### while 循环 {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

### 守卫段 —— custodi {#guard-sections-custodi}

`custodi` 用于在函数主体之前组织提前退出检查。
每一条 `si` 子句都是一个顺序守卫：

```faber
functio divide(numerus a, numerus b) → numerus {
    custodi {
        si b ≡ 0 {
            redde 0
        }
    }
    redde a / b
}
```

`custodi` 在 v1 中不可被 break —— 它是护栏，不是循环。

### 模式匹配 —— elige {#pattern-matching-elige}

`elige` 选择第一个匹配的分支：

```faber
functio describe(numerus value) → textus {
    elige value {
        casu 1 { redde "one" }
        casu 2 { redde "two" }
        ceterum { redde "many" }
    }
}
```

### 标签联合匹配 —— discerne {#tagged-union-matching-discerne}

`discerne` 对 `discretio` 变体进行穷尽匹配：

```faber
discretio Exitus {
    Bonum { textus nuntius },
    Malum { textus causa }
}

functio refer(Exitus eventus) → textus {
    discerne eventus {
        casu Bonum fixum nuntius { redde nuntius }
        casu Malum fixum causa { redde "Error: §"(causa) }
    }
}
```

### try 块 —— fac / cape {#try-blocks-fac-cape}

`fac` 开启一个可能抛出的块，`cape` 负责恢复：

```faber
functio divide(numerus a, numerus b) → numerus {
    redde a / b
}

functio tutus(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    } cape err {
        mone err
        redde 0
    }
}
```

## Generics

函数、类型别名、`genus` 与 `implendum` 接受类型参数，使用 `<T>` 语法。

### 泛型函数 {#generic-functions}

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

### 显式调用处类型参数 {#explicit-callsite-type-arguments}

```faber
functio identitas<T>(T valor) → T { redde valor }

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde nihil
}

fixum _ value ← identitas<numerus>(7)
fixum _ maybe ← primum<numerus>([value])
```

### 泛型 genus {#generic-genus}

```faber
genus Par<T> {
    T primus
    T secundus
}
```

### 尺寸参数 {#size-parameters}

`magnitudo` 在泛型参数列表中声明一个尺寸/索引参数：

```faber
functio crea<T, magnitudo N>() → tensor<T, [N]> {
    redde vacua
}
```
