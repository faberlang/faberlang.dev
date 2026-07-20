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
Faber 有三個變數關鍵字，以及專用的指派字元。關鍵差異在於 `fixum`（只能寫入一次）與 `varia`（可自由重新指派），以及 `←`（執行期流程）與 `=`（結構欄位形狀）之間的區別。

## fixum — 不可變繫結 {#fixum-immutable-binding}

`fixum` 繫結只能寫入一次。宣告時可以提供初始值，也可以不提供；若未提供初始值，則必須在讀取前恰好指派一次。第二次指派會被拒絕。

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

延遲初始化：

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

## varia — 可變繫結 {#varia-mutable-binding}

`varia` 繫結可以自由重新指派：

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

## sit — 推導的不可變語法糖 {#sit-inferred-immutable-sugar}

`sit` 是 `fixum _` 的語法糖——具有推導型別的不可變繫結：

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

## 執行期繫結與結構定義 {#runtime-binding-vs-structural-definition}

Faber 將多數語言合併在 `=` 中的概念分開：

| 字元 | 作用 | 用於 |
|-------|------|---------|
| `←` | 執行期流程 | 初始繫結、重新指派、變更 |
| `=` | 結構形狀 | 常值與中繼資料中的欄位名稱 |

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

## ex 欄位擷取 {#ex-field-extraction}

`ex` 將值中的欄位擷取至區域繫結：

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

## 後置遞增與遞減 {#postfix-increment-and-decrement}

`⊕` 與 `⊖` 是可變 `numerus` 儲存處的後置遞增／遞減陳述式。它們只能作為陳述式使用——沒有運算式值，也沒有前置形式：

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ⊕
    # i becomes 0
    i ⊖
}
```
