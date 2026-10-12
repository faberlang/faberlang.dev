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

<<<FENCE 0>>>
