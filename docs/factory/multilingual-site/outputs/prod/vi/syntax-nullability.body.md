Faber phân biệt sự vắng mặt trong một giá trị với việc cung cấp tùy chọn tại vị trí khai báo.

## Giá trị nullable — T ∪ nihil {#nullable-values}

Dùng `T ∪ nihil` khi giá trị có thể vắng mặt:

<<<FENCE 0>>>

## Vị trí khai báo tùy chọn — sponte {#optional-declaration-slots}

Đặt `sponte` sau tên khi tham số hoặc trường có thể được lược bỏ bởi bên gọi hoặc hàm khởi tạo:

<<<FENCE 1>>>

Các dấu mượn có thể kết hợp với tham số tùy chọn:

<<<FENCE 2>>>

## Khẳng định non-null — ! {#non-null-assertion}

Dùng `!.`, `![`, `!(` để khẳng định rằng một giá trị nullable không phải là `nihil`:

<<<FENCE 3>>>

Khẳng định non-null trên `nihil` sẽ hủy thực thi tại thời điểm chạy.

## Kết hợp nullish — vel {#nullish-coalescing}

<<<FENCE 4>>>

## ignotum {#ignotum}

`ignotum` là kiểu unknown cấp cao nhất dành cho các lối thoát tạm thời và tri thức chưa hoàn chỉnh. Đây không phải là cơ chế biểu diễn tính nullable.
