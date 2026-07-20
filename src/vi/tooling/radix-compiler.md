+++
translation_kind = "translated"

title = "Radix compiler"
section = "tooling"
order = 2
sources = [
  "radix/README.md",
  "radix/AGENTS.md",
]


prose_hash = "sha256:a3572e734d3a664b9ce7f7d1dd57e9a3190982a284e82db7f4c2e1c9dfc4aff3"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Radix là trình biên dịch Faber. Đây là một crate riêng tư (`radix/`) triển khai toàn bộ quy trình biên dịch, từ văn bản mã nguồn đến các back-end đích.

## Quy trình {#pipeline}

Radix hạ cấp mã nguồn Faber qua ba dạng biểu diễn trung gian:

1. **HIR** (IR cấp cao) — lõi ngữ nghĩa. Tích hợp locale đọc, kiểm tra kiểu và các back-end trực tiếp trên HIR hoạt động tại đây.
2. **MIR** (IR cấp trung) — IR có hình dạng phù hợp với quá trình thực thi. Đây là ranh giới sở hữu ngữ nghĩa, nơi diễn ra phân tích mượn và phân tích hiệu ứng.
3. **AIR** (IR tự động vi phân) — phép biến đổi thuần hàm cho việc tự động vi phân và hợp nhất, được các lane đích GPU sử dụng.

## Các lane đích {#target-lanes}

| Lane | IR | Đầu ra | Trạng thái |
|---|---|---|---|
| Runtime CPU | MIR | FMIR (runtime Rust) | Đang phát hành |
| LLVM | MIR | Văn bản LLVM | Thử nghiệm |
| WASM | MIR | Văn bản WebAssembly | Thử nghiệm |
| TypeScript | HIR | Mã nguồn TypeScript | Thử nghiệm |
| Go | HIR | Mã nguồn Go | Thử nghiệm |
| GPU/WGSL | AIR | WGSL qua WGPU | Thử nghiệm |

## Kiến trúc {#architecture}

Radix sử dụng cách tiếp cận phát sinh văn bản thay vì nhúng LLVM. Các back-end đích tạo văn bản bằng ngôn ngữ tương ứng, sau đó văn bản này được biên dịch bằng toolchain riêng của đích. Cách này giữ cho trình biên dịch độc lập và giúp đầu ra của đích dễ đọc đối với con người.

## Chẩn đoán {#diagnostics}

Radix phát ra các mã chẩn đoán có cấu trúc với mã định danh ổn định:

- `LEX0xx` — lỗi lexer
- `PARSE0xx` — lỗi parser
- `SEM0xx` — lỗi phân tích ngữ nghĩa
- `DEFER0xx` — tính năng trì hoãn (cú pháp hợp lệ nhưng chưa được triển khai)

Bạn có thể giải thích mọi chẩn đoán bằng `faber explain <code>`.
