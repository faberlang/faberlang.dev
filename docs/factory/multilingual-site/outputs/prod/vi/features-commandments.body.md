*Chín quy tắc làm cho Faber mang đúng tinh thần Faber.*

Đây là những quy luật thiết kế định hình bản sắc của Faber. Cú pháp có thể
phát triển và tính năng có thể được bổ sung, nhưng các thay đổi phải giữ
được những nguyên tắc này. Một chương trình vi phạm chúng vẫn có thể là Faber
hợp lệ, nhưng không còn mang đúng tinh thần Faber.

Các điều răn này áp dụng ở mọi cấp độ — từ chính ngữ pháp cho đến cách đặt tên
API của thư viện chuẩn. Chúng là lý do người đọc có thể nhận ra mã nguồn Faber
chỉ qua một cái nhìn, bất kể từ khóa được hiển thị bằng ngôn ngữ tự nhiên nào
hay mã được biên dịch cho backend đích nào.

## I. Kiểu dữ liệu trước tên {#i-types-before-names}

Khai báo được đọc từ hình dạng đến liên kết. Kiểu dữ liệu đứng trước vì người
đọc cần biết *đây là loại thực thể nào* trước khi tên cho biết *đó là thực thể
nào*. Cách này phù hợp với những ngôn ngữ có trật tự ngữ pháp đi từ phạm trù
đến thể hiện — tiếng Trung, tiếng Hindi, tiếng Ả Rập — và tạo ra các khai báo
có hình thức nhất quán khi quét qua mã.

<<<FENCE 0>>>

## II. Cơ học thay vì huyền bí {#ii-mechanical-over-magical}

Cùng một cấu trúc phải có cùng ý nghĩa ở mọi nơi. Nếu người đọc cần dựa vào
ngữ cảnh ở nơi xa để biết một ký hiệu thực hiện điều gì, thì cú pháp đó đáng
ngờ. Faber ưu tiên suy luận tường minh và cục bộ — vị trí khai báo phải mang
đủ thông tin để hiểu điều gì sẽ xảy ra tại vị trí sử dụng.

<<<FENCE 1>>>

## III. Ký hiệu mang cấu trúc {#iii-glyphs-carry-structure}

Ý nghĩa cấu trúc và toán tử được biểu thị bằng ký hiệu, không phải bằng từ:
`←` cho liên kết, `→` cho kiểu trả về, `⇥` cho lối thoát khi có lỗi, `∴` cho
thân nhánh rút gọn, `≡` cho phép bằng nhau, `∪` cho kiểu hợp. Ký hiệu mang
tính phổ quát — chúng không bao giờ được bản địa hóa và không bao giờ đổi
nghĩa giữa các cách hiển thị. Người đọc tiếng Thái và người đọc tiếng Pháp
nhìn thấy cùng một ký hiệu, ngay cả khi các từ khóa xung quanh khác nhau.

## IV. Latin mang hành vi {#iv-latin-carries-behaviour}

Từ ngữ dành cho khai báo, câu lệnh, vòng đời và ý định hành vi:
`functio`, `genus`, `fixum`, `varia`, `redde`, `cape`. Các từ này có thể được
liên kết thông qua các gói ngôn ngữ của người đọc — chúng là từ vựng, không
phải ngữ pháp. Việc chọn tiếng Latin không nhằm đề cao tiếng Latin; mục đích
là chọn *một* nguồn cổ điển nhất quán để mọi từ khóa cùng thuộc một văn phong
và không từ khóa nào được ưu tiên chỉ vì đó là ngôn ngữ dùng để viết phần cài
đặt.

## V. Biến cách mang thời gian và luồng thực thi {#v-conjugation-carries-time-and-flow}

Khi cùng một logic gốc có thể chạy đồng bộ, bất đồng bộ hoặc dưới dạng
generator, dạng biến cách của động từ phải biểu thị chế độ thực thi đó. Các
cặp liên quan đến quyền sở hữu — biến đổi so với sao chép và trả ra — dùng
những dạng liên quan của cùng một gốc từ. Đây là nguyên tắc morphologia. Thư
viện chuẩn (Norma) tuân theo quy ước này cho mọi tên phương thức:
`lege` (đọc đồng bộ) so với `leget` (đọc bất đồng bộ), `adde` (biến đổi tại
chỗ) so với `addita` (trả về một bản sao mới). Trình biên dịch không áp đặt
hay tự suy ra các dạng biến cách — đây là chính sách đặt tên, không phải tính
năng ngôn ngữ.

## VI. Một ký hiệu, một nhiệm vụ {#vi-one-sign-one-job}

Một ký hiệu hoặc từ khóa có thể có các bí danh hoàn toàn tương đương, nhưng
không nên mang những ý nghĩa không liên quan. Các bí danh phải quy về một
khái niệm chuẩn duy nhất. Đây là nguyên tắc dẫn đến sự phân tách giữa `←`
(liên kết thời gian chạy) và `=` (hình dạng trường mang tính cấu trúc) trong
Faber — hầu hết ngôn ngữ gộp cả hai vào `=`, nhưng cách nạp chồng đó che khuất
việc một dòng là thao tác luồng dữ liệu hay định nghĩa ở cấp kiểu.

<<<FENCE 2>>>

## VII. Luồng thời gian chạy phải tường minh {#vii-runtime-flow-is-explicit}

Liên kết thời gian chạy, gán lại và biến đổi dùng `←`; định nghĩa cấu trúc
dùng `=`. Khi quét mã nguồn, người đọc có thể thấy ngay mọi thao tác luồng dữ
liệu: mỗi `←` là một sự kiện trong thời gian chạy. Không có sự mơ hồ cú pháp
về việc một `=` cụ thể có nghĩa là “lưu vào biến này” hay “định nghĩa trường
này”.

## VIII. Sự vắng mặt có kiểu {#viii-absence-is-typed}

Các kiểu giá trị có thể rỗng được viết dưới dạng hợp: `T ∪ nihil`. Các vị trí
khai báo tùy chọn dùng dấu đánh dấu sau tên: `sponte`. Đây là hai khái niệm
khác nhau — *một giá trị có thể vắng mặt* so với *một vị trí mà bên gọi có thể
bỏ qua* — và Faber giữ chúng tách biệt về mặt cú pháp thay vì gộp cả hai vào
`T?` hoặc `Option<T>`.

<<<FENCE 3>>>

## IX. Trình biên dịch không đoán để che giấu thông tin còn thiếu {#ix-compiler-does-not-guess}

Thông tin kiểu còn thiếu là vấn đề phân tích cần được sửa từ thượng nguồn,
không phải chi tiết sinh mã cần được che đậy. Khi thông tin thực sự không có,
trình biên dịch không bao giờ âm thầm suy ra một kiểu mà lập trình viên chưa
cung cấp — nó báo phần thiếu và dừng lại. Đây là quy tắc giữ cho Faber trung
thực: nếu người đọc không thể xác định ý nghĩa của một ký hiệu từ mã nguồn
cục bộ, trình biên dịch cũng không được giả vờ rằng nó có thể.

## Mục đích {#purpose}

Các điều răn tồn tại để trả lời một câu hỏi xuất hiện trong mọi cuộc thảo
luận về thiết kế ngôn ngữ: “Thay đổi này có còn là Faber không?” Chúng là
phép kiểm tra các bất biến — không dựa trên danh sách tính năng, mà dựa trên
bản sắc. Một thay đổi vi phạm điều răn vẫn có thể là một ý tưởng tốt, nhưng
phải được nhìn nhận là sự rời khỏi bản sắc thiết kế của Faber, thay vì một
bổ sung thông thường.

Trong thực tế, các điều răn thường được dùng làm tiêu chí xem xét cho những đề
xuất cú pháp mới. Một đề xuất làm suy yếu “kiểu dữ liệu trước tên” bằng cách
thêm lựa chọn đặt tên trước, hoặc làm mờ “một ký hiệu, một nhiệm vụ” bằng cách
nạp chồng một ký hiệu, phải giải thích vì sao Faber nên uốn cong bản sắc của
mình cho tính năng đó.
