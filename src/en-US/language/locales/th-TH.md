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

Generated from the packs; the canonical (Latin) name keys the full [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          ไทย
| ---------------  --------------
| all              ทั้งหมด
| and              และ
| any              ใดก็ได้
| argmax           ดัชนีค่าสูงสุด
| argmin           ดัชนีค่าต่ําสุด
| args             อาร์กิวเมนต์
| as               ในชื่อ
| assert           ยืนยัน
| async            อะซิงก์
| async_generator  สตรีมอะซิงก์
| async_main       เริ่มอะซิงก์
| async_setup      จะเตรียม
| async_teardown   จะหลังเตรียม
| at               ที่
| await            รอทิ้ง
| await_const      รอคง
| await_var        รอแปร
| before           ก่อน
| bench            วัด
| between          ระหว่าง
| break            หยุด
| call             ถึง
| case             กรณี
| catch            จับ
| class            ชนิด
| cli              cli
| coalesce         หรือว่าง
| column           คอลัมน์
| command          คำสั่ง
| comptime         นำหน้า
| const            คงที่
| continue         ไปต่อ
| conversion       การแปลง
| —                แปลง
| copy             สำเนา
| count            นับ
| cursor           เคอร์เซอร์
| debug            ดู
| default          อื่น
| describe         ทดสอบชุด
| description      คำอธิบาย
| do               ทำ
| elif             ถ้าไม่ก็
| else             มิฉะนั้น
| embed            ฝัง
| empty            เซตว่าง
| enum             ลำดับ
| errors           ข้อผิดพลาด
| exit             ทางออก
| expect_failure   คาดหวัง_ล้มเหลว
| false            เท็จ
| flaky            เปราะบาง
| fn               ฟังก์ชัน
| for              วน
| format           จารึก
| fragment         ส่วนย่อย
| free             อิสระ
| from             ออก
| future           อนาคต
| generator        สตรีม
| global           โกลบอล
| guard            คุ้มครอง
| if               ถ้า
| implements       เติมเต็ม
| import           นำเข้า
| interface        สัญญา
| internal         ภายในองค์กร
| is               เป็น
| kernel           เคอร์เนล
| lambda           ปิดล้อม
| lane             เลน
| let              อนุมานคงที่
| line             บรรทัด
| long             ยาว
| main             เริ่ม
| match            แยก
| max              สูงสุด
| min              ต่ำสุด
| module           โมดูล
| mut              ใน
| name             ชื่อ
| nan              nan
| nihil            ว่าง
| not              ไม่
| null             ว่างเปล่า
| only             เฉพาะ
| only_in          เฉพาะใน
| operand          ตัวถูกดำเนินการ
| option           ตัวเลือก
| optional         สมัครใจ
| options          ทางเลือก
| or               หรือ
| own              เป็นเจ้าของ
| panic            ตาย
| pass             เงียบ
| per              ตาม
| primus_quem      primus_quem
| print            บันทึก
| private          ส่วนตัว
| product          ผลคูณ
| protected        ป้องกัน
| public           สาธารณะ
| radix            radix
| range            ช่วง
| read             อ่าน
| readonly         ไม่เปลี่ยนแปลง
| reduce           ลดรูป
| ref              จาก
| reject           ปฏิเสธ
| rename           เปลี่ยนชื่อ
| repeat           ทำซ้ำ
| require          ต้องการ
| rest             ที่เหลือ
| return           คืน
| return_await     รอคืน
| schema           สคีมา
| self             ตัวฉัน
| setup            เตรียม
| shared           commune
| short            สั้น
| size             ขนาด
| skip             ละเว้น
| spread           กระจาย
| static           ของชนิด
| step             ต่อ
| sum              ผลรวม
| switch           เลือก
| tag              แท็ก
| teardown         หลังเตรียม
| test             ทดสอบ
| then             ดังนั้น
| thread           เส้นใย
| throw            โยน
| throws           โยนผล
| timeout          เวลา
| todo             ค้าง
| trap             ดัก
| true             จริง
| tuple            ทูเพิล
| type             ชนิดนามแฝง
| ubi              ubi
| union            สหภาพแยก
| unstable         ไม่เสถียร
| until            จนถึง
| var              แปร
| variant          สร้าง
| vertex           จุดยอด
| via              ผ่านทาง
| warn             เตือน
| while            ขณะ
| within           ภายใน
| wrapping         โมดูลัส
| write            เขียน
| yield            ให้
```

### Types {#types}

```text locale=la
| English      ไทย
| -----------  ------------
| any          อะไรก็ได้
| ascii        ascii
| atomic       อะตอมิก
| bool         ตรรกะ
| byte         ไบต์เดี่ยว
| bytes        ไบต์
| census       สำมะโน
| channel      ช่องทาง
| char         อักขระ
| filter       ตัวกรอง
| float        เศษ
| frame        เฟรม
| instant      อินสแตนซ์
| int          จํานวน
| intervallum  อันตรภาค
| iterator     ตัวชี้
| json         json
| list         รายการ
| map          ตาราง
| matrix       เมทริกซ์
| never        ไม่เคย
| none         นัล
| object       ออบเจ็กต์
| promise      คำมั่น
| queue        คิว
| record       ratio
| recv         รับ
| regex        regex
| saturating   อิ่มตัว
| send         ส่ง
| series       ซีรีส์
| set          ชุด
| sparsa       กระจัดกระจาย
| stack        สแตก
| string       ข้อความ
| tensor       เทนเซอร์
| trapping     แม่นยำ
| unknown      ไม่รู้
| value        ค่า
| vector       เวกเตอร์
| void         เปล่า
| wrapping_ty  ค่ามอดุลัส
```

### Intrinsics {#intrinsics}

```text locale=la
| English               ไทย
| --------------------  ------------------
| abs                   ค่าสัมบูรณ์
| add                   เพิ่ม
| added                 เพิ่มแล้ว
| added_bias            เพิ่มไบแอส
| all                   ทั้งหมด
| any                   ใดก็ได้
| append                ต่อท้าย
| apply                 ประยุกต์
| approx                ประมาณ
| argmax                ดัชนีค่าสูงสุด
| argmin                ดัชนีค่าต่ําสุด
| at_least              อย่างน้อย
| at_most               อย่างมาก
| bit_and               และบิต
| bit_and_assign        และบิตกําหนด
| bit_or                หรือบิต
| bit_or_assign         หรือบิตกําหนด
| ceiling               ปัดขึ้น
| clamp                 จํากัดค่า
| compare_exchange      เทียบแล้วสลับ
| complement            กลับบิต
| complemented          กลับบิตแล้ว
| contains              ประกอบด้วย
| cos                   โคไซน์
| create                สร้าง
| cross                 ครอสโปรดักต์
| cross_entropy         ครอสเอนโทรปี
| cumulate              สะสม
| cursor                ตัวชี้
| delete                ลบ
| densify               ทําให้หนาแน่น
| difference            ผลต่าง
| divide                หาร
| divide                การหาร
| divided               หารแล้ว
| dot                   ดอตโปรดักต์
| drop                  ข้าม
| end                   สิ้นสุด
| ends_with             ลงท้ายด้วย
| escape                เอสเคป
| exchange              สลับ
| exp                   เอกซ์โพเนนเชียล
| fill                  เติม
| filter                กรอง
| find                  ค้นหา
| find_all              ค้นหาทั้งหมด
| first                 ตัวแรก
| flatten               ทําให้แบน
| flip                  พลิกค่า
| flipped               พลิกแล้ว
| floor                 ปัดลง
| formata               formata
| from_flat             สร้างจากข้อมูลแบน
| gather                รวบรวม
| gelu                  gelu
| get                   ดึง
| greater               มากกว่า
| group                 กลุ่ม
| has                   มีอยู่
| intersect             ตัดกัน
| intersection          ส่วนตัด
| invert                ผกผัน
| is_empty              ว่าง
| is_subset             เป็นชุดย่อย
| is_superset           เป็นชุดครอบ
| keys                  คีย์
| last                  ตัวสุดท้าย
| layer_norm            เลเยอร์นอร์ม
| length                ความยาว
| less                  น้อยกว่า
| ln                    ลอการิทึมธรรมชาติ
| load                  โหลด
| log10                 ลอการิทึมฐานสิบ
| lowercase             ตัวพิมพ์เล็ก
| map                   แปลง
| matches               ตรงกับ
| materialize           ทําให้เป็นรูปธรรม
| matmul                คูณเมทริกซ์
| maximum               สูงสุด
| mean                  ค่าเฉลี่ย
| minimum               ต่ําสุด
| modulo                มอดูโล
| modulo_assign         มอดูโลกําหนด
| multiplied            คูณแล้ว
| multiply              คูณ
| named                 กลุ่มชื่อ
| negate                กลับเครื่องหมาย
| negated               กลับเครื่องหมายแล้ว
| nonzero_count         นับไม่ศูนย์
| normalize             ทําให้เป็นบรรทัดฐาน
| power                 ยกกําลัง
| put                   ใส่
| reduce                ลดรูป
| relu                  เรลูแอกทิเวชัน
| remove_first          ลบตัวแรก
| remove_last           ลบตัวท้าย
| replace               แทนที่
| reshape               เปลี่ยนรูปร่าง
| reverse               กลับลําดับ
| rms_norm              rms_norm
| rope_norm             rope_norm
| round                 ปัดเศษ
| set                   กําหนด
| shape                 รูปร่าง
| shift_left            เลื่อนซ้าย
| shift_right           เลื่อนขวา
| shifted_left          เลื่อนซ้ายแล้ว
| shifted_right         เลื่อนขวาแล้ว
| sign                  เครื่องหมาย
| silu                  silu
| sin                   ไซน์
| slice                 ตัดช่วง
| softmax               ซอฟต์แมกซ์
| sort                  เรียง
| sorted                เรียงแล้ว
| split                 แยก
| sqrt                  รากที่สอง
| start                 เริ่มต้น
| starts_with           ขึ้นต้นด้วย
| store                 เก็บ
| subtract              ลบออก
| subtracted            ลบออกแล้ว
| sum                   ผลรวม
| swizzle               swizzle
| symmetric_difference  ผลต่างสมมาตร
| take                  ส่วนต้น
| take_last             เอาท้าย
| tan                   แทนเจนต์
| text                  ข้อความ
| transpose             ทรานสโพส
| trim                  ตัดช่องว่าง
| truncate              ตัดทิ้ง
| union                 ส่วนรวม
| union                 ส่วนรวม
| uppercase             ตัวพิมพ์ใหญ่
| values                ค่าทั้งหมด
```

---

[All reader locales](/language/reader-locales.html) · [Full keyword mapping](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
