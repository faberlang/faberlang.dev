Các gói Faber thực tế — không phải những đoạn mã mẫu đơn giản. Mã nguồn nằm
trong kho lưu trữ công khai [faberlang/examples](https://github.com/faberlang/examples).
Hãy dùng các ví dụ này khi cần xem cách tổ chức ứng dụng, cách kết nối CLI,
hoặc cách tổ chức corpus của ngôn ngữ.

## Cách chạy một ví dụ {#how-to-run}

<<<FENCE 0>>>

Lệnh chạy chính xác thay đổi theo từng gói — hãy đọc `README.md` của từng gói.

## Các gói ứng dụng {#applications}

| Gói | Vai trò | Bắt đầu tại đây |
|---|---|---|
| **AI Workbench** | CLI đa lệnh để lập danh mục mô hình cục bộ, tạo embedding và thực hiện các quy trình suy luận; xác thực harness Python | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · trang web: [AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | CLI mailspace cục bộ thuần Faber (lưu bằng tệp + lane SQLite tùy chọn) cho các lệnh điều phối tác tử | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | Chiến dịch ứng dụng lớn hơn, tái triển khai các tiện ích phổ biến cùng các harness kiểm tra tương đương | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | Các tầng workload và hợp đồng cho GPU / hệ thống | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | Các bản minh họa về scripting và tương tác với kernel | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | Các gói phác thảo về tự động hóa | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | Các bản minh họa gói locale để ánh xạ lại từ khóa | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | Tài liệu thực hành về kho lưu trữ gói | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## Corpus ngôn ngữ {#corpus}

Cây **corpus** là tài liệu tham chiếu cho các từ khóa và cấu trúc: mỗi cấu trúc
có một thư mục riêng, chứa nhiều chương trình `.fab` nhỏ. Đây là nguồn chân lý
cho các trang [Corpus](/corpus/) được tạo trên trang web này.

| Bề mặt | URL |
|---|---|
| Cây mã nguồn | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| Tài liệu được tạo | [/corpus/](/corpus/) |
| Ghi chú hệ sinh thái | [Corpus ngôn ngữ](/ecosystem/corpus.html) |

## Khảo sát thư viện chuẩn {#stdlib}

Các ví dụ thư viện chuẩn Norma nằm trong kho **norma**, không nằm dưới
`examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` nếu có
- Trang web: [Norma](/ecosystem/norma.html)

## Thứ tự học được đề xuất {#order}

1. Cài đặt CLI từ trang [Cài đặt](/start/install.html).
2. Đọc lướt [Chuyến tham quan nhanh](/start/) để nắm hình dạng ngôn ngữ.
3. Mở các trang **corpus** cho mọi từ khóa bạn chưa nhận ra ([Trang chính Corpus](/corpus/)).
4. Đọc toàn bộ **AI Workbench** hoặc **ViviLite** để hiểu cấu trúc ứng dụng.
5. Dùng [Cú pháp](/syntax/) và [Công cụ](/tooling/) làm tài liệu tham chiếu trong khi chỉnh sửa.

## Lộ trình cho tác tử {#agent-path}

- Kỹ năng: [examples](/.well-known/agent-skills/examples/SKILL.md)
- Kỹ năng: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- Chỉ mục: [`/llms.txt`](/llms.txt)

## Trước đó {#previous}

| Trước đó | Tiếp theo |
|---|---|
| [Các dự án và ví dụ](/start/projects.html) | [Tính năng](/features/) |
