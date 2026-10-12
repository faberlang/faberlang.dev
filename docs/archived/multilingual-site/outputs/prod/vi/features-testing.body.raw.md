Faber có một framework kiểm thử hạng nhất được tích hợp sẵn trong ngôn ngữ, với ba từ khóa: `probandum` khai báo một nhóm kiểm thử, `proba` khai báo một ca kiểm thử đơn lẻ, và `adfirma` khẳng định một điều kiện. Các bài kiểm thử nằm trong cùng tệp với mã mà chúng kiểm thử, được chạy bằng `faber test`, và sử dụng cùng pipeline biên dịch như mã sản phẩm — nhận biết locale, kiểm tra kiểu, và hỗ trợ nhiều đích.

## Ba từ khóa {#keywords}

| Từ khóa | Vai trò | Tương đương gần đúng |
|---------|---------|----------------------|
| `probandum` | Khai báo một nhóm kiểm thử có tên | `describe`, `#[cfg(test)] mod` |
| `proba` | Khai báo một ca kiểm thử đơn lẻ | `it`, `#[test]` |
| `adfirma` | Khẳng định một điều kiện tại thời điểm chạy | `assert!`, `assert_eq!` |

### probandum — nhóm kiểm thử {#probandum-test-suite}

Một khối `probandum` nhóm các ca kiểm thử có liên quan. Các nhóm có thể lồng nhau để tổ chức kiểm thử theo cấp bậc:

<<<FENCE 0>>>

### proba — ca kiểm thử {#proba-test-case}

Một khối `proba` chứa logic kiểm thử. Khối này có thể sử dụng mọi mã Faber —
liên kết biến, lời gọi hàm, luồng điều khiển — và kết thúc bằng một hoặc nhiều
khẳng định `adfirma`. Có thể gắn thẻ cho các bài kiểm thử bằng một marker `tag`
tùy chọn để chạy có chọn lọc:

<<<FENCE 1>>>

### adfirma — khẳng định {#adfirma-assertion}

`adfirma` đánh giá một biểu thức boolean và báo lỗi nếu biểu thức đó sai.
Một chuỗi thông báo tùy chọn cung cấp ngữ cảnh khi xảy ra lỗi:

<<<FENCE 2>>>

## Quy trình {#workflow}

Các bài kiểm thử được chạy thông qua lệnh `faber test`:

<<<FENCE 3>>>

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

<<<FENCE 4>>>

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
