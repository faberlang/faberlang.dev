## Đoạn trích system prompt (reader pack)

Phát ra Faber theo locale người-đọc tiếng Việt, dùng từ khóa tiếng Việt cho khai báo, điều khiển luồng, vòng lặp, trả về, boolean, các kiểu nguyên thủy thông dụng, và tập hợp list/map khi phù hợp. Giữ nguyên cú pháp glyph của Faber. Các token mã nguồn Latin Faber trong khối code chỉ giữ làm điểm đánh dấu.

## Hướng dẫn

Dịch phần văn xuôi bên dưới từ tiếng Anh sang ngôn ngữ đích. Tuân thủ các quy tắc sau:

- Chỉ dịch văn xuôi. KHÔNG dịch khối code.
- Giữ nguyên {#anchors} (neo tiêu đề).
- Giữ nguyên cấu trúc markdown (tiêu đề, đoạn văn, danh sách).
- Giữ nguyên hình dạng bảng (số cột, căn lề).
- Giữ nguyên liên kết. Đường dẫn có thể giữ tuyệt đối (/start/...) vì bộ sinh sẽ thêm tiền tố đường dẫn locale.
- Các điểm rào được hiển thị dưới dạng điểm đánh dấu "<<<FENCE n>>>". Giữ nguyên các điểm đánh dấu này trong đầu ra của bạn.
- Trả về toàn bộ nội dung thân cùng với các điểm đánh dấu tại chỗ.
- Chỉ trả về thân Markdown đã dịch (không có frontmatter, lời mở đầu, ghi chú, hay lời bạt).

## Các gói Faber thực tế — không phải đoạn mã đồ chơi. Mã nguồn nằm trong kho công khai
[faberlang/examples](https://github.com/faberlang/examples).
Dùng những gói này khi bạn cần xem cách ứng dụng được tổ chức, cách các CLI
được kết nối, hoặc cách kho ngữ liệu ngôn ngữ được sắp xếp.

## Cách chạy một ví dụ {#how-to-run}

<<<FENCE 0>>>

Lệnh vào chính xác khác nhau theo từng gói — hãy đọc `README.md` của mỗi gói.

## Gói ứng dụng {#applications}

| Gói | Vai trò | Bắt đầu từ đây |
|---|---|---|
| **AI Workbench** | CLI đa lệnh cho kiểm kê mô hình cục bộ, embedding, và quy trình suy luận; xác thực bằng harness Python | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · trang: [AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | CLI mailspace cục bộ thuần Faber (lưu file + lane SQLite tùy chọn) cho các lệnh phối hợp agent | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | Chiến dịch ứng dụng lớn hơn cài đặt lại các tiện ích thông dụng với harness tương đương | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | Các bậc và hợp đồng khối lượng công việc GPU / hệ thống | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | Demo scripting và giao diện kernel | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | Gói phác thảo tự động hóa | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | Gói demo locale cho ánh xạ lại từ khóa | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | Tài liệu thí nghiệm kho gói | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## Kho ngữ liệu ngôn ngữ {#corpus}

Cây **corpus** là tham chiếu từ khóa và cấu trúc: một thư mục cho mỗi
cấu trúc, nhiều chương trình `.fab` nhỏ. Đây là nguồn chân lý cho các
trang [Corpus](/corpus/) được sinh ra trên trang này.

| Bề mặt | URL |
|---|---|
| Cây mã nguồn | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| Tài liệu sinh | [/corpus/](/corpus/) |
| Ghi chú hệ sinh thái | [Language corpus](/ecosystem/corpus.html) |

## Tham quan thư viện chuẩn {#stdlib}

Các mẫu mực thư viện chuẩn Norma nằm trong kho **norma**, không phải trong
`examples/`:

- [faberlang/norma](https://github.com/faberlang/norma) — `norma/exempla/` khi có mặt
- Trang: [Norma](/ecosystem/norma.html)

## Thứ tự học gợi ý {#order}

1. [Cài đặt](/start/install.html) CLI.
2. Lướt [Tham quan nhanh](/start/) để nắm hình dạng ngôn ngữ.
3. Mở các trang **corpus** cho bất kỳ từ khóa nào bạn không nhận ra ([Trung tâm Corpus](/corpus/)).
4. Đọc **AI Workbench** hoặc **ViviLite** từ đầu đến cuối để nắm hình dạng ứng dụng.
5. Dùng [Cú pháp](/syntax/) và [Công cụ](/tooling/) làm tài liệu tham khảo khi soạn thảo.

## Đường dẫn agent {#agent-path}

- Kỹ năng: [examples](/.well-known/agent-skills/examples/SKILL.md)
- Kỹ năng: [corpus](/.well-known/agent-skills/corpus/SKILL.md)
- Chỉ mục: [`/llms.txt`](/llms.txt)

## Trước đó {#previous}

| Trước | Tiếp |
|---|---|
| [Dự án và ví dụ](/start/projects.html) | [Tính năng](/features/) |
