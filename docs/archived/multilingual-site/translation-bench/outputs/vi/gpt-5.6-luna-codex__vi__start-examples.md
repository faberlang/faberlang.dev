Các gói Faber thực tế — không phải những đoạn mã mẫu đơn giản. Mã nguồn nằm trong
kho công khai [faberlang/examples](https://github.com/faberlang/examples).
Hãy dùng các gói này khi bạn cần xem cách tổ chức ứng dụng, cách kết nối CLI,
hoặc cách sắp xếp kho ngữ liệu của ngôn ngữ.

## Cách chạy một ví dụ {#how-to-run}

<<<FENCE 0>>>

Các lệnh khởi chạy chính xác khác nhau tùy gói — hãy đọc `README.md` của từng gói.

## Các gói ứng dụng {#applications}

| Gói | Vai trò | Bắt đầu tại đây |
|---|---|---|
| **AI Workbench** | CLI đa lệnh để kiểm kê mô hình cục bộ, tạo embedding và thực hiện các quy trình suy luận; xác thực bằng harness Python | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · trang: [AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | CLI mailspace cục bộ thuần Faber (dựa trên tệp + lane SQLite tùy chọn) cho các lệnh điều phối agent | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | Chiến dịch tái triển khai ứng dụng quy mô lớn hơn cho các tiện ích phổ biến, kèm các harness kiểm tra tương đương | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | Các nấc và hợp đồng workload GPU / hệ thống | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | Các bản minh họa hướng đến scripting và kernel | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | Các gói phác thảo về tự động hóa | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | Các bản minh họa gói locale để ánh xạ lại từ khóa | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | Tài liệu thực hành về package store | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## Kho ngữ liệu ngôn ngữ {#corpus}

Cây **corpus** là tài liệu tham chiếu cho từ khóa và cấu trúc: mỗi cấu trúc có
một thư mục riêng, chứa nhiều chương trình `.fab` nhỏ. Đây là nguồn chuẩn cho
các trang [Corpus](/corpus/) được tạo trên trang web này.

| Bề mặt | URL |
|---|---|
| Cây mã nguồn | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| Tài liệu được tạo | [/corpus/](/corpus/) |
| Ghi chú hệ sinh thái | [Kho ngữ liệu ngôn ngữ](/ecosystem/corpus.html) |

## Các chuyến tham quan stdlib {#stdlib}

Các exempla của thư viện chuẩn Norma nằm trong repo **norma**, không nằm dưới
`examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` nếu có
- Trang web: [Norma](/ecosystem/norma.html)

## Thứ tự học được đề xuất {#order}

1. [Cài đặt](/start/install.html) CLI.
2. Xem lướt [Chuyến tham quan nhanh](/start/) để nắm hình dạng của ngôn ngữ.
3. Mở các trang **corpus** cho bất kỳ từ khóa nào bạn chưa nhận ra ([trang tổng quan Corpus](/corpus/)).
4. Đọc **AI Workbench** hoặc **ViviLite** từ đầu đến cuối để hiểu cấu trúc ứng dụng.
5. Dùng [Cú pháp](/syntax/) và [Bộ công cụ](/tooling/) làm tài liệu tham khảo khi chỉnh sửa.

## Lộ trình cho agent {#agent-path}

- Skill: [examples](/.well-known/agent-skills/examples/SKILL.md)
- Skill: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- Chỉ mục: [`/llms.txt`](/llms.txt)

## Trước đó {#previous}

| Trước đó | Tiếp theo |
|---|---|
| [Các dự án và ví dụ](/start/projects.html) | [Tính năng](/features/) |