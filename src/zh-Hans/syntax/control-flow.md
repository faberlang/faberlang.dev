+++
translation_kind = "translated"

title = "Control flow"
section = "syntax"
order = 4
sources = [
  "radix/README.md (Control Flow Shape, Canonical Surface)",
  "examples/corpus/si/",
  "examples/corpus/itera/",
  "examples/corpus/dum/",
  "examples/corpus/custodi/",
  "examples/corpus/discerne/",
  "examples/corpus/elige/",
]


prose_hash = "sha256:a3b4f77dd7b65f73e835e9e2f65070f22930ad14df15c71a262b81113827a814"
code_hash = "sha256:e257a14fcd068ec06da9199895e899ffb03f352663185ce892b355beadb5cd0b"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
## 条件分支 {#conditional-branching}

### si / sin / secus {#si-sin-secus}

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

### 使用 ergo 的紧凑分支 {#compact-branch-with-ergo}

单语句分支体使用 `ergo`：

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    si ready ergo redde value
    redde nihil
}
```

## 迭代 {#iteration}

### 值 —— itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ergo redde item
    }
    redde nihil
}
```

### 键 —— itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

### 范围 —— itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

## while 循环 {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

## 守卫段 —— custodi {#guard-sections-custodi}

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

## 模式匹配 —— elige {#pattern-matching-elige}

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

## 标签联合匹配 —— discerne {#tagged-union-matching-discerne}

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

## try 块 —— fac / cape {#try-blocks-fac-cape}

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
