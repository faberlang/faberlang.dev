*Ranh giới giữa Faber và mọi cách mà một hệ điều hành có thể triển khai I/O.*

`ad` là nguyên thủy gọi capability cấp thấp của Faber — ranh giới
giữa mã Faber và thế giới bên ngoài. Nó mở một cuộc hội thoại có kiểu
(`sermo`) với tài nguyên máy chủ được xác định bằng chuỗi route, sau đó
trao đổi các frame có cấu trúc (`scrinium`) qua các luồng một chiều.
Kernel máy chủ phân phối mỗi route đến một crate provider có thể cắm,
crate này triển khai I/O thực tế — hệ thống tệp, mạng, console, thời gian,
tính ngẫu nhiên hoặc bất kỳ khả năng nào khác mà hệ điều hành cung cấp.

## Nguyên thủy `ad` {#ad}

`ad` là một từ khóa, không phải một hàm. Nó mở một cuộc hội thoại
không trong suốt với route được đặt tên bằng một literal `ascii` và dữ liệu
mở tùy chọn:

<<<FENCE 0>>>

Chuỗi route tuân theo mẫu `prefix:verb`. Kernel máy chủ
chỉ đối sánh **prefix** — provider sở hữu mọi verb dưới prefix đó:

<<<FENCE 1>>>

`ad` không phải là một giao diện gọi hàm ngoại. Nó không gọi các hàm C,
không tải thư viện động và không nhúng hợp ngữ nội tuyến. Đây là một ranh
giới truyền thông điệp có cấu trúc: Faber gửi các frame có kiểu và nhận
các frame có kiểu, mà không cần biết provider được triển khai bằng Rust,
chạy trong cùng tiến trình, ủy quyền cho một system call hay chuyển tiếp
đến một máy chủ từ xa.

## Các kiểu frame {#types}

Năm kiểu do trình biên dịch sở hữu tạo thành hệ thống frame:

| Kiểu | Vai trò | Bề mặt chính |
|------|------|-------------|
| `sermo` | Tay cầm cuộc hội thoại — một trao đổi hai chiều đang diễn ra | Được tạo bởi `ad`; được rút cạn qua `↦ T` hoặc tách thành các view |
| `scrinium<T>` | Bao frame — một thông điệp có cấu trúc trong cuộc hội thoại | Các trường: `id`, `call`, `status`, `data`, `created_ms`, `from`, `trace` |
| `status` | Enum đánh dấu vòng đời | `request`, `item`, `byte`, `bulk`, `done`, `error`, `cancel` |
| `meus<T>` | Luồng một chiều gửi đi — gửi frame đến provider | `da(T)`, `fini() → status` |
| `tuus<T>` | Luồng một chiều nhận vào — nhận frame từ provider | `accipe()`, `cursor()`, `exhauri()`, `fini()` |

### Sử dụng các view định hướng {#using-directional-views}

<<<FENCE 2>>>

### Vật chất hóa đơn giản {#simple-materialization}

Với trường hợp phổ biến — mở, gửi dữ liệu mở và rút cạn tất cả frame
phản hồi thành một giá trị — `sermo ↦ T` thu gọn cuộc hội thoại:

<<<FENCE 3>>>

Việc vật chất hóa sử dụng một bộ thu định hướng theo kiểu: `↦ textus`
nối tất cả frame nhận vào, `↦ json` phân tích payload đã nối,
còn `↦ lista<T>` thu thập các frame vào một danh sách.

## Provider máy chủ {#providers}

Các nhóm hiệu ứng được triển khai dưới dạng các crate provider riêng
trong `faberlang/host-providers-rs`. Mỗi provider sở hữu mọi verb dưới
prefix của mình:

| Provider | Prefix | Miền I/O |
|----------|--------|------------|
| `solum` | `solum:*` | Hệ thống tệp: đọc, ghi, siêu dữ liệu, thao tác thư mục |
| `processus` | `processus:*` | Thực thi tiến trình: tạo, pipe, mã thoát |
| `consolum` | `consolum:*` | I/O console: stdin, stdout, stderr |
| `tempus` | `tempus:*` | Thời gian: hiện tại, ngủ, bộ định thời |
| `aleator` | `aleator:*` | Tính ngẫu nhiên: entropy, phân phối |
| `http` | `http:*` | Client HTTP (Tier D, khi được hợp nhất) |

Các provider là những crate riêng với các dependency riêng — `solum`
không kéo theo HTTP, còn `http` không kéo theo mã hệ thống tệp.
Mỗi provider xuất một hàm `register()` mà manifest máy chủ được sinh ra
sẽ gọi khi khởi động.

## Ngăn xếp lớp {#layers}

<<<FENCE 4>>>

Trình biên dịch sinh ra cơ chế phân phối tổng quát — nó không bao giờ
nhúng tên crate provider vào mã được sinh. Runtime cung cấp
`HostDispatch` và giao thức cuộc hội thoại. Kernel (từ
`host-kernel-rs`) định tuyến frame đến provider thích hợp dựa trên prefix.
Provider (từ `host-providers-rs`) thực hiện I/O thực tế.

Điều này có nghĩa là mã Faber được sinh ra **trung lập với provider**.
Cùng một binary đã biên dịch có thể liên kết với các triển khai provider
khác nhau — provider hệ thống tệp thực cho môi trường production, provider
mô phỏng cho việc kiểm thử — bằng cách thay đổi manifest biên dịch.

## Manifest biên dịch {#manifest}

Các provider cần liên kết được kiểm soát bởi manifest biên dịch được sinh
ra và bảng `[dispatch]` trong `faber.toml`:

<<<FENCE 5>>>

Trong quá trình biên soạn, provider bị thiếu sẽ tạo lỗi runtime
`E_NO_ROUTE`. Trong chế độ nghiêm ngặt (tương lai), mọi prefix `ad` trong
chương trình phải xuất hiện trong manifest biên dịch, và trình biên dịch
sẽ xác thực rằng manifest capability của provider bao phủ các route được
sử dụng.

## Kiến trúc {#architecture}

Nền tảng máy chủ được chia thành ba repository trong tổ chức
`faberlang`:

| Repository | Vai trò |
|------------|------|
| `host-kernel-rs` | Bộ định tuyến mỏng — sở hữu `Frame`, `Conversation`, vòng đời kết thúc, phân phối theo prefix, lỗi có cấu trúc (`E_NO_ROUTE`), tổng hợp manifest capability |
| `host-native-rs` | Gắn kết native — worker, hook khởi động `register_providers`, tích hợp `host_register.rs` được sinh ra |
| `host-providers-rs` | Các triển khai provider — Cargo workspace với các crate theo từng họ (`solum`, `processus`, v.v.) |

Mỗi crate provider sở hữu các dependency native của riêng mình. Provider
`http` chỉ kéo `hyper` và `tokio` khi HTTP được bật. Provider `solum`
sử dụng các API tệp tiêu chuẩn và không có thêm dependency mạng.

> **Cùng route, mọi máy chủ.** Vì `ad` phân phối dựa trên chuỗi route và provider có thể cắm, cùng một mã nguồn Faber có thể nhắm đến một binary native (`host-native-rs`), một runtime WASM (kernel máy chủ làm bộ chuyển đổi Frame/Wasm) hoặc một tiến trình TypeScript Node.js (`host-providers-ts`) mà không cần thay đổi một dòng mã Faber nào.

## Wrapper Norma {#stdlib}

Phần lớn mã Faber không gọi trực tiếp `ad`. Thư viện chuẩn Norma
bọc các route `ad` phổ biến trong các hàm có kiểu:

<<<FENCE 6>>>

Các hàm wrapper này cung cấp an toàn kiểu, tài liệu và xử lý lỗi mà không
che giấu sự thật rằng I/O đi qua ranh giới `ad`. Các wrapper Norma là mã
nguồn mở và nằm dưới `norma/src/`.

## Tài liệu tham khảo {#references}

1. `radix/docs/design/frame-stream-types.md` — đặc tả đầy đủ cho sermo, scrinium, status, meus, tuus
2. `radix/docs/design/host-provider-gateway.md` — kiến trúc bộ định tuyến mỏng, hợp đồng provider, manifest biên dịch
3. `faberlang/host-kernel-rs/` — triển khai bộ định tuyến kernel
4. `faberlang/host-native-rs/` — gắn kết và đăng ký native
5. `faberlang/host-providers-rs/` — các crate provider (solum, processus, consolum, tempus, aleator, http)
6. `examples/corpus/ad/` — các tệp ví dụ sermo
