+++
translation_kind = "translated"

title = "String and template literals"
section = "syntax"
order = 8
sources = [
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
]


prose_hash = "sha256:61bc93552e4a6ccc2a3a51453c146c31eee8331c6e82a3b17de5bc70f4ce24b0"
code_hash = "sha256:e7cba6e75a702466f92ecdbaa2c9d777b027a09a7f1b0414387cc746376d3075"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
تستخدم Faber دلالات المحددات — كل صيغة اقتباس تعني شكل مصدر مختلف. وهي ليست مرادفات قابلة للتبادل.

## الصيغ الحرفية {#literal-forms}

| الصيغة | النوع | الدور |
|------|------|------|
| `'…'` | `ascii` | رموز آلية ثابتة؛ لا `§`؛ لا `(…)` |
| `"…"` | `textus` | سلاسل يونيكود نصية قصيرة؛ `(…)` يُنتِج |
| `«…»` | `textus` | يونيكود كتلي/متعدد الأسطر؛ `(…)` يُنتِج |
| `` `…` `` | `forma` | قوالب مأسورة؛ `(…)` يأسر |
| `{ … }` | `json` | وثيقة JSON في زمن الترجمة |
| `|…|` | `octeti` | بايتات سداسية عشرية في زمن الترجمة |
| `[ … ]` | `lista<T>` | قيمة حرفية من نوع قائمة Faber |

## تطبيق قالب السلسلة النصية {#string-template-application}

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

## السلاسل النصية الكتلية {#block-strings}

تستخدم الكتل متعددة الأسطر علامات التنصيص المزدوجة `«…»`:

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

## القوالب المأسورة (forma) {#captured-templates}

تأسر قوالب الفاصلة العليا المائلة النص والوسائط دون إنتاج.
آمنة للحمولات المقيّدة SQL/URL:

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

## JSON المُضمّن {#inline-json}

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
