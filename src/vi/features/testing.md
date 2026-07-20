+++
translation_kind = "translated"

title = "Inline testing"
section = "features"
order = 7
sources = []


prose_hash = "sha256:85bf7bf8e3bbf81859e9163f3f1898d0a41aa347101b4ea5a299599abf47f756"
code_hash = "sha256:5c17d1f1d1850fa59128bd6e4a57dce82f2b3ef4be816ff3f5d7275481335af9"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
Faber có một framework kiểm thử hạng nhất được tích hợp sẵn trong ngôn ngữ, với ba từ khóa: `probandum` khai báo một nhóm kiểm thử, `proba` khai báo một ca kiểm thử đơn lẻ, và `adfirma` khẳng định một điều kiện. Các bài kiểm thử nằm trong cùng tệp với mã mà chúng kiểm thử, được chạy bằng `faber test`, và sử dụng cùng pipeline biên dịch như mã sản phẩm — nhận biết locale, kiểm tra kiểu, và hỗ trợ nhiều đích.

## Ba từ khóa {#keywords}

| Từ khóa | Vai trò | Tương đương gần đúng |
|---------|---------|----------------------|
| `probandum` | Khai báo một nhóm kiểm thử có tên | `describe`, `#[cfg(test)] mod` |
| `proba` | Khai báo một ca kiểm thử đơn lẻ | `it`, `#[test]` |
| `adfirma` | Khẳng định một điều kiện tại thời điểm chạy | `assert!`, `assert_eq!` |

### probandum — nhóm kiểm thử {#probandum-test-suite}

Một khối `probandum` nhóm các ca kiểm thử có liên quan. Các nhóm có thể lồng nhau để tổ chức kiểm thử theo cấp bậc:

```faber
probandum "arithmetica" {
    proba "unum plus unum" {
        adfirma 1 + 1 ≡ 2
    }

    proba "multiplicatio" {
        adfirma 3 * 4 ≡ 12
    }

    probandum "implicata" {
        proba "comparatio" {
            fixum _ x ← 10
            adfirma x ≥ 10
        }
    }
}
```

### proba — ca kiểm thử {#proba-test-case}

Một khối `proba` chứa logic kiểm thử. Khối này có thể sử dụng mọi mã Faber —
liên kết biến, lời gọi hàm, luồng điều khiển — và kết thúc bằng một hoặc nhiều
khẳng định `adfirma`. Có thể gắn thẻ cho các bài kiểm thử bằng một marker `tag`
tùy chọn để chạy có chọn lọc:

```text
proba "echo formats operands with one space" tag "coreutils" {
    adfirma echo_textus(["hello", "world"]) ≡ "hello world"
}
```

### adfirma — khẳng định {#adfirma-assertion}

`adfirma` đánh giá một biểu thức boolean và báo lỗi nếu biểu thức đó sai.
Một chuỗi thông báo tùy chọn cung cấp ngữ cảnh khi xảy ra lỗi:

```faber
incipit {
    fixum _ x ← 10

    # Simple assertion
    adfirma x > 0

    # With custom message
    adfirma x ≡ 10, "x decem esse debet"

    # Multiple assertions in sequence
    fixum _ nomen ← "Marcus"
    adfirma nomen ≡ "Marcus"
    adfirma nomen ≠ "", "nomen vacuum non sit"
}
```

## Quy trình {#workflow}

Các bài kiểm thử được chạy thông qua lệnh `faber test`:

```text
faber test                        # run all tests in the current package
faber test examples/coreutils/packages/echo  # run tests for a specific package
```

Vì các bài kiểm thử nằm cạnh mã nguồn trong cùng tệp `.fab`, nên không có cấu trúc
thư mục kiểm thử riêng, không cần khai báo module kiểm thử, và cũng không có sự
khác biệt trong script build giữa bản build kiểm thử và bản build sản phẩm. Trình
biên dịch nhận biết khối nào là mã kiểm thử và khối nào là mã sản phẩm dựa trên
các từ khóa được sử dụng — `probandum` và `proba` được phân tích cú pháp nhưng
được loại khỏi các bản build sản phẩm.

## Ví dụ thực tế {#real-world}

Gói coreutils `echo` minh họa framework kiểm thử trong thực tế.
Các bài kiểm thử nằm trong cùng tệp với phần triển khai, bao phủ việc phân tích
tùy chọn, mở rộng escape và các trường hợp biên:

```text
probandum "echo formatting" tag "coreutils" {
    proba "empty operands format as empty text" {
        fixum lista<textus> words ← vacua
        adfirma echo_textus(words) ≡ ""
    }

    proba "single operand is unchanged" {
        adfirma echo_textus(["hello"]) ≡ "hello"
    }

    proba "-E is a leading no-op option" {
        adfirma echo_textus(["-E", "hello", "world"]) ≡ "hello world"
    }

    proba "-n suppresses the trailing newline flag" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }

    proba "-e expands the declared escape subset" {
        adfirma echo_textus(["-e", "a\\nb"]) ≡ "a\nb"
        adfirma echo_textus(["-e", "a\\tb"]) ≡ "a\tb"
    }
}
```

## Ghi chú thiết kế {#design}

Một số lựa chọn thiết kế làm framework kiểm thử của Faber khác với các phương pháp
thông thường:

- **Không có binary kiểm thử riêng.** Bài kiểm thử là các khai báo trong cùng tệp nguồn, không phải một đích biên dịch riêng. Trình biên dịch lọc các khối kiểm thử khỏi đầu ra sản phẩm.
- **Dùng thẻ, không dùng thư mục.** Bài kiểm thử được tổ chức bằng các marker `tag` thay vì cấu trúc thư mục. Một bài kiểm thử có thể thuộc nhiều trục tổ chức mà không cần di chuyển.
- **Đầy đủ pipeline biên dịch.** Bài kiểm thử được kiểm tra kiểu, phân tích và nhận biết locale — cùng cờ `--reader-locale` cũng áp dụng cho đầu ra kiểm thử.
- **Nhiều đích.** Bài kiểm thử chạy qua backend mà gói nhắm tới — bộ bước MIR cho `faber test --interpret`, Rust đã biên dịch cho `faber test`.
- **Nhóm lồng nhau.** Các khối `probandum` có thể lồng nhau, phản ánh cấu trúc của mã mà chúng kiểm thử.

## Tham khảo {#references}

1. `examples/corpus/probandum/` — các tệp ví dụ `probandum`
2. `examples/corpus/proba/` — các tệp ví dụ `proba`
3. `examples/corpus/adfirma/` — các tệp ví dụ `adfirma`
4. `examples/coreutils/packages/echo/src/main.fab` — cách sử dụng thực tế với các thẻ
