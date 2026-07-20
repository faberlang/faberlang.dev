+++
translation_kind = "translated"

title = "Hello, Faber"
section = "hello"
order = 2
sources = []

prose_hash = "sha256:3a78129bf3787f7c726e39104c95fe9bde78855c4a9f63650410c5cef9610067"
code_hash = "sha256:1ee50be729b09d1bfba27a1f994ef4d1a47c73a645764f9d5986c9bab1aecfb8"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
Viết chương trình Faber hữu ích và ngắn gọn nhất: một điểm vào gói định dạng một chuỗi rồi in chuỗi đó.

## Điều kiện tiên quyết {#prerequisites}

Trước tiên, hãy hoàn tất [Cài đặt và tải xuống](/start/install.html). Bạn cần có tệp nhị phân `faber` trong `PATH` và một shell đang ở thư mục làm việc nơi bạn có thể tạo tệp.

## Tạo một gói {#create-package}

```bash
mkdir salve-munde
cd salve-munde
mkdir src
cat > faber.toml <<'EOF'
[package]
name = "salve-munde"
version = "0.1.0"
EOF
cat > src/main.fab <<'EOF'
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
EOF
```

## Kiểm tra gói {#check}

```bash
faber check .
```

`faber check` chạy phần đầu vào của trình biên dịch: phân tích từ vựng, phân tích cú pháp, kiểm tra kiểu và hạ cấp đủ xa để phát hiện các lỗi thông thường trong gói mà không cần xây dựng tệp nhị phân gốc. Nếu lệnh thất bại, trước tiên hãy đọc mã chẩn đoán; các chẩn đoán của Faber được thiết kế để làm mã tra cứu ổn định.

## Chạy chương trình {#run}

```bash
faber run .
```

Kết quả dự kiến:

```text
Salve, munde!
```

## Những gì bạn vừa sử dụng {#what-you-used}

| Mã nguồn | Ý nghĩa |
|---|---|
| `functio salve(textus nomen) → textus` | Hàm tên `salve`, tham số theo kiểu trước, trả về văn bản |
| `fixum textus msg ← ...` | Khai báo bất biến |
| `"Salve, §!"(nomen)` | Chuỗi định dạng có nội suy giá trị hiển thị |
| `redde msg` | Trả về |
| `incipit` | Điểm vào của gói |
| `nota m` | In một giá trị ghi chú/kết quả |

## Chứng minh bản địa hóa {#locale-proof}

Chương trình trên là cách hiển thị chuẩn theo locale đọc tiếng Latinh. Các locale đọc khác có thể hiển thị cùng một chương trình ngữ nghĩa bằng các bộ từ khóa khác nhau, đồng thời giữ nguyên glyph và mã định danh. Hãy bắt đầu với phần chứng minh đầy đủ tại [Locale đọc](/features/reader-locale.html) trước khi viết các gói không dùng chữ Latinh.

## Tiếp theo {#next}

| Trước | Tiếp theo |
|---|---|
| [Cài đặt và tải xuống](/start/install.html) | [Các lệnh bạn sẽ sử dụng](/start/commands.html) |
