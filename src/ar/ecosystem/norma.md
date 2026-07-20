+++
translation_kind = "translated"

title = "Norma standard library"
section = "ecosystem"
order = 1
sources = [
  "radix/README.md (Standard Library section)",
  "sibling norma/ repository",
  "norma/exempla/",
  "radix/docs/stdlib/morphologia.md",
]


prose_hash = "sha256:f333d0ee78b78e5ad3ebfb1bfdda0a4069a9b7daf3579d8c55d6b83c668be833"
code_hash = "sha256:0ef63774f36a5e950889dcae691b2a9c5add05fe03c89c061ba60d829195f2ff"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
نورما هي المكتبة القياسية للغة Faber. توفّر وحدات مسطّحة ذات أسماء لاتينية
يُوصَل إليها عبر المسارات `norma:*`. تصريحات المكتبة القياسية هي شيفرة Faber
مصدرية ضمن مستودع `norma` الشقيق.

## الوحدات {#modules}

| الوحدة | المجال |
|--------|--------|
| `norma:solum` | عمليات نظام الملفات |
| `norma:solum/path` | عمليات مسارات خالصة |
| `norma:http` | عميل HTTP |
| `norma:processus` | تنفيذ العمليات |
| `norma:consolum` | الإدخال والإخراج الطرفي (stdin, stdout, stderr) |
| `norma:json` | تحليل JSON وتسلسله |
| `norma:toml` | تحليل TOML |
| `norma:yaml` | تحليل YAML |
| `norma:valor` | تنقّل الترميز |
| `norma:tensor` | مساعدات جسر الموترات |
| `norma:tempus` | الوقت والمدة |
| `norma:aleator` | العشوائية |

## اصطلاح تسمية Morphologia {#morphologia-naming-convention}

تتّبع Norma سياسة morphologia في جميع أسماء الدوال. يحمل تصريف
الفعل اللاتيني نمط التنفيذ:

| الجذر | متزامن | غير متزامن | المعنى |
|------|------|-------|---------|
| `leg-` | `lege` | `leget` | قراءة |
| `scrib-` | `scribe` | `scribet` | كتابة |
| `quaer-` | — | `quaeret` | استعلام (محدود) |
| `quaer-` | — | `quaerent` | استعلام (تدفّق) |

أزواج الملكية (تعديل مقابل نسخ خارجي):

| تعديل | نسخ خارجي | المعنى |
|--------|----------|---------|
| `adde` | `addita` | إضافة |
| `inverte` | `inversa` | عكس |
| `filtra` | `filtrata` | تصفية |

## الاستعمال {#usage}

```faber locale=la
importa ex "norma:solum" privata solum

functio legeConfig() → textus {
    redde solum.lege("config.toml")
}
```
