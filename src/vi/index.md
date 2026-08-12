+++
translation_kind = "translated"

title = "Faber"
section = ""
order = 0
sources = []

prose_hash = "sha256:e63352acf54515593d9aeccf392881d72018d55e6b21d6e1ddd5a3979bef91b8"
code_hash = "sha256:a02ba6ea46d65efd212b09e097d3240402bfe1d46f89b993e389cd53ca1a9c9e"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
**Faber** là một ngôn ngữ lập trình hướng gói với từ vựng hành vi bằng tiếng Latinh, ngữ pháp chính quy nhỏ gọn và hệ thống kiểu tĩnh ưu tiên kiểu. Mã nguồn được biên dịch qua trình biên dịch Radix thành mã Rust có thể xem xét và các tệp nhị phân native. Đặc tính kiến trúc cốt lõi của ngôn ngữ là ý nghĩa nằm trong lõi ngữ nghĩa — HIR (biểu diễn trung gian cấp cao) — thay vì trong bất kỳ dạng hiển thị cụ thể nào.

Tên gọi bắt nguồn từ từ Latinh *maker* hoặc *craftsman*. Trình biên dịch có tên Radix, bắt nguồn từ từ Latinh *root*. Ngôn ngữ được Ian Zepp phát triển và phát hành theo giấy phép MIT.

**Bạn mới bắt đầu?** Hãy bắt đầu với [Cài đặt và tải xuống](/start/install.html), sau đó đi theo lộ trình khởi đầu: [Hello](/start/hello.html), [Các lệnh](/cheatsheet/commands.html) và [Dự án](/start/projects.html).

## Tải xuống Faber 1.6.0 {#download}

Bản phát hành hiện tại: **Faber 1.6.0** (thẻ `faber-v1.6.0`), phát hành ngày 2026-08-10. Các gói CLI dựng sẵn cho macOS và Linux; mỗi gói gồm cây `bin/` và `share/` — đặt `bin/faber` vào `PATH`, giữ `share/faber` bên cạnh tệp nhị phân để các gói ngôn ngữ phân giải được.

| Nền tảng | Gói lưu trữ | Mã kiểm tra |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [faber-v1.6.0-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-aarch64-apple-darwin.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [faber-v1.6.0-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-x86_64-unknown-linux-gnu.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

Cài đặt nhanh (ví dụ macOS arm64):

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.6.0/faber-v1.6.0-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
# Gói chứa cây bin/ và share/; giữ chúng cùng nhau để các gói ngôn ngữ phân giải bên cạnh tệp nhị phân
sudo mv bin/faber /usr/local/bin/faber
sudo mv share/faber /usr/local/share/faber
faber --version
```

Tất cả ghi chú và tài sản của bản phát hành: [github.com/faberlang/releases · faber-v1.6.0](https://github.com/faberlang/releases/releases/tag/faber-v1.6.0).
Hướng dẫn từng bước: [Hướng dẫn cài đặt](/start/install.html). Danh mục lịch sử đầy đủ:
[Các bản phát hành](/releases/).

| | |
|---|---|
| **Mô hình** | Hướng gói; phân tầng ngữ nghĩa |
| **Kiểu** | Tĩnh, ưu tiên kiểu; nullable qua `T ∪ nihil` |
| **Glyph** | `← → ∴ ≡ ∪ ⇥` |
| **Thiết kế bởi** | Ian Zepp |
| **Xuất hiện lần đầu** | 2025 |
| **Trình biên dịch** | Radix (Rust) |
| **Các tuyến** | Ứng dụng (HIR) · Hệ thống (MIR) |
| **Đích chính** | Rust → tệp nhị phân native |
| **Locale người đọc** | 7 locale đã phát hành (la, ar, hi, vi, th-TH, zh-Hans, zh-Hant) |
| **Thư viện chuẩn** | Norma (`norma:*`) |
| **Giấy phép** | MIT |

## Bắt đầu tại đây {#start-here}

| Đường dẫn | Đối tượng | Nội dung |
|---|---|---|
| [Cài đặt](/start/install.html) | Người dùng | Tải xuống, PATH, lệnh `faber check` đầu tiên |
| [Hello](/start/hello.html) | Người dùng | Tạo và chạy `salve-munde` |
| [Các lệnh](/cheatsheet/commands.html) | Người dùng + tác nhân | Vòng lặp CLI hằng ngày: check, build, run, test, explain |
| [Dự án](/start/projects.html) | Người dùng + tác nhân | Chuyển từ hello-world sang các gói thực tế |
| [Tham quan nhanh](/start/) | Người dùng | Hình dạng ngôn ngữ trong năm phút |
| [Ví dụ](/examples/) | Người dùng + tác nhân | Các gói thực tế: ứng dụng CLI, mailspace, GPU, corpus |
| [`/llms.txt`](/llms.txt) | Tác nhân | Chỉ mục máy — bắt đầu tại đây nếu bạn là một mô hình |
| [Hướng dẫn tác nhân](/agents/index.md) | Tác nhân | Cách học Faber và phát hành một gói |
| [Kỹ năng tác nhân](/.well-known/agent-skills/index.json) | Tác nhân | Các hướng dẫn kỹ năng tập trung (cài đặt, ngôn ngữ, ví dụ, …) |

## Trạng thái portal {#portal-status}

Trang `/` này là Speculum Porta cho trang tiếng Anh: một điểm vào không gắn locale, định tuyến người dùng đến các trang cài đặt/khởi đầu, định tuyến tác nhân đến các bề mặt máy và nêu trạng thái gói locale mà không thương lượng tại thời điểm trình duyệt chạy.
Giai đoạn 7 là một bản thử nghiệm đa locale từng phần, không phải một trang đã bản địa hóa hoàn chỉnh:
chỉ `th-TH`, `zh-Hans`, `zh-Hant`, `vi`, `ar` và `hi` có các lát cắt nội dung portal/khởi đầu do tác giả viết cùng các trang corpus được sinh tự động, còn phần văn bản do tác giả viết vẫn quay về tiếng Anh.

| Locale | Trạng thái | Ghi chú |
|---|---|---|
| `la` | Trang chính tắc đang hoạt động | Toàn bộ trang tiếng Anh/Latinh được sinh tự động |
| `th-TH` | Bản thử nghiệm từng phần Giai đoạn 7 | Lát cắt portal/khởi đầu do tác giả viết cùng corpus được sinh tự động; văn bản dự phòng bằng tiếng Anh; toàn bộ tài liệu do tác giả viết đang chờ hoàn thiện |
| `zh-Hans` | Bản thử nghiệm từng phần Giai đoạn 7 | Lát cắt portal/khởi đầu do tác giả viết cùng corpus được sinh tự động; văn bản dự phòng bằng tiếng Anh; toàn bộ tài liệu do tác giả viết đang chờ hoàn thiện |
| `vi` | Bản thử nghiệm từng phần Giai đoạn 7 | Lát cắt portal/khởi đầu do tác giả viết cùng corpus được sinh tự động; văn bản dự phòng bằng tiếng Anh; toàn bộ tài liệu do tác giả viết đang chờ hoàn thiện |
| `zh-Hant` | Bản thử nghiệm từng phần Giai đoạn 7 | Lát cắt portal/khởi đầu do tác giả viết cùng corpus được sinh tự động; văn bản dự phòng bằng tiếng Anh; toàn bộ tài liệu do tác giả viết đang chờ hoàn thiện |
| `ar` | Bản thử nghiệm từng phần Giai đoạn 7 | Lát cắt portal/khởi đầu do tác giả viết cùng corpus được sinh tự động; văn bản dự phòng bằng tiếng Anh; toàn bộ tài liệu do tác giả viết đang chờ hoàn thiện |
| `hi` | Bản thử nghiệm từng phần Giai đoạn 7 | Lát cắt portal/khởi đầu do tác giả viết cùng corpus được sinh tự động; văn bản dự phòng bằng tiếng Anh; toàn bộ tài liệu do tác giả viết đang chờ hoàn thiện |

Ví dụ đang hoạt động trong tiếng Latinh chính tắc:

```faber
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
```

Xem [Locale người đọc](/language/reader-locales.html) để xem cùng một chương trình ngữ nghĩa được hiển thị qua các gói tiếng Thái, tiếng Trung giản thể, tiếng Trung phồn thể, tiếng Ả Rập, tiếng Hindi và tiếng Việt.

## Tổng quan {#overview}

Faber được thiết kế dựa trên một nhận thức cốt lõi: biểu diễn trung gian là sự thật, và không có đích đến hay bề mặt ngôn ngữ tự nhiên nào được ưu tiên. Một chương trình Faber được viết bằng từ khóa Latinh có thể được hiển thị bằng từ khóa tiếng Thái, tiếng Ả Rập hoặc tiếng Trung thông qua cùng cơ chế hiển thị chương trình đó thành Rust, Go hoặc WebAssembly — vì HIR là nguồn thẩm quyền và mọi đầu ra đều là một *dạng hiển thị* của nó.

Ngôn ngữ đưa ra ba lựa chọn tín hiệu có chủ đích và phối hợp với nhau:

- **Khai báo ưu tiên kiểu** — hướng hình dạng về phía phép liên kết: `textus nomen`, không phải `nomen: textus`.
- **Từ hành vi Latinh** — khai báo, câu lệnh và vòng đời: `functio`, `genus`, `fixum`, `redde`, `si`.
- **Glyph cấu trúc** — luồng giá trị và các mối nối kiểu: `←` (liên kết), `→`
  (kiểu trả về), `∴` (khớp nối đóng), `≡` (bằng nhau), `∪` (hợp).

Kết quả là mã nguồn có hình dạng ngữ pháp ổn định, có thể được xem xét, biến đổi và hạ cấp mà không làm mất cảm nhận về ý định của người đọc.

## Tài liệu {#documentation}

| Phần | Mô tả |
|---|---|
| [Lịch sử](/reference/design.html) | Dòng thời gian phát triển, ảnh hưởng và lịch sử phát hành |
| [Các bản phát hành](/releases/) | Bản tải xuống Faber mới nhất cùng mọi thẻ và tệp nhị phân đã phát hành |
| [Tính năng](/language/) | Locale người đọc, các tuyến biên dịch, từ vựng Latinh, hệ thống glyph, nguyên tắc thiết kế |
| [Cú pháp](/language/) | Tài liệu tham khảo đầy đủ: kiểu, hàm, luồng điều khiển, lỗi, generic, collection |
| [Công cụ](/toolchain/) | Pipeline trình biên dịch Radix, CLI Faber, các đích sinh mã, scripting |
| [Hệ sinh thái](/libraries/) | Norma, Cista, Triga, coreutils, AI Workbench, corpus |
| [Corpus](/corpus/) | Các trang từ khóa và cấu trúc được sinh từ corpus công khai |
| [Tham chiếu](/reference/) | Ngữ pháp EBNF, tài liệu thiết kế, kho mã |

## Ví dụ nhanh {#quick-example}

Một hàm đơn giản minh họa các mẫu Faber chính — tham số ưu tiên kiểu, kiểu trả về bằng glyph, hợp nullable, các từ điều khiển Latinh:

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

## Hiển thị trực tiếp {#live-rendering}

Theo mặc định, hàm chia ở trên được hiển thị trong gói Latinh. Trình biên dịch có thể hiển thị cùng một chương trình trong bảy locale người đọc — tiếng Thái, tiếng Trung giản thể, tiếng Trung phồn thể, tiếng Ả Rập, tiếng Hindi và tiếng Việt — mỗi locale ánh xạ lại từ khóa và kiểu sang ngôn ngữ đó trong khi glyph và định danh vẫn không đổi. Đây không phải là một lớp dịch được áp dụng cho trang; đây là cùng cơ chế mà trình biên dịch sử dụng để tạo mã nguồn bản địa hóa.

Xem tài liệu [locale người đọc](/language/reader-locales.html) để biết thảo luận đầy đủ.

## Kho mã {#repositories}

| Kho | Vai trò |
|---|---|
| [faberlang/faber](https://github.com/faberlang/faber) | API đích công khai và trang chủ dự án |
| [faberlang/releases](https://github.com/faberlang/releases) | Tài sản CLI theo từng bản phát hành |
| [faberlang/norma](https://github.com/faberlang/norma) | Mã nguồn thư viện chuẩn |
| [faberlang/cista](https://github.com/faberlang/cista) | CLI/thư viện kho gói |
| [faberlang/triga](https://github.com/faberlang/triga) | Thư viện đồ họa / hình học |
| [faberlang/examples](https://github.com/faberlang/examples) | Corpus, lộ trình, các gói ứng dụng |
| [faberlang/faberlang.dev](https://github.com/faberlang/faberlang.dev) | Trang tài liệu này |
