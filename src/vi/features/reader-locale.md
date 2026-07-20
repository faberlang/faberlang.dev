+++
translation_kind = "translated"

title = "Reader locale"
section = "features"
order = 1
sources = []


prose_hash = "sha256:4b909cabbc40f43896ed8b7b15ac304b8a10b008d73df027bf4a3c2ac975ffed"
code_hash = "sha256:ee712d08c1cd8884f42aa5e872441223a539f58bf4cdcc50824748dc1108f58d"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
Reader locale là hệ thống của Faber để kết xuất mã nguồn, chẩn đoán trình biên dịch và từ khóa ngôn ngữ theo ngôn ngữ con người của người đọc — mà không phân nhánh ngữ nghĩa. Một lập trình viên Thái có thể đọc và viết mã nguồn Faber bằng từ khóa tiếng Thái, nhận lỗi trình biên dịch bằng tiếng Thái và cộng tác thông qua cùng một HIR như người dùng tiếng Latin hoặc tiếng Trung. Cơ chế bản địa hóa mã từ tiếng Latin sang tiếng Thái cũng chính là cơ chế phát mã sang Rust: `HIR → surface` — không dạng nào được ưu tiên.

## Vấn đề {#problem}

Các mô hình ngôn ngữ lớn đã bản địa hóa **cuộc hội thoại** xoay quanh việc lập trình — một nhà khoa học máy tính người Thái có thể yêu cầu LLM trợ giúp bằng tiếng Thái — nhưng chưa bản địa hóa **hiện vật** bền vững. Mã được sinh ra, API, lỗi trình biên dịch và tài liệu vẫn mang hình dạng tiếng Anh. Năng lực tiếng Anh trở thành rào cản để học khoa học máy tính, không chỉ là rào cản trong hội thoại.

Reader locale là phản hồi thiết kế cho vấn đề này: ngôn ngữ mà con người dùng để *hiểu* Faber — mã nguồn, chẩn đoán và tùy chọn là cách viết của stdlib — mà không cần tiếng Anh làm điều kiện tiên quyết. Đây không phải là quốc tế hóa ứng dụng (bao phủ đầy đủ ma trận chuỗi). Đây là hỗ trợ phương ngữ dành cho người đọc: các gói tùy chọn, bao phủ một phần trên một lõi ngữ nghĩa không bị phân nhánh.

> **Luận đề sản phẩm:** Tiếng Anh không nên là ngôn ngữ bắt buộc để xem xét ý định phần mềm. LLM đã bản địa hóa cuộc hội thoại xoay quanh việc lập trình; reader locale bản địa hóa hiện vật bền vững.

## Cách hoạt động {#how}

Một gói reader locale ánh xạ từ khóa Faber, cách viết kiểu nguyên thủy và mẫu chẩn đoán sang ngôn ngữ đích. Các gói là tệp TOML với ba bảng:

- `[keywords]` — ánh xạ tên từ khóa sang cách viết được bản địa hóa
- `[types]` — ánh xạ tên kiểu nguyên thủy sang cách viết được bản địa hóa
- `[diagnostics.*]` — ánh xạ mã chẩn đoán sang mẫu thông báo được bản địa hóa
- `[llm]` — các đoạn nhắc hệ thống và ví dụ mẫu để LLM sinh mã

Trình biên dịch xác thực các gói dựa trên một khung Latin được sinh tự động — mọi từ khóa và kiểu đều phải có cách viết được định nghĩa hoặc phải kế thừa rõ ràng từ Latin. Các dòng còn thiếu tạo ra cơ chế dự phòng hiển thị được thay vì khoảng trống im lặng.

Chọn một locale trên dòng lệnh hoặc trong `faber.toml`:

```text
faber check --reader-locale th-TH program.fab
```

```toml
# faber.toml
[reader]
locale = "zh-Hans"
```

### Thành phần nào được bản địa hóa và thành phần nào không {#what-localises}

| Lớp | Trong HIR? | Hành vi |
|---|---|---|
| Từ khóa, kiểu, cụm từ ghép đôi | Có | Không mất mát qua mọi kết xuất |
| Glyph `← → ∴ ≡ ∪ ⇥` | Có (bất biến) | Giống hệt trong mọi kết xuất |
| Cấu trúc kiểu đứng trước | Có | Giống hệt trong mọi kết xuất |
| Chữ số | — | Chỉ ASCII trong mọi locale |
| Chú thích | Không | Ngoài phạm vi trình biên dịch; do LLM trung gian, tùy chọn |
| Tên định danh | Không | Được giữ nguyên từng byte |
| Cách viết stdlib | Không | Lớp phủ theo từng locale |

Đảm bảo kiến trúc quan trọng là: bất kỳ bề mặt locale nào cũng có thể trở thành bất kỳ bề mặt nào khác, bao gồm cả Latin, vào bất kỳ lúc nào. Tệp Faber được bản địa hóa không bao giờ là cái bẫy vì nó không bao giờ là dạng duy nhất mà mã có thể có. `faber format --canonical` chính xác là `faber format --reader-locale=la`.

## Các gói đã phát hành {#locales}

Radix hiện phát hành bảy gói:

| Mã | Ngôn ngữ | Chữ viết | Trạng thái |
|---|---|---|---|
| `la` | Latina (Latin) | Latin | **Chuẩn** |
| `th-TH` | ไทย | Thái | **Bằng chứng tham chiếu** |
| `zh-Hans` | 简体中文 | Tiếng Trung giản thể | Bằng chứng độ bao phủ |
| `zh-Hant` | 繁體中文 | Tiếng Trung phồn thể | Bằng chứng độ bao phủ |
| `ar` | العربية | Ả Rập | Bằng chứng độ bao phủ |
| `hi` | हिन्दी | Devanagari | Bằng chứng độ bao phủ |
| `vi` | Tiếng Việt | Tiếng Việt (Latin) | Bằng chứng độ bao phủ |

Năm locale tham chiếu được chọn vì **tạo áp lực kiến trúc tập thể** — cùng nhau, chúng buộc mọi vấn đề Unicode và phát mã mà nền tảng phải chịu được phải xuất hiện. Bốn locale dùng chữ viết phi Latin; tiếng Việt là trường hợp đối chứng dùng chữ Latin:

| Locale | Mức độ tiếp cận | Áp lực kiến trúc |
|---|---|---|
| `th-TH` | Cao | Chữ viết không có khoảng trắng — bài kiểm tra áp lực cho bộ tách token |
| `zh-Hans` / `zh-Hant` | Rất cao | Từ khóa ghép đôi; kế thừa gói anh em; thu gọn độ rộng NFKC |
| `ar` | Cao | Viết từ phải sang trái; cô lập bidi trong chẩn đoán |
| `hi` | Rất cao | Cụm matra/virama; chữ số Indic |
| `vi` | Cao | Dấu phụ dày đặc trên chữ Latin; các trường hợp biên NFKC |

*Tập tham chiếu được chọn để bao phủ kiến trúc, không phải dân số. Chỉ riêng dân số sẽ không chứng minh được điều gì mà nền tảng chưa xử lý.*

## Ví dụ mã nguồn được bản địa hóa {#examples}

Mỗi trong sáu locale không chuẩn đều có một gói Faber hoàn chỉnh dưới
`examples/reader-locale/` với mã nguồn được bản địa hóa, các trường hợp kiểm thử chẩn đoán và một manifest `faber.toml`. Cùng một chương trình `greet` được kết xuất trên tất cả locale đã phát hành:

**Latin** `la` — *chuẩn*

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

Kết xuất chuẩn. `faber format --canonical` chính xác là
`faber format --reader-locale=la`. Từ khóa Latin ánh xạ vào chính chúng;
tên kiểu là cách viết chuẩn.

**ไทย** `th-TH` — *bằng chứng tham chiếu*

```text
ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ {
    ค่าคงที่ ข้อความ msg ← "Salve, §!"(nomen)
    คืนค่า msg
}

เริ่มต้น {
    ค่าคงที่ ข้อความ m ← salve("มุนเด")
    แจ้ง m
}
```

Bằng chứng về nêm tiếp cận. Tiếng Thái là một chữ viết không có khoảng trắng — không có ranh giới giữa các từ — khiến nó trở thành bài kiểm tra áp lực cho bộ tách token và là động lực kiến trúc ban đầu cho hệ thống reader locale. Mọi ranh giới token phải được bộ phân tích từ vựng xác định chỉ thông qua việc khớp từ khóa.

**简体中文** `zh-Hans`

```text
函数 问候(文本 名字) → 文本 {
    常量 文本 问候语 ← "你好，§!"(名字)
    返回 问候语
}

入口 {
    常量 文本 消息 ← 问候("世界")
    显示 消息
}
```

Từ khóa ghép đôi (如果/否则 cho si/secus) yêu cầu các nhóm từ khóa trong gói; dấu câu toàn độ rộng/nửa độ rộng; thu gọn độ rộng NFKC tại điểm vào của bộ phân tích từ vựng. Đây là trường hợp phát mã LLM khó nhất do ranh giới token của CJK. Một gói anh em cho tiếng Trung phồn thể (zh-Hant) kế thừa và ghi đè các gốc của zh-Hans.

**العربية** `ar`

```text
دالة salve(نص nomen) → نص {
    ثابت نص msg ← "مرحبا، §!"(nomen)
    أعد msg
}

بداية {
    ثابت نص m ← salve("عالم")
    اعرض m
}
```

Chữ viết từ phải sang trái được nhúng bên trong khối mã LTR theo thứ tự logic. Từ khóa được bọc trong `<bdi>` (cô lập hai chiều) trong đầu ra chẩn đoán HTML của trình biên dịch để ngăn biến dạng RFO (phải theo sau trái). Mã nguồn thô sử dụng chữ Ả Rập theo thứ tự logic; lớp hiển thị xử lý cách trình bày bidi.

**हिन्दी** `hi`

```text
फलन salve(पाठ nomen) → पाठ {
    स्थिर पाठ msg ← "Salve, §!"(nomen)
    लौटा msg
}

आरंभ {
    स्थिर पाठ m ← salve("जगत")
    दिखा m
}
```

Chữ viết Devanagari với các cụm phụ âm matra/virama. Điều này chứng minh đường đi cho họ Indic rộng hơn — Bengali, Tamil và Telugu kế thừa cùng một hạ tầng định hình — dù việc biên soạn gói cho từng ngôn ngữ vẫn là công việc riêng. Các glyph chữ số Indic (०-९) không được chấp nhận trong literal số; chữ số ASCII được giữ nguyên qua mọi locale.

**Tiếng Việt** `vi`

```text
hàm chào(vănbản tên) → vănbản {
    hằng vănbản lời_chào ← "Xin chào, §!"(tên)
    trả lời_chào
}

bắtđầu {
    hằng vănbản thông_điệp ← chào("thế giới")
    in thông_điệp
}
```

Trường hợp đối chứng: chữ viết Latin nhưng không phải tiếng Anh. Mật độ dấu phụ cao (ế, ệ, ả) tạo áp lực cho các trường hợp biên NFKC trong bộ phân tích từ vựng. Điều này ngăn một kiến trúc chỉ hoạt động trên các chữ viết khác thường nhưng chưa được kiểm chứng trên Latin có dấu phụ. Định danh sử dụng các từ tiếng Việt (chào, tên, lời_chào, thông_điệp), được trình biên dịch giữ nguyên từng byte.

> Các glyph (`← → ∴ ≡ ∪ ⇥`),
> vị trí cấu trúc và tên định danh là **giống hệt** trong cả sáu kết xuất trên. Chỉ từ khóa và tên kiểu thay đổi. HIR hoàn toàn là cùng một chương trình — trình biên dịch coi cả sáu là tương đương. Kết xuất Faber sang tiếng Thái cũng là cùng một thao tác trình biên dịch như kết xuất sang Rust:
> `HIR → surface`, không dạng nào được ưu tiên.

## Chẩn đoán được bản địa hóa {#diagnostics}

Chẩn đoán là **sự kiện có cấu trúc trước khi là văn xuôi**. Mỗi chẩn đoán mang một mã ổn định (`LEX###`, `PARSE###`, `SEM###`,
`WARN###`) và các đối số có tên; gói sở hữu văn bản mẫu được kết xuất. Điều này có nghĩa là bộ kết xuất chẩn đoán có thể phát thông báo bằng bất kỳ locale nào mà không thay đổi hạ tầng chẩn đoán.

Các gói ví dụ reader locale bao gồm các trường hợp kiểm thử chẩn đoán — không tương thích kiểu, biến chưa được định nghĩa, số không phải ASCII — chứng minh toàn bộ pipeline nhận biết locale:

- `examples/reader-locale/vi/src/type-mismatch.fab`
- `examples/reader-locale/vi/src/undefined-variable.fab`
- `examples/reader-locale/vi/src/non-ascii-number.fab`
- `examples/reader-locale/vi/src/keyword-suggestion.fab`
- `examples/reader-locale/vi/src/keyword-edit-distance.fab`

Cô lập bidi được tích hợp sẵn: các từ khóa Ả Rập bên trong khối mã LTR theo thứ tự logic được bọc trong phần tử `<bdi>` trong đầu ra HTML, ngăn biến dạng RFO (phải theo sau trái) vốn sẽ khiến các đoạn RTL không thể đọc được.

## Trạng thái {#status}

| Lớp | Trạng thái |
|---|---|
| Lược đồ gói, bí danh, kế thừa, xác thực, chẩn đoán, hiện vật LLM | **Đã phát hành** |
| Phân tích từ vựng nhận biết gói, phân giải kiểu, lựa chọn manifest/CLI, cơ chế dự phòng hiển thị được | **Đã phát hành** |
| Kết xuất chẩn đoán do gói sở hữu, `faber explain`, hiển thị cô lập bidi | **Đã phát hành** |
| Định dạng Faber chuẩn | **Đã phát hành** |
| Phát hành lại Faber được bản địa hóa (`format --reader-locale`) | Một phần |
| Lớp phủ thuật ngữ stdlib, độ trung thực phát mã LLM được đo lường, độ bao phủ locale hoàn chỉnh | Hoãn |
| Sinh tài liệu đa ngôn ngữ | Đề xuất |

Điều kiện tiên quyết của nền tảng — chuẩn hóa NFKC tại điểm vào của bộ phân tích từ vựng — đã hoàn tất. Bảng từ khóa, đối số có tên của chẩn đoán, bộ kết xuất và việc phân phối gói đã được phát hành. Các lớp định hướng dài hạn (phát hành lại được bản địa hóa, thuật ngữ stdlib, chuẩn đo độ trung thực phát mã LLM, tài liệu đa ngôn ngữ được sinh tự động) vẫn được xác định rõ là một phần hoặc hoãn.

## Tài liệu tham khảo {#references}

1. `radix/docs/design/reader-locale.md` — tài liệu thiết kế đầy đủ (69 KB)
2. `examples/reader-locale/` — 6 gói locale với mã nguồn được bản địa hóa
3. `stdlib/reader/*/pack.toml` — 7 định nghĩa gói đã cài đặt
4. `radix/crates/radix/src/reader_locale.rs` — triển khai thời gian chạy
5. `radix/docs/design/faber-canonical-surface.md` — chế độ chuẩn và `faber format`
6. `radix/docs/factory/lex-nfkc-normalization/` — bản phân phối điều kiện tiên quyết NFKC
