+++
translation_kind = "translated"

title = "History"
section = "history"
order = 0
sources = []


prose_hash = "sha256:99390038c112db9d79c728a21f5bc2c804af48f6de648df7e6ff6f2f0bc32a99"
code_hash = "sha256:8cfe9c845ef9a1247454bc890937eafa78a38164428679c7a6981c3c8cf3b9c4"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
## الأصول {#origins}

أُجري أول التزام (commit) إلى مصرف راديكس (Radix) في **20 ديسمبر 2025**
كمشروع Bun + TypeScript مع ملف `docs/decisions.md` واحد. كرّس الالتزام الثاني
خمسة سجلات قرارات معمارية (ADR) ما تزال تُشكّل اللغة حتى اليوم.

**ADR-003**، بعنوان "نهايات الحالة تحمل دلالة معنوية،" أرسى منذ البداية
أن الصرف اللاتيني سيكون أكثر من مجرد غلاف للكلمات المفتاحية — سيفهم
المصرف الإعراب والتصريف ليستنبط قصد البرنامج. كانت تخطيطات الحالة الأصلية:

```text
Nominative  (subject)       →  return value, caller
Accusative  (direct object)  →  primary argument
Dative      (indirect obj.)  →  recipient, callback, destination
Genitive    (possession)     →  property access, "of" relationships
Ablative    (instrument)     →  dependencies, context, "using X"
```

أشارت الوثيقة نفسها: *"تصريف الأفعال سؤال متابعة طبيعي (زمن المستقبل → غير تزامني؟)."*
نمت هذه البذرة إلى اصطلاح التسمية الحديث **morphologia**، حيث تستعمل المكتبة
المعيارية صيغ الأفعال اللاتينية المصرّفة للإشارة إلى التزامني مقابل غير التزامني
والتحوير مقابل النسخ الخارجي — دون أن يُطلب من المصرف نفسه فهم قواعد اللغة اللاتينية.

بدأ المشروع بلغة TypeScript، ثم أُعيدت كتابته لاحقًا بلغة Rust، وجُمّدت القواعد
النحوية لخط الإصدار 1.x مع طبعة 2026. سجلات ADR الخمسة الأصلية (امتداد الملف
`.fab`، تلميحات الأخطاء، نهايات الحالة، محلل النزول التكراري، AST المخصص)
لا تزال مرئية في تاريخ git.

## الإصدارات {#releases}

أرشيفات CLI مُجمّعة مسبقًا — إصدار Faber الحالي في الأعلى، ثم كل وسم منشور
وثنائي من [faberlang/releases](https://github.com/faberlang/releases):

- **[الإصدارات](/history/releases.html)** — روابط التحميل وسجل المخزون التاريخي
- **[التثبيت والتحميل](/start/install.html)** — إعداد PATH وأول أمر `faber check`
