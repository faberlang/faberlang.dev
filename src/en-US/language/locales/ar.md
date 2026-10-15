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

Generated from the packs; read a row across to translate one term. The Latin column is the pack key, which keys the [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          Latin        العربية
| ---------------  -----------  --------------
| all              omnia        الكل
| and              et           و
| any              quilibet     أي
| argmax           argmaxima    فهرس_الأكبر
| argmin           argminima    فهرس_الأصغر
| args             argumenta    وسائط
| as               ut           كـ
| asc              ascendens    تصاعدي
| assert           adfirma      أكد
| async            fiet         غيرمتزامن
| async_generator  fient        مولد_غيرمتزامن
| async_main       incipiet     استهلال
| async_setup      praeparabit  سيهيئ
| async_teardown   postparabit  سيلحق
| at               apud         عند
| await            tacebit      انتظر
| await_const      figendum     انتظر_ثابت
| await_var        variandum    انتظر_متغير
| axis             axis         محور
| before           ante         قبل
| bench            metior       قس
| between          inter        بين
| break            rumpe        اكسر
| call             ad           اتصل
| case             casu         حالة
| catch            cape         التقط
| class            genus        صنف
| cli              cli          cli
| coalesce         vel          عوض
| column           columna      عمود
| command          imperium     أمر
| comptime         praefixum    بادئة
| const            fixum        ثابت
| continue         perge        تابع
| conversion       conversio    تحويل
| —                conversion   حوّل
| copy             exemplum     نسخة
| count            numeratio    العدّ
| cursor           cursor       cursor
| debug            vide         شاهد
| default          ceterum      افتراضي
| desc             descendens   تنازلي
| describe         probandum    مختبر
| description      descriptio   وصف
| do               fac          افعل
| elif             sin          وإلاإذا
| else             secus        وإلا
| embed            insere       تضمين
| empty            vacua        فارغ
| enum             ordo         ترتيب
| errors           errata       مخطئ
| exit             exitus       مخرج
| expect_failure   erratur      توقع_الفشل
| false            falsum       خطأ
| flaky            fragilis     هش
| fn               functio      دالة
| for              itera        كرر
| format           scriptum     حرر
| fragment         fragment     جزء
| from             ex           من
| future           futura       مستقبل
| generator        fiunt        مولد
| global           ubique       عمومي
| guard            custodi      احرس
| if               si           إذا
| implements       implet       حقق
| import           importa      استورد
| interface        implendum    عقد
| internal         interna      داخلي
| is               est          هو
| kernel           nucleum      نواة
| lambda           clausura     إغلاق
| lane             lane         مسار
| let              sit          ليكن
| line             lineam       سطرا
| long             longum       مفصل
| main             incipit      بداية
| match            discerne     طابق
| max              maxima       الأقصى
| min              minima       الأدنى
| module           regio        وحدة
| mut              varia        قابل_للتغيير
| mut              varia        قابل_للتغيير
| name             nomen        اسم
| nan              nonnumerus   nan
| not              non          ليس
| null             nulla        خال
| only             solum        فقط
| only_in          solum_in     حصري
| operand          operandus    معامل
| option           optio        خيار
| optional         sponte       اختياري
| options          optiones     خيارات
| or               aut          أو
| own              penes        ملك
| panic            mori         انهر
| pass             tacet        صمت
| per              pro          حسب
| primus_quem      primus_quem  primus_quem
| print            nota         اعرض
| private          privata      خاص
| product          factum       حاصل_الضرب
| protected        protecta     محمي
| public           publica      عام
| radix            radix        radix
| range            ab           نطاق
| read             lege         اقرأ
| readonly         immutata     ثابتة
| reduce           reducta      اختزل
| ref              de           عن
| reject           reice        ارفض
| rename           verte        إعادة_تسمية
| repeat           repete       معاد
| require          requirit     يتطلب
| rest             ceteri       باقي
| return           redde        أعد
| return_await     reddet       أعد_منتظرا
| schema           schema       مخطط
| self             ego          ذات
| setup            praepara     جهز
| shared           commune      مشترك
| short            brevis       مختصر
| size             magnitudo    حجم
| skip             omitte       أهمل
| sort             ordinata     رتب
| spread           sparge       انشر
| static           generis      سكوني
| step             per          كل
| sum              summa        المجموع
| switch           elige        اختر
| tag              tag          وسم
| teardown         postpara     لاحق
| test             proba        اختبر
| then             ergo         إذن
| thread           filum        خيط
| throw            iace         ارم
| throws           iacit        يرمي
| timeout          temporis     زمني
| todo             futurum      مستقبلي
| trap             capta        فخ
| true             verum        صواب
| tuple            iuncta       توبل
| type             typus        نمط
| ubi              ubi          ubi
| union            discretio    تمايز
| unstable         nondum       غير_مستقر
| until            usque        حتى
| variant          finge        أنشئ
| vertex           vertex       رأس
| via              via          عبر
| warn             mone         نبه
| while            dum          طالما
| within           intra        ضمن
| wrapping         modulus      حلقة
| write            scribe       اكتب
| yield            cede         سلم
```

### Types {#types}

```text locale=la
| English      Latin        العربية
| -----------  -----------  -------------
| any          quidlibet    مهما
| ascii        ascii        أسكي
| atomic       atomic       ذري
| bool         bivalens     منطقي
| byte         octetus      بايت
| bytes        octeti       بايتات
| census       census       تعداد
| channel      sermo        قناة
| char         littera      حرف
| clamp        clampa       تثبيت_الحافة
| filter       filtrum      مرشح
| float        fractus      كسر
| frame        scrinium     إطار
| instant      instans      لحظة
| int          numerus      عدد
| intervallum  intervallum  فترة
| iterator     cursor_t     مؤشر
| json         json         جسون
| ledger       tabulae      دفتر
| list         lista        قائمة
| map          tabula       جدول
| matrix       matrix       مصفوفة
| never        numquam      أبدا
| none         nihil        نوع_لاشيء
| object       objectum     كائن
| promise      promissum    وعد
| queue        queue        طابور
| record       ratio        ratio
| recv         tuus         استقبال
| reflect      reflexa      انعكاس_الحافة
| regex        regex        تعبير
| saturating   saturatus    مشبع
| send         meus         إرسال
| series       series       سلسلة
| set          copia        مجموعة
| sparsa       sparsa       متفرقة
| stack        stack        مكدس
| string       textus       نص
| tensor       tensor       موتر
| trapped      interceptum  محتجز
| trapping     exactus      دقيق
| unknown      ignotum      مجهول
| value        valor        قيمة
| vector       vector       متجه
| void         vacuum       فراغ
| wrap         involuta     التفاف_الحافة
| wrapping_ty  modulus_t    نوع_حلقة
```

### Intrinsics {#intrinsics}

```text locale=la
| English               Latin                  العربية
| --------------------  ---------------------  -------------------
| abs                   absolutum              القيمة_المطلقة
| add                   adde                   أضف
| added                 addita                 مضاف
| added_bias            addita_bias            مضاف_الانحياز
| all                   omnia                  الكل
| any                   quilibet               أي
| append                appende                ألحق
| apply                 applica                طبق
| approx                approximata            مقارب
| argmax                argmaxima              فهرس_الأكبر
| argmin                argminima              فهرس_الأصغر
| at                    apud                   عند
| at_least              maxime                 على_الأقل
| at_most               minime                 على_الأكثر
| bit_and               coniuncta              و_بت
| bit_and_assign        coniunge               و_بت_إسناد
| bit_or                disiuncta              أو_بت
| bit_or_assign         disiunge               أو_بت_إسناد
| ceiling               tectum                 تقريب_لأعلى
| clamp                 coercere               قيد
| compare_exchange      compare_exchange       قارن_وبدل
| complement            complementa            كمل
| complemented          complementata          مكمل
| contains              continet               يحتوي
| cos                   cosinus                جيب_التمام
| count_nonzero         nonnihil               عدّ_اللاصفريّات
| create                crea                   أنشئ
| cross                 transversum            الجداء_الاتجاهي
| cross_entropy         crux_entropia          إنتروبيا_متقاطعة
| cumulate              cumulata               تراكمي
| cursor                cursor                 مؤشر
| delete                dele                   امسح
| densify               densata                كثف
| difference            differentia            الفرق
| difference_symmetric  symmetrica             الفرق_المتماثل
| divide                divida                 اقسم
| divided               divisa                 مقسوم
| dot                   productum              الجداء_النقطي
| drop                  omissa                 أسقط
| end                   terminus               النهاية
| ends_with             finis                  ينتهي_ب
| escape                munita                 تهريب
| exchange              exchange               بدل
| exp                   exponentia             الأسي
| expanded              expande                وسع
| fill                  reple                  املأ
| filter                filtrata               رشح
| find                  inventa                ابحث
| find_all              collecta               ابحث_عن_الكل
| first                 primus                 الأول
| flatten               planata                سطح
| flip                  alterna                اقلب
| flipped               alternata              مقلوب
| floor                 pavimentum             تقريب_لأسفل
| formata               formata                formata
| gather                gather                 اجمع_بالفهرس
| gelu                  gelu                   gelu
| get                   accipe                 اجلب
| greater               maior                  أكبر
| group                 coetus                 مجموعة
| has                   habet                  يملك
| intersect             inter                  تقاطع
| intersection          intersectio            التقاطع
| invert                inversa                معكوس
| is_empty              vacua                  فارغ
| is_subset             subcopia               مجموعة_جزئية
| is_superset           supercopia             مجموعة_شاملة
| keys                  claves                 المفاتيح
| last                  ultimus                الأخير
| length                longitudo              طول
| less                  minor                  أصغر
| limes                 limes                  حافة
| ln                    logarithmus            اللوغاريتم_الطبيعي
| load                  load                   حمل
| log10                 logarithmus_decimalis  اللوغاريتم_العشري
| lowercase             minuscula              أحرف_صغيرة
| map                   mappata                حول
| matches               consentit              يطابق
| materialize           materialize            جسد
| matmul                matmul                 ضرب_المصفوفات
| maximum               maximus                الأقصى
| mean                  media                  المتوسط
| minimum               minimus                الأدنى
| modulo                modulata               الباقي
| modulo_assign         modula                 أسند_الباقي
| multiplied            multiplicata           مضروب
| multiply              multiplica             اضرب
| named                 nominatus              مسماة
| negate                nega                   اعكس_الإشارة
| negated               negativa               معكوس_الإشارة
| norm_layer            laminatio              تطبيع_الطبقة
| norm_rms              rms_norm               rms_norm
| norm_rope             rope_norm              rope_norm
| normalize             normalizata            طبّع
| power                 potentia               قوة
| put                   pone                   ضع
| reduce                reducta                اختزل
| relu                  activatio_relu         تنشيط_ريلو
| remove_first          decapita               احذف_الأول
| remove_last           detrahe                احذف_الأخير
| replace               muta                   استبدل
| reshape               forma                  أعد_التشكيل
| reverse               inverte                اعكس
| rope_half             rope_half              rope_half
| round                 rotunda                قرب
| set                   ponde                  اضبط
| shape                 magnitudines           الأبعاد
| shift                 disloco                أزح
| shift_left            sinistra               أزح_يسارا
| shift_right           dextra                 أزح_يمينا
| shifted_left          sinistrata             مزاح_يسارا
| shifted_right         dextrata               مزاح_يمينا
| sign                  signum                 إشارة
| silu                  silu                   silu
| sin                   sinus                  جيب
| slice                 sectio                 شريحة
| softmax               activatio_softmax      تنشيط_سوفتماكس
| softmax_causal        softmax_causal         تنشيط_سوفتماكس_سببي
| sort                  ordina                 رتب
| sorted                ordinata               مرتب
| split                 divide                 افصل
| sqrt                  radix                  الجذر_التربيعي
| start                 principium             البداية
| starts_with           initium                يبدأ_ب
| store                 store                  خزن
| subtract              subtrahe               اطرح
| subtracted            subtracta              مطروح
| sum                   summa                  المجموع
| swizzle               swizzle                swizzle
| take                  prima                  خذ_الأولى
| take_last             ultima                 خذ_الأخيرة
| tan                   tangens                الظل
| text                  inventum               النص
| transpose             transpone              منقول
| trim                  recide                 شذب
| truncate              trunca                 اقتطع
| union                 unio                   الاتحاد
| union                 union                  اتحاد
| uppercase             maiuscula              أحرف_كبيرة
| values                valores                القيم
```

---

[All reader locales](/language/reader-locales.html) · [Keyword reference](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
