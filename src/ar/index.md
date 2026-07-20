+++
translation_kind = "translated"

title = "Faber"
section = ""
order = 0
sources = []

prose_hash = "sha256:e63352acf54515593d9aeccf392881d72018d55e6b21d6e1ddd5a3979bef91b8"
code_hash = "sha256:a02ba6ea46d65efd212b09e097d3240402bfe1d46f89b993e389cd53ca1a9c9e"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
**Faber** هي لغة برمجة موجهة للحزم بمفردات سلوكية لاتينية، وقواعد نحوية منتظمة صغيرة، ونظام أنواع ثابت قائم على النوع أولاً. يُصرَّف المصدر عبر مصرف Radix إلى Rust قابل للمراجعة وثنائيات أصلية. الخاصية المعمارية المميزة لها هي أن المعنى يكمن في نواة دلالية — التمثيل الوسيط عالي المستوى (HIR) — بدلاً من أي تصيير معين.

الاسم مشتق من الكلمة اللاتينية التي تعني *صانع* أو *حرفي*. سُمي المصرف Radix، من الكلمة اللاتينية *جذر*. طُوِّرت اللغة بواسطة Ian Zepp وصدرت تحت رخصة MIT.

**جديد هنا؟** ابدأ بـ [التثبيت والتحميل](/start/install.html)، ثم شغّل مسار البداية المتسلسل: [مرحباً](/start/hello.html)، [الأوامر](/start/commands.html)، و[المشاريع](/start/projects.html).

## تحميل Faber 1.1.1 {#download}

الإصدار الحالي: **Faber 1.1.1** (الوسم `faber-v1.1.1`). أرشيفات CLI مُجمَّعة مسبقاً لأنظمة macOS و Linux؛ استخرج الثنائي `faber-v1.1.1-<target-triple>/faber` وضعه في `PATH` لديك.

| المنصة | الأرشيف | المجموع الاختباري |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [faber-v1.1.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

تثبيت سريع (مثال macOS arm64):

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.1.1-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

جميع ملاحظات الإصدار والموجودات: [github.com/faberlang/releases · faber-v1.1.1](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1).
خطوة بخطوة: [دليل التثبيت](/start/install.html). الجرد التاريخي الكامل:
[الإصدارات](/history/releases.html).

| | |
|---|---|
| **النمط** | موجه للحزم؛ تجهيز دلالي |
| **التحقق من الأنواع** | ثابت، النوع أولاً؛ يقبل القيمة الفارغة عبر `T ∪ لا شيء` |
| **الرموز** | `← → ∴ ≡ ∪ ⇥` |
| **صممها** | Ian Zepp |
| **أول ظهور** | 2024 |
| **المصرف** | Radix (Rust) |
| **المسارات** | تطبيقي (HIR) · أنظمة (MIR) |
| **الهدف الأساسي** | Rust → ثنائي أصلي |
| **لغات القارئ** | 7 مُصدَّرة (la, ar, hi, vi, th-TH, zh-Hans, zh-Hant) |
| **المكتبة القياسية** | Norma (`norma:*`) |
| **الرخصة** | MIT |

## ابدأ هنا {#start-here}

| المسار | لمن | ماذا |
|---|---|---|
| [التثبيت](/start/install.html) | بشري | تحميل، PATH، أول `faber check` |
| [مرحباً](/start/hello.html) | بشري | إنشاء وتشغيل `salve-munde` |
| [الأوامر](/start/commands.html) | بشري + وكيل | حلقة CLI اليومية: check, build, run, test, explain |
| [المشاريع](/start/projects.html) | بشري + وكيل | الانتقال من hello-world إلى حزم حقيقية |
| [جولة سريعة](/start/) | بشري | شكل اللغة في خمس دقائق |
| [أمثلة](/start/examples.html) | بشري + وكيل | حزم حقيقية: تطبيقات CLI، مساحة بريد، GPU، corpus |
| [`/llms.txt`](/llms.txt) | وكيل | فهرس آلي — ابدأ هنا إذا كنت نموذجاً |
| [دليل الوكيل](/agents/index.md) | وكيل | كيفية تعلم Faber وشحن حزمة |
| [مهارات الوكيل](/.well-known/agent-skills/index.json) | وكيل | أدلة مهارات مركزة (تثبيت، لغة، أمثلة، …) |

## حالة البوابة {#portal-status}

صفحة `/` هذه هي Speculum Porta للموقع الإنجليزي: نقطة دخول بلا لغة محلية توجه الأشخاص إلى صفحات التثبيت/البداية، وتوجه الوكلاء إلى الأسطح الآلية، وتوضح حالة حزمة اللغة المحلية دون تفاوض زمن المتصفح. المرحلة 7 هي إثبات جزئي متعدد اللغات، وليس موقعاً محلياً مكتملاً: فقط `th-TH`، `zh-Hans`، `zh-Hant`، `vi`، `ar`، و`hi` تمتلك شرائح بوابة/بداية مُنشأة بالإضافة إلى صفحات corpus مُنشأة، والنثر المؤلَّف لا يزال يرجع إلى الإنجليزية.

| اللغة المحلية | الحالة | ملاحظات |
|---|---|---|
| `la` | الموقع القانوني الحي | موقع إنجليزي/لاتيني مُنشأ بالكامل |
| `th-TH` | إثبات جزئي للمرحلة 7 | شريحة بوابة/بداية مُنشأة بالإضافة إلى corpus مُنشأ؛ نثر إنجليزي احتياطي؛ الوثائق الكاملة المؤلَّفة معلقة |
| `zh-Hans` | إثبات جزئي للمرحلة 7 | شريحة بوابة/بداية مُنشأة بالإضافة إلى corpus مُنشأ؛ نثر إنجليزي احتياطي؛ الوثائق الكاملة المؤلَّفة معلقة |
| `vi` | إثبات جزئي للمرحلة 7 | شريحة بوابة/بداية مُنشأة بالإضافة إلى corpus مُنشأ؛ نثر إنجليزي احتياطي؛ الوثائق الكاملة المؤلَّفة معلقة |
| `zh-Hant` | إثبات جزئي للمرحلة 7 | شريحة بوابة/بداية مُنشأة بالإضافة إلى corpus مُنشأ؛ نثر إنجليزي احتياطي؛ الوثائق الكاملة المؤلَّفة معلقة |
| `ar` | إثبات جزئي للمرحلة 7 | شريحة بوابة/بداية مُنشأة بالإضافة إلى corpus مُنشأ؛ نثر إنجليزي احتياطي؛ الوثائق الكاملة المؤلَّفة معلقة |
| `hi` | إثبات جزئي للمرحلة 7 | شريحة بوابة/بداية مُنشأة بالإضافة إلى corpus مُنشأ؛ نثر إنجليزي احتياطي؛ الوثائق الكاملة المؤلَّفة معلقة |

عينة حية باللاتينية القانونية:

```faber
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
```

انظر [لغة القارئ](/features/reader-locale.html) لنفس البرنامج الدلالي المُصيَّر عبر حزم التايلاندية، والصينية المبسطة، والصينية التقليدية، والعربية، والهندية، والفيتنامية.

## نظرة عامة {#overview}

صُممت Faber حول فكرة محورية: التمثيل الوسيط هو الحقيقة، ولا يتمتع أي هدف أو سطح لغة بشرية بامتياز. يمكن تصيير برنامج Faber مكتوب بكلمات لاتينية مفتاحية إلى كلمات تايلاندية، أو عربية، أو صينية مفتاحية عبر نفس الآلية التي تصيره إلى Rust، أو Go، أو WebAssembly — لأن HIR هو السلطة وكل مخرج هو *تصيير* له.

تتخذ اللغة ثلاثة خيارات إشارية متعمدة تعمل معاً:

- **تصريحات النوع أولاً** — يتجه الشكل نحو الربط: `نص nomen`، وليس `nomen: نص`.
- **كلمات سلوكية لاتينية** — التصريحات، والتعليمات، ودورة الحياة: `دالة`، `نوع`، `ثابت`، `أعد`، `إذا`.
- **رموز بنيوية** — تدفق القيم ووصلات الأنواع: `←` (ربط)، `→` (نوع الإرجاع)، `∴` (تفرع مضغوط)، `≡` (تساوي)، `∪` (اتحاد).

النتيجة هي مصدر ذو شكل نحوي مستقر يمكن مراجعته، وتحويله، وتخفيضه دون فقدان إحساس القارئ بالقصد.

## التوثيق {#documentation}

| القسم | الوصف |
|---|---|
| [التاريخ](/history/) | الجدول الزمني للتطوير، والتأثيرات، وتاريخ الإصدارات |
| [الإصدارات](/history/releases.html) | أحدث تحميل لـ Faber بالإضافة إلى كل وسم وثنائي منشور |
| [الميزات](/features/) | لغة القارئ، مسارات التصريف، المفردات اللاتينية، نظام الرموز، مبادئ التصميم |
| [الصياغة](/syntax/) | مرجع كامل: الأنواع، الدوال، تدفق التحكم، الأخطاء، العموميات، المجموعات |
| [الأدوات](/tooling/) | خط أنابيب مصرف Radix، واجهة Faber CLI، أهداف توليد الشيفرة، البرمجة النصية |
| [النظام البيئي](/ecosystem/) | Norma، Cista، Triga، coreutils، AI Workbench، corpus |
| [المدونة](/corpus/) | صفحات كلمات مفتاحية وبنى مُنشأة من المدونة العامة |
| [المراجع](/references/) | قواعد EBNF، وثائق التصميم، المستودعات |

## مثال سريع {#quick-example}

دالة بسيطة توضح أنماط Faber الأساسية — معاملات النوع أولاً، نوع إرجاع رمزي، اتحاد يقبل القيمة الفارغة، كلمات تحكم لاتينية:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## التصيير الحي {#live-rendering}

دالة divide أعلاه مُصيَّرة في الحزمة اللاتينية افتراضياً. يستطيع المصرف تصيير نفس البرنامج بسبع لغات قارئ — التايلاندية، والصينية المبسطة، والصينية التقليدية، والعربية، والهندية، والفيتنامية — كل منها يعيد تعيين الكلمات المفتاحية والأنواع إلى تلك اللغة بينما تبقى الرموز والمعرفات دون تغيير. هذه ليست طبقة ترجمة تُطبَّق على الصفحة؛ إنها نفس الآلية التي يستخدمها المصرف لإنتاج مصدر محلي.

انظر توثيق [لغة القارئ](/features/reader-locale.html) للنقاش الكامل.

## المستودعات {#repositories}

| المستودع | الدور |
|---|---|
| [faberlang/faber](https://github.com/faberlang/faber) | واجهة CLI العامة للمستخدم |
| [faberlang/releases](https://github.com/faberlang/releases) | موجودات الإصدارات الموسومة لـ CLI |
| [faberlang/faber-runtime](https://github.com/faberlang/faber-runtime) | أنواع وقت التشغيل لـ Rust المُنشأ |
| [faberlang/norma](https://github.com/faberlang/norma) | مصدر المكتبة القياسية |
| [faberlang/cista](https://github.com/faberlang/cista) | CLI/lib مخزن الحزم |
| [faberlang/triga](https://github.com/faberlang/triga) | مكتبة الرسوميات/الهندسة |
| [faberlang/examples](https://github.com/faberlang/examples) | المدونة، المسارات، حزم التطبيقات |
| [faberlang/faberlang.dev](https://github.com/faberlang/faberlang.dev) | موقع التوثيق هذا |
