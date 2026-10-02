+++
title = "Vietnamese reader locale"
section = "locales"
order = 15
sources = [
  "radix/locale/<locale>/pack.toml",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

**Tiếng Việt** — the `vi` reader pack. Script: Latin (Vietnamese); direction: left-to-right.

| Field | Value |
|---|---|
| **Locale code** | `vi` |
| **Native name** | Tiếng Việt |
| **Script** | Latin (Vietnamese) |
| **Direction** | left-to-right |

Latin script, but not English — the control case. Heavy diacritics stress NFKC equivalence, and multi-word keywords join with underscores (`bắt_đầu`).

## English ↔ Vietnamese {#mapping}

Generated from the packs; the canonical (Latin) name keys the full [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          Tiếng Việt
| ---------------  -------------------
| all              tất_cả
| and              và
| any              bất_kỳ
| argmax           argmax
| argmin           argmin
| args             đối_số
| as               như
| assert           khẳng_định
| async            async
| async_generator  async_sinh
| async_main       bắt_đầu_bất_đồng_bộ
| async_setup      sẽ_chuẩn_bị
| async_teardown   sẽ_sau_chuẩn_bị
| at               tại
| await            đợi_bỏ
| await_const      đợi_hằng
| await_var        đợi_biến
| before           trước
| bench            đo_lường
| between          giữa
| break            dừng
| call             gọi
| case             trường_hợp
| catch            bắt
| class            kiểu
| cli              cli
| coalesce         hoặc_nếu_rỗng
| column           cột
| command          lệnh
| comptime         tiền_tố
| const            hằng
| continue         tiếp
| conversion       chuyển_đổi
| —                chuyển
| copy             sao_chép
| count            đếm
| cursor           con_trỏ
| debug            xem
| default          mặc_định
| describe         đối_tượng_kiểm_thử
| description      mô_tả
| do               làm
| elif             nếukhôngthì
| else             khác
| embed            nhúng
| empty            tập_rỗng
| enum             liệt_kê
| errors           lỗi
| exit             thoát
| expect_failure   mong_đợi_thất_bại
| false            sai
| flaky            mong_manh
| fn               hàm
| for              lặp
| format           văn_bản_hóa
| fragment         mảnh
| free             tự_do
| from             từ
| future           tương_lai
| generator        sinh
| global           toàn_cục
| guard            canh_gác
| if               nếu
| implements       thực_thi
| import           nhập
| interface        giao_ước
| internal         nội_bộ
| is               là
| kernel           hạt_nhân
| lambda           đóng
| lane             làn
| let              đặt
| line             dòng
| long             dài
| main             bắt_đầu
| match            phân_tích
| max              lớn_nhất
| min              nhỏ_nhất
| module           vùng
| mut              vào
| name             tên
| nan              nan
| nihil            rỗng
| not              không
| null             không_gì
| only             chỉ
| only_in          chỉ_trong
| operand          toán_hạng
| option           tùy_chọn
| optional         tự_nguyện
| options          lựa_chọn
| or               hoặc
| own              sở_hữu
| panic            chết
| pass             im_lặng
| per              theo
| primus_quem      primus_quem
| print            ghi_chú
| private          riêng_tư
| product          tích
| protected        bảo_vệ
| public           công_khai
| radix            radix
| range            khoảng
| read             đọc
| readonly         bất_biến
| reduce           rút_gọn
| ref              ra
| reject           từ_chối
| rename           đổi_tên
| repeat           lặp_lại
| require          yêu_cầu
| rest             còn_lại
| return           trả
| return_await     đợi_trả
| schema           lược_đồ
| self             tôi
| setup            chuẩn_bị
| shared           commune
| short            ngắn
| size             kích_thước
| skip             bỏ_qua
| spread           rải
| static           tĩnh
| step             qua
| sum              tổng
| switch           chọn
| tag              nhãn
| teardown         sau_chuẩn_bị
| test             kiểm_thử
| then             do_đó
| thread           sợi
| throw            ném
| throws           ném_lỗi
| timeout          thời_gian
| todo             việc_cần_làm
| trap             bẫy
| true             đúng
| tuple            bộ
| type             kiểu_tên
| ubi              ubi
| union            hợp_nhất
| unstable         không_ổn_định
| until            tới
| var              biến
| variant          tạo
| vertex           đỉnh
| via              thông_qua
| warn             cảnh_báo
| while            trong_khi
| within           trong
| wrapping         môđun
| write            viết
| yield            nhường
```

### Types {#types}

```text locale=la
| English      Tiếng Việt
| -----------  -------------
| any          bất_kỳ
| ascii        ascii
| atomic       nguyên_tử
| bool         logic
| byte         byte_đơn
| bytes        byte
| census       điều_tra
| channel      kênh
| char         ký_tự
| filter       bộ_lọc
| float        thập_phân
| frame        khung
| instant      thời_điểm
| int          số
| intervallum  miền
| iterator     bộ_lặp
| json         json
| list         danh_sách
| map          bảng
| matrix       ma_trận
| never        không_bao_giờ
| none         rỗng_ty
| object       đối_tượng
| promise      lời_hứa
| queue        hàng_đợi
| record       ratio
| recv         nhận
| regex        chính_quy
| saturating   bão_hòa
| send         gửi
| series       chuỗi
| set          tập_hợp
| sparsa       thưa
| stack        ngăn_xếp
| string       văn_bản
| tensor       ten_xo
| trapping     chính_xác
| unknown      chưa_biết
| value        giá_trị
| vector       vectơ
| void         trống
| wrapping_ty  môđun_kiểu
```

### Intrinsics {#intrinsics}

```text locale=la
| English               Tiếng Việt
| --------------------  -----------------
| abs                   giá_trị_tuyệt_đối
| add                   thêm
| added                 đã_thêm
| added_bias            đã_thêm_độ_lệch
| all                   tất_cả
| any                   bất_kỳ
| append                nối_đuôi
| apply                 áp_dụng
| approx                xấp_xỉ
| argmax                argmax
| argmin                argmin
| at_least              ít_nhất
| at_most               nhiều_nhất
| bit_and               và_bit
| bit_and_assign        và_bit_gán
| bit_or                hoặc_bit
| bit_or_assign         hoặc_bit_gán
| ceiling               làm_tròn_lên
| clamp                 giới_hạn
| compare_exchange      so_sánh_và_đổi
| complement            bù
| complemented          đã_bù
| contains              chứa
| cos                   cos
| create                tạo
| cross                 tích_có_hướng
| cross_entropy         entropy_chéo
| cumulate              tích_lũy
| cursor                bộ_lặp
| delete                xóa
| densify               làm_đặc
| difference            hiệu
| divide                chia
| divide                phép_chia
| divided               đã_chia
| dot                   tích_vô_hướng
| drop                  bỏ_qua
| end                   kết_thúc
| ends_with             kết_thúc_bằng
| escape                thoát_ký_tự
| exchange              đổi
| exp                   hàm_mũ
| fill                  điền
| filter                lọc
| find                  tìm
| find_all              tìm_tất_cả
| first                 đầu_tiên
| flatten               làm_phẳng
| flip                  lật
| flipped               đã_lật
| floor                 làm_tròn_xuống
| formata               formata
| from_flat             dựng_từ_phẳng
| gather                thu_thập
| gelu                  gelu
| get                   lấy
| greater               lớn_hơn
| group                 nhóm
| has                   có
| intersect             giao_với
| intersection          giao
| invert                nghịch_đảo
| is_empty              rỗng
| is_subset             là_tập_con
| is_superset           là_tập_cha
| keys                  khóa
| last                  cuối_cùng
| layer_norm            chuẩn_hóa_lớp
| length                độ_dài
| less                  nhỏ_hơn
| ln                    lôgarit_tự_nhiên
| load                  nạp
| log10                 lôgarit_thập_phân
| lowercase             chữ_thường
| map                   ánh_xạ
| matches               khớp
| materialize           hiện_thực_hóa
| matmul                nhân_ma_trận
| maximum               lớn_nhất
| mean                  trung_bình
| minimum               nhỏ_nhất
| modulo                chia_lấy_dư
| modulo_assign         chia_lấy_dư_gán
| multiplied            đã_nhân
| multiply              nhân
| named                 đặt_tên
| negate                đổi_dấu
| negated               đã_đổi_dấu
| nonzero_count         đếm_khác_không
| normalize             chuẩn_hóa
| power                 lũy_thừa
| put                   đặt
| reduce                rút_gọn
| relu                  kích_hoạt_relu
| remove_first          bỏ_đầu
| remove_last           bỏ_cuối
| replace               thay
| reshape               định_hình_lại
| reverse               đảo
| rms_norm              rms_norm
| rope_norm             rope_norm
| round                 làm_tròn
| set                   thiết_lập
| shape                 hình_dạng
| shift_left            dịch_trái
| shift_right           dịch_phải
| shifted_left          đã_dịch_trái
| shifted_right         đã_dịch_phải
| sign                  dấu
| silu                  silu
| sin                   sin
| slice                 cắt
| softmax               kích_hoạt_softmax
| sort                  sắp_xếp
| sorted                đã_sắp_xếp
| split                 tách
| sqrt                  căn_bậc_hai
| start                 bắt_đầu
| starts_with           bắt_đầu_bằng
| store                 lưu
| subtract              trừ
| subtracted            đã_trừ
| sum                   tổng
| swizzle               swizzle
| symmetric_difference  hiệu_đối_xứng
| take                  lấy_đầu
| take_last             lấy_cuối
| tan                   tan
| text                  văn_bản
| transpose             chuyển_vị
| trim                  cắt_khoảng_trắng
| truncate              cắt_bỏ
| union                 hợp
| union                 hợp
| uppercase             chữ_hoa
| values                giá_trị
```

---

[All reader locales](/language/reader-locales.html) · [Full keyword mapping](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
