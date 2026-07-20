+++
translation_kind = "translated"

title = "Data types"
section = "syntax"
order = 1
sources = [
  "radix/README.md (Core Type Surfaces, Numeric Widths, Tensors And Sparsa, GPU Core Types)",
  "radix/docs/design/numeric-type-sugar.md",
  "radix/docs/design/tensor-intrinsics.md",
  "radix/docs/design/lista-intrinsics.md",
  "radix/docs/design/comparison-operators.md",
  "radix/EBNF.md",
  "examples/corpus/typi/",
  "examples/corpus/tensor/",
  "examples/corpus/lista/",
]


prose_hash = "sha256:b3f22d05ed3eb8bbc5d3322fd71f7677a77ba9909b6c80f1cfa00455320e7de5"
code_hash = "sha256:c2351c4cdd58a84dd89c4adc956cce28ce5d7a3db572eae85b44d4a6dbb5d48a"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
يمتلك Faber نظام أنواع ثابتاً، النوع أولاً. كل تصريح يضع النوع قبل الاسم: `textus nomen`، وليس `nomen: textus`. يغطي نظام الأنواع البدائيات القياسية، والمجموعات العامة، والأعداد محددة الحجم، والموترات، وأنواع السجلات الموجهة لوحدة معالجة الرسوميات.

## الأنواع البدائية {#primitive-types}

| النوع | الدور | مثال حرفي |
|------|------|-----------------|
| `textus` | سلسلة نصية يونيكود | `"Salve, munde"` |
| `ascii` | رمز آلة ثابت | `'solum:lege'` |
| `numerus` | عدد صحيح بإشارة (الافتراضي i64) | `42` |
| `fractus` | عدد عشري (الافتراضي f64) | `3.14` |
| `bivalens` | قيمة منطقية | `verum`، `falsum` |
| `vacuum` | وحدة / بلا قيمة | — |
| `nihil` | معدوم / غائب | `nihil` |
| `instans` | مدة / لحظة زمنية | — |
| `json` | قيمة JSON وقت الترجمة | `{ "key": "value" }` |
| `octeti` | تسلسل بايتات ست عشرية | \|00ff\| |

## الأنواع العددية محددة الحجم {#sized-numeric-types}

يمتلك `numerus` و`fractus` عرضين افتراضيين (i64 وf64) وصيغاً ذات عرض صريح:

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

يتوفر اختزال العرض في موضع النوع: `i8` … `u64`، `f16`، `f32`، `f64` تكافئ `numerus<W>` / `fractus<W>`.

## الأنواع القابلة للإعدام {#nullable-types}

تستخدم القيم القابلة للإعدام صيغة الاتحاد `T ∪ nihil`:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio maybe() → textus ∪ nihil {
    redde nihil
}
```

لا توجد صيغة `T?` أو `Option<T>` في Faber. الاتحاد صريح.

## أسماء الأنواع المستعارة {#type-aliases}

```faber
typus UserId = numerus
```

## الأنواع العامة {#generics}

تقبل الدوال، وأسماء الأنواع المستعارة، و`genus`، و`implendum` معاملات نوع بصيغة `<T>`:

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

تُدعم معاملات النوع الصريحة في موقع الاستدعاء:

```faber
functio identitas<T>(T valor) → T { redde valor }

fixum numerus value ← identitas<numerus>(7)
```

## المجموعات {#collections}

| النوع | الدور | اختزال |
|------|------|-------|
| `lista<T>` | مجموعة ديناميكية مرتبة | `lf32`، `lu32` |
| `tabula<K, V>` | خريطة مفتاح-قيمة | — |
| `tensor<T, Figura>` | حاوية كثيفة ثابتة الشكل | `tf32[4]`، `ti64[2,3]` |
| `sparsa<T, Figura>` | حاوية متفرقة ثابتة الشكل | `sf32[4]`، `si64[2,3]` |
| `intervallum` | نوع مجال | — |
| `copia<T>` | مجموعة غير مرتبة | — |
| `cursor<T>` | دفق كسول | — |

```faber
fixum lista<numerus> nums ← [1, 2, 3]
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## أنواع الموترات {#tensor-types}

`tensor<T, Figura>` هو الحاوية الكثيفة ثابتة الشكل:

| الصيغة | المعنى |
|------|---------|
| `tensor<T, Figura>` | التهجئة القانونية |
| `tensor<T, []>` | الرتبة 0 (حاوية قياسية) |
| `tensor<T, _>` | فجوة استدلال الشكل |
| `tensor<T, [N]>` | الرتبة 1 (متجه) |
| `tensor<T, [N, M]>` | الرتبة 2 (مصفوفة) |

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

## أنواع نواة وحدة معالجة الرسوميات {#gpu-core-types}

يتعرف مسار الأنظمة على هذه الأنواع لأعمال وحدة معالجة الرسوميات والسجلات.
ترفضها أهداف الحزمة التي تفتقر إلى دعم العتاد:

```faber
functio half(f16 x) → f16 { redde x }

functio add(matrix<f32, [2, 2]> a, matrix<f32, [2, 2]> b) → matrix<f32, [2, 2]> {
    redde a.addita(b)
}

functio swap(atomic<i32> cell, i32 value) → i32 {
    redde cell.exchange(value)
}
```

## علامات الاستعارة على الأنواع {#borrow-markers}

يمكن أن تظهر علامات الاستعارة (`de`، `in`، `ex`) على الأنواع في مواضع المعاملات للإشارة إلى كيفية تمرير القيمة:

```faber locale=la
# shared borrow — caller retains ownership
functio imprime(de textus label) → vacuum { }

# mutable borrow — caller lends mutable access
functio duplica(in numerus value) → vacuum { }

# move — caller gives up ownership
functio consume(ex textus buffer) → textus {
    redde buffer
}
```

## سياسة المقارنة {#comparison-policy}

| المعامل | العائلة | السلوك |
|----------|--------|-----------|
| `≡`، `≠` | مساواة تامة | تتطلب أنواعاً متطابقة؛ استثناء `nihil` |
| `≈`، `≉` | مساواة قيمة عددية | الشبكة العددية فقط |
| `<`، `≤`، `>`، `≥` | ترتيب | عددي، لحظي، نص قياسي |
| `intra` | احتواء مجال | عدد ضمن مجال |
| `inter` | عضوية مجموعة | عنصر في مجموعة |
