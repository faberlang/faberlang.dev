+++
translation_kind = "translated"

title = "Examples"
section = "examples"
order = 5
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
  "examples/ai-workbench/ (README.md, package, harness)",
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]
+++

## Examples

Các gói Faber thực tế — không phải những đoạn mã mẫu đơn giản. Mã nguồn nằm
trong kho lưu trữ công khai [faberlang/examples](https://github.com/faberlang/examples).
Hãy dùng các ví dụ này khi cần xem cách tổ chức ứng dụng, cách kết nối CLI,
hoặc cách tổ chức corpus của ngôn ngữ.

### Cách chạy một ví dụ {#how-to-run}

```bash
# CLI on PATH (see Install)
faber --version

# Clone examples
git clone https://github.com/faberlang/examples.git

# Type-check a package; dependencies resolve through faber.lock
# and the Cista package store.
faber check examples/ai-workbench/packages/faber-ai

# Build / run / test when the package supports it
faber build examples/ai-workbench/packages/faber-ai -t rust
faber test examples/ai-workbench/packages/faber-ai
```

Lệnh chạy chính xác thay đổi theo từng gói — hãy đọc `README.md` của từng gói.

### Các gói ứng dụng {#applications}

| Gói | Vai trò | Bắt đầu tại đây |
|---|---|---|
| **AI Workbench** | CLI đa lệnh để lập danh mục mô hình cục bộ, tạo embedding và thực hiện các quy trình suy luận; xác thực harness Python | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · trang web: [AI Workbench](/start/examples.html) |
| **ViviLite** | CLI mailspace cục bộ thuần Faber (lưu bằng tệp + lane SQLite tùy chọn) cho các lệnh điều phối tác tử | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | Chiến dịch ứng dụng lớn hơn, tái triển khai các tiện ích phổ biến cùng các harness kiểm tra tương đương | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | Các tầng workload và hợp đồng cho GPU / hệ thống | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | Các bản minh họa về scripting và tương tác với kernel | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | Các gói phác thảo về tự động hóa | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | Các bản minh họa gói locale để ánh xạ lại từ khóa | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | Tài liệu thực hành về kho lưu trữ gói | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

### Corpus ngôn ngữ {#corpus}

Cây **corpus** là tài liệu tham chiếu cho các từ khóa và cấu trúc: mỗi cấu trúc
có một thư mục riêng, chứa nhiều chương trình `.fab` nhỏ. Đây là nguồn chân lý
cho các trang [Corpus](/corpus/) được tạo trên trang web này.

| Bề mặt | URL |
|---|---|
| Cây mã nguồn | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| Tài liệu được tạo | [/corpus/](/corpus/) |
| Ghi chú hệ sinh thái | [Corpus ngôn ngữ](/libraries/corpus.html) |

### Khảo sát thư viện chuẩn {#stdlib}

Các ví dụ thư viện chuẩn Norma nằm trong kho **norma**, không nằm dưới
`examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` nếu có
- Trang web: [Norma](/libraries/norma.html)

### Thứ tự học được đề xuất {#order}

1. Cài đặt CLI từ trang [Cài đặt](/start/install.html).
2. Đọc lướt [Chuyến tham quan nhanh](/start/) để nắm hình dạng ngôn ngữ.
3. Mở các trang **corpus** cho mọi từ khóa bạn chưa nhận ra ([Trang chính Corpus](/corpus/)).
4. Đọc toàn bộ **AI Workbench** hoặc **ViviLite** để hiểu cấu trúc ứng dụng.
5. Dùng [Cú pháp](/language/) và [Công cụ](/toolchain/) làm tài liệu tham chiếu trong khi chỉnh sửa.

### Lộ trình cho tác tử {#agent-path}

- Kỹ năng: [examples](/.well-known/agent-skills/examples/SKILL.md)
- Kỹ năng: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- Chỉ mục: [`/llms.txt`](/llms.txt)

### Trước đó {#previous}

| Trước đó | Tiếp theo |
|---|---|
| [Các dự án và ví dụ](/start/projects.html) | [Tính năng](/language/) |

## AI Workbench

AI Workbench là một ứng dụng CLI Faber dành cho việc kiểm kê mô hình cục bộ, kiểm tra siêu dữ liệu, tạo embedding, lập chỉ mục và thực hiện các quy trình suy luận. Ứng dụng này minh họa cách Faber xây dựng một ứng dụng CLI đa lệnh đáng kể với I/O thực, đầu ra JSON và việc xác thực bằng bộ kiểm thử Python.

### Gói {#package}

`examples/ai-workbench/packages/faber-ai/` với các lệnh con CLI:

- `model inspect` — truy vấn bí danh, tuyến xử lý và trạng thái của các mô hình cục bộ
- `embed` — tạo embedding từ dữ liệu văn bản đầu vào

### Các lệnh {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

### Xác thực {#validation}

AI Workbench bao gồm hơn 20 tập lệnh harness Python để so sánh đầu ra của Faber với các bản đồ fixture về kiểm kê mô hình, suy luận, bằng chứng GPU, vòng đời phiên và việc tái sử dụng gói — qua đó minh họa hoạt động xác thực xuyên ngôn ngữ đối với các tệp nhị phân Faber đã biên dịch.

## Coreutils

Faber tái triển khai GNU coreutils như một minh chứng cho làn ứng dụng. Đây là các chương trình CLI thực tế, cho thấy Faber có thể xây dựng các tệp nhị phân hoạt động với argv, stdio, mã thoát và I/O của máy chủ. Kết quả được kiểm chứng bằng các tiện ích GNU trên máy chủ thông qua một bộ kiểm tra tương đương.

### Các tiện ích đã triển khai {#implemented-utilities}

**Giai đoạn 1 — khung ban đầu + true/false**  
`true`, `false`

**Giai đoạn 2 — các trình trợ giúp dùng chung + kiểm thử nội tuyến**  
`echo`, `basename`, `dirname`, `printf`, `seq`

**Giai đoạn 3 — các lát stdin nullable**  
`cat`, `head`, `tail`, `wc`, `tac`, `uniq`, `fold`, `nl`, `expand`,  
`unexpand`, `sort`, `cut`, `grep`, `tr`, `tee`, `paste`

**Đã tạo khung — Giai đoạn 5+**  
`rm`, `cp`, `mv`, `mkdir`, `touch`, `pwd`, `readlink`, `realpath`,  
`join`, `comm`, `od`, `cksum`, `split`, `yes`, `printenv`

### Ví dụ — echo {#example--echo}

Gói `echo` minh họa các mẫu Faber được sử dụng xuyên suốt coreutils:
chú thích CLI, phân tích tùy chọn, kiểm thử nội tuyến với
`probandum`/`proba`/`adfirma`, và các mô-đun dùng chung:

```faber locale=la
importa ex "norma:consolum" privata consolum

functio echo_textus(lista<textus> words) → textus {
    redde ""
}

functio echo_novam_lineam(lista<textus> words) → bivalens {
    redde falsum
}

probandum "echo formatting" tag "coreutils" {
    proba "empty operands" {
        adfirma echo_textus([]) ≡ ""
    }
    proba "-n suppresses newline" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }
}

@ cli "echo"
@ descriptio "GNU coreutils echo parity exemplum"
@ operandus ceteri textus words
incipit argumenta args {
    # ... CLI logic here
}
```

### Chạy chương trình {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
