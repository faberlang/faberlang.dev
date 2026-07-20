+++
translation_kind = "translated"

title = "Nullability and optionality"
section = "syntax"
order = 11
sources = [
  "radix/README.md (Nullability and Optionality)",
  "examples/corpus/nihil/",
  "examples/corpus/sponte/",
  "examples/corpus/nonnihil/",
]


prose_hash = "sha256:0bf95ac93cff7571775fd0874fcd4d1b00ce96a7a3f47f75b6da1ed1c2dd2d57"
code_hash = "sha256:08e8387c2c18e42258c69e0ff67816e5f9d187787ef444f20380f76264a4827b"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber 區分值中的缺失與宣告位置上的可選提供。

## 可為空值 — T ∪ nihil {#nullable-values}

當值可能缺失時，使用 `T ∪ nihil`：

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## 可選宣告槽位 — sponte {#optional-declaration-slots}

當參數或欄位可由呼叫者或建構函式省略時，在名稱後使用 `sponte`：

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

借用標記可以與可選參數結合：

```faber
functio process(de numerus depth sponte) → vacuum { }
```

## 非空值斷言 — ! {#non-null-assertion}

使用 `!.`、`![`、`!(` 來斷言可為空值不是 `nihil`：

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

對 `nihil` 進行非空值斷言會在執行階段中止。

## 空值合併 — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

## ignotum {#ignotum}

`ignotum` 是頂層未知型別，用於逃生閘道與不完整的知識。它不是可為空值的機制。
