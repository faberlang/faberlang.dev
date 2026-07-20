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
Faber تمتلك ثلاث كلمات مفتاحية للمتغيرات ورمز تخصيص مخصص. الفرق الأساسي
هو بين `fixum` (كتابة مرة واحدة) و `varia` (قابل لإعادة التخصيص بحرية)،
وبين `←` (تدفق وقت التشغيل) و `=` (شكل الحقل الهيكلي).

## fixum — ربط غير قابل للتغيير {#fixum-immutable-binding}

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

## varia — ربط قابل للتغيير {#varia-mutable-binding}

روابط `varia` قابلة لإعادة التخصيص بحرية:

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

## sit — اختصار للربط غير القابل للتغيير مع استنتاج النوع {#sit-inferred-immutable-sugar}

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

## الربط وقت التشغيل مقابل التعريف الهيكلي {#runtime-binding-vs-structural-definition}

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

## استخراج الحقول باستخدام ex {#ex-field-extraction}

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

## الزيادة والنقصان اللاحقة {#postfix-increment-and-decrement}

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
