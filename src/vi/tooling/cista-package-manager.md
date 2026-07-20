+++
translation_kind = "translated"

title = "Cista package manager"
section = "tooling"
order = 3
sources = [
  "cista/README.md",
]


prose_hash = "sha256:05d23a68f89274ac712edd9df74eceb081ecb757827aedd26e944afc3a23ab42"
code_hash = "sha256:8911c196f515c978b54a345902a35f102715550c60930e2efee379e50e6c7c1e"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Cista là trình quản lý gói của Faber. Trình quản lý này xử lý việc phân giải gói, quản lý phụ thuộc và kho gói công khai.

## Tổng quan {#overview}

Cista quản lý các gói Faber được định nghĩa bằng các tệp manifest `faber.toml`. Mỗi gói khai báo tên, điểm vào, backend đích và các phụ thuộc.

## Manifest gói {#manifest}

```text
faber.toml

[nomen]
speculum-gen

[ingressus]
main.fab

[scopulus]
rust

[genus]
bin
```

Trường `[nomen]` là tên gói, `[ingressus]` là mô-đun điểm vào, `[scopulus]` chọn đích sinh mã, còn `[genus]` khai báo loại gói (`bin` cho tệp thực thi, `lib` cho thư viện).

## Phụ thuộc {#dependencies}

Các gói khai báo những phụ thuộc mà Cista sẽ phân giải từ kho gói. Việc phân giải phụ thuộc tạo ra một tệp khóa để bảo đảm các bản dựng có thể tái lập.

## Trạng thái {#status}

Cista đang được tích cực phát triển. Registry gói công khai (`cista.dev`) là một chiến dịch riêng, tách biệt với việc triển khai trang web. Việc phân giải gói cục bộ hoạt động đối với các gói nằm trong cùng một workspace.
