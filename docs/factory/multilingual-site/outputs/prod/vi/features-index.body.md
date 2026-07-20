Thiết kế của Faber dựa trên ba lựa chọn tín hiệu: khai báo ưu tiên kiểu,
từ vựng hành vi bằng tiếng Latinh và các glyph cấu trúc. Những đặc điểm này
bổ trợ lẫn nhau — mỗi đặc điểm củng cố các đặc điểm còn lại để tạo ra mã
nguồn dễ đọc, dễ kiểm tra và có thể chuyển đổi giữa các luồng thực thi.

## Ngôn ngữ đọc {#reader-locale}

Trình biên dịch là bộ dịch. Các gói ngôn ngữ đọc cho phép cùng một mã nguồn
được hiển thị bằng nhiều ngôn ngữ tự nhiên mà không thay đổi ngữ nghĩa.
[Đọc thêm →](/features/reader-locale.html)

## Các luồng biên dịch {#compilation-lanes}

Faber hạ cấp qua ba biểu diễn trung gian (HIR, MIR, AIR) đến nhiều backend
đích, bao gồm runtime Rust, WASM, TypeScript, Go và GPU/WGSL.
[Đọc thêm →](/features/compilation-lanes.html)

## Từ vựng Latinh và glyph {#latin-and-glyphs}

Kiểu đứng trước tên. Các từ Latinh mang hành vi. Các glyph cấu trúc mang luồng
giá trị và hình dạng kiểu. Kết quả thể hiện ý định thay vì cơ chế.
[Đọc thêm →](/features/latin-and-glyphs.html)

## Chín điều răn {#commandments}

Chín luật thiết kế chi phối mọi quyết định về ngôn ngữ, từ lựa chọn từ khóa đến
xử lý lỗi. Đây là các tiêu chí dùng để đánh giá tính năng mới.
[Đọc thêm →](/features/commandments.html)

## Dạng chuẩn và cú pháp rút gọn {#canonical-vs-sugar}

Mọi bề mặt cú pháp rút gọn đều có một dạng khai triển chuẩn. Trình định dạng
có thể chuyển đổi qua lại giữa hai dạng. Cú pháp rút gọn là sự tiện lợi; dạng
chuẩn là hợp đồng.

[Đọc thêm →](/features/canonical-vs-sugar.html)

## Lời gọi năng lực và frame {#frames}

Nguyên thủy `ad` cung cấp cơ chế điều phối dựa trên năng lực. Các kiểu frame
xác định ranh giới I/O giữa mã Faber và các nhà cung cấp của máy chủ.
[Đọc thêm →](/features/frames.html)

## Kiểm thử nội tuyến {#testing}

Các bộ kiểm thử nằm cùng mã nguồn và sử dụng ba từ khóa:
`probandum`, `proba` và `adfirma`. Không cần tệp nhị phân kiểm thử riêng.
[Đọc thêm →](/features/testing.html)
