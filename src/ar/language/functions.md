+++
translation_kind = "translated"

title = "Functions and control flow"
section = "language"
order = 3
sources = [
  "radix/README.md (Language Orientation, Borrowing and Mutability, How Faber Feels)",
  "examples/corpus/functio/",
  "examples/corpus/de/",
  "examples/corpus/in/",
  "examples/corpus/ex/",
  "radix/docs/design/semantic-ownership.md",
  "radix/README.md (Control Flow Shape, Canonical Surface)",
  "examples/corpus/si/",
  "examples/corpus/itera/",
  "examples/corpus/dum/",
  "examples/corpus/custodi/",
  "examples/corpus/discerne/",
  "examples/corpus/elige/",
  "radix/README.md (Type and Size Generics)",
  "examples/corpus/generic/",
  "examples/corpus/functio/generic-call-type-args.fab",
]
+++

## Functions

الدوال في Faber تُصرَّح باستخدام `functio`، مع صيغة المعاملات بذكر النوع أولاً ونوع الإرجاع برمز.

### الصيغة الأساسية {#basic-syntax}

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

### أمثلة {#examples}

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

### قيم الإرجاع {#return-values}

استخدم `redde` للإرجاع العادي:

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

`redde` مجردة لنوع الإرجاع `vacuum`:

```faber
functio tace() → vacuum {
    redde
}
```

### الاستعارة وقابلية التعديل (de, in, ex) {#borrowing-and-mutability}

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

### نقطة الدخول {#entry-point}

نقطة دخول البرنامج هي `incipit`:

```faber
incipit {
    nota "ingressus"
}
```

### نقطة دخول CLI {#cli-entry-point}

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

### وضع التمرير — `sponte` {#passing-mode-sponte}

`sponte` تُعلِّم معاملًا يمكن للمستدعي حذفه:

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```

## Control flow

### التفرّع الشرطي {#conditional-branching}

#### si / sin / secus {#si-sin-secus}

```faber
incipit {
    fixum _ condition ← verum
    si condition {
        # truthy branch
        nota "matched"
    }
}
```

مع فروع else-if و else:

```faber
incipit {
    fixum _ score ← 85
    si score ≥ 90 {
        nota "A"
    } sin score ≥ 80 {
        nota "B"
    } secus {
        nota "C"
    }
}
```

#### التفرّع المُدمَج باستخدام ergo {#compact-branch-with-ergo}

يستخدم جسم التفرّع ذو العبارة الواحدة `ergo`:

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    si ready ergo redde value
    redde nihil
}
```

### التكرار {#iteration}

#### القيم — itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ergo redde item
    }
    redde nihil
}
```

#### المفاتيح — itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

#### النطاق — itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

### حلقات طالما {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

### أقسام الحارس — custodi {#guard-sections-custodi}

يُجمّع `custodi` فحوصات الخروج المُبكّر قبل جسم الدالة الرئيسي.
كل عبارة `si` هي حارس تسلسلي:

```faber
functio divide(numerus a, numerus b) → numerus {
    custodi {
        si b ≡ 0 {
            redde 0
        }
    }
    redde a / b
}
```

`custodi` غير قابل للكسر في الإصدار 1 — إنه سور حماية، وليس حلقة.

### مطابقة الأنماط — elige {#pattern-matching-elige}

يختار `elige` أول ذراع مُطابِق:

```faber
functio describe(numerus value) → textus {
    elige value {
        casu 1 { redde "one" }
        casu 2 { redde "two" }
        ceterum { redde "many" }
    }
}
```

### مطابقة الاتحادات المُوسَمة — discerne {#tagged-union-matching-discerne}

يُطابِق `discerne` متغيرات `discretio` بشكل شامل:

```faber
discretio Exitus {
    Bonum { textus nuntius },
    Malum { textus causa }
}

functio refer(Exitus eventus) → textus {
    discerne eventus {
        casu Bonum fixum nuntius { redde nuntius }
        casu Malum fixum causa { redde "Error: §"(causa) }
    }
}
```

### كتل المحاولة — fac / cape {#try-blocks-fac-cape}

يفتح `fac` كتلة قد ترمي استثناءً، ويستردّ `cape` السيطرة:

```faber
functio divide(numerus a, numerus b) → numerus {
    redde a / b
}

functio tutus(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    } cape err {
        mone err
        redde 0
    }
}
```

## Generics

الدوال وأسماء الأنواع المستعارة و`genus` و`implendum` تقبل وسائط النوع باستخدام الصيغة `<T>`.

### الدوال العمومية {#generic-functions}

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

### وسائط النوع الصريحة في موقع الاستدعاء {#explicit-callsite-type-arguments}

```faber
functio identitas<T>(T valor) → T { redde valor }

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde nihil
}

fixum _ value ← identitas<numerus>(7)
fixum _ maybe ← primum<numerus>([value])
```

### الأنواع العمومية {#generic-genus}

```faber
genus Par<T> {
    T primus
    T secundus
}
```

### وسائط الحجم {#size-parameters}

يُعلن `magnitudo` عن وسيط حجم/فهرس في قوائم الوسائط العمومية:

```faber
functio crea<T, magnitudo N>() → tensor<T, [N]> {
    redde vacua
}
```
