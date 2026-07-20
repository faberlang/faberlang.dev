+++
translation_kind = "translated"

title = "Functions"
section = "syntax"
order = 3
sources = [
  "radix/README.md (Language Orientation, Borrowing and Mutability, How Faber Feels)",
  "examples/corpus/functio/",
  "examples/corpus/de/",
  "examples/corpus/in/",
  "examples/corpus/ex/",
  "radix/docs/design/semantic-ownership.md",
]


prose_hash = "sha256:ccb89a2cbb2274f10a9cf14807cb355ac88f2a65ac03fb0a5d6cea62f999df28"
code_hash = "sha256:c87e3ad8847578d6410ecd0d2147894a502f9700487a2d53bf6e86334209d5ad"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
الدوال في Faber تُصرَّح باستخدام `functio`، مع صيغة المعاملات بذكر النوع أولاً ونوع الإرجاع برمز.

## الصيغة الأساسية {#basic-syntax}

```faber
functio twice(numerus n) → numerus {
    redde n
}
```

مع قناة أخطاء:

```faber
functio parse(textus input) → numerus ⇥ textus {
    redde 0
}
```

## أمثلة {#examples}

```faber
# No parameters, no return
functio saluta() {
    nota "Salve, Mundus!"
}

# Parameter, no explicit return
functio dic(textus verbum) {
    nota verbum
}

# Parameter and return type
functio duplica(numerus n) → numerus {
    redde n * 2
}

# Multiple parameters
functio adde(numerus a, numerus b) → numerus {
    redde a + b
}
```

## قيم الإرجاع {#return-values}

استخدم `redde` للإرجاع العادي:

```faber
functio porta(numerus x) → numerus {
    si x < 0 ∴ redde 0
    redde x * 2
}
```

`redde` مجردة لنوع الإرجاع `vacuum`:

```faber
functio tace() → vacuum {
    redde
}
```

## الاستعارة وقابلية التعديل (de, in, ex) {#borrowing-and-mutability}

يُحدد Faber كيفية تمرير القيمة باستخدام حروف جر قصيرة على المعاملات:

| العلامة | الغرض | التخفيض النموذجي إلى Rust |
|---------|-------|--------------------------|
| *(بدون)* | قيمة مملوكة | `T` بالقيمة |
| `de` | استعارة مشتركة (للقراءة فقط) | `&T` |
| `in` | استعارة قابلة للتعديل | `&mut T` |
| `ex` | استهلاك (نقل إلى الدالة المستدعاة) | `T` بالنقل |

```faber locale=la
# Shared borrow
functio imprime(de textus label) → vacuum {
    nota label
}

# Mutable borrow
functio duplica(in numerus value) → vacuum {
    value ← value * 2
}

# Consume
functio consume(ex textus buffer) → textus {
    redde buffer
}

# Owned
functio salve(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}
```

الكلمات نفسها (`de`, `ex`) تُعاد استخدامها في تراكيب أخرى — لا تقرأ كل `ex` بمعنى "استهلاك":

| السياق | الدور |
|--------|-------|
| `de textus name` على معامل | استعارة مشتركة |
| `in numerus count` على معامل | استعارة قابلة للتعديل |
| `ex textus buffer` على معامل | نقل إلى الدالة المستدعاة |
| `itera ex items fixum item` | تكرار على القيم |
| `itera de tabula fixum key` | تكرار على المفاتيح |
| `ex source fixum x, ceteri rest` | تفكيك الحقول |
| `importa ex "path"` | استيراد من وحدة |

## نقطة الدخول {#entry-point}

نقطة دخول البرنامج هي `incipit`:

```faber
incipit {
    nota "ingressus"
}
```

## نقطة دخول CLI {#cli-entry-point}

بالنسبة لبرامج CLI، تستقبل `incipit argumenta` معاملات سطر الأوامر المُحلَّلة:

```faber locale=la
@ cli "echo"
@ descriptio "Prints text"
@ operandus ceteri textus words
incipit argumenta args {
    itera ex args.words fixum word {
        nota word
    }
}
```

## وضع التمرير — `sponte` {#passing-mode-sponte}

`sponte` تُعلِّم معاملًا يمكن للمستدعي حذفه:

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```
