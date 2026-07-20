Norma là thư viện chuẩn của Faber. Thư viện cung cấp các mô-đun tên bằng tiếng Latinh, được truy cập qua các đường dẫn `norma:*`. Các khai báo của thư viện chuẩn là mã nguồn Faber trong kho `norma` lân cận.

## Các mô-đun {#modules}

| Mô-đun | Miền chức năng |
|--------|----------------|
| `norma:solum` | Thao tác với hệ thống tệp |
| `norma:solum/path` | Thao tác thuần với tên đường dẫn |
| `norma:http` | HTTP client |
| `norma:processus` | Thực thi tiến trình |
| `norma:consolum` | I/O console (stdin, stdout, stderr) |
| `norma:json` | Phân tích cú pháp và tuần tự hóa JSON |
| `norma:toml` | Phân tích cú pháp TOML |
| `norma:yaml` | Phân tích cú pháp YAML |
| `norma:valor` | Điều hướng codec |
| `norma:tensor` | Hàm hỗ trợ cầu nối tensor |
| `norma:tempus` | Thời gian và khoảng thời gian |
| `norma:aleator` | Tính ngẫu nhiên |

## Quy ước đặt tên morphologia {#morphologia-naming-convention}

Norma tuân theo chính sách morphologia cho mọi tên phương thức. Việc chia động từ tiếng Latinh thể hiện chế độ thực thi:

| Gốc | Đồng bộ | Bất đồng bộ | Ý nghĩa |
|------|------|---------|---------|
| `leg-` | `lege` | `leget` | Đọc |
| `scrib-` | `scribe` | `scribet` | Ghi |
| `quaer-` | — | `quaeret` | Truy vấn (hữu hạn) |
| `quaer-` | — | `quaerent` | Truy vấn (luồng) |

Các cặp quyền sở hữu (biến đổi so với sao chép kết quả):

| Biến đổi | Sao chép kết quả | Ý nghĩa |
|---------|-------------------|---------|
| `adde` | `addita` | Thêm |
| `inverte` | `inversa` | Đảo ngược |
| `filtra` | `filtrata` | Lọc |

## Cách sử dụng {#usage}

<<<FENCE 0>>>
