+++
translation_kind = "translated"

title = "Inline testing"
section = "features"
order = 7
sources = []


prose_hash = "sha256:85bf7bf8e3bbf81859e9163f3f1898d0a41aa347101b4ea5a299599abf47f756"
code_hash = "sha256:5c17d1f1d1850fa59128bd6e4a57dce82f2b3ef4be816ff3f5d7275481335af9"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
تمتلك Faber إطار عمل اختبارات من الدرجة الأولى مدمجًا في اللغة بثلاث كلمات
مفتاحية: `probandum` تُعلن عن مجموعة اختبارات، و`proba` تُعلن عن حالة اختبار
مفردة، و`adfirma` تؤكد صحة شرط. تعيش الاختبارات في نفس الملف مع الشيفرة التي
تختبرها، وتُشغَّل عبر `faber test`، وتدعم نفس خط أنابيب التصريف الخاص بشيفرة
الإنتاج — واعية بالإعدادات المحلية، مدققة الأنواع، ومتعددة الأهداف.

## الكلمات المفتاحية الثلاث {#keywords}

| الكلمة المفتاحية | الدور | المكافئ التقريبي |
|------------------|-------|------------------|
| `probandum` | تُعلن عن مجموعة اختبارات مسماة | `describe`، `#[cfg(test)] mod` |
| `proba` | تُعلن عن حالة اختبار مفردة | `it`، `#[test]` |
| `adfirma` | تؤكد صحة شرط أثناء التنفيذ | `assert!`، `assert_eq!` |

### probandum — مجموعة الاختبارات {#probandum-test-suite}

تجمّع كتلة `probandum` حالات الاختبار المرتبطة ببعضها. يمكن تداخل المجموعات
لتنظيم الاختبارات بشكل هرمي:

```faber
probandum "arithmetica" {
    proba "unum plus unum" {
        adfirma 1 + 1 ≡ 2
    }

    proba "multiplicatio" {
        adfirma 3 * 4 ≡ 12
    }

    probandum "implicata" {
        proba "comparatio" {
            fixum _ x ← 10
            adfirma x ≥ 10
        }
    }
}
```

### proba — حالة الاختبار {#proba-test-case}

تحتوي كتلة `proba` على منطق الاختبار. يمكنها استخدام أي شيفرة Faber —
ارتباطات المتغيرات، استدعاءات الدوال، تدفق التحكم — وتنتهي بتأكيد `adfirma`
واحد أو أكثر. يمكن وسم الاختبارات بعلامة `tag` اختيارية للتنفيذ الانتقائي:

```text
proba "echo formats operands with one space" tag "coreutils" {
    adfirma echo_textus(["hello", "world"]) ≡ "hello world"
}
```

### adfirma — التأكيد {#adfirma-assertion}

تقيّم `adfirma` تعبيرًا منطقيًا وتُبلغ عن الفشل إذا كان خاطئًا. توفر رسالة
نصية اختيارية سياقًا عند الفشل:

```faber
incipit {
    fixum _ x ← 10

    # Simple assertion
    adfirma x > 0

    # With custom message
    adfirma x ≡ 10, "x decem esse debet"

    # Multiple assertions in sequence
    fixum _ nomen ← "Marcus"
    adfirma nomen ≡ "Marcus"
    adfirma nomen ≠ "", "nomen vacuum non sit"
}
```

## سير العمل {#workflow}

تُشغَّل الاختبارات عبر الأمر `faber test`:

```text
faber test                        # run all tests in the current package
faber test examples/coreutils/packages/echo  # run tests for a specific package
```

لأن الاختبارات تعيش جنبًا إلى جنب مع المصدر في نفس ملف `.fab`، فلا يوجد هيكل
مجلدات منفصل للاختبارات، ولا إعلان لوحدة اختبارات، ولا تمييز في سكربت البناء
بين بنائي الاختبار والإنتاج. يعرف المصرف أي الكتل هي شيفرة اختبار وأيها شيفرة
إنتاج من خلال الكلمات المفتاحية المستخدمة — تُحلَّل `probandum` و`proba` لكنها
تُستبعد من بنائي الإنتاج.

## مثال من العالم الحقيقي {#real-world}

توضح حزمة `echo` في coreutils إطار عمل الاختبارات عمليًا. تعيش الاختبارات في
نفس ملف التنفيذ، وتغطي تحليل الخيارات، توسيع الرموز الخاصة، والحالات الحدية:

```text
probandum "echo formatting" tag "coreutils" {
    proba "empty operands format as empty text" {
        fixum lista<textus> words ← vacua
        adfirma echo_textus(words) ≡ ""
    }

    proba "single operand is unchanged" {
        adfirma echo_textus(["hello"]) ≡ "hello"
    }

    proba "-E is a leading no-op option" {
        adfirma echo_textus(["-E", "hello", "world"]) ≡ "hello world"
    }

    proba "-n suppresses the trailing newline flag" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }

    proba "-e expands the declared escape subset" {
        adfirma echo_textus(["-e", "a\\nb"]) ≡ "a\nb"
        adfirma echo_textus(["-e", "a\\tb"]) ≡ "a\tb"
    }
}
```

## ملاحظات التصميم {#design}

تميز عدة خيارات تصميمية إطار اختبارات Faber عن النهج التقليدية:

- **لا يوجد ثنائي اختبار منفصل.** الاختبارات هي تصريحات في نفس ملف المصدر، وليست هدف تصريف منفصل. يصفي المصرف كتل الاختبار من مخرجات الإنتاج.
- **الوسوم، وليس المجلدات.** تُنظم الاختبارات بعلامات `tag` بدلًا من هيكل المجلدات. يمكن للاختبار الانتماء إلى عدة محاور تنظيمية دون نقله.
- **خط أنابيب تصريف كامل.** الاختبارات مدققة الأنواع، محللة، وواعية بالإعدادات المحلية — نفس علم `--reader-locale` ينطبق على مخرجات الاختبار.
- **متعدد الأهداف.** تشغّل الاختبارات عبر أي خلفية يستهدفها الرزمة — مُنفّذ MIR لـ `faber test --interpret`، وRust مصرف لـ `faber test`.
- **مجموعات متداخلة.** يمكن تداخل كتل `probandum`، معكسةً هيكل الشيفرة التي تختبرها.

## المراجع {#references}

1. `examples/corpus/probandum/` — ملفات probandum النموذجية
2. `examples/corpus/proba/` — ملفات proba النموذجية
3. `examples/corpus/adfirma/` — ملفات adfirma النموذجية
4. `examples/coreutils/packages/echo/src/main.fab` — استخدام واقعي مع الوسوم
