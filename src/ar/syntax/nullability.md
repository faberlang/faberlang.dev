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
تُميِّز Faber بين غياب القيمة وتوفيرها الاختياري في موقع الإعلان.

## القيم القابلة للعدم — T ∪ nihil {#nullable-values}

استخدِم `T ∪ nihil` عندما يمكن أن تكون القيمة غائبة:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

## فتحات الإعلان الاختيارية — sponte {#optional-declaration-slots}

استخدِم `sponte` بعد الاسم عندما يمكن للمُستدعي أو المنشئ حذف مُعامل أو حقل:

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

يمكن دمج علامات الاستعارة مع المُعاملات الاختيارية:

```faber
functio process(de numerus depth sponte) → vacuum { }
```

## تأكيد عدم العدم — ! {#non-null-assertion}

استخدِم `!.` و `![` و `!(` لتأكيد أن القيمة القابلة للعدم ليست `nihil`:

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

يؤدي تأكيد عدم العدم على `nihil` إلى إجهاض التنفيذ وقت التشغيل.

## الدمج العدمي — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

## ignotum {#ignotum}

`ignotum` هو النوع غير المعروف عالي المستوى لمخارج الطوارئ والمعرفة غير
المكتملة. وهو ليس آليةً للتعامل مع العدم.
