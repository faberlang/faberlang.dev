Bên cạnh đường dẫn Rust đã biên dịch, Faber hỗ trợ thực thi thông dịch trong tiến trình thông qua bộ tiến từng bước MIR.

## Cách sử dụng {#usage}

<<<FENCE 0>>>

Lệnh này chạy mã nguồn Faber trong cùng tiến trình sau phần đầu thông thường của trình biên dịch (từ phân tích cú pháp đến kiểm tra kiểu và hạ cấp MIR), mà không gọi `rustc` hoặc tạo một tiến trình xây dựng.

## Cách hoạt động {#how-it-works}

Trình biên dịch tạo ra HIR đã được phân tích, MIR đã được kiểm tra hợp lệ và bảng nội tại thời gian chạy đã được phân giải. Bộ tiến từng bước MIR chuyển trực tiếp các khối MIR đến máy chủ, bỏ qua vòng chuyển đổi phát sinh/khởi tạo wasm:

<<<FENCE 1>>>

## Độ trễ {#latency}

Đường dẫn kịch bản chạy cùng frontend tuyến tính với đường dẫn biên dịch, cộng thêm thời gian tiến từng bước tỉ lệ với phần mã mà kịch bản thực sự thực thi:

| Giai đoạn | Chi phí |
|-------|------|
| Frontend (kịch bản 100 dòng) | ~0.6 ms |
| Tiến từng bước MIR | Tỉ lệ với số câu lệnh được thực thi |

Bộ tiến từng bước không bao giờ gọi `rustc` hoặc tạo tiến trình, vì vậy thời gian khởi động đủ nhanh để tạo cảm giác như chạy một shell script.

## Hạn chế {#limitations}

- Bộ tiến từng bước MIR không hỗ trợ mọi tuyến I/O của máy chủ như đường dẫn đã biên dịch — một số wrapper `norma:*` chỉ hoạt động khi biên dịch
- Bộ tiến từng bước là trình thực thi chẩn đoán/tham chiếu thuần MIR, không phải runtime sản xuất cho các ứng dụng đã triển khai
- Việc biên dịch gói thông qua Cargo vẫn là đường dẫn sản phẩm chính
