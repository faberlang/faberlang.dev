+++
translation_kind = "translated"

title = "Codegen targets"
section = "tooling"
order = 1
sources = [
  "radix/docs/design/target-capability-matrix.md (40 KB)",
  "radix/README.md (Codegen Targets and HIR/MIR Split)",
  "faber targets CLI output",
]


prose_hash = "sha256:ceba78ab8cc04dea45e96377964059873b7b20582f3f069e74cdde8c65e72841"
code_hash = "sha256:efae27bbf8b10e74385b4ced2bb6b500d0ffc2dea16d0c43ef64b138ba88fc4f"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Faber có một ngôn ngữ và nhiều hợp đồng biên dịch. Không phải mọi tính năng đều phải hạ xuống mọi đích. Trang này ghi lại những tính năng mà mỗi đích hỗ trợ, loại bỏ, cảnh báo hoặc từ chối.

## Động từ chính sách {#policy-verbs}

| Động từ | Ý nghĩa |
|------|---------|
| **Hỗ trợ** | Hạ mã với ngữ nghĩa dự kiến |
| **Loại bỏ** | Kiểm tra kiểu thành công; quá trình sinh mã loại bỏ ngữ nghĩa riêng của đích |
| **Cảnh báo** | Faber hợp lệ; không có hiệu lực hoặc hành vi bị suy giảm trên đích |
| **Từ chối** | Quá trình kiểm tra hoặc phát sinh lỗi với chẩn đoán rõ ràng |
| **Trì hoãn** | Phân tích cú pháp/liên kết thành công; chưa triển khai hạ mã cho bất kỳ đích nào |
| **Giới hạn** | Hợp đồng ổn định với các cổng tập con rõ ràng |

## Bảng đích {#target-table}

| Đích | Tuyến | Biên dịch | Chạy | Đóng gói | Chính sách |
|--------|------|-------|-----|---------|--------|
| `rust` | HIR | có | có | có | **Hỗ trợ** |
| `fmir-text` | MIR | có | có | có | **Hỗ trợ** |
| `fmir` | MIR | có | có | có | **Hỗ trợ** |
| `fmir-bin` | MIR | có | có | có | **Hỗ trợ** |
| `faber` | HIR | có | không | không | **Hỗ trợ** |
| `ts` | HIR | có | không | không | **Thăm dò** |
| `go` | HIR | có | không | không | **Loại bỏ** |
| `wasm` | MIR | có | không | không | **Giới hạn** |
| `wasm-text` | MIR | có | không | không | **Giới hạn** |
| `llvm-text` | MIR | có | không | không | **Giới hạn** |
| `metal-text` | MIR | có | không | không | **Giới hạn** |
| `wgsl-text` | MIR | có | không | không | **Giới hạn** |
| `sexp` | MIR | có | không | không | **Giới hạn** |

## Định tuyến quy trình {#pipeline-routing}

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck → Analysis
                                                              ↓
                                    ┌─────────────────────────┴──────────┐
                                    │                                    │
                              HIR backends                        MIR backends
                                    │                                    │
            Rust · Faber · TS · Go            fmir · wasm · llvm · metal · wgsl · sexp
```

## Tuyến ứng dụng (HIR) {#application-lane-hir}

| Đích | Mức sàn đo được |
|--------|---------------|
| Rust | Tuyến sản xuất. Chế độ mượn, sinh CLI, hạ `Result` có thể thất bại. |
| Faber | Chế độ xem mã nguồn chuẩn / vòng khứ hồi. Không phải backend thực thi. |
| TypeScript | Đã phân tích 288/318 · 268/318 hợp lệ khi kiểm tra kiểu · 262/318 có thể chạy |
| Go | 146/216 đạt. Chế độ mượn bị loại bỏ; `ad` bị từ chối. |

## Tuyến hệ thống (MIR) {#systems-lane-mir}

| Đích | Mức sàn đo được |
|--------|---------------|
| fmir* | Ảnh MIR của gói; trình chạy chứng minh tính độc lập với mã nguồn. |
| wasm | 200/289 đã phát sinh · 195/289 xác thực · 171/289 chạy được với host giả lập |
| llvm-text | 249/289 đã phát sinh · 232/289 hợp lệ với trình kiểm tra · 65/289 có thể chạy |
| metal-text | Tập con kernel an toàn trên thiết bị; 88 kiểm thử tập trung. Chiến dịch đã tạm dừng. |
| wgsl-text | Xác thực bằng naga 30.x. 87 kiểm thử tập trung. Có sidecar phản chiếu. |
| sexp | 193 đã phát sinh · 190 được biên dịch bằng Racket · 190 chạy bằng Racket. Đích xác thực. |

Để xem các cờ năng lực hiện tại, hãy chạy `faber targets`.
