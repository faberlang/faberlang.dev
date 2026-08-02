+++
translation_kind = "translated"

title = "Types and values"
section = "language"
order = 2
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
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "examples/corpus/fixum/",
  "examples/corpus/sit/",
  "radix/README.md (Tensors And Sparsa)",
  "radix/docs/design/tabula-intrinsics.md",
  "examples/corpus/tabula/",
  "examples/corpus/sparsa/",
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
  "radix/README.md (Nullability and Optionality)",
  "examples/corpus/nihil/",
  "examples/corpus/sponte/",
  "examples/corpus/nonnihil/",
  "radix/README.md (Conversion and Construction)",
  "radix/docs/design/conversio-valor.md",
  "radix/docs/design/failable-conversio.md",
]
+++

## Data types

يمتلك Faber نظام أنواع ثابتاً، النوع أولاً. كل تصريح يضع النوع قبل الاسم: `textus nomen`، وليس `nomen: textus`. يغطي نظام الأنواع البدائيات القياسية، والمجموعات العامة، والأعداد محددة الحجم، والموترات، وأنواع السجلات الموجهة لوحدة معالجة الرسوميات.

### الأنواع البدائية {#primitive-types}

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

### الأنواع العددية محددة الحجم {#sized-numeric-types}

يمتلك `numerus` و`fractus` عرضين افتراضيين (i64 وf64) وصيغاً ذات عرض صريح:

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

يتوفر اختزال العرض في موضع النوع: `i8` … `u64`، `f16`، `f32`، `f64` تكافئ `numerus<W>` / `fractus<W>`.

### الأنواع القابلة للإعدام {#nullable-types}

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

### أسماء الأنواع المستعارة {#type-aliases}

```faber
typus UserId = numerus
```

### الأنواع العامة {#generics}

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

### المجموعات {#collections}

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

### أنواع الموترات {#tensor-types}

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

### أنواع نواة وحدة معالجة الرسوميات {#gpu-core-types}

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

### علامات الاستعارة على الأنواع {#borrow-markers}

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

### سياسة المقارنة {#comparison-policy}

| المعامل | العائلة | السلوك |
|----------|--------|-----------|
| `≡`، `≠` | مساواة تامة | تتطلب أنواعاً متطابقة؛ استثناء `nihil` |
| `≈`، `≉` | مساواة قيمة عددية | الشبكة العددية فقط |
| `<`، `≤`، `>`، `≥` | ترتيب | عددي، لحظي، نص قياسي |
| `intra` | احتواء مجال | عدد ضمن مجال |
| `inter` | عضوية مجموعة | عنصر في مجموعة |

## Variables and binding

Faber تمتلك ثلاث كلمات مفتاحية للمتغيرات ورمز تخصيص مخصص. الفرق الأساسي
هو بين `fixum` (كتابة مرة واحدة) و `varia` (قابل لإعادة التخصيص بحرية)،
وبين `←` (تدفق وقت التشغيل) و `=` (شكل الحقل الهيكلي).

### fixum — ربط غير قابل للتغيير {#fixum-immutable-binding}

روابط `fixum` تُكتب مرة واحدة. يمكن التصريح بها مع مهيئ أو بدونه؛ إذا تم
التصريح بدون مهيئ، يجب تخصيصها مرة واحدة بالضبط قبل القراءة. التخصيص
الثاني مرفوض.

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

التهيئة المؤجلة:

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

### varia — ربط قابل للتغيير {#varia-mutable-binding}

روابط `varia` قابلة لإعادة التخصيص بحرية:

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

### sit — اختصار للربط غير القابل للتغيير مع استنتاج النوع {#sit-inferred-immutable-sugar}

`sit` هو اختصار لـ `fixum _` — رابط غير قابل للتغيير مع نوع مستنتج:

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

### الربط وقت التشغيل مقابل التعريف الهيكلي {#runtime-binding-vs-structural-definition}

Faber يفصل ما تدمجه معظم اللغات في `=`:

| الرمز | الدور | الاستخدام |
|-------|------|---------|
| `←` | تدفق وقت التشغيل | الربط الأولي، إعادة التخصيص، التغيير |
| `=` | الشكل الهيكلي | أسماء الحقول داخل القيم الحرفية والبيانات الوصفية |

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

### استخراج الحقول باستخدام ex {#ex-field-extraction}

`ex` يستخرج الحقول من قيمة إلى روابط محلية:

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

### الزيادة والنقصان اللاحقة {#postfix-increment-and-decrement}

`⊕` و `⊖` هما عبارتا زيادة ونقصان لاحقة للأماكن `numerus` القابلة
للتغيير. هما عبارات فقط — لا قيمة تعبيرية، ولا أشكال بادئة:

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ⊕
    # i becomes 0
    i ⊖
}
```

## Collections

لدى Faber عدة أنواع مجموعات مملوكة للمترجم. طرائقها القانونية
موجودة في المترجم، وليس في المكتبة القياسية.

### Lista — مجموعة ديناميكية مرتبة {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

النشر باستخدام `sparge`:

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

الطرائق الرئيسية: `longitudo`، `accipe`، `appende`، `summa`، `primus`، `novissimus`.

### Tabula — خريطة مفتاح-قيمة {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

### Tensor — مصفوفة كثيفة ثابتة الشكل {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

تبسيط Tensor (للأكواد ذات الحسابات العددية الكثيفة):

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

الطرائق الرئيسية: `forma`، `accipe`، `ponde`، `crea`، `structa`، `strue`،
بالإضافة إلى الحساب العنصري، وضرب المصفوفات (`multiplicatio`)،
والاختزالات (`summa`، `productum`).

### Sparsa — مصفوفة متفرقة ثابتة الشكل {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

التحويل بين الكثيف والمتفرق:

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

### Cursors — تيارات كسولة {#cursors}

`cursor<T>` هو نوع تيار كسول. يُنشأ من مكررات المجموعات،
أو مناظير tuus، أو دوال مولدة. يُستهلك عبر `itera ex`:

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

### Intervallum — نطاقات {#intervallum}

```faber
# exclusive range: 0, 1, 2, 3, 4
itera ab 0‥5 fixum i {
    nota i
}
# inclusive range: 0, 1, 2, 3, 4, 5
itera ab 0…5 fixum i {
    nota i
}
```

`‥` هو حد نطاق حصري؛ `…` هو حد شامل.

## String and template literals

تستخدم Faber دلالات المحددات — كل صيغة اقتباس تعني شكل مصدر مختلف. وهي ليست مرادفات قابلة للتبادل.

### الصيغ الحرفية {#literal-forms}

| الصيغة | النوع | الدور |
|------|------|------|
| `'…'` | `ascii` | رموز آلية ثابتة؛ لا `§`؛ لا `(…)` |
| `"…"` | `textus` | سلاسل يونيكود نصية قصيرة؛ `(…)` يُنتِج |
| `«…»` | `textus` | يونيكود كتلي/متعدد الأسطر؛ `(…)` يُنتِج |
| `` `…` `` | `forma` | قوالب مأسورة؛ `(…)` يأسر |
| `{ … }` | `json` | وثيقة JSON في زمن الترجمة |
| `|…|` | `octeti` | بايتات سداسية عشرية في زمن الترجمة |
| `[ … ]` | `lista<T>` | قيمة حرفية من نوع قائمة Faber |

### تطبيق قالب السلسلة النصية {#string-template-application}

تُنسّق Faber النص عبر تطبيق قالب السلسلة النصية: قيمة حرفية `"…"` أو `«…»`
تحتوي ثقوب `§`، ثم وسيطات بين قوسين:

```faber
functio greet(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}

fixum numerus pagina ← 3
fixum numerus totum ← 10
fixum textus code ← "200"
fixum textus label ← "OK"

fixum _ msg ← "Page § of §"(pagina, totum)
fixum _ block ← «status: § (§)»(code, label)
```

القواعد الأساسية:
- `§` (U+00A7) هو ثقب القالب
- الثقوب الموضعية: `§0`، `§1`، … للترتيب الصريح
- اللاحقة `!` تختار تنسيق العرض: `"Salve, §!"(nomen)`
- ملحقة `(وسائط)` هي تطبيق قالب، وليس استدعاء دالة

### السلاسل النصية الكتلية {#block-strings}

تستخدم الكتل متعددة الأسطر علامات التنصيص المزدوجة `«…»`:

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

### القوالب المأسورة (forma) {#captured-templates}

تأسر قوالب الفاصلة العليا المائلة النص والوسائط دون إنتاج.
آمنة للحمولات المقيّدة SQL/URL:

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

### JSON المُضمّن {#inline-json}

الصيغة المجردة `{ … }` هي JSON مُضمّن: وثيقة `json` في زمن الترجمة، وليست
كائن Faber مجهول. المفاتيح هي سلاسل نصية بين علامتي تنصيص مفصولة بـ `:`:

```faber
fixum _ empty ← {}
fixum _ user ← { "name": "Marcus", "age": 30, "active": true }
fixum _ nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
```

لبناء genus مُنمّط، استخدم اسم النوع وشكل الحقل `=`:

```faber
genus Point {
    numerus x
    numerus y
}
fixum _ p ← Point { x = 10, y = 20 }
```

## Nullability and optionality

تُميِّز Faber بين غياب القيمة وتوفيرها الاختياري في موقع الإعلان.

### القيم القابلة للعدم — T ∪ nihil {#nullable-values}

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

### فتحات الإعلان الاختيارية — sponte {#optional-declaration-slots}

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

### تأكيد عدم العدم — ! {#non-null-assertion}

استخدِم `!.` و `![` و `!(` لتأكيد أن القيمة القابلة للعدم ليست `nihil`:

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

يؤدي تأكيد عدم العدم على `nihil` إلى إجهاض التنفيذ وقت التشغيل.

### الدمج العدمي — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

### ignotum {#ignotum}

`ignotum` هو النوع غير المعروف عالي المستوى لمخارج الطوارئ والمعرفة غير
المكتملة. وهو ليس آليةً للتعامل مع العدم.

## Conversion and construction

عاملَا تحويل مهمّان: أحدهما لوقت التشغيل والآخر لوقت الترجمة:

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus value ← 7
fixum _ text ← value ∷ textus
```

### التحويل وقت التشغيل — ↦ {#runtime-conversion}

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

### الإسناد الثابت — ∷ {#static-ascription}

استعمل `∷` للإسناد الثابت الصريح للنوع. هو لاحق وموجّه بالنوع الهدف:

```faber
fixum numerus value ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

### الدمج العدمي — vel {#nullish-coalescing}

استعمل `vel` للدمج العدمي حينما تكون القيمة `nihil`:

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
