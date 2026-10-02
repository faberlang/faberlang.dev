+++
title = "Arabic reader locale"
section = "locales"
order = 12
sources = [
  "radix/locale/<locale>/pack.toml",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

**العربية** — the `ar` reader pack. Script: Arabic; direction: right-to-left.

| Field | Value |
|---|---|
| **Locale code** | `ar` |
| **Native name** | العربية |
| **Script** | Arabic |
| **Direction** | right-to-left |

Right-to-left script written in logical order inside a left-to-right code block. HTML diagnostics wrap Arabic keywords in `<bdi>` so an error does not point at the wrong character.

## English ↔ Arabic {#mapping}

Generated from the packs; the canonical (Latin) name keys the full [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          العربية
| ---------------  --------------
| all              الكل
| and              و
| any              أي
| argmax           فهرس_الأكبر
| argmin           فهرس_الأصغر
| args             وسائط
| as               كـ
| assert           أكد
| async            غيرمتزامن
| async_generator  مولد_غيرمتزامن
| async_main       استهلال
| async_setup      سيهيئ
| async_teardown   سيلحق
| at               عند
| await            انتظر
| await_const      انتظر_ثابت
| await_var        انتظر_متغير
| before           قبل
| bench            قس
| between          بين
| break            اكسر
| call             اتصل
| case             حالة
| catch            التقط
| class            صنف
| cli              cli
| coalesce         عوض
| column           عمود
| command          أمر
| comptime         بادئة
| const            ثابت
| continue         تابع
| conversion       تحويل
| —                حوّل
| copy             نسخة
| count            العدّ
| cursor           cursor
| debug            شاهد
| default          افتراضي
| describe         مختبر
| description      وصف
| do               افعل
| elif             وإلاإذا
| else             وإلا
| embed            تضمين
| empty            فارغ
| enum             ترتيب
| errors           مخطئ
| exit             مخرج
| expect_failure   توقع_الفشل
| false            خطأ
| flaky            هش
| fn               دالة
| for              كرر
| format           حرر
| fragment         جزء
| free             حر
| from             من
| future           مستقبل
| generator        مولد
| global           عمومي
| guard            احرس
| if               إذا
| implements       حقق
| import           استورد
| interface        عقد
| internal         داخلي
| is               هو
| kernel           نواة
| lambda           إغلاق
| lane             مسار
| let              ليكن
| line             سطرا
| long             مفصل
| main             بداية
| match            طابق
| max              الأقصى
| min              الأدنى
| module           وحدة
| mut              في
| name             اسم
| nan              nan
| nihil            لاشيء
| not              ليس
| null             خال
| only             فقط
| only_in          حصري
| operand          معامل
| option           خيار
| optional         اختياري
| options          خيارات
| or               أو
| own              ملك
| panic            انهر
| pass             صمت
| per              حسب
| primus_quem      primus_quem
| print            اعرض
| private          خاص
| product          حاصل_الضرب
| protected        محمي
| public           عام
| radix            radix
| range            نطاق
| read             اقرأ
| readonly         ثابتة
| reduce           اختزل
| ref              عن
| reject           يرفض
| rename           إعادة_تسمية
| repeat           معاد
| require          يتطلب
| rest             باقي
| return           أعد
| return_await     أعد_منتظرا
| schema           مخطط
| self             ذات
| setup            جهز
| shared           commune
| short            مختصر
| size             حجم
| skip             أهمل
| spread           انشر
| static           سكوني
| step             كل
| sum              المجموع
| switch           اختر
| tag              وسم
| teardown         لاحق
| test             اختبر
| then             إذن
| thread           خيط
| throw            ارم
| throws           يرمي
| timeout          زمني
| todo             مستقبلي
| trap             فخ
| true             صواب
| tuple            توبل
| type             نمط
| ubi              ubi
| union            تمايز
| unstable         غير_مستقر
| until            حتى
| var              متغير
| variant          أنشئ
| vertex           رأس
| via              عبر
| warn             نبه
| while            طالما
| within           ضمن
| wrapping         حلقة
| write            اكتب
| yield            سلم
```

### Types {#types}

```text locale=la
| English      العربية
| -----------  ---------
| any          مهما
| ascii        أسكي
| atomic       ذري
| bool         منطقي
| byte         بايت
| bytes        بايتات
| census       تعداد
| channel      قناة
| char         حرف
| filter       مرشح
| float        كسر
| frame        إطار
| instant      لحظة
| int          عدد
| intervallum  فترة
| iterator     مؤشر
| json         جسون
| list         قائمة
| map          جدول
| matrix       مصفوفة
| never        أبدا
| none         نوع_لاشيء
| object       كائن
| promise      وعد
| queue        طابور
| record       ratio
| recv         استقبال
| regex        تعبير
| saturating   مشبع
| send         إرسال
| series       سلسلة
| set          مجموعة
| sparsa       متفرقة
| stack        مكدس
| string       نص
| tensor       موتر
| trapping     دقيق
| unknown      مجهول
| value        قيمة
| vector       متجه
| void         فراغ
| wrapping_ty  نوع_حلقة
```

### Intrinsics {#intrinsics}

```text locale=la
| English               العربية
| --------------------  ------------------
| abs                   القيمة_المطلقة
| add                   أضف
| added                 مضاف
| added_bias            مضاف_الانحياز
| all                   الكل
| any                   أي
| append                ألحق
| apply                 طبق
| approx                مقارب
| argmax                فهرس_الأكبر
| argmin                فهرس_الأصغر
| at_least              على_الأقل
| at_most               على_الأكثر
| bit_and               و_بت
| bit_and_assign        و_بت_إسناد
| bit_or                أو_بت
| bit_or_assign         أو_بت_إسناد
| ceiling               تقريب_لأعلى
| clamp                 قيد
| compare_exchange      قارن_وبدل
| complement            كمل
| complemented          مكمل
| contains              يحتوي
| cos                   جيب_التمام
| create                أنشئ
| cross                 الجداء_الاتجاهي
| cross_entropy         إنتروبيا_متقاطعة
| cumulate              تراكمي
| cursor                مؤشر
| delete                امسح
| densify               كثف
| difference            الفرق
| divide                اقسم
| divide                قسمة
| divided               مقسوم
| dot                   الجداء_النقطي
| drop                  أسقط
| end                   النهاية
| ends_with             ينتهي_ب
| escape                تهريب
| exchange              بدل
| exp                   الأسي
| fill                  املأ
| filter                رشح
| find                  ابحث
| find_all              ابحث_عن_الكل
| first                 الأول
| flatten               سطح
| flip                  اقلب
| flipped               مقلوب
| floor                 تقريب_لأسفل
| formata               formata
| from_flat             ابن_من_مسطح
| gather                اجمع_بالفهرس
| gelu                  gelu
| get                   اجلب
| greater               أكبر
| group                 مجموعة
| has                   يملك
| intersect             تقاطع
| intersection          التقاطع
| invert                معكوس
| is_empty              فارغ
| is_subset             مجموعة_جزئية
| is_superset           مجموعة_شاملة
| keys                  المفاتيح
| last                  الأخير
| layer_norm            تطبيع_الطبقة
| length                طول
| less                  أصغر
| ln                    اللوغاريتم_الطبيعي
| load                  حمل
| log10                 اللوغاريتم_العشري
| lowercase             أحرف_صغيرة
| map                   حول
| matches               يطابق
| materialize           جسد
| matmul                ضرب_المصفوفات
| maximum               الأقصى
| mean                  المتوسط
| minimum               الأدنى
| modulo                الباقي
| modulo_assign         أسند_الباقي
| multiplied            مضروب
| multiply              اضرب
| named                 مسماة
| negate                اعكس_الإشارة
| negated               معكوس_الإشارة
| nonzero_count         عدّ_اللاصفريّات
| normalize             طبّع
| power                 قوة
| put                   ضع
| reduce                اختزل
| relu                  تنشيط_ريلو
| remove_first          احذف_الأول
| remove_last           احذف_الأخير
| replace               استبدل
| reshape               أعد_التشكيل
| reverse               اعكس
| rms_norm              rms_norm
| rope_norm             rope_norm
| round                 قرب
| set                   اضبط
| shape                 الأبعاد
| shift_left            أزح_يسارا
| shift_right           أزح_يمينا
| shifted_left          مزاح_يسارا
| shifted_right         مزاح_يمينا
| sign                  إشارة
| silu                  silu
| sin                   جيب
| slice                 شريحة
| softmax               تنشيط_سوفتماكس
| sort                  رتب
| sorted                مرتب
| split                 افصل
| sqrt                  الجذر_التربيعي
| start                 البداية
| starts_with           يبدأ_ب
| store                 خزن
| subtract              اطرح
| subtracted            مطروح
| sum                   المجموع
| swizzle               swizzle
| symmetric_difference  الفرق_المتماثل
| take                  خذ_الأولى
| take_last             خذ_الأخيرة
| tan                   الظل
| text                  النص
| transpose             منقول
| trim                  شذب
| truncate              اقتطع
| union                 الاتحاد
| union                 اتحاد
| uppercase             أحرف_كبيرة
| values                القيم
```

---

[All reader locales](/language/reader-locales.html) · [Full keyword mapping](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
