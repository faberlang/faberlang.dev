+++
translation_kind = "translated"

title = "Norma standard library"
section = "ecosystem"
order = 1
sources = [
  "radix/README.md (Standard Library section)",
  "sibling norma/ repository",
  "norma/exempla/",
  "radix/docs/stdlib/morphologia.md",
]


prose_hash = "sha256:f333d0ee78b78e5ad3ebfb1bfdda0a4069a9b7daf3579d8c55d6b83c668be833"
code_hash = "sha256:0ef63774f36a5e950889dcae691b2a9c5add05fe03c89c061ba60d829195f2ff"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
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

```faber locale=la
importa ex "norma:solum" privata solum

functio legeConfig() → textus {
    redde solum.lege("config.toml")
}
```
