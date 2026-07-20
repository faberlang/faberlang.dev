+++
translation_kind = "translated"

title = "Compilation lanes"
section = "features"
order = 2
sources = []


prose_hash = "sha256:24bf11962b4a33f41f7c1f5746e0022669763b2d5d7c4982302e6337dc877817"
code_hash = "sha256:c3c0a1262dc6618a5d0012cd094f1b9482ac31149830c36bb11762a3690ac665"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
Faber có một frontend dùng chung duy nhất — phân tích từ vựng, phân tích cú pháp, kiểm tra kiểu — sau đó rẽ thành nhiều tuyến hạ thấp tùy theo nhu cầu của target. Các biểu diễn trung gian tạo thành một pipeline: mã nguồn được phân tích thành HIR, có thể được hạ thấp tùy chọn xuống MIR, và có thể đi qua AIR trước khi phát sinh mã cuối cùng. Mỗi IR phục vụ một mục đích riêng, và mỗi target sử dụng IR phù hợp với nhu cầu của nó.

## Tổng quan pipeline {#overview}

```text
Source (.fab)  →  Lex  →  Parse  →  Collect  →  Resolve  →  Lower  →  Typecheck  →  Analysis
                                                              │
                                                    HIR (semantic core)
                                                    ┌─────┴─────┐
                                                    │           │
                                              Reader locale    MIR lowering
                                              (input/output)    │
                                                                │
                                                      ┌─────────┴─────────┐
                                                      │                   │
                                                CPU lanes           GPU lanes
                                                      │                   │
                                            ┌────┬────┼────┬────┐     ┌───┴───┐
                                            │    │    │    │    │     │       │
                                          FMIR LLVM WASM  TS  Go   WGSL   Metal
                                                                          (hold)
```

Frontend dùng chung phục vụ mọi target. Sau khi phân tích ngữ nghĩa tạo ra HIR, trình biên dịch chọn tuyến dựa trên target:

- **HIR-direct** — phát sinh trực tiếp từ HIR đã kiểm tra kiểu cho các backend có hình dạng ngôn ngữ (Rust, Faber, TypeScript, Go)
- **HIR → MIR** — hạ thấp xuống MIR có hình dạng thực thi, sau đó phát sinh mã cho các target hệ thống và target cấp thấp
- **HIR → MIR → AIR → MIR** — đi vòng qua AIR hàm thuần cho các phép biến đổi tự động vi phân và hợp nhất, sau đó quay lại MIR

## HIR — Biểu diễn trung gian cấp cao {#hir}

HIR là nguồn sự thật. Đây là một IR có kiểu và có hình dạng ngôn ngữ, bảo toàn các khai báo, thông tin kiểu và các quan hệ cấu trúc. Mọi chương trình Faber, bất kể locale nguồn ban đầu hay đích target, đều đi qua biểu diễn này.

### Tích hợp reader locale {#reader-locale-integration}

Reader locale hoạt động thông qua HIR. Một tệp nguồn Faber được viết bằng các từ khóa tiếng Thái sẽ được phân tích cú pháp và hạ thấp thành cùng một HIR như mã nguồn tương đương bằng Latin. Locale là cách hiển thị bề mặt của HIR, không phải một nhánh riêng trong lõi ngữ nghĩa.

- **Đầu vào:** mã nguồn bản địa hóa (tiếng Thái, tiếng Trung, tiếng Ả Rập, v.v.) → HIR đã chuẩn hóa — **đã phát hành**
- **Đầu ra:** HIR → phát sinh lại mã nguồn bản địa hóa — **đang triển khai** (đang được thực hiện)

Khi hướng đầu ra được phát hành, `faber format --reader-locale=th-TH` sẽ chuyển đổi vòng mọi mã nguồn Faber qua HIR và phát sinh mã với các từ khóa tiếng Thái, hoàn tất tính đối xứng: cùng một HIR có thể tạo ra bề mặt của bất kỳ locale nào, cũng như có thể tạo ra bất kỳ backend target nào.

### Backend HIR-direct {#hir-direct-backends}

Các target này phát sinh mã trực tiếp từ HIR đã kiểm tra kiểu mà không hạ thấp xuống MIR. Chúng giữ cấu trúc cấp nguồn lâu hơn và phù hợp với đầu ra có hình dạng ngôn ngữ:

| Target | Trạng thái | Vai trò |
|---|---|---|
| `Rust` | **Chính** | Tuyến sản xuất. Đóng gói, build, chạy, kiểm thử. Cargo + rustc cho các binary native. |
| `Faber` | **Hỗ trợ** | Khung nhìn mã nguồn chuẩn qua trình định dạng `forma`. Tính ổn định khi chuyển đổi vòng. |
| `TypeScript` | Thăm dò | Chỉ phát sinh tệp. Chứng minh ngữ nghĩa trên các dạng target khác nhau. |
| `Go` | Loại bỏ | Chỉ phát sinh tệp. Các chế độ mượn bị loại bỏ; `ad` bị từ chối. |

## MIR — Biểu diễn trung gian cấp giữa {#mir}

MIR là IR có hình dạng thực thi. Nó biểu diễn luồng điều khiển, biến cục bộ, lời gọi runtime, các vị trí, nhánh và các cạnh lỗi — những thông tin mà các target cấp thấp cần. Trong khi HIR bảo toàn cấu trúc mã nguồn, MIR làm phẳng cấu trúc đó thành một đồ thị luồng điều khiển.

Việc hạ thấp HIR → MIR chuyển các cấu trúc có hình dạng ngôn ngữ thành các bước thực thi. MIR được kiểm tra sau khi hạ thấp để phát hiện các vấn đề cấu trúc trước khi bất kỳ backend nào cố gắng phát sinh mã.

> **Quyền sở hữu ngữ nghĩa.** Faber duy trì ranh giới rõ ràng giữa các quy tắc được thực thi trong HIR/MIR (kiểm tra kiểu, gán xác định, lint chế độ mượn) và các quy tắc được giao cho toolchain target (phân tích vòng đời Rust, an toàn kiểu Go). Điều này ngăn trình biên dịch thực hiện trùng lặp công việc mà các trình biên dịch target đã xử lý đúng.

## Tuyến vòng qua AIR {#air}

AIR (Autograd / AI Representation) là một tuyến biến đổi hàm thuần đi vòng khỏi đường HIR → MIR. Tuyến này được kích hoạt bằng chú thích tường minh trên từng hàm:

```faber
@ radix lane "air"
functio loss(numerus predicted, numerus expected) → numerus {
    fixum numerus delta ← predicted - expected
    redde delta * delta
}
```

Các hàm trên tuyến AIR phải đáp ứng chính sách thuần — không biến đổi, không hiệu ứng, không vòng lặp. Các hàm vi phạm chính sách này sẽ bị từ chối với một chẩn đoán trước khi bắt đầu hạ thấp AIR. Phần còn lại của chương trình tiếp tục sử dụng Faber thông thường với biến đổi, hiệu ứng và vòng lặp.

Sau khi phép biến đổi AIR hoàn tất công việc (tương lai: tự động vi phân, hợp nhất), kết quả được hạ thấp lại xuống MIR và gia nhập lại pipeline backend MIR thông thường. AIR không sở hữu backend nào và không có bộ kiểm tra kiểu độc lập — đây là một điểm kiểm tra biến đổi, không phải một IR song song.

```text
HIR  →  AIR purity check  →  HIR to AIR lowering  →  AIR validation  →  AIR to MIR re-lowering  →  MIR backend
```

Kiến trúc này phản ánh cách tiếp cận của JAX: duy trì một biểu diễn hàm thuần cho các phép biến đổi, chỉ hạ thấp xuống IR mệnh lệnh ở bước cuối. AIR tồn tại vì chạy tự động vi phân trên MIR mệnh lệnh sẽ đòi hỏi khôi phục tính thuần từ mã đã được hạ thấp thành các phép biến đổi.

## Các tuyến target CPU {#cpu}

Các target CPU tiếp nhận MIR và tạo ra artifact thực thi hoặc văn bản cho các toolchain bên ngoài. Faber phát sinh văn bản khi có thể và dựa vào các toolchain cấp thấp hơn cho bước biên dịch cuối — tương tự cách trình biên dịch C phát sinh mã assembly cho trình hợp dịch và trình liên kết.

### FMIR — runtime MIR riêng của Faber {#fmir}

FMIR là bộ thực thi package bản địa MIR. Trình biên dịch trích xuất MIR thành một payload nhị phân và bọc payload đó bằng một trình nạp kernel Rust ngắn. Kết quả là một executable tự chứa, chạy MIR thông qua stepper trong tiến trình của Faber — không cần cài đặt runtime riêng.

| Định dạng | Mô tả |
|---|---|
| `fmir-text` | Ảnh văn bản FMIR có thể kiểm tra tại `target/faber-mir/image.fmir.txt` |
| `fmir` | Ảnh FMIR nhị phân nhỏ gọn tại `target/faber-mir/image.fmir` |
| `fmir-bin` | Runner tự chứa tại `target/faber-mir/exe/run` — nhúng các byte FMIR |

### Văn bản LLVM {#llvm}

Faber phát sinh LLVM IR dưới dạng văn bản (`.ll`), không phải LLVM codegen tích hợp. IR được phát sinh dành cho các bước toolchain bên ngoài — việc kiểm tra, tối ưu hóa và phát sinh mã native do các công cụ LLVM phía sau xử lý. Đây là target trung gian và kiểm tra, không phải một tuyến phát sinh mã native được nhúng trong trình biên dịch.

### WASM {#wasm}

Faber phát sinh WebAssembly ở cả định dạng văn bản (`.wat`) và nhị phân (`.wasm`). Wasm được phát sinh sử dụng các import host bên ngoài (các ký hiệu runtime `faber_*`) và được kiểm tra thông qua `wasm-tools validate`. Wasm là target được hỗ trợ có giới hạn — nó chứng minh pipeline hạ thấp MIR cho một định dạng tiêu chuẩn mở, nhưng không phải runtime phân phối package.

| Định dạng | Target CLI | Đầu ra |
|---|---|---|
| `wasm-text` | `-t wasm-text` (bí danh `wat`) | Định dạng văn bản WAT |
| `wasm` | `-t wasm` | Module Wasm nhị phân |

### TypeScript và Go (HIR-direct) {#typescript-go}

Mặc dù thường được dùng để phát sinh tệp cấp ứng dụng, TypeScript và Go cũng đóng vai trò là các target chứng minh: chúng xác thực rằng ngữ nghĩa của Faber có thể chuyển sang các hệ thống kiểu được sử dụng rộng rãi, ngay cả khi việc biên dịch package và thực thi runtime hiện vẫn chỉ dành cho Rust.

## Các tuyến target GPU {#gpu}

### WGSL (qua WGPU) {#wgsl}

Faber phát sinh mã nguồn compute shader WGSL thông qua pipeline MIR. WGSL được phát sinh được kiểm tra qua `naga` (30.x) và bao gồm sidecar reflection cho metadata bind-group. Tuyến này bao phủ tập kernel an toàn trên thiết bị: hỗ trợ các device view `f32` rank-1; view rank-2 bị từ chối. WGSL không phải runtime khởi chạy GPU — Faber phát sinh mã nguồn shader, nhưng việc thực thi cần một runtime WebGPU bên ngoài.

### Metal (tạm dừng) {#metal}

Việc phát sinh văn bản compute shader Metal đã được thiết kế và triển khai một phần, nhưng hiện đang tạm dừng. Kiến trúc này tuân theo cùng mô hình như WGSL: Faber phát sinh mã nguồn Metal Shading Language cho tập kernel an toàn trên thiết bị, còn toolchain bên ngoài xử lý việc biên dịch và thực thi. Công việc dự kiến sẽ tiếp tục.

## Ghi chú kiến trúc {#comparison}

Kiến trúc biên dịch của Faber tương tự về tinh thần với cách trình biên dịch Rust hoạt động. Rust hạ thấp qua HIR → MIR → LLVM IR và nhúng trực tiếp toolchain LLVM cho việc phát sinh mã native cuối cùng. Faber áp dụng cách tiếp cận mềm dẻo hơn: phát sinh văn bản cho các toolchain bên ngoài (văn bản LLVM, WGSL, Metal, WAT) thay vì nhúng chúng, đồng thời dành việc phát sinh mã trực tiếp cho runtime riêng của mình (FMIR) và target package chính (Rust, nơi Cargo và rustc xử lý pipeline phía sau).

Cách tiếp cận phát sinh văn bản có nghĩa là Faber không bao giờ cần đóng gói LLVM, runtime Wasm hoặc driver GPU — đó vẫn là các dependency bên ngoài do người dùng lựa chọn. Đổi lại, Faber không thể cung cấp quy trình build bằng một lệnh duy nhất cho mọi target; người dùng phải cài đặt toolchain phù hợp cho backend đã chọn.

## Tổng quan target {#matrix}

| Target | IR | Họ | Build | Chạy | Đóng gói |
|---|---|---|---|---|---|
| `Rust` | HIR | CPU | có | có | có |
| `fmir` / `fmir-bin` | MIR | CPU | có | có | có |
| `Faber` (format) | HIR | — | không | không | không |
| `TypeScript` | HIR | CPU | không | không | không |
| `Go` | HIR | CPU | không | không | không |
| `LLVM text` | MIR | CPU | không | không | không |
| `WASM` / `WAT` | MIR | CPU | không | không | không |
| `WGSL` | MIR | GPU | không | không | không |
| `Metal` (tạm dừng) | MIR | GPU | không | không | không |

*`build`, `run` và `package` mô tả các quy trình Faber. Các toolchain bên ngoài (rustc, wasm-tools, naga) xử lý việc biên dịch cuối cùng cho các target phát sinh văn bản.*
