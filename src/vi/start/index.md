+++

title = "Bắt đầu"
section = "start"
order = 0
sources = []

translation_kind = "translated"

prose_hash = "sha256:fb813c0842ab3507898c97a7f766728b584ea8188cd53534db006768b83372ce"
code_hash = "sha256:4e3dec0ba47836476297e320d6822e4528d0f7edb88f02133372d6375d79adae"
source_commit = "6658dc687c30abd27b12dc4307f8ffef48170d46"
source_locale = "en-US"
+++
Faber Romanus do các mô hình viết, nên bạn cài đặt nó bằng cách đưa cho mô hình của bạn một liên kết.

::agent-pass::

## Mô hình của bạn làm gì {#what-your-model-does}

1. Đọc tệp sảnh tại liên kết đó, cho biết Faber là gì và mỗi bước nằm ở đâu.
2. Tải bản phát hành hiện tại cho máy của bạn và xác minh checksum.
3. Cài đặt lệnh `faber`.
4. Viết một chương trình hello nhỏ và chạy `faber check` trên đó.

Mọi việc diễn ra trên máy của bạn, và mô hình sẽ báo lại khi phép kiểm tra thành công.

## Rồi hãy nhờ nó làm gì đó {#then-ask}

Khi phép kiểm tra thành công, hãy trò chuyện với mô hình như với một đồng nghiệp. Mỗi lời nhắc bên dưới đều có nút sao chép.

Viết một chương trình và nhờ giải thích:

```text prompt
Hãy viết một chương trình Faber nhỏ in ra mười số chính phương đầu tiên. Kiểm tra bằng faber check, chạy bằng faber run, rồi giải thích cho tôi từng dòng.
```

Mang mã bạn đã có vào:

```text prompt
Tôi đã có sẵn hàm này: <dán vào đây>. Hãy dịch nó sang Faber, kiểm tra, rồi build cho Rust bằng faber build -t rust và cho tôi biết điều gì đã thay đổi.
```

Đọc bằng ngôn ngữ của bạn:

```text prompt
Hãy tạo một bản sao chương trình hello được viết bằng tiếng Việt bằng faber convert --to vi. Kiểm tra bản sao, rồi cho tôi xem cả hai phiên bản cạnh nhau.
```

Xem trình biên dịch nói gì về một lỗi:

```text prompt
Hãy cố tình làm hỏng chương trình hello bằng cách đưa vào một giá trị sai kiểu. Chạy faber check, đọc cho tôi chẩn đoán, và dùng faber explain với mã của nó để tôi hiểu ý nghĩa.
```

## Đọc kèm {#read-along}

Bạn không cần viết Faber để đọc nó. Các trang này cho thấy mô hình của bạn viết gì và vì sao nó trông như vậy.

- [Tổng quan](/en-US/language/overview.html): một chương trình thật, những gì ngôn ngữ mang lại cho bạn, và nơi nó biên dịch tới.
- [Bảng tra cứu nhanh](/en-US/cheatsheet/): các dạng của ngôn ngữ và lệnh `faber`, mỗi chủ đề một trang ngắn.
- [Thuật ngữ A–Z](/corpus/az.html): mọi từ khóa và thuật ngữ, kèm ví dụ.
- [Ngôn ngữ người đọc](/language/reader-locales.html): cùng một chương trình trong tám bề mặt ngôn ngữ.
