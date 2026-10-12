Cista là trình quản lý gói của Faber. Trình quản lý này xử lý việc phân giải gói, quản lý phụ thuộc và kho gói công khai.

## Tổng quan {#overview}

Cista quản lý các gói Faber được định nghĩa bằng các tệp manifest `faber.toml`. Mỗi gói khai báo tên, điểm vào, backend đích và các phụ thuộc.

## Manifest gói {#manifest}

<<<FENCE 0>>>

Trường `[nomen]` là tên gói, `[ingressus]` là mô-đun điểm vào, `[scopulus]` chọn đích sinh mã, còn `[genus]` khai báo loại gói (`bin` cho tệp thực thi, `lib` cho thư viện).

## Phụ thuộc {#dependencies}

Các gói khai báo những phụ thuộc mà Cista sẽ phân giải từ kho gói. Việc phân giải phụ thuộc tạo ra một tệp khóa để bảo đảm các bản dựng có thể tái lập.

## Trạng thái {#status}

Cista đang được tích cực phát triển. Registry gói công khai (`cista.dev`) là một chiến dịch riêng, tách biệt với việc triển khai trang web. Việc phân giải gói cục bộ hoạt động đối với các gói nằm trong cùng một workspace.
