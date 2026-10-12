AI Workbench là một ứng dụng CLI Faber dành cho việc kiểm kê mô hình cục bộ, kiểm tra siêu dữ liệu, tạo embedding, lập chỉ mục và thực hiện các quy trình suy luận. Ứng dụng này minh họa cách Faber xây dựng một ứng dụng CLI đa lệnh đáng kể với I/O thực, đầu ra JSON và việc xác thực bằng bộ kiểm thử Python.

## Gói {#package}

`examples/ai-workbench/packages/faber-ai/` với các lệnh con CLI:

- `model inspect` — truy vấn bí danh, tuyến xử lý và trạng thái của các mô hình cục bộ
- `embed` — tạo embedding từ dữ liệu văn bản đầu vào

## Các lệnh {#commands}

<<<FENCE 0>>>

## Xác thực {#validation}

AI Workbench bao gồm hơn 20 tập lệnh harness Python để so sánh đầu ra của Faber với các bản đồ fixture về kiểm kê mô hình, suy luận, bằng chứng GPU, vòng đời phiên và việc tái sử dụng gói — qua đó minh họa hoạt động xác thực xuyên ngôn ngữ đối với các tệp nhị phân Faber đã biên dịch.
