+++
translation_kind = "translated"

title = "Variables and binding"
section = "syntax"
order = 2
sources = [
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "examples/corpus/fixum/",
  "examples/corpus/sit/",
]


prose_hash = "sha256:2e0180766e816022e87ea9eb6c8c531d30993227db9aa56c9224c9a98d3d984f"
code_hash = "sha256:122027c8f10ed33d224e3b23653279e91d19d9a17f432190340909eea5dd9ab3"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber 拥有三个变量关键字和一个专门的赋值符。核心区别在于 `fixum`（一次写入）与 `varia`（可自由重赋值），以及 `←`（运行时流）与 `=`（结构体字段形状）。

## fixum — 不可变绑定 {#fixum-immutable-binding}

`fixum` 绑定只能写入一次。声明时可带或不带初始化式；若声明时不带，则必须在读取之前精确赋值一次。第二次赋值会被拒绝。

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

延迟初始化：

```faber
incipit {
    fixum numerus factor
    si verum {
        factor ← 10
    } secus {
        factor ← 100
    }
    nota factor
}
```

## varia — 可变绑定 {#varia-mutable-binding}

`varia` 绑定可自由重赋值：

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

## sit — 推断不可变语法糖 {#sit-inferred-immutable-sugar}

`sit` 是 `fixum _` 的语法糖——一种类型推断的不可变绑定：

```faber
incipit {
    sit salve ← "Salve"
    sit nomen ← "Marcus"
    sit x ← 42

    # Deferred form
    sit label
    label ← "deferred"
}
```

## 运行时绑定与结构体定义 {#runtime-binding-vs-structural-definition}

Faber 将大多数语言合并为 `=` 的语义拆分为两种：

| 符号 | 角色 | 用途 |
|-------|------|---------|
| `←` | 运行时流 | 初始绑定、重赋值、变更 |
| `=` | 结构形状 | 字面量与元数据内的字段名 |

```faber
genus Point {
    numerus x
    numerus y
}

incipit {
    # Runtime: ← attaches a value to a name at execution time
    varia numerus count ← 0
    varia textus label ← "ready"
    count ← count + 1

    # Structural: = defines field values inside a type literal
    fixum _ p ← Point {
        x = 10,
        y = 20
    }
}
```

## ex 字段提取 {#ex-field-extraction}

`ex` 将值的字段提取为局部绑定：

```faber
genus Persona {
    textus nomen
    numerus aetas
}

incipit {
    fixum _ p ← Persona { nomen = "Marcus", aetas = 30 }
    ex p fixum nomen, aetas
    # prints "Marcus"
    nota nomen
}
```

## 后缀自增与自减 {#postfix-increment-and-decrement}

`⊕` 和 `⊖` 是用于可变 `numerus` 位置的后缀自增/自减语句。它们仅作为语句使用——没有表达式值，也没有前缀形式：

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ⊕
    # i becomes 0
    i ⊖
}
```
