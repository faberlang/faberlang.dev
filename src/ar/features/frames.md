+++
translation_kind = "translated"

title = "Capability calls and frames"
section = "features"
order = 3
sources = []


prose_hash = "sha256:73113e85aed18df405d85a15f57dbf3cc159c46fc6619396ab03a18bcf29007f"
code_hash = "sha256:85216f4b5f4405e693c3b4f1e237565bc609da16172a0225ff18098fe6397ce4"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
*الدرز بين Faber وكل طريقة يمكن لنظام التشغيل بها تنفيذ الإدخال/الإخراج.*

`ad` هو بدائي استدعاء القدرة منخفض المستوى في Faber — الحد الفاصل
بين كود Faber والعالم الخارجي. يفتح محادثة مُنمَّطة
(`sermo`) مع مورد مضيف يُعرَّف بسلسلة مسار، ثم
يتبادل إطارات مهيكلة (`scrinium`) عبر أنصاف تيارات موجَّهة.
يُرسل نواة المضيف كل مسار إلى صندوق مزود قابل للتوصيل، والذي
ينفذ الإدخال/الإخراج الفعلي — نظام الملفات، الشبكات، الطرفية، الوقت، العشوائية،
أو أي شيء آخر يمكن لنظام التشغيل فعله.

## بدائي `ad` {#ad}

`ad` كلمة مفتاحية، وليس دالة. يفتح محادثة معتمة
مع مسار يُسمَّى بثابت `ascii` وبيانات افتتاحية اختيارية:

```text
# Simple materialized call: open, send opener, drain response
fixum textus content ← ad 'solum:lege' ("config.toml") ↦ textus

# Typed conversation handle for streaming interaction
fixum sermo s ← ad 'processus:curre' ("ls", ["-la"])
```

تتبع سلسلة المسار نمط `prefix:verb`. تطابق نواة المضيف
على **البادئة فقط** — يمتلك المزود كل الأفعال تحت تلك
البادئة:

```text
solum:lege   ─┐
solum:modum  ─┼─►  prefix "solum"  ──►  solum provider crate
solum:vincula─┘
```

`ad` ليس واجهة دوال أجنبية. لا يستدعي دوال C،
ولا يحمّل مكتبات ديناميكية، ولا يضمّن تجميعًا مضمّنًا. إنه
حد تمرير رسائل مهيكل: يرسل Faber إطارات مُنمَّطة ويستقبل
إطارات مُنمَّطة، دون معرفة ما إذا كان المزود منفذًا بلغة Rust،
أو يعمل داخل العملية، أو يفوض إلى استدعاء نظام، أو يعيد التوجيه إلى مضيف بعيد.

## أنواع الإطارات {#types}

تشكل خمسة أنواع مملوكة للمصرّف نظام الإطارات:

| النوع | الدور | السطح الرئيسي |
|------|------|-------------|
| `sermo` | مقبض محادثة — تبادل ثنائي الاتجاه قيد التنفيذ | يُنشأ بواسطة `ad`؛ يُستنزف عبر `↦ T` أو يُقسَّم إلى مناظير |
| `scrinium<T>` | غلاف إطار — رسالة مهيكلة واحدة في محادثة | حقول: `id`، `call`، `status`، `data`، `created_ms`، `from`، `trace` |
| `status` | تعداد علامة دورة الحياة | `request`، `item`، `byte`، `bulk`، `done`، `error`، `cancel` |
| `meus<T>` | نصف تيار صادر — إرسال إطارات إلى المزود | `da(T)`، `fini() → status` |
| `tuus<T>` | نصف تيار وارد — استقبال إطارات من المزود | `accipe()`، `cursor()`، `exhauri()`، `fini()` |

### استخدام المناظير الموجهة {#using-directional-views}

```text
# Open a conversation, get directional views
fixum sermo s ← ad 'solum:scribe' ("output.txt")
fixum meus<textus> out ← s.meus<textus>()
fixum tuus<textus> input ← s.tuus<textus>()

# Send content frames
out.da("line one")
out.da("line two")
out.fini()

# Read response frames
itera ex input.cursor() fixum frame {
    nota frame.data
}
fixum status inbound ← input.fini()
```

### التجسيد البسيط {#simple-materialization}

للحالة الشائعة — فتح، إرسال بيانات افتتاحية، استنزاف كل إطارات الاستجابة إلى قيمة
واحدة — يطوي `sermo ↦ T` المحادثة:

```text
# Read a file: open + drain into textus
fixum textus body ← ad 'solum:lege' ("config.toml") ↦ textus

# Parse JSON from an HTTP response
fixum json data ← ad 'http:peti' ("https://api.example.com/data") ↦ json
```

يستخدم التجسيد جامعًا موجَّهًا بالنوع: `↦ textus`
يربط كل الإطارات الواردة، `↦ json` يحلل الحمولة المربوطة،
`↦ lista<T>` يجمع الإطارات في قائمة.

## مزودو المضيف {#providers}

تُنفذ عائلات التأثير كصناديق مزود منفصلة تحت
`faberlang/host-providers-rs`. يمتلك كل مزود كل الأفعال تحت
بادئته:

| المزود | البادئة | نطاق الإدخال/الإخراج |
|----------|--------|------------|
| `solum` | `solum:*` | نظام الملفات: قراءة، كتابة، بيانات وصفية، عمليات الأدلة |
| `processus` | `processus:*` | تنفيذ العمليات: تشغيل، أنابيب، رموز خروج |
| `consolum` | `consolum:*` | إدخال/إخراج الطرفية: stdin، stdout، stderr |
| `tempus` | `tempus:*` | الوقت: الآن، إسبات، مؤقتات |
| `aleator` | `aleator:*` | العشوائية: إنتروبيا، توزيعات |
| `http` | `http:*` | عميل HTTP (المستوى د، عند الهبوط) |

المزودات صناديق منفصلة بتبعيَّاتها الخاصة — `solum`
لا يسحب HTTP، و`http` لا يسحب كود نظام الملفات.
يصدّر كل مزود دالة `register()` يستدعيها بيان
المضيف المُولَّد عند بدء التشغيل.

## مكدس الطبقات {#layers}

```text
Faber source:     ad 'solum:lege' (path) ↦ textus
Compiler:         sermo open + generic attach (no provider crate names)
Runtime:          HostDispatch + conversation protocol (faber-runtime)
Kernel:           route(frame) → provider for prefix
Provider:         solum provider reads file, returns content
```

يُصدر المصرّف إرسالًا عامًا — لا يضمّن أبدًا أسماء صناديق المزود
في الكود المُولَّد. يوفر وقت التشغيل `HostDispatch` وبروتوكول
المحادثة. توجه النواة (من `host-kernel-rs`)
الإطارات إلى المزود الصحيح بناءً على البادئة. ينفذ المزود (من
`host-providers-rs`) الإدخال/الإخراج الفعلي.

هذا يعني أن كود Faber المُولَّد **محايد تجاه المزود**. يمكن ربط نفس
الثنائي المجمَّع بتطبيقات مزود مختلفة — مزود
نظام ملفات حقيقي للإنتاج، ومزود وهمي للاختبار — بتغيير
بيان التجميع.

## بيان التجميع {#manifest}

يُتحكم في أي المزودات تُربط بواسطة بيان التجميع المُولَّد
وجدول `[dispatch]` في `faber.toml`:

```text
[target.rust]
host = "native"

[dispatch]
providers = ["solum", "processus", "consolum", "tempus", "aleator"]

[dispatch.providers.http]
enabled = true
```

أثناء التأليف، تنتج المزودات المفقودة خطأ وقت تشغيل `E_NO_ROUTE`.
في الوضع الصارم (مستقبلًا)، يجب أن يظهر كل بادئة `ad` في البرنامج
في بيان التجميع، ويتحقق المصرّف من أن بيان قدرة
المزود يغطي المسارات المستخدمة.

## المعمارية {#architecture}

تنقسم منصة المضيف عبر ثلاثة مستودعات في
منظمة `faberlang`:

| المستودع | الدور |
|------------|------|
| `host-kernel-rs` | موجِّه رفيع — يمتلك `Frame`، `Conversation`، دورة حياة الطرفية، إرسال البادئات، الأخطاء المهيكلة (`E_NO_ROUTE`)، تجميع بيان القدرة |
| `host-native-rs` | إرفاق أصلي — عمال، خطاف بدء `register_providers`، تكامل `host_register.rs` المُولَّد |
| `host-providers-rs` | تطبيقات المزود — مساحة عمل Cargo بصناديق لكل عائلة (`solum`، `processus`، إلخ) |

يمتلك كل صندوق مزود تبعيَّاته الأصلية الخاصة. يسحب مزود `http`
`hyper` و`tokio` فقط عند تمكين HTTP.
يستخدم مزود `solum` واجهات برمجة ملفات قياسية دون
تبعيات شبكة إضافية.

> **نفس المسار، أي مضيف.** لأن `ad` يرسل على سلاسل المسار والمزودات قابلة للتوصيل، يمكن لنفس مصدر Faber استهداف ثنائي أصلي (host-native-rs)، أو وقت تشغيل WASM (host-kernel كمحوّل Frame/Wasm)، أو عملية TypeScript Node.js (host-providers-ts) دون تغيير سطر واحد من كود Faber.

## مغلّفات Norma {#stdlib}

معظم كود Faber لا يستدعي `ad` مباشرة. تغلّف مكتبة Norma
القياسية مسارات `ad` الشائعة في دوال مُنمَّطة:

```text
# Norma wraps ad in typed, reviewed functions
functio lege(textus via) → textus {
    redde ad 'solum:lege' (via) ↦ textus
}

functio scribe(textus via, textus content) → vacuum {
    fixum vacuum _ ← ad 'solum:scribe' (via, content) ↦ vacuum
}

functio curre(textus command, lista<textus> args) → textus {
    redde ad 'processus:curre' (command, args) ↦ textus
}
```

توفر هذه الدوال المغلفة أمان الأنواع، والتوثيق، ومعالجة
الأخطاء دون إخفاء حقيقة أن الإدخال/الإخراج يعبر حد
`ad`. مغلفات Norma مفتوحة المصدر وتوجد تحت
`norma/src/`.

## المراجع {#references}

1. `radix/docs/design/frame-stream-types.md` — المواصفة الكاملة لـ sermo، scrinium، status، meus، tuus
2. `radix/docs/design/host-provider-gateway.md` — معمارية الموجه الرفيع، عقود المزود، بيان التجميع
3. `faberlang/host-kernel-rs/` — تطبيق موجه النواة
4. `faberlang/host-native-rs/` — الإرفاق الأصلي والتسجيل
5. `faberlang/host-providers-rs/` — صناديق المزود (solum، processus، consolum، tempus، aleator، http)
6. `examples/corpus/ad/` — ملفات أمثلة sermo
