+++
title = "Thai reader locale"
section = "locales"
order = 14
sources = [
  "radix/locale/<locale>/pack.toml",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

**ไทย** — the `th-TH` reader pack. Script: Thai; direction: left-to-right.

| Field | Value |
|---|---|
| **Locale code** | `th-TH` |
| **Native name** | ไทย |
| **Script** | Thai |
| **Direction** | left-to-right |

A spaceless script: there are no inter-word boundaries, so the lexer resolves every token boundary by keyword matching. Combining vowel and tone marks stack on base characters.

## English ↔ Thai {#mapping}

Generated from the packs; read a row across to translate one term. The Latin column is the pack key, which keys the [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          Latin        ไทย
| ---------------  -----------  --------------
| all              omnia        ทั้งหมด
| and              et           และ
| any              quilibet     ใดก็ได้
| argmax           argmaxima    ดัชนีค่าสูงสุด
| argmin           argminima    ดัชนีค่าต่ําสุด
| args             argumenta    อาร์กิวเมนต์
| as               ut           ในชื่อ
| asc              ascendens    น้อยไปมาก
| assert           adfirma      ยืนยัน
| async            fiet         อะซิงก์
| async_generator  fient        สตรีมอะซิงก์
| async_main       incipiet     เริ่มอะซิงก์
| async_setup      praeparabit  จะเตรียม
| async_teardown   postparabit  จะหลังเตรียม
| at               apud         ที่
| await            tacebit      รอทิ้ง
| await_const      figendum     รอคง
| await_var        variandum    รอแปร
| axis             axis         แกน
| before           ante         ก่อน
| bench            metior       วัด
| between          inter        ระหว่าง
| break            rumpe        หยุด
| call             ad           ถึง
| case             casu         กรณี
| catch            cape         จับ
| class            genus        ชนิด
| cli              cli          cli
| coalesce         vel          หรือว่าง
| column           columna      คอลัมน์
| command          imperium     คำสั่ง
| comptime         praefixum    นำหน้า
| const            fixum        คงที่
| continue         perge        ไปต่อ
| conversion       conversio    การแปลง
| —                conversion   แปลง
| copy             exemplum     สำเนา
| count            numeratio    นับ
| cursor           cursor       เคอร์เซอร์
| debug            vide         ดู
| default          ceterum      อื่น
| desc             descendens   มากไปน้อย
| describe         probandum    ทดสอบชุด
| description      descriptio   คำอธิบาย
| do               fac          ทำ
| elif             sin          ถ้าไม่ก็
| else             secus        มิฉะนั้น
| embed            insere       ฝัง
| empty            vacua        เซตว่าง
| enum             ordo         ลำดับ
| errors           errata       ข้อผิดพลาด
| exit             exitus       ทางออก
| expect_failure   erratur      คาดหวัง_ล้มเหลว
| false            falsum       เท็จ
| flaky            fragilis     เปราะบาง
| fn               functio      ฟังก์ชัน
| for              itera        วน
| format           scriptum     จารึก
| fragment         fragment     ส่วนย่อย
| from             ex           ออก
| future           futura       อนาคต
| generator        fiunt        สตรีม
| global           ubique       โกลบอล
| guard            custodi      คุ้มครอง
| if               si           ถ้า
| implements       implet       เติมเต็ม
| import           importa      นำเข้า
| interface        implendum    สัญญา
| internal         interna      ภายในองค์กร
| is               est          เป็น
| kernel           nucleum      เคอร์เนล
| lambda           clausura     ปิดล้อม
| lane             lane         เลน
| let              sit          อนุมานคงที่
| line             lineam       บรรทัด
| long             longum       ยาว
| main             incipit      เริ่ม
| match            discerne     แยก
| max              maxima       สูงสุด
| min              minima       ต่ำสุด
| module           regio        โมดูล
| mut              in           ใน
| name             nomen        ชื่อ
| nan              nonnumerus   nan
| not              non          ไม่
| null             nulla        ว่างเปล่า
| only             solum        เฉพาะ
| only_in          solum_in     เฉพาะใน
| operand          operandus    ตัวถูกดำเนินการ
| option           optio        ตัวเลือก
| optional         sponte       สมัครใจ
| options          optiones     ทางเลือก
| or               aut          หรือ
| own              penes        เป็นเจ้าของ
| panic            mori         ตาย
| pass             tacet        เงียบ
| per              pro          ตาม
| primus_quem      primus_quem  primus_quem
| print            nota         บันทึก
| private          privata      ส่วนตัว
| product          factum       ผลคูณ
| protected        protecta     ป้องกัน
| public           publica      สาธารณะ
| radix            radix        radix
| range            ab           ช่วง
| read             lege         อ่าน
| readonly         immutata     ไม่เปลี่ยนแปลง
| reduce           reducta      ลดรูป
| ref              de           จาก
| reject           reice        ปฏิเสธ
| rename           verte        เปลี่ยนชื่อ
| repeat           repete       ทำซ้ำ
| require          requirit     ต้องการ
| rest             ceteri       ที่เหลือ
| return           redde        คืน
| return_await     reddet       รอคืน
| schema           schema       สคีมา
| self             ego          ตัวฉัน
| setup            praepara     เตรียม
| shared           commune      ใช้ร่วม
| short            brevis       สั้น
| size             magnitudo    ขนาด
| skip             omitte       ละเว้น
| sort             ordinata     เรียง
| spread           sparge       กระจาย
| static           generis      ของชนิด
| step             per          ต่อ
| sum              summa        ผลรวม
| switch           elige        เลือก
| tag              tag          แท็ก
| teardown         postpara     หลังเตรียม
| test             proba        ทดสอบ
| then             ergo         ดังนั้น
| thread           filum        เส้นใย
| throw            iace         โยน
| throws           iacit        โยนผล
| timeout          temporis     เวลา
| todo             futurum      ค้าง
| trap             capta        ดัก
| true             verum        จริง
| tuple            iuncta       ทูเพิล
| type             typus        ชนิดนามแฝง
| ubi              ubi          ubi
| union            discretio    สหภาพแยก
| unstable         nondum       ไม่เสถียร
| until            usque        จนถึง
| var              varia        แปร
| variant          finge        สร้าง
| vertex           vertex       จุดยอด
| via              via          ผ่านทาง
| warn             mone         เตือน
| while            dum          ขณะ
| within           intra        ภายใน
| wrapping         modulus      โมดูลัส
| write            scribe       เขียน
| yield            cede         ให้
```

### Types {#types}

```text locale=la
| English      Latin        ไทย
| -----------  -----------  ------------
| any          quidlibet    อะไรก็ได้
| ascii        ascii        ascii
| atomic       atomic       อะตอมิก
| bool         bivalens     ตรรกะ
| byte         octetus      ไบต์เดี่ยว
| bytes        octeti       ไบต์
| census       census       สำมะโน
| channel      sermo        ช่องทาง
| char         littera      อักขระ
| clamp        clampa       ตรึงขอบ
| filter       filtrum      ตัวกรอง
| float        fractus      เศษ
| frame        scrinium     เฟรม
| instant      instans      อินสแตนซ์
| int          numerus      จํานวน
| intervallum  intervallum  อันตรภาค
| iterator     cursor_t     ตัวชี้
| json         json         json
| ledger       tabulae      สมุดบัญชี
| list         lista        รายการ
| map          tabula       ตาราง
| matrix       matrix       เมทริกซ์
| never        numquam      ไม่เคย
| none         nihil        นัล
| object       objectum     ออบเจ็กต์
| promise      promissum    คำมั่น
| queue        queue        คิว
| record       ratio        ratio
| recv         tuus         รับ
| reflect      reflexa      สะท้อนขอบ
| regex        regex        regex
| saturating   saturatus    อิ่มตัว
| send         meus         ส่ง
| series       series       ซีรีส์
| set          copia        ชุด
| sparsa       sparsa       กระจัดกระจาย
| stack        stack        สแตก
| string       textus       ข้อความ
| tensor       tensor       เทนเซอร์
| trapping     exactus      แม่นยำ
| unknown      ignotum      ไม่รู้
| value        valor        ค่า
| vector       vector       เวกเตอร์
| void         vacuum       เปล่า
| wrap         involuta     วนขอบ
| wrapping_ty  modulus_t    ค่ามอดุลัส
```

### Intrinsics {#intrinsics}

```text locale=la
| English               Latin                  ไทย
| --------------------  ---------------------  --------------------
| abs                   absolutum              ค่าสัมบูรณ์
| add                   adde                   เพิ่ม
| added                 addita                 เพิ่มแล้ว
| added_bias            addita_bias            เพิ่มไบแอส
| all                   omnia                  ทั้งหมด
| any                   quilibet               ใดก็ได้
| append                appende                ต่อท้าย
| apply                 applica                ประยุกต์
| approx                approximata            ประมาณ
| argmax                argmaxima              ดัชนีค่าสูงสุด
| argmin                argminima              ดัชนีค่าต่ําสุด
| at                    apud                   ที่
| at_least              maxime                 อย่างน้อย
| at_most               minime                 อย่างมาก
| bit_and               coniuncta              และบิต
| bit_and_assign        coniunge               และบิตกําหนด
| bit_or                disiuncta              หรือบิต
| bit_or_assign         disiunge               หรือบิตกําหนด
| ceiling               tectum                 ปัดขึ้น
| clamp                 coercere               จํากัดค่า
| compare_exchange      compare_exchange       เทียบแล้วสลับ
| complement            complementa            กลับบิต
| complemented          complementata          กลับบิตแล้ว
| contains              continet               ประกอบด้วย
| cos                   cosinus                โคไซน์
| count_nonzero         nonnihil               นับไม่ศูนย์
| create                crea                   สร้าง
| cross                 transversum            ครอสโปรดักต์
| cross_entropy         crux_entropia          ครอสเอนโทรปี
| cumulate              cumulata               สะสม
| cursor                cursor                 ตัวชี้
| delete                dele                   ลบ
| densify               densata                ทําให้หนาแน่น
| difference            differentia            ผลต่าง
| difference_symmetric  symmetrica             ผลต่างสมมาตร
| divide                divida                 หาร
| divide                divisio                การหาร
| divided               divisa                 หารแล้ว
| dot                   productum              ดอตโปรดักต์
| drop                  omissa                 ข้าม
| end                   terminus               สิ้นสุด
| ends_with             finis                  ลงท้ายด้วย
| escape                munita                 เอสเคป
| exchange              exchange               สลับ
| exp                   exponentia             เอกซ์โพเนนเชียล
| expanded              expande                ขยายมุมมอง
| fill                  reple                  เติม
| filter                filtrata               กรอง
| find                  inventa                ค้นหา
| find_all              collecta               ค้นหาทั้งหมด
| first                 primus                 ตัวแรก
| flatten               planata                ทําให้แบน
| flip                  alterna                พลิกค่า
| flipped               alternata              พลิกแล้ว
| floor                 pavimentum             ปัดลง
| formata               formata                formata
| gather                gather                 รวบรวม
| gelu                  gelu                   gelu
| get                   accipe                 ดึง
| greater               maior                  มากกว่า
| group                 coetus                 กลุ่ม
| has                   habet                  มีอยู่
| intersect             inter                  ตัดกัน
| intersection          intersectio            ส่วนตัด
| invert                inversa                ผกผัน
| is_empty              vacua                  ว่าง
| is_subset             subcopia               เป็นชุดย่อย
| is_superset           supercopia             เป็นชุดครอบ
| keys                  claves                 คีย์
| last                  ultimus                ตัวสุดท้าย
| length                longitudo              ความยาว
| less                  minor                  น้อยกว่า
| limes                 limes                  ขอบ
| ln                    logarithmus            ลอการิทึมธรรมชาติ
| load                  load                   โหลด
| log10                 logarithmus_decimalis  ลอการิทึมฐานสิบ
| lowercase             minuscula              ตัวพิมพ์เล็ก
| map                   mappata                แปลง
| matches               consentit              ตรงกับ
| materialize           materialize            ทําให้เป็นรูปธรรม
| matmul                matmul                 คูณเมทริกซ์
| maximum               maximus                สูงสุด
| mean                  media                  ค่าเฉลี่ย
| minimum               minimus                ต่ําสุด
| modulo                modulata               มอดูโล
| modulo_assign         modula                 มอดูโลกําหนด
| multiplied            multiplicata           คูณแล้ว
| multiply              multiplica             คูณ
| named                 nominatus              กลุ่มชื่อ
| negate                nega                   กลับเครื่องหมาย
| negated               negativa               กลับเครื่องหมายแล้ว
| norm_layer            laminatio              เลเยอร์นอร์ม
| norm_rms              rms_norm               rms_norm
| norm_rope             rope_norm              rope_norm
| normalize             normalizata            ทําให้เป็นบรรทัดฐาน
| power                 potentia               ยกกําลัง
| put                   pone                   ใส่
| reduce                reducta                ลดรูป
| relu                  activatio_relu         เรลูแอกทิเวชัน
| remove_first          decapita               ลบตัวแรก
| remove_last           detrahe                ลบตัวท้าย
| replace               muta                   แทนที่
| reshape               forma                  เปลี่ยนรูปร่าง
| reverse               inverte                กลับลําดับ
| rope_half             rope_half              rope_half
| round                 rotunda                ปัดเศษ
| set                   ponde                  กําหนด
| shape                 magnitudines           รูปร่าง
| shift                 disloco                เลื่อน
| shift_left            sinistra               เลื่อนซ้าย
| shift_right           dextra                 เลื่อนขวา
| shifted_left          sinistrata             เลื่อนซ้ายแล้ว
| shifted_right         dextrata               เลื่อนขวาแล้ว
| sign                  signum                 เครื่องหมาย
| silu                  silu                   silu
| sin                   sinus                  ไซน์
| slice                 sectio                 ตัดช่วง
| softmax               activatio_softmax      ซอฟต์แมกซ์
| softmax_causal        softmax_causal         ซอฟต์แมกซ์_เชิงสาเหตุ
| sort                  ordina                 เรียง
| sorted                ordinata               เรียงแล้ว
| split                 divide                 แยก
| sqrt                  radix                  รากที่สอง
| start                 principium             เริ่มต้น
| starts_with           initium                ขึ้นต้นด้วย
| store                 store                  เก็บ
| subtract              subtrahe               ลบออก
| subtracted            subtracta              ลบออกแล้ว
| sum                   summa                  ผลรวม
| swizzle               swizzle                swizzle
| take                  prima                  ส่วนต้น
| take_last             ultima                 เอาท้าย
| tan                   tangens                แทนเจนต์
| text                  inventum               ข้อความ
| transpose             transpone              ทรานสโพส
| trim                  recide                 ตัดช่องว่าง
| truncate              trunca                 ตัดทิ้ง
| union                 unio                   ส่วนรวม
| union                 union                  ส่วนรวม
| uppercase             maiuscula              ตัวพิมพ์ใหญ่
| values                valores                ค่าทั้งหมด
```

---

[All reader locales](/language/reader-locales.html) · [Keyword reference](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
