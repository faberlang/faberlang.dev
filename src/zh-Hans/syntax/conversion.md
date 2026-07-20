+++
translation_kind = "translated"

title = "Conversion and construction"
section = "syntax"
order = 9
sources = [
  "radix/README.md (Conversion and Construction)",
  "radix/docs/design/conversio-valor.md",
  "radix/docs/design/failable-conversio.md",
]


prose_hash = "sha256:5804f612f8d3df38cbb8bf659a1e16484df7bab2c0fb0ca31f24f2281821aeb6"
code_hash = "sha256:a9b4077c5847b3cd815b5494ca2fdaed9f8eb83835307924dacd7a7fb6b72270"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
两个重要的转换运算符,一个用于运行时,一个用于编译时:

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus value ← 7
fixum _ text ← value ∷ textus
```

## 运行时转换 — ↦ {#runtime-conversion}

使用 `↦` 进行运行时转换,尤其是可能失败的解析或强制转换。用 `⇥` 提供内联恢复:

```faber
fixum textus input ← "9"
fixum _ n ← "42" ↦ numerus
fixum _ safe ← input ↦ numerus ⇥ 0
```

类型驱动的具象化:

```faber
fixum textus path ← "/etc/hosts"
fixum _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
fixum _ body ← ad 'solum:lege' (path) ↦ textus
```

## 静态标注 — ∷ {#static-ascription}

使用 `∷` 进行显式静态类型标注。它是后置的,并且由目标类型驱动:

```faber
fixum numerus value ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

## 空值合并 — vel {#nullish-coalescing}

当值为 `nihil` 时,使用 `vel` 进行空值合并:

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
