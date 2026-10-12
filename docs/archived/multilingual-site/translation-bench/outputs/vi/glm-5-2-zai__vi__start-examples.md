Các gói Faber thực tế — không phải đoạn mã minh họa. Mã nguồn nằm trong kho
[faberlang/examples](https://github.com/faberlang/examples) công khai.
Hãy dùng chúng khi bạn cần xem cách ứng dụng được tổ chức, cách CLI được
kết nối, hoặc cách ngữ liệu ngôn ngữ được sắp xếp.

## Cách chạy một ví dụ {#how-to-run}

<<<FENCE 0>>>

Lệnh khởi chạy chính xác thay đổi theo từng gói — hãy đọc `README.md` của từng gói.

## Các gói ứng dụng {#applications}

| Gói | Vai trò | Bắt đầu từ đây |
|---|---|---|
| **AI Workbench** | CLI đa lệnh dành cho kiểm kê mô hình cục bộ, embedding và quy trình suy luận; kiểm chứng harness Python | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · trang: [AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | CLI mailspace cục bộ thuần Faber (dựa trên tệp + làn SQLite tùy chọn) cho các lệnh điều phối agent | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | Chiến dịch ứng dụng quy mô lớn tái dựng các tiện ích phổ biến kèm harness tương đương | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | Bậc và hợp đồng khối lượng công việc GPU / hệ thống | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | Bản demo hướng scripting và hạt nhân | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | Các gói phác thảo tự động hóa | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | Bản demo gói ngôn ngữ cho ánh xạ lại từ khóa | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | Tài liệu lab cho package-store | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## Ngữ liệu ngôn ngữ {#corpus}

Cây **corpus** là tài liệu tham chiếu cho từ khóa và cấu trúc: một thư mục
cho mỗi cấu trúc, nhiều chương trình `.fab` nhỏ. Đây là nguồn sự thật cho
các trang [Corpus](/corpus/) được sinh ra trên trang này.

| Mặt | URL |
|---|---|
| Cây mã nguồn | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| Tài liệu đã sinh | [/corpus/](/corpus/) |
| Ghi chú hệ sinh thái | [Ngữ liệu ngôn ngữ](/ecosystem/corpus.html) |

## Khám phá stdlib {#stdlib}

Các exempla của thư viện chuẩn Norma nằm trong repo **norma**, không nằm
dưới `examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` nếu có
- Trang: [Norma](/ecosystem/norma.html)

## Thứ tự học đề xuất {#order}

1. [Cài đặt](/start/install.html) CLI.
2. Lướt [Quick tour](/start/) để nắm hình thái ngôn ngữ.
3. Mở các trang **corpus** cho bất kỳ từ khóa nào bạn chưa quen ([Hub Corpus](/corpus/)).
4. Đọc từ đầu đến cuối **AI Workbench** hoặc **ViviLite** để hiểu hình thái ứng dụng.
5. Dùng [Syntax](/syntax/) và [Tooling](/tooling/) làm tài liệu tham chiếu trong khi chỉnh sửa.

## Đường dẫn agent {#agent-path}

- Kỹ năng: [examples](/.well-known/agent-skills/examples/SKILL.md)
- Kỹ năng: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- Chỉ mục: [`/llms.txt`](/llms.txt)

## Trang trước {#previous}

| Trang trước | Trang kế |
|---|---|
| [Dự án và ví dụ](/start/projects.html) | [Tính năng](/features/) |
