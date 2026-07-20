+++
translation_kind = "translated"


title = "Control flow"
section = "syntax"
order = 4
sources = [
  "radix/README.md (Control Flow Shape, Canonical Surface)",
  "examples/corpus/si/",
  "examples/corpus/itera/",
  "examples/corpus/dum/",
  "examples/corpus/custodi/",
  "examples/corpus/discerne/",
  "examples/corpus/elige/",
]



prose_hash = "sha256:a3b4f77dd7b65f73e835e9e2f65070f22930ad14df15c71a262b81113827a814"
code_hash = "sha256:e257a14fcd068ec06da9199895e899ffb03f352663185ce892b355beadb5cd0b"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
## التفرّع الشرطي {#conditional-branching}

### si / sin / secus {#si-sin-secus}

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

### التفرّع المُدمَج باستخدام ergo {#compact-branch-with-ergo}

يستخدم جسم التفرّع ذو العبارة الواحدة `ergo`:

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    si ready ergo redde value
    redde nihil
}
```

## التكرار {#iteration}

### القيم — itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ergo redde item
    }
    redde nihil
}
```

### المفاتيح — itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

### النطاق — itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

## حلقات طالما {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

## أقسام الحارس — custodi {#guard-sections-custodi}

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

## مطابقة الأنماط — elige {#pattern-matching-elige}

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

## مطابقة الاتحادات المُوسَمة — discerne {#tagged-union-matching-discerne}

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

## كتل المحاولة — fac / cape {#try-blocks-fac-cape}

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
