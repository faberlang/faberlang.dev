+++
translation_kind = "translated"

title = "Install and download"
section = "install"
order = 1
sources = []

prose_hash = "sha256:662becbb3dd5349058bcdfec9219fd07f6fe4217c2e5115c0aade45e0f17f0d4"
code_hash = "sha256:cc9de43077b1262ee3d9edfbd3bd56c4ae51bcca18d0316fa0bb95312f3033b7"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
Cài đặt CLI **Faber** từ bản phát hành dựng sẵn hiện tại. Phần đầu của trình biên dịch được tích hợp trong tệp nhị phân `faber`; bạn không cần cài đặt Radix riêng cho công việc với gói thông thường.

Trang này được viết dựa trên các tạo phẩm phát hành của kho mã Faber 1.1.1. Công thức của trình quản lý gói có thể chậm hơn bản phát hành của kho mã; nếu Homebrew hoặc trình quản lý khác báo phiên bản Radix/Faber cũ hơn, hãy ưu tiên các tệp lưu trữ bên dưới cho lộ trình này.

## Bản phát hành hiện tại {#current-release}

| Trường | Giá trị |
|---|---|
| **Phiên bản** | 1.1.1 |
| **Thẻ** | `faber-v1.1.1` |
| **Trang phát hành** | [faber-v1.1.1 trên GitHub](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1) |
| **Tất cả bản phát hành** | [Danh mục các bản phát hành của trang](/history/releases.html) |
| **Giấy phép** | MIT |

## Tệp lưu trữ dựng sẵn {#archives}

| Nền tảng | Tải xuống | SHA-256 |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

Các tệp lưu trữ được giải nén thành `faber-v1.1.1-<target-triple>/faber`. Các tệp checksum có thể ghi đường dẫn dựng ban đầu, vì vậy hãy xác minh bằng cách so sánh trường băm đầu tiên với tệp lưu trữ cục bộ thay vì dựa vào việc khớp đường dẫn của `sha256sum -c`.

### macOS arm64 {#macos}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
# place on PATH, e.g.:
sudo mv faber-v1.1.1-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

### Linux x64 {#linux}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(sha256sum faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.1.1-x86_64-unknown-linux-gnu/faber /usr/local/bin/
faber --version
```

## Xác minh {#verify}

```bash
faber --version
faber explain SEM001
```

Bạn sẽ thấy một dòng phiên bản của CLI và phần giải thích chẩn đoán. Nếu không tìm thấy `faber`, hãy kiểm tra xem thư mục chứa tệp nhị phân đã nằm trong `PATH` hay chưa.

## Kiểm tra gói đầu tiên {#first-package}

Khi CLI đã có trên `PATH`, hãy sao chép các ví dụ công khai (hoặc bất kỳ gói Faber nào) và kiểm tra kiểu. Các gói sản phẩm phân giải phần phụ thuộc từ kho Cista thông qua `faber.lock`; các bản sao mã nguồn cục bộ chỉ dùng cho các ghi đè phát triển thư viện được chỉ định rõ ràng.

```bash
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

Xem thêm các gói: [Ví dụ](/start/examples.html). Bề mặt CLI: [Công cụ dựng Faber](/tooling/faber-build-tool.html).

## Trạng thái Homebrew {#homebrew}

Việc phát hành qua Homebrew hiện chưa phải là nguồn có thẩm quyền cho lộ trình bắt đầu này. Nếu một công thức cung cấp trình biên dịch cũ như Radix 0.38.0 trong khi trang này ghi lại Faber 1.1.1, hãy xem công thức đó là chậm cập nhật và sử dụng tệp lưu trữ bản phát hành dựng sẵn. Cổng xác minh bằng container cho trang này vẫn còn tồn đọng cho đến khi việc phát hành công thức được cập nhật.

## Dựng từ mã nguồn {#from-source}

Tệp dựng sẵn là lựa chọn được khuyến nghị cho tác nhân và hầu hết nhà phát triển. Việc dựng từ mã nguồn yêu cầu cây trình biên dịch Radix riêng tư và nằm ngoài phạm vi của trang này. Hãy ưu tiên các tệp lưu trữ ở trên, trừ khi bạn đang làm việc trực tiếp trên trình biên dịch.

## Lộ trình cho tác nhân {#agent-path}

Tác nhân nên tải skill **install** và chỉ mục tác nhân thay vì quét HTML này:

- [`/llms.txt`](/llms.txt)
- [skill install](/.well-known/agent-skills/install/SKILL.md)
- [Hướng dẫn tác nhân](/agents/index.md)

## Tiếp theo {#next}

| Trước | Tiếp theo |
|---|---|
| [Tham quan nhanh](/start/) | [Xin chào, Faber](/start/hello.html) |
