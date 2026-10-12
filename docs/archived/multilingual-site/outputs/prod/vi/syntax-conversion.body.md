Hai toán tử chuyển đổi quan trọng, một toán tử dùng khi chạy chương trình và một toán tử dùng tại thời điểm biên dịch:

<<<FENCE 0>>>

## Chuyển đổi khi chạy chương trình — ↦ {#runtime-conversion}

Dùng `↦` để chuyển đổi khi chạy chương trình, đặc biệt là khi phân tích cú pháp hoặc ép kiểu có thể thất bại. Cung cấp xử lý phục hồi nội tuyến bằng `⇥`:

<<<FENCE 1>>>

Vật chất hóa theo kiểu:

<<<FENCE 2>>>

## Gán kiểu tĩnh — ∷ {#static-ascription}

Dùng `∷` để gán kiểu tĩnh một cách tường minh. Toán tử này đặt ở hậu tố và được điều khiển bởi kiểu đích:

<<<FENCE 3>>>

## Kết hợp giá trị null — vel {#nullish-coalescing}

Dùng `vel` để kết hợp giá trị null khi một giá trị là `nihil`:

<<<FENCE 4>>>
