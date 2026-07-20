+++
translation_kind = "translated"

title = "Error handling"
section = "syntax"
order = 5
sources = [
  "radix/README.md (Return and Error Channels)",
  "examples/corpus/iace/",
  "examples/corpus/fac/",
  "examples/corpus/cape/",
  "radix/docs/design/failable-conversio.md",
]


prose_hash = "sha256:7b9b055ee1b8fc13b23faefb29514dd947982a0f768d911767255fdc0ee9f738"
code_hash = "sha256:81aa5174263eeb0a80a64870335680dec64748cbdb7896e4de78021d8c4f197f"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
فابر تفصل ثلاثة أفكار مترابطة تدمجها لغات كثيرة في شكل واحد:

| Construct | المعنى |
|-----------|--------|
| `→ T` | قناة عودة النجاح المعتادة |
| `T ∪ nihil` | غياب في نطاق قيمة النجاح |
| `⇥ E` | قناة خروج بديلة قابلة للاسترداد للأخطاء |

## عودة طبيعية {#normal-return}

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

## دوال قابلة للفشل {#failable-functions}

استخدم `⇥` حين يمكن لدالة أن تخرج عبر قناة خطأ:

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}
```

## رمي — iace {#throwing--iace}

`iace` ترسل قيمة على قناة الخطأ:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

## استرداد — fac / cape {#recovery--fac--cape}

يسترد المستدعون محليًا بكتلة `fac` ومعالج `cape`:

```faber
functio divide(numerus a, numerus b) → numerus {
    si b ≡ 0 {
        redde 0
    }
    redde a / b
}

functio tutum(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    }
    cape err {
        mone err
        redde 0
    }
}
```

لا يُعد الاستدعاء المباشر القابل للفشل تعبيرًا عاديًا. ضع استدعاءات
الدوال من النمط `→ T ⇥ E` داخل حدود `fac` / `cape` نشطة.

## استرداد تحويل مضمن {#inline-conversion-recovery}

يمكن لـ `⇥` أيضًا تحديد قيمة استرداد مضمنة على تحويلات `↦`:

```faber
fixum textus raw ← "42"
fixum _ n ← raw ↦ numerus ⇥ 0
```

## تأثير قابل للفشل فقط {#effectonly-failable}

للدوال التي تخطئ لكن لا تعيد قيمة نجاح، احذف `→ T`:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

## الحالة الراهنة {#current-status}

`→` و `redde` و `⇥` و `iace` و `fac` / `cape` هي أسطح نحوية ومدققة
حية. خفض Rust و Go لسلوك `⇥` / `iace` / `cape` الكامل وقت التشغيل لا
يزال فجوة خلفية — فهذه تجتاز فحص النمط لكنها لا تصدر بعد شيفرة وقت تشغيل
قابلة للفشل إلى كل الأهداف.
