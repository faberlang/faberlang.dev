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

Faber 中的函式使用 `functio` 宣告，採用型別優先的參數語法，並使用字形回傳型別。

### 基本語法 {#basic-syntax}

```faber
functio twice(numerus n) → numerus {
    redde n
}
```

帶有錯誤通道：

```faber
functio parse(textus input) → numerus ⇥ textus {
    redde 0
}
```

### 範例 {#examples}

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

### 回傳值 {#return-values}

使用 `redde` 進行一般回傳：

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

`vacuum` 回傳型別的裸 `redde`：

```faber
functio tace() → vacuum {
    redde
}
```

### 借用與可變性（de、in、ex） {#borrowing-and-mutability}

Faber 使用參數上的簡短介系詞標記值的傳遞方式：

| 標記 | 意圖 | 常見的 Rust 降低方式 |
|--------|------|----------------------|
| *(無)* | 擁有值 | 以值傳遞的 `T` |
| `de` | 共用借用（唯讀） | `&T` |
| `in` | 可變借用 | `&mut T` |
| `ex` | 消耗（移入被呼叫者） | 以移動傳遞的 `T` |

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

相同的詞（`de`、`ex`）也會在其他結構中重複使用——不要將每個 `ex` 都解讀為「消耗」：

| 表面語法 | 角色 |
|---------|------|
| 參數上的 `de textus name` | 共用借用 |
| 參數上的 `in numerus count` | 可變借用 |
| 參數上的 `ex textus buffer` | 移入被呼叫者 |
| `itera ex items fixum item` | 迭代值 |
| `itera de tabula fixum key` | 迭代鍵 |
| `ex source fixum x, ceteri rest` | 解構欄位 |
| `importa ex "path"` | 從模組匯入 |

### 進入點 {#entry-point}

程式的進入點是 `incipit`：

```faber
incipit {
    nota "ingressus"
}
```

### CLI 進入點 {#cli-entry-point}

對於 CLI 程式，`incipit argumenta` 會接收已解析的命令列引數：

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

### 傳遞模式——`sponte` {#passing-mode-sponte}

`sponte` 標記可由呼叫者省略的參數：

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```

## Control flow

### 條件分支 {#conditional-branching}

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

#### 使用 ergo 的精簡分支 {#compact-branch-with-ergo}

單一敘述的分支主體使用 `ergo`：

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    si ready ergo redde value
    redde nihil
}
```

### 迭代 {#iteration}

#### 值 — itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ergo redde item
    }
    redde nihil
}
```

#### 鍵 — itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

#### 範圍 — itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

### While 迴圈 {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

### 保護區段 — custodi {#guard-sections-custodi}

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

### 模式比對 — elige {#pattern-matching-elige}

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

### 標記聯集比對 — discerne {#tagged-union-matching-discerne}

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

### Try 區塊 — fac / cape {#try-blocks-fac-cape}

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

## Generics

函式、型別別名、`genus` 與 `implendum` 接受使用 `<T>` 語法的型別參數。

### 泛型函式 {#generic-functions}

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

### 明確的呼叫點型別引數 {#explicit-callsite-type-arguments}

```faber
functio identitas<T>(T valor) → T { redde valor }

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde nihil
}

fixum _ value ← identitas<numerus>(7)
fixum _ maybe ← primum<numerus>([value])
```

### 泛型 `genus` {#generic-genus}

```faber
genus Par<T> {
    T primus
    T secundus
}
```

### 大小參數 {#size-parameters}

`magnitudo` 會在泛型參數列表中宣告大小／索引參數：

```faber
functio crea<T, magnitudo N>() → tensor<T, [N]> {
    redde vacua
}
```
