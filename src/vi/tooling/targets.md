+++
title = "Tính tương thích của đích"
section = "targets"
order = 2
sources = "radix/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"

translation_kind = "translated"
prose_hash = "sha256:d0cdd215aab566f8216011a69109a1d5adbf4432b5060544703493bff8bb6acc"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "331061d5d641a6172960d263d2656f9ca154b91f"
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

**Được tạo**: 2026-07-19 bởi `scripta/generate-ebnf-matrix.py` — **không chỉnh sửa**.
**Đo lường**: `emit_hir_target_matrix` + `emit_mir_target_matrix` (trong tiến trình, không dùng toolchain bên ngoài).
**Kết nối**: các term trong `examples/corpus/index.toml` → exempla.

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
| rust | 265 | 268 | 99% |
| go | 247 | 268 | 92% |
| ts | 262 | 268 | 98% |
| faber | 268 | 268 | 100% |

**Tuyến hệ thống (MIR → tạo phẩm thiết bị/IR)**

| đích | có khả năng | có thể phân tích | % |
|---|---|---|---|
| llvm-text | 247 | 255 | 97% |
| wasm-text | 203 | 255 | 80% |
| wasm | 202 | 255 | 79% |
| metal-text | 6 | 254 | 2% |
| wgsl-text | 6 | 254 | 2% |
| sexp-struct | 196 | 254 | 77% |
| sexp | 195 | 254 | 77% |
| scena | 216 | 254 | 85% |

## Từ khóa — tuyến ứng dụng

### từ khóa

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `abstractus` | ✓ | ✓ | ✓ | ✓ |
| `ab` | ✓ | ✓ | ✓ | ✓ |
| `ad` | ✓ | ✓ | ✓ | ✓ |
| `adfirma` | ✓ | ✓ | ✓ | ✓ |
| `ante` | ✓ | ✓ | ✓ | ✓ |
| `argumenta` | ✓ | ✓ | ✓ | ✓ |
| `cape` | ✓ | ✓ | ✓ | ✓ |
| `casu` | ✓ | ✓ | ✓ | ✓ |
| `cede` | ✓ | ✓ | ✓ | ✓ |
| `ceteri` | ✓ | ✓ | ✓ | ✓ |
| `ceterum` | ✓ | ✓ | ✓ | ✓ |
| `clausura` | ✓ | ✓ | ✓ | ✓ |
| `cli` | ✓ | ✓ | ✓ | ✓ |
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
| `finge` | ✓ | ✓ | ✓ | ✓ |
| `fixum` | ✓ | ✓ | ✓ | ✓ |
| `fragilis` | ✓ | ✓ | ✓ | ✓ |
| `functio` | ✓ | ✓ | ✓ | ✓ |
| `futura` | ✓ | ✓ | ✓ | ✓ |
| `futurum` | ✓ | ✓ | ✓ | ✓ |
| `generis` | ✓ | ✓ | ✓ | ✓ |
| `genus` | ✓ | ✓ | ✓ | ✓ |
| `iace` | ✓ | ✓ | ✓ | ✓ |
| `immutata` | ✓ | ✓ | ✓ | ✓ |
| `implet` | ✓ | ✓ | ✓ | ✓ |
| `importa` | ✓ | ✓ | ✓ | ✓ |
| `in` | ✓ | ✓ | ✓ | ✓ |
| `incipiet` | ✓ | ✓ | ✓ | ✓ |
| `incipit` | ✓ | ✓ | ✓ | ✓ |
| `inter` | ✓ | ✓ | ✓ | ✓ |
| `intra` | ✓ | ✓ | ✓ | ✓ |
| `itera` | ✓ | ✓ | ✓ | ✓ |
| `lege` | ✓ | ✓ | ✓ | ✓ |
| `lineam` | ✓ | ✓ | ✓ | ✓ |
| `mone` | ✓ | ✓ | ✓ | ✓ |
| `mori` | ✓ | ✓ | ✓ | ✓ |
| `nexum` | ✓ | ✓ | ✓ | ✓ |
| `nihil` | ✓ | ✓ | ✓ | ✓ |
| `numquam` | ✓ | ✓ | ✓ | ✓ |
| `non` | ✓ | ✓ | ✓ | ✓ |
| `omitte` | ✓ | ✓ | ✓ | ✓ |
| `omnia` | ✓ | ✓ | ✓ | ✓ |
| `operandus` | ✓ | ✓ | ✓ | ✓ |
| `optio` | ✓ | ✓ | ✓ | ✓ |
| `optiones` | ✓ | ✓ | ✓ | ✓ |
| `ordo` | ✓ | ✓ | ✓ | ✓ |
| `implendum` | ✓ | ✓ | ✓ | ✓ |
| `per` | ✓ | ✓ | ✓ | ✓ |
| `perge` | ✓ | ✓ | ✓ | ✓ |
| `postpara` | ✓ | ✓ | ✓ | ✓ |
| `postparabit` | ✓ | ✓ | ✓ | ✓ |
| `prae` | ✓ | ✓ | ✓ | ✓ |
| `praefixum` | ✓ | ✓ | ✓ | ✓ |
| `praepara` | ✓ | ✓ | ✓ | ✓ |
| `praeparabit` | ✓ | ✓ | ✓ | ✓ |
| `privata` | ✓ | ✓ | ✓ | ✓ |
| `proba` | ✓ | ✓ | ✓ | ✓ |
| `probandum` | ✓ | ✓ | ✓ | ✓ |
| `protecta` | — | — | — | — |
| `publica` | ✓ | ✓ | ✓ | ✓ |
| `redde` | ✓ | ✓ | ✓ | ✓ |
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
| `tag` | ✓ | ✓ | ✓ | ✓ |
| `temporis` | ✓ | ✓ | ✓ | ✓ |
| `typus` | ✓ | ✓ | ✓ | ✓ |
| `ubique` | ✓ | ✓ | ✓ | ✓ |
| `usque` | ✓ | ✓ | ✓ | ✓ |
| `ut` | ✓ | ✓ | ✓ | ✓ |
| `varia` | ✓ | ✓ | ✓ | ✓ |
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

## Từ khóa — tuyến hệ thống

### từ khóa

| term | llvm-text | wasm-text | wasm | metal-text | wgsl-text | sexp-struct | sexp | scena |
|---|---|---|---|---|---|---|---|---|
| `abstractus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ab` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ad` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `adfirma` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ante` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `argumenta` | — | — | — | — | — | — | — | — |
| `cape` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `casu` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `cede` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `ceteri` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ceterum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `clausura` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `cli` | — | — | — | — | — | — | — | — |
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
| `finge` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fixum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `fragilis` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `functio` | ✓ | ◐ | ◐ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `futura` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `futurum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `generis` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `genus` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `iace` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `immutata` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `implet` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `importa` | ✓ | ✓ | ✓ | ✕ | ✕ | ◐ | ◐ | ◐ |
| `in` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `incipiet` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `incipit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `inter` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `intra` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `itera` | ✓ | ✓ | ◐ | ✕ | ✕ | ◐ | ◐ | ✓ |
| `lege` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `lineam` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `mone` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `mori` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `nexum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `nihil` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `numquam` | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| `non` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `omitte` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `omnia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `operandus` | — | — | — | — | — | — | — | — |
| `optio` | — | — | — | — | — | — | — | — |
| `optiones` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `ordo` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `implendum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `per` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `perge` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `postpara` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `postparabit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `prae` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `praefixum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `praepara` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `praeparabit` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `privata` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `proba` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `probandum` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `protecta` | — | — | — | — | — | — | — | — |
| `publica` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `redde` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
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
| `tag` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `temporis` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✕ |
| `typus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ubique` | — | — | — | — | — | — | — | — |
| `usque` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `ut` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| `varia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
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
| `modulus<u32>` | ◐ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
| `modulus<u64>` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ |
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

## Các term khác (`existing-home` / không chỉ định)

### existing-home

| term | rust | go | ts | faber |
|---|---|---|---|---|
| `alias` | ✓ | ✓ | ✓ | ✓ |
| `atomic` | ✕ | ✓ | ✓ | ✓ |
| `arena` | ✓ | ✓ | ✓ | ✓ |
| `@` | ✓ | ✓ | ✓ | ✓ |
| `bivalens` | ✓ | ✓ | ✓ | ✓ |
| `copia` | ✓ | ✓ | ✓ | ✓ |
| `f16` | ✕ | ✓ | ✓ | ✓ |
| `fractus` | ✓ | ✓ | ✓ | ✓ |
| `iacit` | ✓ | ✓ | ✓ | ✓ |
| `ignotum` | ✓ | ✓ | ✓ | ✓ |
| `imperia` | ✓ | ✓ | ✓ | ✓ |
| `imperium` | ✓ | ✓ | ✓ | ✓ |
| `instans` | ✓ | ✓ | ✓ | ✓ |
| `lista` | ✓ | ✓ | ✓ | ✓ |
| `manifest` | ✓ | ✓ | ✓ | ✓ |
| `matrix` | ✕ | ✕ | ✓ | ✓ |
| `metior` | ✓ | ✓ | ✓ | ✓ |
| `nondum` | ✓ | ✓ | ✓ | ✓ |
| `numerus` | ✓ | ✓ | ✓ | ✓ |
| `objectum` | ✓ | ✓ | ✓ | ✓ |
| `octeti` | ✓ | ✓ | ✓ | ✓ |
| `prima` | ✓ | ✓ | ✓ | ✓ |
| `promissum` | ✓ | ✓ | ✓ | ✓ |
| `requirit` | ✓ | ✓ | ✓ | ✓ |
| `string` | ✓ | ✓ | ✓ | ✓ |
| `block-string` | ✓ | ✓ | ✓ | ✓ |
| `sed` | ✓ | ✓ | ✓ | ✓ |
| `summa` | ✓ | ✓ | ✓ | ✓ |
| `tabula` | ✓ | ✓ | ✓ | ✓ |
| `tensor` | ✓ | ✕ | ✓ | ✓ |
| `targets` | ✓ | ✓ | ✓ | ✓ |
| `textus` | ✓ | ✓ | ✓ | ✓ |
| `ultima` | ✓ | ✓ | ✓ | ✓ |
| `versio` | ✓ | ✓ | ✓ | ✓ |
| `vector` | ✓ | ✓ | ✓ | ✓ |
