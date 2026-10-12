Các package Faber thực tế — không phải snippet đồ chơi. Mã nguồn nằm trong kho công khai
[faberlang/examples](https://github.com/faberlang/examples).
Dùng các ví dụ này khi bạn cần xem ứng dụng được cấu trúc thế nào, CLI
được nối ra sao, hoặc corpus ngôn ngữ được tổ chức như thế nào.

## Cách chạy một ví dụ {#how-to-run}

<<<FENCE 0>>>

Lệnh entry chính xác khác nhau theo từng package — hãy đọc `README.md` của mỗi package.

## Application packages {#applications}

| Package | Vai trò | Bắt đầu tại đây |
|---|---|---|
| **AI Workbench** | CLI đa lệnh cho inventory model cục bộ, embeddings và workflow inference; xác thực harness Python | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · site: [AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | CLI mailspace cục bộ thuần Faber (file-backed + lane SQLite tùy chọn) cho các lệnh phối hợp agent | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | Chiến dịch ứng dụng lớn hơn, tái hiện các utility phổ biến kèm harness parity | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | Các bậc workload GPU / systems và contract | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | Demo scripting và hướng kernel | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | Các package phác thảo automation | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | Demo locale pack cho keyword remapping | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | Tài liệu lab cho package-store | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## Corpus ngôn ngữ {#corpus}

Cây **corpus** là tham chiếu keyword và construct: một thư mục
cho mỗi construct, nhiều chương trình `.fab` nhỏ. Đây là nguồn sự thật cho
các trang [Corpus](/corpus/) được sinh trên site này.

| Bề mặt | URL |
|---|---|
| Cây mã nguồn | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| Tài liệu sinh ra | [/corpus/](/corpus/) |
| Ghi chú ecosystem | [Corpus ngôn ngữ](/ecosystem/corpus.html) |

## Tour stdlib {#stdlib}

Các exempla thư viện chuẩn Norma nằm trong repo **norma**, không nằm dưới
`examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` khi có
- Site: [Norma](/ecosystem/norma.html)

## Thứ tự học gợi ý {#order}

1. [Cài đặt](/start/install.html) CLI.
2. Lướt [Tour nhanh](/start/) để nắm hình dạng ngôn ngữ.
3. Mở các trang **corpus** cho mọi keyword bạn chưa nhận ra ([Trung tâm Corpus](/corpus/)).
4. Đọc **AI Workbench** hoặc **ViviLite** từ đầu đến cuối để nắm hình dạng ứng dụng.
5. Dùng [Cú pháp](/syntax/) và [Công cụ](/tooling/) làm tham chiếu khi chỉnh sửa.

## Đường agent {#agent-path}

- Skill: [examples](/.well-known/agent-skills/examples/SKILL.md)
- Skill: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- Index: [`/llms.txt`](/llms.txt)

## Trước đó {#previous}

| Trước | Tiếp |
|---|---|
| [Dự án và ví dụ](/start/projects.html) | [Tính năng](/features/) |
