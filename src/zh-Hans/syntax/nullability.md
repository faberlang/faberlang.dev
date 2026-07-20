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
Faber 在值层面区分"空缺"与声明位置的"可选提供"。

## 可空值 — T ∪ nihil {#nullable-values}

当值可能缺失时，使用 `T ∪ nihil`：

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

## 可选声明槽 — sponte {#optional-declaration-slots}

当参数或字段可由调用者或构造函数省略时，在名称之后使用 `sponte`：

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

借用标记可与可选参数组合使用：

```faber
functio process(de numerus depth sponte) → vacuum { }
```

## 非空断言 — ! {#non-null-assertion}

使用 `!.`, `![`, `!(` 来断言某个可空值不是 `nihil`：

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

对 `nihil` 进行非空断言会在运行时中止。

## 空值合并 — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

## ignotum {#ignotum}

`ignotum` 是用于应急通道和不完整知识的顶层未知类型。它不是一种可空性机制。
