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
Faber 中的函式使用 `functio` 宣告，採用型別優先的參數語法，並使用字形回傳型別。

## 基本語法 {#basic-syntax}

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

## 範例 {#examples}

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

## 回傳值 {#return-values}

使用 `redde` 進行一般回傳：

```faber
functio porta(numerus x) → numerus {
    si x < 0 ∴ redde 0
    redde x * 2
}
```

`vacuum` 回傳型別的裸 `redde`：

```faber
functio tace() → vacuum {
    redde
}
```

## 借用與可變性（de、in、ex） {#borrowing-and-mutability}

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

## 進入點 {#entry-point}

程式的進入點是 `incipit`：

```faber
incipit {
    nota "ingressus"
}
```

## CLI 進入點 {#cli-entry-point}

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

## 傳遞模式——`sponte` {#passing-mode-sponte}

`sponte` 標記可由呼叫者省略的參數：

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```
