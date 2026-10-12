Faber tách biệt ba ý liên quan mà nhiều ngôn ngữ gộp vào cùng một dạng:

| Cấu trúc | Ý nghĩa |
|-----------|---------|
| `→ T` | Kênh trả về thành công thông thường |
| `T ∪ nihil` | Sự vắng mặt trong miền giá trị thành công |
| `⇥ E` | Kênh thoát thay thế có thể phục hồi dành cho lỗi |

## Trả về thông thường {#normal-return}

<<<FENCE 0>>>

## Hàm có thể thất bại {#failable-functions}

Dùng `⇥` khi một hàm có thể thoát qua kênh lỗi:

<<<FENCE 1>>>

## Ném — iace {#throwing--iace}

`iace` gửi một giá trị qua kênh lỗi:

<<<FENCE 2>>>

## Phục hồi — fac / cape {#recovery--fac--cape}

Bên gọi phục hồi cục bộ bằng khối `fac` và trình xử lý `cape`:

<<<FENCE 3>>>

Một lời gọi hàm có thể thất bại trực tiếp không phải là một biểu thức thông thường. Đặt lời gọi đến các hàm `→ T ⇥ E` bên trong một ranh giới `fac` / `cape` đang hoạt động.

## Phục hồi chuyển đổi nội tuyến {#inline-conversion-recovery}

`⇥` cũng có thể chỉ định một giá trị phục hồi nội tuyến trên các phép chuyển đổi `↦`:

<<<FENCE 4>>>

## Hàm có thể thất bại chỉ tạo hiệu ứng {#effectonly-failable}

Đối với các hàm có lỗi nhưng không trả về giá trị thành công, hãy bỏ qua `→ T`:

<<<FENCE 5>>>

## Trạng thái hiện tại {#current-status}

`→`, `redde`, `⇥`, `iace` và `fac` / `cape` là các bề mặt ngữ pháp và trình kiểm tra đang hoạt động. Việc hạ cấp cho Rust và Go đối với toàn bộ hành vi thời gian chạy của `⇥` / `iace` / `cape` vẫn còn thiếu ở phần backend — các cấu trúc này vượt qua bước kiểm tra kiểu, nhưng hiện chưa phát sinh mã thời gian chạy có thể thất bại cho tất cả các đích.
