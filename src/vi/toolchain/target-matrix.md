+++
title = "Tính tương thích của đích"
section = "targets"
order = 2
sources = "faber/docs/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"

translation_kind = "translated"
prose_hash = "sha256:b3536d8c9fab0622a390939f881750639929acd17972834bf595a908d531ec01"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "abae3f195790fe8cfe9061376b8f66e3d08489b9"
source_locale = "en-US"
+++

Faber là một ngôn ngữ với nhiều hợp đồng biên dịch. Trang này là **ma trận khả
năng hạ mã được đo lường**: với mỗi thuật ngữ trong corpus, đích nào có thể hạ
mã thuật ngữ đó và ở mức hỗ trợ nào.

Các động từ chính sách (hỗ trợ / loại bỏ / cảnh báo / từ chối / trì hoãn) và định
tuyến pipeline nằm trên [Codegen targets](/tooling/codegen-targets.html). Trang
này là danh sách hàng lớn, dễ quét — các đích trên application-lane của HIR và
systems-lane của MIR nằm cạnh nhau trong các bảng bên dưới.

Tóm tắt CLI trực tiếp: `faber targets`.

**Được dựng**: unknown bởi `faber/scripta/render-matrices.py` từ JSON đo lường radix — **không chỉnh sửa**.
**Đo lường**: `emit_hir_target_matrix` + `emit_mir_target_matrix` (trong tiến trình, không dùng toolchain bên ngoài).
**Kết nối**: các term trong `corpus/index.toml` → exempla.

Đây là **ma trận hỗ trợ grammar×target chính thức được tạo tự động**. Ma trận
báo cáo **khả năng hạ mã** — target X có thể hạ grammar production Y hay không —
cho mọi term trong exempla corpus. Ngữ nghĩa thời gian chạy (các động từ chính
sách erase/warn/defer), hợp đồng theo từng đích và định tuyến pipeline nằm trên
[Codegen targets](/tooling/codegen-targets.html), tài liệu này liên kết ngược về
đây để hiển thị các hàng.

## Chú giải

| Ký hiệu | Ý nghĩa |
|---|---|
| ✓ | Được hỗ trợ đầy đủ — mọi exempla có thể phân tích của term đều hạ mã được |
| ◐ | Một phần — một số exempla hạ mã được, một số có khoảng trống đã đo |
| ○ | Đã lên kế hoạch — chưa hạ mã; curated overlay (`scripta/ebnf-matrix-overrides.toml`) |
| ✕ | Không hỗ trợ — không có exempla nào hạ mã được; khoảng trống đo được là có thật theo mặc định |
| — | Chưa đo — không có exempla có thể phân tích cho term này trên lane này |

> ✓ nghĩa là các corpus exempla sử dụng term này hạ mã được thành target. Điều đó
> **không** đảm bảo ngữ nghĩa thời gian chạy giống hệt nhau. Một số target *loại
> bỏ* hoặc *cảnh báo* với một số construct (ví dụ Go loại bỏ các chế độ mượn
> `de`/`in`/`ex`) — chúng vẫn hiển thị ✓ ở đây vì chúng hạ mã được. Xem tài liệu
> chính sách để hiểu rõ điểm này.

## Tóm tắt trên toàn corpus (tất cả term đã đăng ký)

**Tuyến ứng dụng (HIR → ngôn ngữ nguồn được phát ra)**

| đích | có khả năng | có thể phân tích | % |
|---|---|---|---|
| rust | 340 | 344 | 99% |
| go | 319 | 344 | 93% |
| ts | 344 | 344 | 100% |
| faber | 344 | 344 | 100% |

**Tuyến hệ thống (MIR → tạo phẩm thiết bị/IR)**

| đích | có khả năng | có thể phân tích | % |
|---|---|---|---|
| llvm-text | 311 | 338 | 92% |
| wasm-text | 249 | 338 | 74% |
| wasm | 249 | 338 | 74% |
| sexp-struct | 272 | 338 | 80% |
| sexp | 272 | 338 | 80% |
| scena | 282 | 338 | 83% |

## Từ khóa — tuyến ứng dụng

### từ khóa

| term | rust | go | ts | faber |
|---|---|---|---|---|
| <a id="abstractus"></a>`abstractus` | ✓ | ✓ | ✓ | ✓ |
| <a id="ab"></a>`ab` | ✓ | ✓ | ✓ | ✓ |
| <a id="ad"></a>`ad` | ✓ | ✕ | ✓ | ✓ |
| <a id="adfirma"></a>`adfirma` | ✓ | ✓ | ✓ | ✓ |
| <a id="ante"></a>`ante` | ✓ | ✓ | ✓ | ✓ |
| <a id="atomic"></a>`atomic` | ✕ | ✓ | ✓ | ✓ |
| <a id="argumenta"></a>`argumenta` | ✓ | ✓ | ✓ | ✓ |
| <a id="bivalens"></a>`bivalens` | ✓ | ✓ | ✓ | ✓ |
| <a id="cape"></a>`cape` | ✓ | ✓ | ✓ | ✓ |
| <a id="casu"></a>`casu` | ✓ | ✓ | ✓ | ✓ |
| <a id="cede"></a>`cede` | ✓ | ✓ | ✓ | ✓ |
| <a id="ceteri"></a>`ceteri` | ✓ | ✓ | ✓ | ✓ |
| <a id="ceterum"></a>`ceterum` | ✓ | ✓ | ✓ | ✓ |
| <a id="clausura"></a>`clausura` | ✓ | ✓ | ✓ | ✓ |
| <a id="cli"></a>`cli` | ✓ | ✓ | ✓ | ✓ |
| <a id="copia"></a>`copia` | ✓ | ✓ | ✓ | ✓ |
| <a id="cura"></a>`cura` | ✓ | ✓ | ✓ | ✓ |
| <a id="curata"></a>`curata` | ✓ | ✓ | ✓ | ✓ |
| <a id="cursor"></a>`cursor` | ✓ | ✓ | ✓ | ✓ |
| <a id="custodi"></a>`custodi` | ✓ | ✓ | ✓ | ✓ |
| <a id="de"></a>`de` | ✓ | ✓ | ✓ | ✓ |
| <a id="descriptio"></a>`descriptio` | ✓ | ✓ | ✓ | ✓ |
| <a id="discerne"></a>`discerne` | ✓ | ✓ | ✓ | ✓ |
| <a id="discretio"></a>`discretio` | ✓ | ✓ | ✓ | ✓ |
| <a id="dum"></a>`dum` | ✓ | ✓ | ✓ | ✓ |
| <a id="ego"></a>`ego` | ✓ | ✓ | ✓ | ✓ |
| <a id="elige"></a>`elige` | ✓ | ✓ | ✓ | ✓ |
| <a id="errata"></a>`errata` | ✓ | ✓ | ✓ | ✓ |
| <a id="est"></a>`est` | ✓ | ✓ | ✓ | ✓ |
| <a id="ex"></a>`ex` | ✓ | ✓ | ✓ | ✓ |
| <a id="exitus"></a>`exitus` | ✓ | ✓ | ✓ | ✓ |
| <a id="fac"></a>`fac` | ✓ | ✓ | ✓ | ✓ |
| <a id="falsum"></a>`falsum` | ✓ | ✓ | ✓ | ✓ |
| <a id="fient"></a>`fient` | ✓ | ✓ | ✓ | ✓ |
| <a id="fiet"></a>`fiet` | ✓ | ✓ | ✓ | ✓ |
| <a id="figendum"></a>`figendum` | ✓ | ✓ | ✓ | ✓ |
| <a id="finge"></a>`finge` | ✓ | ✓ | ✓ | ✓ |
| <a id="fiunt"></a>`fiunt` | ✓ | ✓ | ✓ | ✓ |
| <a id="fixum"></a>`fixum` | ✓ | ✓ | ✓ | ✓ |
| <a id="fragilis"></a>`fragilis` | ✓ | ✓ | ✓ | ✓ |
| <a id="fractus"></a>`fractus` | ✓ | ✓ | ✓ | ✓ |
| <a id="functio"></a>`functio` | ✓ | ✓ | ✓ | ✓ |
| <a id="futura"></a>`futura` | ✓ | ✓ | ✓ | ✓ |
| <a id="futurum"></a>`futurum` | ✓ | ✓ | ✓ | ✓ |
| <a id="generis"></a>`generis` | ✓ | ✓ | ✓ | ✓ |
| <a id="genus"></a>`genus` | ✓ | ✓ | ✓ | ✓ |
| <a id="iace"></a>`iace` | ✓ | ✓ | ✓ | ✓ |
| <a id="iacit"></a>`iacit` | ✓ | ✓ | ✓ | ✓ |
| <a id="ignotum"></a>`ignotum` | ✓ | ✓ | ✓ | ✓ |
| <a id="immutata"></a>`immutata` | ✓ | ✓ | ✓ | ✓ |
| <a id="implet"></a>`implet` | ✓ | ✓ | ✓ | ✓ |
| <a id="importa"></a>`importa` | ✓ | ✓ | ✓ | ✓ |
| <a id="in"></a>`in` | — | — | — | — |
| <a id="incipiet"></a>`incipiet` | ✓ | ✓ | ✓ | ✓ |
| <a id="incipit"></a>`incipit` | ✓ | ✓ | ✓ | ✓ |
| <a id="inter"></a>`inter` | ✓ | ✓ | ✓ | ✓ |
| <a id="intra"></a>`intra` | ✓ | ✓ | ✓ | ✓ |
| <a id="instans"></a>`instans` | ✓ | ✓ | ✓ | ✓ |
| <a id="itera"></a>`itera` | ✓ | ◐ | ✓ | ✓ |
| <a id="lege"></a>`lege` | ✓ | ✓ | ✓ | ✓ |
| <a id="lineam"></a>`lineam` | ✓ | ✓ | ✓ | ✓ |
| <a id="lista"></a>`lista` | ✓ | ✓ | ✓ | ✓ |
| <a id="matrix"></a>`matrix` | ✓ | ✕ | ✓ | ✓ |
| <a id="mone"></a>`mone` | ✓ | ✓ | ✓ | ✓ |
| <a id="mori"></a>`mori` | ✓ | ✓ | ✓ | ✓ |
| <a id="nexum"></a>`nexum` | ✓ | ✓ | ✓ | ✓ |
| <a id="nihil"></a>`nihil` | ✓ | ✓ | ✓ | ✓ |
| <a id="numquam"></a>`numquam` | ✓ | ✓ | ✓ | ✓ |
| <a id="numerus"></a>`numerus` | ✓ | ✓ | ✓ | ✓ |
| <a id="non"></a>`non` | ✓ | ✓ | ✓ | ✓ |
| <a id="omitte"></a>`omitte` | ✓ | ✓ | ✓ | ✓ |
| <a id="omnia"></a>`omnia` | ✓ | ✓ | ✓ | ✓ |
| <a id="operandus"></a>`operandus` | ✓ | ✓ | ✓ | ✓ |
| <a id="optio"></a>`optio` | ✓ | ✓ | ✓ | ✓ |
| <a id="optiones"></a>`optiones` | ✓ | ✓ | ✓ | ✓ |
| <a id="ordo"></a>`ordo` | ✓ | ✓ | ✓ | ✓ |
| <a id="octeti"></a>`octeti` | ✓ | ✓ | ✓ | ✓ |
| <a id="implendum"></a>`implendum` | ✓ | ✓ | ✓ | ✓ |
| <a id="per"></a>`per` | ✓ | ✓ | ✓ | ✓ |
| <a id="perge"></a>`perge` | ✓ | ✓ | ✓ | ✓ |
| <a id="postpara"></a>`postpara` | ✓ | ✓ | ✓ | ✓ |
| <a id="postparabit"></a>`postparabit` | ✓ | ✓ | ✓ | ✓ |
| <a id="prae"></a>`prae` | ✓ | ✓ | ✓ | ✓ |
| <a id="praefixum"></a>`praefixum` | — | — | — | — |
| <a id="praepara"></a>`praepara` | ✓ | ✓ | ✓ | ✓ |
| <a id="praeparabit"></a>`praeparabit` | ✓ | ✓ | ✓ | ✓ |
| <a id="promissum"></a>`promissum` | ✓ | ✓ | ✓ | ✓ |
| <a id="privata"></a>`privata` | ✓ | ✓ | ✓ | ✓ |
| <a id="proba"></a>`proba` | ✓ | ✓ | ✓ | ✓ |
| <a id="probandum"></a>`probandum` | ✓ | ✓ | ✓ | ✓ |
| <a id="protecta"></a>`protecta` | — | — | — | — |
| <a id="publica"></a>`publica` | ✓ | ✓ | ✓ | ✓ |
| <a id="ratio"></a>`ratio` | ✓ | ✓ | ✓ | ✓ |
| <a id="redde"></a>`redde` | ✓ | ✓ | ✓ | ✓ |
| <a id="reddet"></a>`reddet` | ✓ | ✓ | ✓ | ✓ |
| <a id="repete"></a>`repete` | ✓ | ✓ | ✓ | ✓ |
| <a id="requirit"></a>`requirit` | ✓ | ✓ | ✓ | ✓ |
| <a id="reice"></a>`reice` | ✓ | ✓ | ✓ | ✓ |
| <a id="rumpe"></a>`rumpe` | ✓ | ✓ | ✓ | ✓ |
| <a id="scribe"></a>`scribe` | ✓ | ✓ | ✓ | ✓ |
| <a id="scriptum"></a>`scriptum` | ✓ | ✓ | ✓ | ✓ |
| <a id="secus"></a>`secus` | ✓ | ✓ | ✓ | ✓ |
| <a id="si"></a>`si` | ✓ | ✓ | ✓ | ✓ |
| <a id="sic"></a>`sic` | ✓ | ✓ | ✓ | ✓ |
| <a id="sin"></a>`sin` | ✓ | ✓ | ✓ | ✓ |
| <a id="sit"></a>`sit` | ✓ | ✓ | ✓ | ✓ |
| <a id="solum-in"></a>`solum_in` | ✓ | ✓ | ✓ | ✓ |
| <a id="solum"></a>`solum` | ✓ | ✓ | ✓ | ✓ |
| <a id="sparge"></a>`sparge` | ✓ | ✓ | ✓ | ✓ |
| <a id="sponte"></a>`sponte` | ✓ | ✓ | ✓ | ✓ |
| <a id="sub"></a>`sub` | — | — | — | — |
| <a id="selective-import"></a>`selective_import` | ✓ | ✓ | ✓ | ✓ |
| <a id="tacet"></a>`tacet` | ✓ | ✓ | ✓ | ✓ |
| <a id="tacebit"></a>`tacebit` | ✓ | ✓ | ✓ | ✓ |
| <a id="tabula"></a>`tabula` | ✓ | ✓ | ✓ | ✓ |
| <a id="tag"></a>`tag` | ✓ | ✓ | ✓ | ✓ |
| <a id="temporis"></a>`temporis` | ✓ | ✓ | ✓ | ✓ |
| <a id="tensor"></a>`tensor` | ✓ | ✓ | ✓ | ✓ |
| <a id="textus"></a>`textus` | ✓ | ✓ | ✓ | ✓ |
| <a id="typus"></a>`typus` | ✓ | ✓ | ✓ | ✓ |
| <a id="ubique"></a>`ubique` | ✓ | ✓ | ✓ | ✓ |
| <a id="usque"></a>`usque` | ✓ | ✓ | ✓ | ✓ |
| <a id="ut"></a>`ut` | ✓ | ✓ | ✓ | ✓ |
| <a id="varia"></a>`varia` | ✓ | ✓ | ✓ | ✓ |
| <a id="variandum"></a>`variandum` | ✓ | ✓ | ✓ | ✓ |
| <a id="vector"></a>`vector` | ✓ | ◐ | ✓ | ✓ |
| <a id="vacuum"></a>`vacuum` | ✓ | ✓ | ✓ | ✓ |
| <a id="verum"></a>`verum` | ✓ | ✓ | ✓ | ✓ |
| <a id="vide"></a>`vide` | ✓ | ✓ | ✓ | ✓ |

## Toán tử — tuyến ứng dụng

### nhóm toán tử

| term | rust | go | ts | faber |
|---|---|---|---|---|
| <a id=""></a>`⊜` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∧` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`·` | ◐ | ◐ | ✓ | ✓ |
| <a id=""></a>`×` | ✓ | ○ | ✓ | ✓ |
| <a id=""></a>`⊗` | ✓ | ○ | ✓ | ✓ |
| <a id=""></a>`⊙` | ✓ | ◐ | ✓ | ✓ |
| <a id=""></a>`→` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`←` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↤` | ✓ | ✓ | ✓ | ✓ |
| <a id="aut"></a>`aut` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`![` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!.` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≠` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!(` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊻` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↦` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇒` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`‥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`…` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≡` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`=` | ✓ | ✓ | ✓ | ✓ |
| <a id="et"></a>`et` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≤` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↓` | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u16"></a>`modulus<u16>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u32"></a>`modulus<u32>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u64"></a>`modulus<u64>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u8"></a>`modulus<u8>` | ✓ | ✕ | ✓ | ✓ |
| <a id="non-est"></a>`non est` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊚` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∨` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∪` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↑` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?[` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?.` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?(` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`§` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇐` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊘` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊛` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`¬` | ✓ | ✓ | ✓ | ✓ |
| <a id="vel"></a>`vel` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∷` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∴` | ✓ | ✓ | ✓ | ✓ |
| <a id="ergo"></a>`ergo` | ✓ | ✓ | ✓ | ✓ |

## Từ khóa — tuyến hệ thống

### từ khóa

| term | llvm-text | wasm-text | wasm | sexp-struct | sexp | scena |
| --- | --- | --- | --- | --- | --- | --- |
| <a id="abstractus"></a>`abstractus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ab"></a>`ab` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ad"></a>`ad` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| <a id="adfirma"></a>`adfirma` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ante"></a>`ante` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="atomic"></a>`atomic` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| <a id="argumenta"></a>`argumenta` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="bivalens"></a>`bivalens` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="cape"></a>`cape` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="casu"></a>`casu` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="cede"></a>`cede` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="ceteri"></a>`ceteri` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ceterum"></a>`ceterum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="clausura"></a>`clausura` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="cli"></a>`cli` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="copia"></a>`copia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="cura"></a>`cura` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="curata"></a>`curata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="cursor"></a>`cursor` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="custodi"></a>`custodi` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="de"></a>`de` | — | — | — | — | — | — |
| <a id="descriptio"></a>`descriptio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="discerne"></a>`discerne` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="discretio"></a>`discretio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="dum"></a>`dum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ego"></a>`ego` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="elige"></a>`elige` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="errata"></a>`errata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="est"></a>`est` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| <a id="ex"></a>`ex` | ◐ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="exitus"></a>`exitus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fac"></a>`fac` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="falsum"></a>`falsum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fient"></a>`fient` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fiet"></a>`fiet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="figendum"></a>`figendum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="finge"></a>`finge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fiunt"></a>`fiunt` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fixum"></a>`fixum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fragilis"></a>`fragilis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="fractus"></a>`fractus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="functio"></a>`functio` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="futura"></a>`futura` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="futurum"></a>`futurum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="generis"></a>`generis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="genus"></a>`genus` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="iace"></a>`iace` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="iacit"></a>`iacit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ignotum"></a>`ignotum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="immutata"></a>`immutata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="implet"></a>`implet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="importa"></a>`importa` | ✓ | ◐ | ◐ | ◐ | ◐ | ◐ |
| <a id="in"></a>`in` | — | — | — | — | — | — |
| <a id="incipiet"></a>`incipiet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="incipit"></a>`incipit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="inter"></a>`inter` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id="intra"></a>`intra` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="instans"></a>`instans` | ✓ | ✕ | ✕ | ✕ | ✕ | ◐ |
| <a id="itera"></a>`itera` | ◐ | ◐ | ◐ | ◐ | ◐ | ✓ |
| <a id="lege"></a>`lege` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="lineam"></a>`lineam` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="lista"></a>`lista` | ◐ | ◐ | ◐ | ◐ | ◐ | ✓ |
| <a id="matrix"></a>`matrix` | ✕ | ✕ | ✕ | ✓ | ✓ | ✕ |
| <a id="mone"></a>`mone` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="mori"></a>`mori` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="nexum"></a>`nexum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="nihil"></a>`nihil` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="numquam"></a>`numquam` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ |
| <a id="numerus"></a>`numerus` | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ |
| <a id="non"></a>`non` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="omitte"></a>`omitte` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="omnia"></a>`omnia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="operandus"></a>`operandus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="optio"></a>`optio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="optiones"></a>`optiones` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="ordo"></a>`ordo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="octeti"></a>`octeti` | ✓ | ◐ | ◐ | ◐ | ◐ | ◐ |
| <a id="implendum"></a>`implendum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="per"></a>`per` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="perge"></a>`perge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="postpara"></a>`postpara` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="postparabit"></a>`postparabit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="prae"></a>`prae` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="praefixum"></a>`praefixum` | — | — | — | — | — | — |
| <a id="praepara"></a>`praepara` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="praeparabit"></a>`praeparabit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="promissum"></a>`promissum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="privata"></a>`privata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="proba"></a>`proba` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="probandum"></a>`probandum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="protecta"></a>`protecta` | — | — | — | — | — | — |
| <a id="publica"></a>`publica` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ratio"></a>`ratio` | — | — | — | — | — | — |
| <a id="redde"></a>`redde` | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ |
| <a id="reddet"></a>`reddet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="repete"></a>`repete` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="requirit"></a>`requirit` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id="reice"></a>`reice` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id="rumpe"></a>`rumpe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="scribe"></a>`scribe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="scriptum"></a>`scriptum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="secus"></a>`secus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="si"></a>`si` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sic"></a>`sic` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sin"></a>`sin` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sit"></a>`sit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="solum-in"></a>`solum_in` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="solum"></a>`solum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="sparge"></a>`sparge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sponte"></a>`sponte` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="sub"></a>`sub` | — | — | — | — | — | — |
| <a id="selective-import"></a>`selective_import` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tacet"></a>`tacet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tacebit"></a>`tacebit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tabula"></a>`tabula` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="tag"></a>`tag` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="temporis"></a>`temporis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="tensor"></a>`tensor` | ✓ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id="textus"></a>`textus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="typus"></a>`typus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ubique"></a>`ubique` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="usque"></a>`usque` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ut"></a>`ut` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="varia"></a>`varia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="variandum"></a>`variandum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vector"></a>`vector` | ✓ | ◐ | ◐ | ◐ | ◐ | ✕ |
| <a id="vacuum"></a>`vacuum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="verum"></a>`verum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vide"></a>`vide` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Toán tử — tuyến hệ thống

### nhóm toán tử

| term | llvm-text | wasm-text | wasm | sexp-struct | sexp | scena |
| --- | --- | --- | --- | --- | --- | --- |
| <a id=""></a>`⊜` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∧` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`·` | ◐ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id=""></a>`×` | ✓ | ○ | ○ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊗` | ○ | ○ | ○ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊙` | ◐ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id=""></a>`→` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇥` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`←` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↤` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="aut"></a>`aut` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`![` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`!.` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`≠` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!(` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊻` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↦` | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ |
| <a id=""></a>`⇒` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`‥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`…` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≡` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`=` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="et"></a>`et` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≤` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↓` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u16"></a>`modulus<u16>` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="modulus-u32"></a>`modulus<u32>` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="modulus-u64"></a>`modulus<u64>` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="modulus-u8"></a>`modulus<u8>` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="non-est"></a>`non est` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊚` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∨` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∪` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↑` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?[` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`?.` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`?(` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`§` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇐` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊘` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊛` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`¬` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vel"></a>`vel` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∷` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id=""></a>`∴` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ergo"></a>`ergo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Các term khác (`existing-home` / không chỉ định)

### existing-home

| term | rust | go | ts | faber |
|---|---|---|---|---|
| <a id="alias"></a>`alias` | ✓ | ✓ | ✓ | ✓ |
| <a id="arena"></a>`arena` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`@` | ✓ | ✓ | ✓ | ✓ |
| <a id="f16"></a>`f16` | ✕ | ✓ | ✓ | ✓ |
| <a id="forma"></a>`forma` | ✓ | ✓ | ✓ | ✓ |
| <a id="imperia"></a>`imperia` | ✓ | ✓ | ✓ | ✓ |
| <a id="imperium"></a>`imperium` | ✓ | ✓ | ✓ | ✓ |
| <a id="iuncta"></a>`iuncta` | ✓ | ✓ | ✓ | ✓ |
| <a id="manifest"></a>`manifest` | ✓ | ✓ | ✓ | ✓ |
| <a id="metior"></a>`metior` | ✓ | ✓ | ✓ | ✓ |
| <a id="named-holes"></a>`named-holes` | ✓ | ✓ | ✓ | ✓ |
| <a id="nondum"></a>`nondum` | ✓ | ✓ | ✓ | ✓ |
| <a id="objectum"></a>`objectum` | ✓ | ✓ | ✓ | ✓ |
| <a id="prima"></a>`prima` | ✓ | ✓ | ✓ | ✓ |
| <a id="string"></a>`string` | ✓ | ✓ | ✓ | ✓ |
| <a id="block-string"></a>`block-string` | ✓ | ✓ | ✓ | ✓ |
| <a id="targets"></a>`targets` | ✓ | ✓ | ✓ | ✓ |
| <a id="ultima"></a>`ultima` | ✓ | ✓ | ✓ | ✓ |
| <a id="versio"></a>`versio` | ✓ | ✓ | ✓ | ✓ |
