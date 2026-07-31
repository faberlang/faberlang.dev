+++
title = "Tính tương thích của đích"
section = "targets"
order = 2
sources = "radix/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"

translation_kind = "translated"
prose_hash = "sha256:f781952d9c1cd489dbd4487770eecaae3ef1c56bb4986a397f1d6d378e74c0a3"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "54a1febec594f9bfc1e66c9bcf25604b52a66978"
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

**Được tạo**: unknown bởi `scripta/generate-ebnf-matrix.py` — **không chỉnh sửa**.
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
| rust | 277 | 279 | 99% |
| go | 258 | 279 | 92% |
| ts | 273 | 279 | 98% |
| faber | 279 | 279 | 100% |

**Tuyến hệ thống (MIR → tạo phẩm thiết bị/IR)**

| đích | có khả năng | có thể phân tích | % |
|---|---|---|---|
| llvm-text | 255 | 265 | 96% |
| wasm-text | 210 | 265 | 79% |
| wasm | 210 | 265 | 79% |
| metal-text | 6 | 265 | 2% |
| wgsl-text | 6 | 265 | 2% |
| sexp-struct | 211 | 265 | 80% |
| sexp | 211 | 265 | 80% |
| scena | 224 | 265 | 85% |

## Từ khóa — tuyến ứng dụng

### từ khóa

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `abstractus` | ✓ | ✓ | ✓ | ✓ |
| `ab` | ✓ | ✓ | ✓ | ✓ |
| `ad` | ✓ | ✓ | ✓ | ✓ |
| `adfirma` | ✓ | ✓ | ✓ | ✓ |
| `ante` | ✓ | ✓ | ✓ | ✓ |
| `atomic` | ✕ | ✓ | ✓ | ✓ |
| `argumenta` | ✓ | ✓ | ✓ | ✓ |
| `bivalens` | ✓ | ✓ | ✓ | ✓ |
| `cape` | ✓ | ✓ | ✓ | ✓ |
| `casu` | ✓ | ✓ | ✓ | ✓ |
| `cede` | ✓ | ✓ | ✓ | ✓ |
| `ceteri` | ✓ | ✓ | ✓ | ✓ |
| `ceterum` | ✓ | ✓ | ✓ | ✓ |
| `clausura` | ✓ | ✓ | ✓ | ✓ |
| `cli` | ✓ | ✓ | ✓ | ✓ |
| `copia` | ✓ | ✓ | ✓ | ✓ |
| `cura` | ✓ | ✓ | ✓ | ✓ |
| `curata` | ✓ | ✓ | ✓ | ✓ |
| `cursor` | ✓ | ✓ | ✓ | ✓ |
| `custodi` | ✓ | ✓ | ✓ | ✓ |
| `de` | ✓ | ✓ | ✓ | ✓ |
| `descriptio` | ✓ | ✓ | ✓ | ✓ |
| `discerne` | ✓ | ✓ | ✓ | ✓ |
| `discretio` | ✓ | ✓ | ✓ | ✓ |
| `dum` | ✓ | ✓ | ✓ | ✓ |
| `ego` | ✓ | ✓ | ✓ | ✓ |
| `elige` | ✓ | ✓ | ✓ | ✓ |
| `errata` | ✓ | ✓ | ✓ | ✓ |
| `est` | ✓ | ✓ | ✓ | ✓ |
| `ex` | ✓ | ✓ | ✓ | ✓ |
| `exitus` | ✓ | ✓ | ✓ | ✓ |
| `fac` | ✓ | ✓ | ✓ | ✓ |
| `falsum` | ✓ | ✓ | ✓ | ✓ |
| `fient` | ✓ | ✓ | ✓ | ✓ |
| `fiet` | ✓ | ✓ | ✓ | ✓ |
| `figendum` | ✓ | ✓ | ✓ | ✓ |
| `finge` | ✓ | ✓ | ✓ | ✓ |
| `fiunt` | ✓ | ✓ | ✓ | ✓ |
| `fixum` | ✓ | ✓ | ✓ | ✓ |
| `fragilis` | ✓ | ✓ | ✓ | ✓ |
| `fractus` | ✓ | ✓ | ✓ | ✓ |
| `functio` | ✓ | ✓ | ✓ | ✓ |
| `futura` | ✓ | ✓ | ✓ | ✓ |
| `futurum` | ✓ | ✓ | ✓ | ✓ |
| `generis` | ✓ | ✓ | ✓ | ✓ |
| `genus` | ✓ | ✓ | ✓ | ✓ |
| `iace` | ✓ | ✓ | ✓ | ✓ |
| `iacit` | ✓ | ✓ | ✓ | ✓ |
| `ignotum` | ✓ | ✓ | ✓ | ✓ |
| `immutata` | ✓ | ✓ | ✓ | ✓ |
| `implet` | ✓ | ✓ | ✓ | ✓ |
| `importa` | ✓ | ✓ | ✓ | ✓ |
| `in` | ✓ | ✓ | ✓ | ✓ |
| `incipiet` | ✓ | ✓ | ✓ | ✓ |
| `incipit` | ✓ | ✓ | ✓ | ✓ |
| `inter` | ✓ | ✓ | ✓ | ✓ |
| `intra` | ✓ | ✓ | ✓ | ✓ |
| `instans` | ✓ | ✓ | ✓ | ✓ |
| `itera` | ✓ | ✓ | ✓ | ✓ |
| `lege` | ✓ | ✓ | ✓ | ✓ |
| `lineam` | ✓ | ✓ | ✓ | ✓ |
| `lista` | ✓ | ✓ | ✓ | ✓ |
| `matrix` | ✓ | ✕ | ✓ | ✓ |
| `mone` | ✓ | ✓ | ✓ | ✓ |
| `mori` | ✓ | ✓ | ✓ | ✓ |
| `nexum` | ✓ | ✓ | ✓ | ✓ |
| `nihil` | ✓ | ✓ | ✓ | ✓ |
| `numquam` | ✓ | ✓ | ✓ | ✓ |
| `numerus` | ✓ | ✓ | ✓ | ✓ |
| `non` | ✓ | ✓ | ✓ | ✓ |
| `omitte` | ✓ | ✓ | ✓ | ✓ |
| `omnia` | ✓ | ✓ | ✓ | ✓ |
| `operandus` | ✓ | ✓ | ✓ | ✓ |
| `optio` | ✓ | ✓ | ✓ | ✓ |
| `optiones` | ✓ | ✓ | ✓ | ✓ |
| `ordo` | ✓ | ✓ | ✓ | ✓ |
| `octeti` | ✓ | ✓ | ✓ | ✓ |
| `implendum` | ✓ | ✓ | ✓ | ✓ |
| `per` | ✓ | ✓ | ✓ | ✓ |
| `perge` | ✓ | ✓ | ✓ | ✓ |
| `postpara` | ✓ | ✓ | ✓ | ✓ |
| `postparabit` | ✓ | ✓ | ✓ | ✓ |
| `prae` | ✓ | ✓ | ✓ | ✓ |
| `praefixum` | — | — | — | — |
| `praepara` | ✓ | ✓ | ✓ | ✓ |
| `praeparabit` | ✓ | ✓ | ✓ | ✓ |
| `promissum` | ✓ | ✓ | ✓ | ✓ |
| `privata` | ✓ | ✓ | ✓ | ✓ |
| `proba` | ✓ | ✓ | ✓ | ✓ |
| `probandum` | ✓ | ✓ | ✓ | ✓ |
| `protecta` | — | — | — | — |
| `publica` | ✓ | ✓ | ✓ | ✓ |
| `redde` | ✓ | ✓ | ✓ | ✓ |
| `reddet` | ✓ | ✓ | ✓ | ✓ |
| `repete` | ✓ | ✓ | ✓ | ✓ |
| `rumpe` | ✓ | ✓ | ✓ | ✓ |
| `scribe` | ✓ | ✓ | ✓ | ✓ |
| `scriptum` | ✓ | ✓ | ✓ | ✓ |
| `secus` | ✓ | ✓ | ✓ | ✓ |
| `si` | ✓ | ✓ | ✓ | ✓ |
| `sic` | ✓ | ✓ | ✓ | ✓ |
| `sin` | ✓ | ✓ | ✓ | ✓ |
| `sit` | ✓ | ✓ | ✓ | ✓ |
| `solum_in` | ✓ | ✓ | ✓ | ✓ |
| `solum` | ✓ | ✓ | ✓ | ✓ |
| `sparge` | ✓ | ✓ | ✓ | ✓ |
| `sponte` | ✓ | ✓ | ✓ | ✓ |
| `sub` | ✓ | ✓ | ✓ | ✓ |
| `tacet` | ✓ | ✓ | ✓ | ✓ |
| `tacebit` | ✓ | ✓ | ✓ | ✓ |
| `tabula` | ✓ | ✓ | ✓ | ✓ |
| `tag` | ✓ | ✓ | ✓ | ✓ |
| `temporis` | ✓ | ✓ | ✓ | ✓ |
| `tensor` | ✓ | ✕ | ✓ | ✓ |
| `textus` | ✓ | ✓ | ✓ | ✓ |
| `typus` | ✓ | ✓ | ✓ | ✓ |
| `ubique` | ✓ | ✓ | ✓ | ✓ |
| `usque` | ✓ | ✓ | ✓ | ✓ |
| `ut` | ✓ | ✓ | ✓ | ✓ |
| `varia` | ✓ | ✓ | ✓ | ✓ |
| `variandum` | ✓ | ✓ | ✓ | ✓ |
| `vector` | ✓ | ✓ | ✓ | ✓ |
| `vacuum` | ✓ | ✓ | ✓ | ✓ |
| `verum` | ✓ | ✓ | ✓ | ✓ |
| `vide` | ✓ | ✓ | ✓ | ✓ |

## Toán tử — tuyến ứng dụng

### nhóm toán tử

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `⊜` | ✓ | ✓ | ✓ | ✓ |
| `∧` | ✓ | ✓ | ✓ | ✓ |
| `→` | ✓ | ✓ | ✓ | ✓ |
| `⇥` | ✓ | ✓ | ✓ | ✓ |
| `←` | ✓ | ✓ | ✓ | ✓ |
| `aut` | ✓ | ✓ | ✓ | ✓ |
| `![` | ✓ | ✓ | ✓ | ✓ |
| `!.` | ✓ | ✓ | ✓ | ✓ |
| `≠` | ✓ | ✓ | ✓ | ✓ |
| `!(` | ✓ | ✓ | ✓ | ✓ |
| `⊻` | ✓ | ✓ | ✓ | ✓ |
| `↦` | ✓ | ◐ | ✓ | ✓ |
| `⇒` | ✓ | ✓ | ✓ | ✓ |
| `‥` | ✓ | ✓ | ✓ | ✓ |
| `…` | ✓ | ✓ | ✓ | ✓ |
| `≡` | ✓ | ✓ | ✓ | ✓ |
| `=` | ✓ | ✓ | ✓ | ✓ |
| `et` | ✓ | ✓ | ✓ | ✓ |
| `≥` | ✓ | ✓ | ✓ | ✓ |
| `≤` | ✓ | ✓ | ✓ | ✓ |
| `⊖` | ✓ | ✓ | ✓ | ✓ |
| `modulus<u16>` | ✓ | ✕ | ✕ | ✓ |
| `modulus<u32>` | ✓ | ✕ | ✕ | ✓ |
| `modulus<u64>` | ✓ | ✕ | ✕ | ✓ |
| `modulus<u8>` | ✓ | ✕ | ✕ | ✓ |
| `non est` | ✓ | ✓ | ✓ | ✓ |
| `⊚` | ✓ | ✓ | ✓ | ✓ |
| `∨` | ✓ | ✓ | ✓ | ✓ |
| `∪` | ✓ | ✓ | ✓ | ✓ |
| `⊕` | ✓ | ✓ | ✓ | ✓ |
| `?[` | ✓ | ✓ | ✓ | ✓ |
| `?.` | ✓ | ✓ | ✓ | ✓ |
| `?(` | ✓ | ✓ | ✓ | ✓ |
| `§` | ✓ | ✓ | ✓ | ✓ |
| `⇐` | ✓ | ✓ | ✓ | ✓ |
| `⊘` | ✓ | ✓ | ✓ | ✓ |
| `⊛` | ✓ | ✓ | ✓ | ✓ |
| `¬` | ✓ | ✓ | ✓ | ✓ |
| `vel` | ✓ | ✓ | ✓ | ✓ |
| `∷` | ✓ | ✓ | ✓ | ✓ |
| `∴` | ✓ | ✓ | ✓ | ✓ |
| `ergo` | ✓ | ✓ | ✓ | ✓ |

## Từ khóa — tuyến hệ thống

### từ khóa

| term | llvm-text | wasm-text | wasm | metal-text | wgsl-text | sexp-struct | sexp | scena |
|---|---|---|---|---|---|---|---|---|
| `abstractus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ab` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ad` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `adfirma` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ante` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `atomic` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `argumenta` | — | — | — | — | — | — | — | — |
| `bivalens` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `cape` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `casu` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `cede` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `ceteri` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ceterum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `clausura` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `cli` | — | — | — | — | — | — | — | — |
| `copia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `cura` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `curata` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `cursor` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `custodi` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `de` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `descriptio` | — | — | — | — | — | — | — | — |
| `discerne` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `discretio` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `dum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ego` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `elige` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `errata` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `est` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `ex` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `exitus` | — | — | — | — | — | — | — | — |
| `fac` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `falsum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fient` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fiet` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `figendum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `finge` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fiunt` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fixum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fragilis` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `fractus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `functio` | ✓ | ◐ | ◐ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `futura` | ◐ | ◐ | ◐ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `futurum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `generis` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `genus` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `iace` | ✓ | ◐ | ◐ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `iacit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ignotum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `immutata` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `implet` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `importa` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ◐ |
| `in` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `incipiet` | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `incipit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `inter` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `intra` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `instans` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `itera` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `lege` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `lineam` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `lista` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `matrix` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `mone` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `mori` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `nexum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `nihil` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `numquam` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `numerus` | ✓ | ◐ | ◐ | ✕ | ✕ | ◐ | ◐ | ◐ |
| `non` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `omitte` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `omnia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `operandus` | — | — | — | — | — | — | — | — |
| `optio` | — | — | — | — | — | — | — | — |
| `optiones` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `ordo` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `octeti` | ✓ | ◐ | ◐ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `implendum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `per` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `perge` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `postpara` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `postparabit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `prae` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `praefixum` | — | — | — | — | — | — | — | — |
| `praepara` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `praeparabit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `promissum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `privata` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `proba` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `probandum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `protecta` | — | — | — | — | — | — | — | — |
| `publica` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `redde` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ◐ |
| `reddet` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `repete` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `rumpe` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `scribe` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `scriptum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `secus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `si` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `sic` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `sin` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `sit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `solum_in` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `solum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `sparge` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `sponte` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `sub` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `tacet` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `tacebit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `tabula` | ✓ | ◐ | ◐ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `tag` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `temporis` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `tensor` | ✓ | ✕ | ✕ | ✕ | ✕ | ◐ | ◐ | ◐ |
| `textus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `typus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ubique` | — | — | — | — | — | — | — | — |
| `usque` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ut` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `varia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `variandum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `vector` | ✓ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ✕ |
| `vacuum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `verum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `vide` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |

## Toán tử — tuyến hệ thống

### nhóm toán tử

| term | llvm-text | wasm-text | wasm | metal-text | wgsl-text | sexp-struct | sexp | scena |
|---|---|---|---|---|---|---|---|---|
| `⊜` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `∧` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `→` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⇥` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `←` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `aut` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `![` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `!.` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `≠` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `!(` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊻` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `↦` | ✓ | ◐ | ◐ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `⇒` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `‥` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `…` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `≡` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `=` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `et` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `≥` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `≤` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊖` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `modulus<u16>` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `modulus<u32>` | ◐ | ✕ | ✕ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `modulus<u64>` | ✕ | ✕ | ✕ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `modulus<u8>` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `non est` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊚` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `∨` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `∪` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊕` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `?[` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `?.` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `?(` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `§` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⇐` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊘` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `⊛` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `¬` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `vel` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `∷` | ✓ | ✕ | ✕ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `∴` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ergo` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |

## Các term khác (`existing-home` / không chỉ định)

### existing-home

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `alias` | ✓ | ✓ | ✓ | ✓ |
| `arena` | ✓ | ✓ | ✓ | ✓ |
| `@` | ✓ | ✓ | ✓ | ✓ |
| `f16` | ✕ | ✓ | ✓ | ✓ |
| `imperia` | ✓ | ✓ | ✓ | ✓ |
| `imperium` | ✓ | ✓ | ✓ | ✓ |
| `manifest` | ✓ | ✓ | ✓ | ✓ |
| `metior` | ✓ | ✓ | ✓ | ✓ |
| `nondum` | ✓ | ✓ | ✓ | ✓ |
| `objectum` | ✓ | ✓ | ✓ | ✓ |
| `prima` | ✓ | ✓ | ✓ | ✓ |
| `requirit` | ✓ | ✓ | ✓ | ✓ |
| `string` | ✓ | ✓ | ✓ | ✓ |
| `block-string` | ✓ | ✓ | ✓ | ✓ |
| `summa` | ✓ | ✓ | ✓ | ✓ |
| `targets` | ✓ | ✓ | ✓ | ✓ |
| `ultima` | ✓ | ✓ | ✓ | ✓ |
| `versio` | ✓ | ✓ | ✓ | ✓ |
