# Locales

One source file uses one locale pack. The files in this canon are English.
Keywords, types, and library members in a file come from that pack.

```faber locale=en
# English source.
main {
    print "en"
}
```

Do not write `//`. That is rejected as `LEX006` `c_style_line_comment`. Do not
put `#` after code on the same line. That is rejected as `LEX007`
`inline_hash_after_code`.

Everything below is the cross-language table, generated from the eight locale
packs so it cannot drift from the compiler by hand.

A program writes the spelling in its own locale's column. English is the spelling
this canon writes. The Latin column is the canonical name, which the compiler also
uses as its internal identity; it is otherwise one locale among eight. Read a row
across to translate a term; read a column down to translate a program. A blank
cell means that locale's pack declares no spelling for the term, which for the
six translations is the signal that the packs disagree; the contested rows are
listed at the end.

## Keywords

| English | Latin | ar | hi | th-TH | vi | zh-Hans | zh-Hant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `all` | `omnia` | `الكل` | `सभी` | `ทั้งหมด` | `tất_cả` | `全部` | `全部` |
| `and` | `et` | `و` | `और` | `และ` | `và` | `且` | `且` |
| `any` | `quilibet` | `أي` | `कोई` | `ใดก็ได้` | `bất_kỳ` | `任一` | `任一` |
| `argmax` | `argmaxima` | `فهرس_الأكبر` | `argmax` | `ดัชนีค่าสูงสุด` | `argmax` | `最大值索引` | `最大值索引` |
| `argmin` | `argminima` | `فهرس_الأصغر` | `argmin` | `ดัชนีค่าต่ําสุด` | `argmin` | `最小值索引` | `最小值索引` |
| `args` | `argumenta` | `وسائط` | `तर्क` | `อาร์กิวเมนต์` | `đối_số` | `参数` | `引數` |
| `as` | `ut` | `كـ` | `रूपमें` | `ในชื่อ` | `như` | `作为` | `作為` |
| `assert` | `adfirma` | `أكد` | `पुष्टि` | `ยืนยัน` | `khẳng_định` | `断言` | `斷言` |
| `async` | `fiet` | `غيرمتزامن` | `async` | `อะซิงก์` | `async` | `异步` | `異步` |
| `async_generator` | `fient` | `مولد_غيرمتزامن` | `async_जनक` | `สตรีมอะซิงก์` | `async_sinh` | `异流` | `異流` |
| `async_main` | `incipiet` | `استهلال` | `आरंभasync` | `เริ่มอะซิงก์` | `bắt_đầu_bất_đồng_bộ` | `异步入口` | `非同步入口` |
| `async_setup` | `praeparabit` | `سيهيئ` | `पूर्वतैयारasync` | `จะเตรียม` | `sẽ_chuẩn_bị` | `异步备置` | `準備非同步` |
| `async_teardown` | `postparabit` | `سيلحق` | `पश्चतैयारasync` | `จะหลังเตรียม` | `sẽ_sau_chuẩn_bị` | `异步收尾` | `後置準備非同步` |
| `at` | `apud` | `عند` | `पर` | `ที่` | `tại` | `在` | `在` |
| `await` | `tacebit` | `انتظر` | `रुको` | `รอทิ้ง` | `đợi_bỏ` | `等弃` | `等棄` |
| `await_const` | `figendum` | `انتظر_ثابت` | `रुको_स्थिर` | `รอคง` | `đợi_hằng` | `等定` | `等定` |
| `await_var` | `variandum` | `انتظر_متغير` | `रुको_चर` | `รอแปร` | `đợi_biến` | `等变` | `等變` |
| `before` | `ante` | `قبل` | `पहले` | `ก่อน` | `trước` | `迄` | `之前` |
| `bench` | `metior` | `قس` | `मापो` | `วัด` | `đo_lường` | `计量` | `測量` |
| `between` | `inter` | `بين` | `बीच` | `ระหว่าง` | `giữa` | `间` | `之間` |
| `break` | `rumpe` | `اكسر` | `तोड़ो` | `หยุด` | `dừng` | `中断` | `中斷` |
| `call` | `ad` | `اتصل` | `सेवा` | `ถึง` | `gọi` | `调用` | `端點` |
| `case` | `casu` | `حالة` | `स्थिति` | `กรณี` | `trường_hợp` | `情况` | `分支` |
| `catch` | `cape` | `التقط` | `पकड़ो` | `จับ` | `bắt` | `捕获` | `捕捉` |
| `class` | `genus` | `صنف` | `वर्ग` | `ชนิด` | `kiểu` | `类` | `類型` |
| `cli` | `cli` | `cli` | `cli` | `cli` | `cli` | `命令行` | `命令行` |
| `coalesce` | `vel` | `عوض` | `डिफ़ॉल्ट` | `หรือว่าง` | `hoặc_nếu_rỗng` | `兜底` | `或取` |
| `column` | `columna` | `عمود` | `कॉलम` | `คอลัมน์` | `cột` | `列` | `欄位` |
| `command` | `imperium` | `أمر` | `आदेश` | `คำสั่ง` | `lệnh` | `命令` | `命令` |
| `comptime` | `praefixum` | `بادئة` | `उपसर्ग` | `นำหน้า` | `tiền_tố` | `前缀` | `前綴` |
| `const` | `fixum` | `ثابت` | `स्थिर` | `คงที่` | `hằng` | `常量` | `定值` |
| `continue` | `perge` | `تابع` | `जारी` | `ไปต่อ` | `tiếp` | `继续` | `繼續` |
| `conversion` | `conversio` | `تحويل` | `रूपांतरण` | `การแปลง` | `chuyển_đổi` | `转换` | `轉換` |
|  | `conversion` | `حوّل` | `बदलें` | `แปลง` | `chuyển` | `变换` | `變換` |
| `copy` | `exemplum` | `نسخة` | `प्रतिलिपि` | `สำเนา` | `sao_chép` | `拷贝` | `拷貝` |
| `count` | `numeratio` | `العدّ` | `गिनती` | `นับ` | `đếm` | `计数` | `計數` |
| `cursor` | `cursor` | `cursor` | `संकेतक` | `เคอร์เซอร์` | `con_trỏ` | `迭代器` | `迭代器` |
| `debug` | `vide` | `شاهد` | `देखो` | `ดู` | `xem` | `查看` | `檢視` |
| `default` | `ceterum` | `افتراضي` | `अन्यतम` | `อื่น` | `mặc_định` | `默认` | `預設` |
| `describe` | `probandum` | `مختبر` | `परीक्षणसमूह` | `ทดสอบชุด` | `đối_tượng_kiểm_thử` | `验题` | `測試規格` |
| `description` | `descriptio` | `وصف` | `विवरण` | `คำอธิบาย` | `mô_tả` | `描述` | `描述` |
| `do` | `fac` | `افعل` | `करो` | `ทำ` | `làm` | `执行` | `執行` |
| `elif` | `sin` | `وإلاإذا` | `अन्यथायदि` | `ถ้าไม่ก็` | `nếukhôngthì` | `否则如果` | `否則若` |
| `else` | `secus` | `وإلا` | `अन्यथा` | `มิฉะนั้น` | `khác` | `否则` | `否則` |
| `embed` | `insere` | `تضمين` | `अंतःस्थापित` | `ฝัง` | `nhúng` | `嵌入` | `嵌入` |
| `empty` | `vacua` | `فارغ` | `खाली` | `เซตว่าง` | `tập_rỗng` | `空集` | `空集` |
| `enum` | `ordo` | `ترتيب` | `क्रम` | `ลำดับ` | `liệt_kê` | `枚举` | `列舉` |
| `errors` | `errata` | `مخطئ` | `त्रुटि` | `ข้อผิดพลาด` | `lỗi` | `勘误` | `錯誤` |
| `exit` | `exitus` | `مخرج` | `निर्गम` | `ทางออก` | `thoát` | `退出` | `出口` |
| `expect_failure` | `erratur` | `توقع_الفشل` | `अपेक्षित_विफलता` | `คาดหวัง_ล้มเหลว` | `mong_đợi_thất_bại` | `预期失败` | `預期失敗` |
| `false` | `falsum` | `خطأ` | `असत्य` | `เท็จ` | `sai` | `假` | `假` |
| `flaky` | `fragilis` | `هش` | `नाज़ुक` | `เปราะบาง` | `mong_manh` | `易碎` | `脆弱` |
| `fn` | `functio` | `دالة` | `फलन` | `ฟังก์ชัน` | `hàm` | `函数` | `函式` |
| `for` | `itera` | `كرر` | `दोहराओ` | `วน` | `lặp` | `遍历` | `遍歷` |
| `format` | `scriptum` | `حرر` | `लिखित` | `จารึก` | `văn_bản_hóa` | `格式化` | `格式文字` |
| `fragment` | `fragment` | `جزء` | `खंड` | `ส่วนย่อย` | `mảnh` | `片段` | `片段` |
| `free` | `libera` | `حر` | `मुक्त` | `อิสระ` | `tự_do` | `自由` | `自由` |
| `from` | `ex` | `من` | `सेवन` | `ออก` | `từ` | `取自` | `取自` |
| `future` | `futura` | `مستقبل` | `भविष्य` | `อนาคต` | `tương_lai` | `未来` | `未來` |
| `generator` | `fiunt` | `مولد` | `जनक` | `สตรีม` | `sinh` | `流` | `流` |
| `global` | `ubique` | `عمومي` | `वैश्विक` | `โกลบอล` | `toàn_cục` | `全局` | `全局` |
| `guard` | `custodi` | `احرس` | `रक्षक` | `คุ้มครอง` | `canh_gác` | `守护` | `守衛` |
| `if` | `si` | `إذا` | `यदि` | `ถ้า` | `nếu` | `如果` | `若` |
| `implements` | `implet` | `حقق` | `लागूकरता` | `เติมเต็ม` | `thực_thi` | `实现` | `實作` |
| `import` | `importa` | `استورد` | `आयात` | `นำเข้า` | `nhập` | `导入` | `匯入` |
| `interface` | `implendum` | `عقد` | `अनुबन्ध` | `สัญญา` | `giao_ước` | `契约` | `待實作介面` |
| `internal` | `interna` | `داخلي` | `आंतरिक` | `ภายในองค์กร` | `nội_bộ` | `内部` | `內部` |
| `is` | `est` | `هو` | `है` | `เป็น` | `là` | `是` | `是` |
| `kernel` | `nucleum` | `نواة` | `कर्नेल` | `เคอร์เนล` | `hạt_nhân` | `内核` | `內核` |
| `lambda` | `clausura` | `إغلاق` | `समापन` | `ปิดล้อม` | `đóng` | `闭包` | `閉包` |
| `lane` | `lane` | `مسار` | `लेन` | `เลน` | `làn` | `车道` | `車道` |
| `let` | `sit` | `ليكن` | `बैठा` | `อนุมานคงที่` | `đặt` | `设` | `設為` |
| `line` | `lineam` | `سطرا` | `पंक्ति` | `บรรทัด` | `dòng` | `行` | `行` |
| `long` | `longum` | `مفصل` | `विस्तृत` | `ยาว` | `dài` | `详` | `詳` |
| `main` | `incipit` | `بداية` | `आरंभ` | `เริ่ม` | `bắt_đầu` | `入口` | `入口` |
| `match` | `discerne` | `طابق` | `मिलाओ` | `แยก` | `phân_tích` | `匹配` | `比對` |
| `max` | `maxima` | `الأقصى` | `अधिकतम` | `สูงสุด` | `lớn_nhất` | `最大` | `最大` |
| `min` | `minima` | `الأدنى` | `न्यूनतम` | `ต่ำสุด` | `nhỏ_nhất` | `最小` | `最小` |
| `module` | `regio` | `وحدة` | `क्षेत्र` | `โมดูล` | `vùng` | `模块` | `模組` |
| `mut` | `in` | `في` | `में` | `ใน` | `vào` | `传入` | `傳入` |
| `name` | `nomen` | `اسم` | `नाम` | `ชื่อ` | `tên` | `名称` | `名稱` |
| `nan` | `nonnumerus` | `nan` | `nan` | `nan` | `nan` | `nan` | `nan` |
| `nihil` | `nihil` | `لاشيء` | `शून्य` | `ว่าง` | `rỗng` | `空` | `空` |
| `not` | `non` | `ليس` | `नहीं` | `ไม่` | `không` | `非` | `非` |
| `null` | `nulla` | `خال` | `शून्यवत्` | `ว่างเปล่า` | `không_gì` | `皆无` | `可空` |
| `only` | `solum` | `فقط` | `केवल` | `เฉพาะ` | `chỉ` | `仅` | `僅限` |
| `only_in` | `solum_in` | `حصري` | `केवलमें` | `เฉพาะใน` | `chỉ_trong` | `仅于` | `僅限於` |
| `operand` | `operandus` | `معامل` | `ऑपरेंड` | `ตัวถูกดำเนินการ` | `toán_hạng` | `操作数` | `操作數` |
| `option` | `optio` | `خيار` | `विकल्प` | `ตัวเลือก` | `tùy_chọn` | `选项` | `選項` |
| `optional` | `sponte` | `اختياري` | `स्वेच्छा` | `สมัครใจ` | `tự_nguyện` | `可选` | `可選` |
| `options` | `optiones` | `خيارات` | `चयन` | `ทางเลือก` | `lựa_chọn` | `可选项` | `可選項` |
| `or` | `aut` | `أو` | `या` | `หรือ` | `hoặc` | `或` | `或` |
| `own` | `penes` | `ملك` | `स्वामित्व` | `เป็นเจ้าของ` | `sở_hữu` | `拥有` | `擁有` |
| `panic` | `mori` | `انهر` | `मरोजाओ` | `ตาย` | `chết` | `崩溃` | `崩潰` |
| `pass` | `tacet` | `صمت` | `मौन` | `เงียบ` | `im_lặng` | `静默` | `靜默` |
| `per` | `pro` | `حسب` | `अनुसार` | `ตาม` | `theo` | `按` | `按` |
| `primus_quem` | `primus_quem` | `primus_quem` | `primus_quem` | `primus_quem` | `primus_quem` | `primus_quem` | `primus_quem` |
| `print` | `nota` | `اعرض` | `दिखाओ` | `บันทึก` | `ghi_chú` | `显示` | `註記` |
| `private` | `privata` | `خاص` | `निजी` | `ส่วนตัว` | `riêng_tư` | `私有` | `私有` |
| `product` | `factum` | `حاصل_الضرب` | `गुणनफल` | `ผลคูณ` | `tích` | `求积` | `求積` |
| `protected` | `protecta` | `محمي` | `संरक्षित` | `ป้องกัน` | `bảo_vệ` | `保护` | `保護` |
| `public` | `publica` | `عام` | `सार्वजनिक` | `สาธารณะ` | `công_khai` | `公开` | `公開` |
| `radix` | `radix` | `radix` | `radix` | `radix` | `radix` | `radix` | `radix` |
| `range` | `ab` | `نطاق` | `सीमा` | `ช่วง` | `khoảng` | `范围` | `範圍` |
| `read` | `lege` | `اقرأ` | `पढ़ो` | `อ่าน` | `đọc` | `读取` | `讀取` |
| `readonly` | `immutata` | `ثابتة` | `अपरिवर्तित` | `ไม่เปลี่ยนแปลง` | `bất_biến` | `不变` | `不變` |
| `reduce` | `reducta` | `اختزل` | `समेटो` | `ลดรูป` | `rút_gọn` | `归约` | `歸約` |
| `ref` | `de` | `عن` | `से` | `จาก` | `ra` | `借自` | `從` |
| `reject` | `reice` | `يرفض` | `अस्वीकार` | `ปฏิเสธ` | `từ_chối` | `拒绝` | `拒絕` |
| `rename` | `verte` | `إعادة_تسمية` | `नाम_बदलें` | `เปลี่ยนชื่อ` | `đổi_tên` | `改名` | `改名` |
| `repeat` | `repete` | `معاد` | `पुनरावृत्ति` | `ทำซ้ำ` | `lặp_lại` | `重复` | `重複` |
| `require` | `requirit` | `يتطلب` | `आवश्यक` | `ต้องการ` | `yêu_cầu` | `需求` | `需要` |
| `rest` | `ceteri` | `باقي` | `बाकी` | `ที่เหลือ` | `còn_lại` | `其余` | `其餘` |
| `return` | `redde` | `أعد` | `लौटाओ` | `คืน` | `trả` | `返回` | `傳回` |
| `return_await` | `reddet` | `أعد_منتظرا` | `रुको_लौटाओ` | `รอคืน` | `đợi_trả` | `等返` | `等返` |
| `schema` | `schema` | `مخطط` | `स्कीमा` | `สคีมา` | `lược_đồ` | `架构` | `結構` |
| `self` | `ego` | `ذات` | `मैं` | `ตัวฉัน` | `tôi` | `自身` | `自身` |
| `setup` | `praepara` | `جهز` | `पूर्वतैयार` | `เตรียม` | `chuẩn_bị` | `备置` | `準備` |
| `shared` | `commune` | `commune` | `commune` | `commune` | `commune` | `commune` | `commune` |
| `short` | `brevis` | `مختصر` | `संक्षिप्त` | `สั้น` | `ngắn` | `简` | `簡` |
| `size` | `magnitudo` | `حجم` | `आकार` | `ขนาด` | `kích_thước` | `维度` | `尺寸` |
| `skip` | `omitte` | `أهمل` | `छोड़ो` | `ละเว้น` | `bỏ_qua` | `跳过` | `略過` |
| `spread` | `sparge` | `انشر` | `फैलाओ` | `กระจาย` | `rải` | `展开` | `展開` |
| `static` | `generis` | `سكوني` | `स्थैतिक` | `ของชนิด` | `tĩnh` | `静态` | `靜態` |
| `step` | `per` | `كل` | `प्रति` | `ต่อ` | `qua` | `步` | `每` |
| `sum` | `summa` | `المجموع` | `योग` | `ผลรวม` | `tổng` | `求和` | `求和` |
| `switch` | `elige` | `اختر` | `चुनो` | `เลือก` | `chọn` | `选择` | `選擇` |
| `tag` | `tag` | `وسم` | `टैग` | `แท็ก` | `nhãn` | `标签` | `標籤` |
| `teardown` | `postpara` | `لاحق` | `पश्चतैयार` | `หลังเตรียม` | `sau_chuẩn_bị` | `收尾` | `後置準備` |
| `test` | `proba` | `اختبر` | `परीक्षण` | `ทดสอบ` | `kiểm_thử` | `测试` | `測試` |
| `then` | `ergo` | `إذن` | `अतः` | `ดังนั้น` | `do_đó` | `则` | `則` |
| `thread` | `filum` | `خيط` | `धागा` | `เส้นใย` | `sợi` | `线程` | `執行緒` |
| `throw` | `iace` | `ارم` | `इधरफेंको` | `โยน` | `ném` | `抛错` | `拋出` |
| `throws` | `iacit` | `يرمي` | `फेंकता` | `โยนผล` | `ném_lỗi` | `可抛` | `可拋` |
| `timeout` | `temporis` | `زمني` | `समय` | `เวลา` | `thời_gian` | `时限` | `時限` |
| `todo` | `futurum` | `مستقبلي` | `लंबित` | `ค้าง` | `việc_cần_làm` | `预期` | `預期` |
| `trap` | `capta` | `فخ` | `जाल` | `ดัก` | `bẫy` | `陷阱` | `陷阱` |
| `true` | `verum` | `صواب` | `सत्य` | `จริง` | `đúng` | `真` | `真` |
| `tuple` | `iuncta` | `توبل` | `टपल` | `ทูเพิล` | `bộ` | `元组` | `元組` |
| `type` | `typus` | `نمط` | `प्रकार` | `ชนิดนามแฝง` | `kiểu_tên` | `类型` | `型別` |
| `ubi` | `ubi` | `ubi` | `ubi` | `ubi` | `ubi` | `ubi` | `ubi` |
| `union` | `discretio` | `تمايز` | `विभेद` | `สหภาพแยก` | `hợp_nhất` | `判别` | `分支聯集` |
| `unstable` | `nondum` | `غير_مستقر` | `अस्थिर` | `ไม่เสถียร` | `không_ổn_định` | `不稳定` | `不穩定` |
| `until` | `usque` | `حتى` | `तक` | `จนถึง` | `tới` | `到` | `直到` |
| `var` | `varia` | `متغير` | `चर` | `แปร` | `biến` | `变量` | `變值` |
| `variant` | `finge` | `أنشئ` | `गढ़ो` | `สร้าง` | `tạo` | `构造` | `虛構` |
| `vertex` | `vertex` | `رأس` | `शीर्ष` | `จุดยอด` | `đỉnh` | `顶点` | `頂點` |
| `via` | `via` | `عبر` | `द्वारा` | `ผ่านทาง` | `thông_qua` | `经由` | `經由` |
| `warn` | `mone` | `نبه` | `चेताओ` | `เตือน` | `cảnh_báo` | `警告` | `警告` |
| `while` | `dum` | `طالما` | `जबतक` | `ขณะ` | `trong_khi` | `当` | `當` |
| `within` | `intra` | `ضمن` | `भीतर` | `ภายใน` | `trong` | `内` | `內含` |
| `wrapping` | `modulus` | `حلقة` | `मॉड्यूल` | `โมดูลัส` | `môđun` | `模数` | `模數` |
| `write` | `scribe` | `اكتب` | `लिखो` | `เขียน` | `viết` | `写入` | `寫出` |
| `yield` | `cede` | `سلم` | `आगेबढ़ो` | `ให้` | `nhường` | `让出` | `讓出` |

## Types

| English | Latin | ar | hi | th-TH | vi | zh-Hans | zh-Hant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `any` | `quidlibet` | `مهما` | `कुछभी` | `อะไรก็ได้` | `bất_kỳ` | `任意` | `任意值` |
| `ascii` | `ascii` | `أسكي` | `ascii` | `ascii` | `ascii` | `窄字串` | `ascii` |
| `atomic` | `atomic` | `ذري` | `परमाणु` | `อะตอมิก` | `nguyên_tử` | `原子` | `原子` |
| `bool` | `bivalens` | `منطقي` | `तार्किक` | `ตรรกะ` | `logic` | `布尔` | `布林` |
| `byte` | `octetus` | `بايت` | `बाइट_मान` | `ไบต์เดี่ยว` | `byte_đơn` | `单字节` | `單位元組` |
| `bytes` | `octeti` | `بايتات` | `बाइट` | `ไบต์` | `byte` | `字节` | `位元組` |
| `census` | `census` | `تعداد` | `गणना` | `สำมะโน` | `điều_tra` | `普查` | `普查` |
| `channel` | `sermo` | `قناة` | `चैनल` | `ช่องทาง` | `kênh` | `通道` | `通道` |
| `char` | `littera` | `حرف` | `अक्षर` | `อักขระ` | `ký_tự` | `字符` | `字元` |
| `filter` | `filtrum` | `مرشح` | `फ़िल्टर` | `ตัวกรอง` | `bộ_lọc` | `过滤器` | `篩選器` |
| `float` | `fractus` | `كسر` | `भिन्न` | `เศษ` | `thập_phân` | `小数` | `小數` |
| `frame` | `scrinium` | `إطار` | `फ़्रेम` | `เฟรม` | `khung` | `帧` | `幀` |
| `instant` | `instans` | `لحظة` | `क्षण` | `อินสแตนซ์` | `thời_điểm` | `时刻` | `執行個體` |
| `int` | `numerus` | `عدد` | `संख्या` | `จํานวน` | `số` | `整数` | `整數` |
| `intervallum` | `intervallum` | `فترة` | `अंतराल` | `อันตรภาค` | `miền` | `区间` | `區間` |
| `iterator` | `cursor_t` | `مؤشر` | `कर्सर` | `ตัวชี้` | `bộ_lặp` | `游标` | `游標` |
| `json` | `json` | `جسون` | `json` | `json` | `json` | `json` | `JSON` |
| `list` | `lista` | `قائمة` | `सूची` | `รายการ` | `danh_sách` | `列表` | `列表` |
| `map` | `tabula` | `جدول` | `तालिका` | `ตาราง` | `bảng` | `映射` | `表格` |
| `matrix` | `matrix` | `مصفوفة` | `आव्यूह` | `เมทริกซ์` | `ma_trận` | `矩阵` | `矩陣` |
| `never` | `numquam` | `أبدا` | `कभीनहीं` | `ไม่เคย` | `không_bao_giờ` | `永不` | `永不` |
| `none` | `nihil` | `نوع_لاشيء` | `शून्य_मान` | `นัล` | `rỗng_ty` | `空类型` | `無` |
| `object` | `objectum` | `كائن` | `वस्तु` | `ออบเจ็กต์` | `đối_tượng` | `对象` | `物件` |
| `promise` | `promissum` | `وعد` | `वादा` | `คำมั่น` | `lời_hứa` | `期约` | `承諾` |
| `queue` | `queue` | `طابور` | `कतार` | `คิว` | `hàng_đợi` | `队列` | `佇列` |
| `record` | `ratio` | `ratio` | `ratio` | `ratio` | `ratio` | `ratio` | `ratio` |
| `recv` | `tuus` | `استقبال` | `पाना` | `รับ` | `nhận` | `接收` | `接收` |
| `regex` | `regex` | `تعبير` | `regex` | `regex` | `chính_quy` | `regex` | `正規表示式` |
| `saturating` | `saturatus` | `مشبع` | `संतृप्त` | `อิ่มตัว` | `bão_hòa` | `饱和` | `飽和` |
| `send` | `meus` | `إرسال` | `भेजना` | `ส่ง` | `gửi` | `发送` | `發送` |
| `series` | `series` | `سلسلة` | `शृंखला` | `ซีรีส์` | `chuỗi` | `序列` | `序列` |
| `set` | `copia` | `مجموعة` | `समुच्चय` | `ชุด` | `tập_hợp` | `集合` | `副本` |
| `sparsa` | `sparsa` | `متفرقة` | `विरल` | `กระจัดกระจาย` | `thưa` | `稀疏` | `稀疏` |
| `stack` | `stack` | `مكدس` | `स्टैक` | `สแตก` | `ngăn_xếp` | `栈` | `堆疊` |
| `string` | `textus` | `نص` | `पाठ` | `ข้อความ` | `văn_bản` | `文本` | `文字` |
| `tensor` | `tensor` | `موتر` | `टेंसर` | `เทนเซอร์` | `ten_xo` | `张量` | `張量` |
| `trapping` | `exactus` | `دقيق` | `सटीक` | `แม่นยำ` | `chính_xác` | `精确` | `精確` |
| `unknown` | `ignotum` | `مجهول` | `अज्ञात` | `ไม่รู้` | `chưa_biết` | `未知` | `未知` |
| `value` | `valor` | `قيمة` | `मान` | `ค่า` | `giá_trị` | `动态值` | `值` |
| `vector` | `vector` | `متجه` | `सदिश` | `เวกเตอร์` | `vectơ` | `向量` | `向量` |
| `void` | `vacuum` | `فراغ` | `रिक्त` | `เปล่า` | `trống` | `无值` | `空值` |
| `wrapping_ty` | `modulus_t` | `نوع_حلقة` | `मॉड्यूल_टाइप` | `ค่ามอดุลัส` | `môđun_kiểu` | `模数类型` | `模數类型` |

## Intrinsics

Latin has no `[intrinsics]` section, so the Latin column carries each intrinsic's canonical name, which is the Latin spelling. Two canonicals can share one English word — `unio` and `union` both read `union` — so read the Latin column to tell them apart.

| English | Latin | ar | hi | th-TH | vi | zh-Hans | zh-Hant |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `abs` | `absolutum` | `القيمة_المطلقة` | `निरपेक्ष` | `ค่าสัมบูรณ์` | `giá_trị_tuyệt_đối` | `绝对值` | `絕對值` |
| `add` | `adde` | `أضف` | `जोड़ो` | `เพิ่ม` | `thêm` | `添加` | `新增` |
| `added` | `addita` | `مضاف` | `जोड़ा` | `เพิ่มแล้ว` | `đã_thêm` | `已添加` | `已新增` |
| `added_bias` | `addita_bias` | `مضاف_الانحياز` | `बायस_जोड़ा` | `เพิ่มไบแอส` | `đã_thêm_độ_lệch` | `加偏置` | `加偏置` |
| `all` | `omnia` | `الكل` | `सभी` | `ทั้งหมด` | `tất_cả` | `全部` | `全部` |
| `any` | `quilibet` | `أي` | `कोई` | `ใดก็ได้` | `bất_kỳ` | `任一` | `任一` |
| `append` | `appende` | `ألحق` | `पीछे_जोड़ो` | `ต่อท้าย` | `nối_đuôi` | `追加` | `附加` |
| `apply` | `applica` | `طبق` | `लगाओ` | `ประยุกต์` | `áp_dụng` | `应用` | `套用` |
| `approx` | `approximata` | `مقارب` | `सन्निकट` | `ประมาณ` | `xấp_xỉ` | `近似` | `近似` |
| `argmax` | `argmaxima` | `فهرس_الأكبر` | `argmax` | `ดัชนีค่าสูงสุด` | `argmax` | `最大值索引` | `最大值索引` |
| `argmin` | `argminima` | `فهرس_الأصغر` | `argmin` | `ดัชนีค่าต่ําสุด` | `argmin` | `最小值索引` | `最小值索引` |
| `at_least` | `maxime` | `على_الأقل` | `कम_से_कम` | `อย่างน้อย` | `ít_nhất` | `至少` | `至少` |
| `at_most` | `minime` | `على_الأكثر` | `अधिक_से_अधिक` | `อย่างมาก` | `nhiều_nhất` | `至多` | `至多` |
| `bit_and` | `coniuncta` | `و_بت` | `बिट_और` | `และบิต` | `và_bit` | `按位与` | `位元與` |
| `bit_and_assign` | `coniunge` | `و_بت_إسناد` | `बिट_और_सौंपो` | `และบิตกําหนด` | `và_bit_gán` | `按位与赋值` | `位元與指派` |
| `bit_or` | `disiuncta` | `أو_بت` | `बिट_या` | `หรือบิต` | `hoặc_bit` | `按位或` | `位元或` |
| `bit_or_assign` | `disiunge` | `أو_بت_إسناد` | `बिट_या_सौंपो` | `หรือบิตกําหนด` | `hoặc_bit_gán` | `按位或赋值` | `位元或指派` |
| `ceiling` | `tectum` | `تقريب_لأعلى` | `ऊपर_पूर्णांक` | `ปัดขึ้น` | `làm_tròn_lên` | `向上取整` | `向上取整` |
| `clamp` | `coercere` | `قيد` | `सीमित_करो` | `จํากัดค่า` | `giới_hạn` | `限幅` | `限幅` |
| `compare_exchange` | `compare_exchange` | `قارن_وبدل` | `तुलना_और_बदलो` | `เทียบแล้วสลับ` | `so_sánh_và_đổi` | `比较并交换` | `比較並交換` |
| `complement` | `complementa` | `كمل` | `पूरक_करो` | `กลับบิต` | `bù` | `取补` | `取補` |
| `complemented` | `complementata` | `مكمل` | `पूरक` | `กลับบิตแล้ว` | `đã_bù` | `已取补` | `已取補` |
| `contains` | `continet` | `يحتوي` | `शामिल` | `ประกอบด้วย` | `chứa` | `包含` | `包含` |
| `cos` | `cosinus` | `جيب_التمام` | `कोज्या` | `โคไซน์` | `cos` | `余弦` | `餘弦` |
| `create` | `crea` | `أنشئ` | `बनाओ` | `สร้าง` | `tạo` | `创建` | `建立` |
| `cross` | `transversum` | `الجداء_الاتجاهي` | `सदिश_गुणनफल` | `ครอสโปรดักต์` | `tích_có_hướng` | `叉积` | `叉積` |
| `cross_entropy` | `crux_entropia` | `إنتروبيا_متقاطعة` | `क्रॉस_एंट्रॉपी` | `ครอสเอนโทรปี` | `entropy_chéo` | `交叉熵` | `交叉熵` |
| `cumulate` | `cumulata` | `تراكمي` | `संचयी` | `สะสม` | `tích_lũy` | `累积` | `累積` |
| `cursor` | `cursor` | `مؤشر` | `कर्सर` | `ตัวชี้` | `bộ_lặp` | `游标` | `游標` |
| `delete` | `dele` | `امسح` | `मिटाओ` | `ลบ` | `xóa` | `删除` | `刪除` |
| `densify` | `densata` | `كثف` | `घना_करो` | `ทําให้หนาแน่น` | `làm_đặc` | `稠密化` | `稠密化` |
| `difference` | `differentia` | `الفرق` | `अंतर` | `ผลต่าง` | `hiệu` | `差集` | `差集` |
| `divide` | `divida` | `اقسم` | `भाग_दो` | `หาร` | `chia` | `除以` | `除以` |
| `divide` | `divisio` | `قسمة` | `विभाजन` | `การหาร` | `phép_chia` | `除法` | `除法` |
| `divided` | `divisa` | `مقسوم` | `विभाजित` | `หารแล้ว` | `đã_chia` | `已除以` | `已除以` |
| `dot` | `productum` | `الجداء_النقطي` | `बिंदु_गुणनफल` | `ดอตโปรดักต์` | `tích_vô_hướng` | `点积` | `點積` |
| `drop` | `omissa` | `أسقط` | `आरंभ_छोड़ो` | `ข้าม` | `bỏ_qua` | `丢弃` | `捨棄` |
| `end` | `terminus` | `النهاية` | `अंत` | `สิ้นสุด` | `kết_thúc` | `结束` | `結束` |
| `ends_with` | `finis` | `ينتهي_ب` | `पर_समाप्त` | `ลงท้ายด้วย` | `kết_thúc_bằng` | `结尾是` | `結尾是` |
| `escape` | `munita` | `تهريب` | `एस्केप` | `เอสเคป` | `thoát_ký_tự` | `转义` | `跳脫` |
| `exchange` | `exchange` | `بدل` | `अदलाबदली` | `สลับ` | `đổi` | `交换` | `交換` |
| `exp` | `exponentia` | `الأسي` | `चरघातांकी` | `เอกซ์โพเนนเชียล` | `hàm_mũ` | `指数` | `指數` |
| `fill` | `reple` | `املأ` | `भरो` | `เติม` | `điền` | `填充` | `填充` |
| `filter` | `filtrata` | `رشح` | `छानो` | `กรอง` | `lọc` | `过滤` | `過濾` |
| `find` | `inventa` | `ابحث` | `खोज` | `ค้นหา` | `tìm` | `查找` | `尋找` |
| `find_all` | `collecta` | `ابحث_عن_الكل` | `सभी_खोज` | `ค้นหาทั้งหมด` | `tìm_tất_cả` | `查找全部` | `尋找全部` |
| `first` | `primus` | `الأول` | `पहला` | `ตัวแรก` | `đầu_tiên` | `第一个` | `第一個` |
| `flatten` | `planata` | `سطح` | `समतल_करो` | `ทําให้แบน` | `làm_phẳng` | `展平` | `展平` |
| `flip` | `alterna` | `اقلب` | `पलटो` | `พลิกค่า` | `lật` | `翻转` | `翻轉` |
| `flipped` | `alternata` | `مقلوب` | `पलटा` | `พลิกแล้ว` | `đã_lật` | `已翻转` | `已翻轉` |
| `floor` | `pavimentum` | `تقريب_لأسفل` | `नीचे_पूर्णांक` | `ปัดลง` | `làm_tròn_xuống` | `向下取整` | `向下取整` |
| `formata` | `formata` | `formata` | `formata` | `formata` | `formata` | `formata` | `formata` |
| `from_flat` | `strue` | `ابن_من_مسطح` | `समतल_से_बनाओ` | `สร้างจากข้อมูลแบน` | `dựng_từ_phẳng` | `由扁平构造` | `由扁平建構` |
| `gather` | `gather` | `اجمع_بالفهرس` | `एकत्र_करो` | `รวบรวม` | `thu_thập` | `收集` | `收集` |
| `gelu` | `gelu` | `gelu` | `gelu` | `gelu` | `gelu` | `gelu` | `gelu` |
| `get` | `accipe` | `اجلب` | `पाओ` | `ดึง` | `lấy` | `获取` | `取得` |
| `greater` | `maior` | `أكبر` | `बड़ा` | `มากกว่า` | `lớn_hơn` | `大于` | `大於` |
| `group` | `coetus` | `مجموعة` | `समूह` | `กลุ่ม` | `nhóm` | `分组` | `分組` |
| `has` | `habet` | `يملك` | `उपस्थित` | `มีอยู่` | `có` | `含有` | `含有` |
| `intersect` | `inter` | `تقاطع` | `प्रतिच्छेद` | `ตัดกัน` | `giao_với` | `相交` | `相交` |
| `intersection` | `intersectio` | `التقاطع` | `प्रतिच्छेदन` | `ส่วนตัด` | `giao` | `交集` | `交集` |
| `invert` | `inversa` | `معكوس` | `व्युत्क्रम` | `ผกผัน` | `nghịch_đảo` | `求逆` | `求逆` |
| `is_empty` | `vacua` | `فارغ` | `रिक्त` | `ว่าง` | `rỗng` | `为空` | `為空` |
| `is_subset` | `subcopia` | `مجموعة_جزئية` | `उपसमुच्चय_है` | `เป็นชุดย่อย` | `là_tập_con` | `是子集` | `是子集` |
| `is_superset` | `supercopia` | `مجموعة_شاملة` | `अधिसमुच्चय_है` | `เป็นชุดครอบ` | `là_tập_cha` | `是超集` | `是超集` |
| `keys` | `claves` | `المفاتيح` | `कुंजियाँ` | `คีย์` | `khóa` | `键列表` | `鍵列表` |
| `last` | `ultimus` | `الأخير` | `अंतिम` | `ตัวสุดท้าย` | `cuối_cùng` | `最后一个` | `最後一個` |
| `layer_norm` | `laminatio` | `تطبيع_الطبقة` | `परत_सामान्यीकरण` | `เลเยอร์นอร์ม` | `chuẩn_hóa_lớp` | `层归一化` | `層正規化` |
| `length` | `longitudo` | `طول` | `लंबाई` | `ความยาว` | `độ_dài` | `长度` | `長度` |
| `less` | `minor` | `أصغر` | `छोटा` | `น้อยกว่า` | `nhỏ_hơn` | `小于` | `小於` |
| `ln` | `logarithmus` | `اللوغاريتم_الطبيعي` | `प्राकृतिक_लघुगणक` | `ลอการิทึมธรรมชาติ` | `lôgarit_tự_nhiên` | `自然对数` | `自然對數` |
| `load` | `load` | `حمل` | `लोड` | `โหลด` | `nạp` | `加载` | `載入` |
| `log10` | `logarithmus_decimalis` | `اللوغاريتم_العشري` | `दशमलव_लघुगणक` | `ลอการิทึมฐานสิบ` | `lôgarit_thập_phân` | `常用对数` | `常用對數` |
| `lowercase` | `minuscula` | `أحرف_صغيرة` | `छोटे_अक्षर` | `ตัวพิมพ์เล็ก` | `chữ_thường` | `小写` | `小寫` |
| `map` | `mappata` | `حول` | `रूपांतरित` | `แปลง` | `ánh_xạ` | `变换` | `變換` |
| `matches` | `consentit` | `يطابق` | `मेल_खाता_है` | `ตรงกับ` | `khớp` | `匹配` | `比對` |
| `materialize` | `materialize` | `جسد` | `मूर्त_करो` | `ทําให้เป็นรูปธรรม` | `hiện_thực_hóa` | `物化` | `物化` |
| `matmul` | `matmul` | `ضرب_المصفوفات` | `आव्यूह_गुणन` | `คูณเมทริกซ์` | `nhân_ma_trận` | `矩阵乘法` | `矩陣乘法` |
| `maximum` | `maximus` | `الأقصى` | `अधिकतम` | `สูงสุด` | `lớn_nhất` | `最大值` | `最大值` |
| `mean` | `media` | `المتوسط` | `माध्य` | `ค่าเฉลี่ย` | `trung_bình` | `均值` | `平均值` |
| `minimum` | `minimus` | `الأدنى` | `न्यूनतम` | `ต่ําสุด` | `nhỏ_nhất` | `最小值` | `最小值` |
| `modulo` | `modulata` | `الباقي` | `शेषफल` | `มอดูโล` | `chia_lấy_dư` | `取模` | `取餘` |
| `modulo_assign` | `modula` | `أسند_الباقي` | `शेषफल_सौंपो` | `มอดูโลกําหนด` | `chia_lấy_dư_gán` | `取模赋值` | `取餘指派` |
| `multiplied` | `multiplicata` | `مضروب` | `गुणित` | `คูณแล้ว` | `đã_nhân` | `已乘以` | `已乘以` |
| `multiply` | `multiplica` | `اضرب` | `गुणा_करो` | `คูณ` | `nhân` | `乘以` | `乘以` |
| `named` | `nominatus` | `مسماة` | `नामित` | `กลุ่มชื่อ` | `đặt_tên` | `命名分组` | `命名分組` |
| `negate` | `nega` | `اعكس_الإشارة` | `चिह्न_पलटो` | `กลับเครื่องหมาย` | `đổi_dấu` | `取负` | `取負` |
| `negated` | `negativa` | `معكوس_الإشارة` | `चिह्न_पलटा` | `กลับเครื่องหมายแล้ว` | `đã_đổi_dấu` | `已取负` | `已取負` |
| `nonzero_count` | `nonnihil` | `عدّ_اللاصفريّات` | `अशून्य_गणना` | `นับไม่ศูนย์` | `đếm_khác_không` | `非零个数` | `非零個數` |
| `normalize` | `normalizata` | `طبّع` | `सामान्यीकृत` | `ทําให้เป็นบรรทัดฐาน` | `chuẩn_hóa` | `归一化` | `正規化` |
| `power` | `potentia` | `قوة` | `घात` | `ยกกําลัง` | `lũy_thừa` | `乘方` | `乘冪` |
| `put` | `pone` | `ضع` | `रखो` | `ใส่` | `đặt` | `放入` | `放入` |
| `reduce` | `reducta` | `اختزل` | `समेटो` | `ลดรูป` | `rút_gọn` | `归约` | `歸約` |
| `relu` | `activatio_relu` | `تنشيط_ريلو` | `रेलू_सक्रियण` | `เรลูแอกทิเวชัน` | `kích_hoạt_relu` | `ReLU` | `ReLU` |
| `remove_first` | `decapita` | `احذف_الأول` | `पहला_हटाओ` | `ลบตัวแรก` | `bỏ_đầu` | `移除首项` | `移除首項` |
| `remove_last` | `detrahe` | `احذف_الأخير` | `अंतिम_हटाओ` | `ลบตัวท้าย` | `bỏ_cuối` | `移除末项` | `移除末項` |
| `replace` | `muta` | `استبدل` | `बदलो` | `แทนที่` | `thay` | `替换` | `替換` |
| `reshape` | `forma` | `أعد_التشكيل` | `आकार_बदलो` | `เปลี่ยนรูปร่าง` | `định_hình_lại` | `重塑` | `重塑` |
| `reverse` | `inverte` | `اعكس` | `उलटो` | `กลับลําดับ` | `đảo` | `反转` | `反轉` |
| `rms_norm` | `rms_norm` | `rms_norm` | `rms_norm` | `rms_norm` | `rms_norm` | `rms_norm` | `rms_norm` |
| `rope_norm` | `rope_norm` | `rope_norm` | `rope_norm` | `rope_norm` | `rope_norm` | `rope_norm` | `rope_norm` |
| `round` | `rotunda` | `قرب` | `निकटतम_पूर्णांक` | `ปัดเศษ` | `làm_tròn` | `四舍五入` | `四捨五入` |
| `set` | `ponde` | `اضبط` | `निर्धारित_करो` | `กําหนด` | `thiết_lập` | `设置` | `設定` |
| `shape` | `magnitudines` | `الأبعاد` | `आकृति` | `รูปร่าง` | `hình_dạng` | `形状` | `形狀` |
| `shift_left` | `sinistra` | `أزح_يسارا` | `बाएँ_सरकाओ` | `เลื่อนซ้าย` | `dịch_trái` | `左移` | `左移` |
| `shift_right` | `dextra` | `أزح_يمينا` | `दाएँ_सरकाओ` | `เลื่อนขวา` | `dịch_phải` | `右移` | `右移` |
| `shifted_left` | `sinistrata` | `مزاح_يسارا` | `बाएँ_सरकाया` | `เลื่อนซ้ายแล้ว` | `đã_dịch_trái` | `已左移` | `已左移` |
| `shifted_right` | `dextrata` | `مزاح_يمينا` | `दाएँ_सरकाया` | `เลื่อนขวาแล้ว` | `đã_dịch_phải` | `已右移` | `已右移` |
| `sign` | `signum` | `إشارة` | `चिह्न` | `เครื่องหมาย` | `dấu` | `符号` | `符號` |
| `silu` | `silu` | `silu` | `silu` | `silu` | `silu` | `silu` | `silu` |
| `sin` | `sinus` | `جيب` | `ज्या` | `ไซน์` | `sin` | `正弦` | `正弦` |
| `slice` | `sectio` | `شريحة` | `टुकड़ा` | `ตัดช่วง` | `cắt` | `切片` | `切片` |
| `softmax` | `activatio_softmax` | `تنشيط_سوفتماكس` | `सॉफ्टमैक्स` | `ซอฟต์แมกซ์` | `kích_hoạt_softmax` | `Softmax` | `Softmax` |
| `sort` | `ordina` | `رتب` | `क्रमबद्ध_करो` | `เรียง` | `sắp_xếp` | `排序` | `排序` |
| `sorted` | `ordinata` | `مرتب` | `क्रमबद्ध` | `เรียงแล้ว` | `đã_sắp_xếp` | `已排序` | `已排序` |
| `split` | `divide` | `افصل` | `बाँटो` | `แยก` | `tách` | `分割` | `分割` |
| `sqrt` | `radix` | `الجذر_التربيعي` | `वर्गमूल` | `รากที่สอง` | `căn_bậc_hai` | `平方根` | `平方根` |
| `start` | `principium` | `البداية` | `आरंभ` | `เริ่มต้น` | `bắt_đầu` | `起始` | `起始` |
| `starts_with` | `initium` | `يبدأ_ب` | `से_आरंभ` | `ขึ้นต้นด้วย` | `bắt_đầu_bằng` | `开头是` | `開頭是` |
| `store` | `store` | `خزن` | `संचय` | `เก็บ` | `lưu` | `存储` | `儲存` |
| `subtract` | `subtrahe` | `اطرح` | `घटाओ` | `ลบออก` | `trừ` | `减去` | `減去` |
| `subtracted` | `subtracta` | `مطروح` | `घटाया` | `ลบออกแล้ว` | `đã_trừ` | `已减去` | `已減去` |
| `sum` | `summa` | `المجموع` | `योग` | `ผลรวม` | `tổng` | `求和` | `求和` |
| `swizzle` | `swizzle` | `swizzle` | `swizzle` | `swizzle` | `swizzle` | `swizzle` | `swizzle` |
| `symmetric_difference` | `symmetrica` | `الفرق_المتماثل` | `सममित_अंतर` | `ผลต่างสมมาตร` | `hiệu_đối_xứng` | `对称差集` | `對稱差集` |
| `take` | `prima` | `خذ_الأولى` | `पहले_लो` | `ส่วนต้น` | `lấy_đầu` | `取前` | `取前` |
| `take_last` | `ultima` | `خذ_الأخيرة` | `अंतिम_लो` | `เอาท้าย` | `lấy_cuối` | `取后` | `取後` |
| `tan` | `tangens` | `الظل` | `स्पर्शज्या` | `แทนเจนต์` | `tan` | `正切` | `正切` |
| `text` | `inventum` | `النص` | `पाठ` | `ข้อความ` | `văn_bản` | `文本` | `文字` |
| `transpose` | `transpone` | `منقول` | `परिवर्त` | `ทรานสโพส` | `chuyển_vị` | `转置` | `轉置` |
| `trim` | `recide` | `شذب` | `छाँटो` | `ตัดช่องว่าง` | `cắt_khoảng_trắng` | `修剪空白` | `修剪空白` |
| `truncate` | `trunca` | `اقتطع` | `काटो` | `ตัดทิ้ง` | `cắt_bỏ` | `截断` | `截斷` |
| `union` | `unio` | `الاتحاد` | `सम्मिलन` | `ส่วนรวม` | `hợp` | `并集` | `聯集` |
| `union` | `union` | `اتحاد` | `सम्मिलन` | `ส่วนรวม` | `hợp` | `并集` | `聯集` |
| `uppercase` | `maiuscula` | `أحرف_كبيرة` | `बड़े_अक्षर` | `ตัวพิมพ์ใหญ่` | `chữ_hoa` | `大写` | `大寫` |
| `values` | `valores` | `القيم` | `मान` | `ค่าทั้งหมด` | `giá_trị` | `值列表` | `值列表` |

### Alias rows

These rows name an accepted alternate spelling. Both spellings are legal.

- `approximata` in `intrinsics` is also written `approximata`.

## Contested rows

2 rows are not declared by every pack. Each is owned by the compiler-side pack fix rather than by this table, which shows them as they are.

- `conversion` in `keywords`: missing from `en`, `la`.
- `nihil` in `keywords`: missing from `la`.

Fetch list: https://faberlang.dev/agents/index.md
