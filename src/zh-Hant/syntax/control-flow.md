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
## 條件分支 {#conditional-branching}

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

包含 else-if 與 else：

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

### 使用 ∴ 的精簡分支 {#compact-branch-with}

單一敘述的分支主體使用 `∴`（或其別名 `ergo`）：

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    si ready ergo redde value
    redde nihil
}
```

## 迭代 {#iteration}

### 值 — itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ergo redde item
    }
    redde nihil
}
```

### 鍵 — itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

### 範圍 — itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

## While 迴圈 {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

## 保護區段 — custodi {#guard-sections-custodi}

`custodi` 會在函式的主要主體之前，集中處理提早退出的檢查。
每個 `si` 子句都是依序執行的保護條件：

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

在 v1 中，`custodi` 不可中斷——它是防護欄，而不是迴圈。

## 模式比對 — elige {#pattern-matching-elige}

`elige` 會選取第一個符合的分支：

```faber
functio describe(numerus value) → textus {
    elige value {
        casu 1 { redde "one" }
        casu 2 { redde "two" }
        ceterum { redde "many" }
    }
}
```

## 標記聯集比對 — discerne {#tagged-union-matching-discerne}

`discerne` 會完整比對 `discretio` 的各個變體：

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

## Try 區塊 — fac / cape {#try-blocks-fac-cape}

`fac` 開啟一個可能拋出例外的區塊，而 `cape` 負責復原：

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
