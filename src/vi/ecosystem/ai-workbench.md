+++
translation_kind = "translated"

title = "AI Workbench"
section = "ecosystem"
order = 4
sources = [
  "examples/ai-workbench/ (README.md, package, harness)",
]


prose_hash = "sha256:3a8940d1ee168b9bdf75f40f70ce5e5eb6b6446f47510df9c3511b2d4d1bef33"
code_hash = "sha256:dc8f04249d6a95c65b63ba0ccd58c402d6f8ed47a96bc15da4b6ad844922d007"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
AI Workbench là một ứng dụng CLI Faber dành cho việc kiểm kê mô hình cục bộ, kiểm tra siêu dữ liệu, tạo embedding, lập chỉ mục và thực hiện các quy trình suy luận. Ứng dụng này minh họa cách Faber xây dựng một ứng dụng CLI đa lệnh đáng kể với I/O thực, đầu ra JSON và việc xác thực bằng bộ kiểm thử Python.

## Gói {#package}

`examples/ai-workbench/packages/faber-ai/` với các lệnh con CLI:

- `model inspect` — truy vấn bí danh, tuyến xử lý và trạng thái của các mô hình cục bộ
- `embed` — tạo embedding từ dữ liệu văn bản đầu vào

## Các lệnh {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

## Xác thực {#validation}

AI Workbench bao gồm hơn 20 tập lệnh harness Python để so sánh đầu ra của Faber với các bản đồ fixture về kiểm kê mô hình, suy luận, bằng chứng GPU, vòng đời phiên và việc tái sử dụng gói — qua đó minh họa hoạt động xác thực xuyên ngôn ngữ đối với các tệp nhị phân Faber đã biên dịch.
