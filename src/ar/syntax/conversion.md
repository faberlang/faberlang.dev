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
عاملَا تحويل مهمّان: أحدهما لوقت التشغيل والآخر لوقت الترجمة:

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus value ← 7
fixum _ text ← value ∷ textus
```

## التحويل وقت التشغيل — ↦ {#runtime-conversion}

استعمل `↦` للتحويل وقت التشغيل، خصوصًا التحليل أو الإكراه الذي قد يفشل.
وفّر استردادًا مضمنًا باستعمال `⇥`:

```faber
fixum textus input ← "9"
fixum _ n ← "42" ↦ numerus
fixum _ safe ← input ↦ numerus ⇥ 0
```

تجسيد موجّه بالنوع:

```faber
fixum textus path ← "/etc/hosts"
fixum _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
fixum _ body ← ad 'solum:lege' (path) ↦ textus
```

## الإسناد الثابت — ∷ {#static-ascription}

استعمل `∷` للإسناد الثابت الصريح للنوع. هو لاحق وموجّه بالنوع الهدف:

```faber
fixum numerus value ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

## الدمج العدمي — vel {#nullish-coalescing}

استعمل `vel` للدمج العدمي حينما تكون القيمة `nihil`:

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
