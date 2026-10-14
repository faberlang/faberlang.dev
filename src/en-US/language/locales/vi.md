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

Generated from the packs; read a row across to translate one term. The Latin column is the canonical name, which keys the [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          Latin        Tiếng Việt
| ---------------  -----------  -------------------
| all              omnia        tất_cả
| and              et           và
| any              quilibet     bất_kỳ
| argmax           argmaxima    argmax
| argmin           argminima    argmin
| args             argumenta    đối_số
| as               ut           như
| asc              ascendens    tăng_dần
| assert           adfirma      khẳng_định
| async            fiet         async
| async_generator  fient        async_sinh
| async_main       incipiet     bắt_đầu_bất_đồng_bộ
| async_setup      praeparabit  sẽ_chuẩn_bị
| async_teardown   postparabit  sẽ_sau_chuẩn_bị
| at               apud         tại
| await            tacebit      đợi_bỏ
| await_const      figendum     đợi_hằng
| await_var        variandum    đợi_biến
| axis             axis         trục
| before           ante         trước
| bench            metior       đo_lường
| between          inter        giữa
| break            rumpe        dừng
| call             ad           gọi
| case             casu         trường_hợp
| catch            cape         bắt
| class            genus        kiểu
| cli              cli          cli
| coalesce         vel          hoặc_nếu_rỗng
| column           columna      cột
| command          imperium     lệnh
| comptime         praefixum    tiền_tố
| const            fixum        hằng
| continue         perge        tiếp
| conversion       conversio    chuyển_đổi
| —                conversion   chuyển
| copy             exemplum     sao_chép
| count            numeratio    đếm
| cursor           cursor       con_trỏ
| debug            vide         xem
| default          ceterum      mặc_định
| desc             descendens   giảm_dần
| describe         probandum    đối_tượng_kiểm_thử
| description      descriptio   mô_tả
| do               fac          làm
| elif             sin          nếukhôngthì
| else             secus        khác
| embed            insere       nhúng
| empty            vacua        tập_rỗng
| enum             ordo         liệt_kê
| errors           errata       lỗi
| exit             exitus       thoát
| expect_failure   erratur      mong_đợi_thất_bại
| false            falsum       sai
| flaky            fragilis     mong_manh
| fn               functio      hàm
| for              itera        lặp
| format           scriptum     văn_bản_hóa
| fragment         fragment     mảnh
| from             ex           từ
| future           futura       tương_lai
| generator        fiunt        sinh
| global           ubique       toàn_cục
| guard            custodi      canh_gác
| if               si           nếu
| implements       implet       thực_thi
| import           importa      nhập
| interface        implendum    giao_ước
| internal         interna      nội_bộ
| is               est          là
| kernel           nucleum      hạt_nhân
| lambda           clausura     đóng
| lane             lane         làn
| let              sit          đặt
| line             lineam       dòng
| long             longum       dài
| main             incipit      bắt_đầu
| match            discerne     phân_tích
| max              maxima       lớn_nhất
| min              minima       nhỏ_nhất
| module           regio        vùng
| mut              in           vào
| name             nomen        tên
| nan              nonnumerus   nan
| not              non          không
| null             nulla        không_gì
| only             solum        chỉ
| only_in          solum_in     chỉ_trong
| operand          operandus    toán_hạng
| option           optio        tùy_chọn
| optional         sponte       tự_nguyện
| options          optiones     lựa_chọn
| or               aut          hoặc
| own              penes        sở_hữu
| panic            mori         chết
| pass             tacet        im_lặng
| per              pro          theo
| primus_quem      primus_quem  primus_quem
| print            nota         ghi_chú
| private          privata      riêng_tư
| product          factum       tích
| protected        protecta     bảo_vệ
| public           publica      công_khai
| radix            radix        radix
| range            ab           khoảng
| read             lege         đọc
| readonly         immutata     bất_biến
| reduce           reducta      rút_gọn
| ref              de           ra
| reject           reice        từ_chối
| rename           verte        đổi_tên
| repeat           repete       lặp_lại
| require          requirit     yêu_cầu
| rest             ceteri       còn_lại
| return           redde        trả
| return_await     reddet       đợi_trả
| schema           schema       lược_đồ
| self             ego          tôi
| setup            praepara     chuẩn_bị
| shared           commune      dùng_chung
| short            brevis       ngắn
| size             magnitudo    kích_thước
| skip             omitte       bỏ_qua
| sort             ordinata     sắp_xếp
| spread           sparge       rải
| static           generis      tĩnh
| step             per          qua
| sum              summa        tổng
| switch           elige        chọn
| tag              tag          nhãn
| teardown         postpara     sau_chuẩn_bị
| test             proba        kiểm_thử
| then             ergo         do_đó
| thread           filum        sợi
| throw            iace         ném
| throws           iacit        ném_lỗi
| timeout          temporis     thời_gian
| todo             futurum      việc_cần_làm
| trap             capta        bẫy
| true             verum        đúng
| tuple            iuncta       bộ
| type             typus        kiểu_tên
| ubi              ubi          ubi
| union            discretio    hợp_nhất
| unstable         nondum       không_ổn_định
| until            usque        tới
| var              varia        biến
| variant          finge        tạo
| vertex           vertex       đỉnh
| via              via          thông_qua
| warn             mone         cảnh_báo
| while            dum          trong_khi
| within           intra        trong
| wrapping         modulus      môđun
| write            scribe       viết
| yield            cede         nhường
```

### Types {#types}

```text locale=la
| English      Latin        Tiếng Việt
| -----------  -----------  -------------
| any          quidlibet    bất_kỳ
| ascii        ascii        ascii
| atomic       atomic       nguyên_tử
| bool         bivalens     logic
| byte         octetus      byte_đơn
| bytes        octeti       byte
| census       census       điều_tra
| channel      sermo        kênh
| char         littera      ký_tự
| clamp        clampa       kẹp_biên
| filter       filtrum      bộ_lọc
| float        fractus      thập_phân
| frame        scrinium     khung
| instant      instans      thời_điểm
| int          numerus      số
| intervallum  intervallum  miền
| iterator     cursor_t     bộ_lặp
| json         json         json
| ledger       tabulae      sổ_cái
| list         lista        danh_sách
| map          tabula       bảng
| matrix       matrix       ma_trận
| never        numquam      không_bao_giờ
| none         nihil        rỗng_ty
| object       objectum     đối_tượng
| promise      promissum    lời_hứa
| queue        queue        hàng_đợi
| record       ratio        ratio
| recv         tuus         nhận
| reflect      reflexa      phản_xạ_biên
| regex        regex        chính_quy
| saturating   saturatus    bão_hòa
| send         meus         gửi
| series       series       chuỗi
| set          copia        tập_hợp
| sparsa       sparsa       thưa
| stack        stack        ngăn_xếp
| string       textus       văn_bản
| tensor       tensor       ten_xo
| trapping     exactus      chính_xác
| unknown      ignotum      chưa_biết
| value        valor        giá_trị
| vector       vector       vectơ
| void         vacuum       trống
| wrap         involuta     vòng_biên
| wrapping_ty  modulus_t    môđun_kiểu
```

### Intrinsics {#intrinsics}

```text locale=la
| English               Latin                  Tiếng Việt
| --------------------  ---------------------  --------------------------
| abs                   absolutum              giá_trị_tuyệt_đối
| add                   adde                   thêm
| added                 addita                 đã_thêm
| added_bias            addita_bias            đã_thêm_độ_lệch
| all                   omnia                  tất_cả
| any                   quilibet               bất_kỳ
| append                appende                nối_đuôi
| apply                 applica                áp_dụng
| approx                approximata            xấp_xỉ
| argmax                argmaxima              argmax
| argmin                argminima              argmin
| at                    apud                   tại
| at_least              maxime                 ít_nhất
| at_most               minime                 nhiều_nhất
| bit_and               coniuncta              và_bit
| bit_and_assign        coniunge               và_bit_gán
| bit_or                disiuncta              hoặc_bit
| bit_or_assign         disiunge               hoặc_bit_gán
| ceiling               tectum                 làm_tròn_lên
| clamp                 coercere               giới_hạn
| compare_exchange      compare_exchange       so_sánh_và_đổi
| complement            complementa            bù
| complemented          complementata          đã_bù
| contains              continet               chứa
| cos                   cosinus                cos
| count_nonzero         nonnihil               đếm_khác_không
| create                crea                   tạo
| cross                 transversum            tích_có_hướng
| cross_entropy         crux_entropia          entropy_chéo
| cumulate              cumulata               tích_lũy
| cursor                cursor                 bộ_lặp
| delete                dele                   xóa
| densify               densata                làm_đặc
| difference            differentia            hiệu
| difference_symmetric  symmetrica             hiệu_đối_xứng
| divide                divida                 chia
| divide                divisio                phép_chia
| divided               divisa                 đã_chia
| dot                   productum              tích_vô_hướng
| drop                  omissa                 bỏ_qua
| end                   terminus               kết_thúc
| ends_with             finis                  kết_thúc_bằng
| escape                munita                 thoát_ký_tự
| exchange              exchange               đổi
| exp                   exponentia             hàm_mũ
| expanded              expande                mở_rộng
| fill                  reple                  điền
| filter                filtrata               lọc
| find                  inventa                tìm
| find_all              collecta               tìm_tất_cả
| first                 primus                 đầu_tiên
| flatten               planata                làm_phẳng
| flip                  alterna                lật
| flipped               alternata              đã_lật
| floor                 pavimentum             làm_tròn_xuống
| formata               formata                formata
| gather                gather                 thu_thập
| gelu                  gelu                   gelu
| get                   accipe                 lấy
| greater               maior                  lớn_hơn
| group                 coetus                 nhóm
| has                   habet                  có
| intersect             inter                  giao_với
| intersection          intersectio            giao
| invert                inversa                nghịch_đảo
| is_empty              vacua                  rỗng
| is_subset             subcopia               là_tập_con
| is_superset           supercopia             là_tập_cha
| keys                  claves                 khóa
| last                  ultimus                cuối_cùng
| length                longitudo              độ_dài
| less                  minor                  nhỏ_hơn
| limes                 limes                  biên
| ln                    logarithmus            lôgarit_tự_nhiên
| load                  load                   nạp
| log10                 logarithmus_decimalis  lôgarit_thập_phân
| lowercase             minuscula              chữ_thường
| map                   mappata                ánh_xạ
| matches               consentit              khớp
| materialize           materialize            hiện_thực_hóa
| matmul                matmul                 nhân_ma_trận
| maximum               maximus                lớn_nhất
| mean                  media                  trung_bình
| minimum               minimus                nhỏ_nhất
| modulo                modulata               chia_lấy_dư
| modulo_assign         modula                 chia_lấy_dư_gán
| multiplied            multiplicata           đã_nhân
| multiply              multiplica             nhân
| named                 nominatus              đặt_tên
| negate                nega                   đổi_dấu
| negated               negativa               đã_đổi_dấu
| norm_layer            laminatio              chuẩn_hóa_lớp
| norm_rms              rms_norm               rms_norm
| norm_rope             rope_norm              rope_norm
| normalize             normalizata            chuẩn_hóa
| power                 potentia               lũy_thừa
| put                   pone                   đặt
| reduce                reducta                rút_gọn
| relu                  activatio_relu         kích_hoạt_relu
| remove_first          decapita               bỏ_đầu
| remove_last           detrahe                bỏ_cuối
| replace               muta                   thay
| reshape               forma                  định_hình_lại
| reverse               inverte                đảo
| rope_half             rope_half              rope_half
| round                 rotunda                làm_tròn
| set                   ponde                  thiết_lập
| shape                 magnitudines           hình_dạng
| shift                 disloco                dịch
| shift_left            sinistra               dịch_trái
| shift_right           dextra                 dịch_phải
| shifted_left          sinistrata             đã_dịch_trái
| shifted_right         dextrata               đã_dịch_phải
| sign                  signum                 dấu
| silu                  silu                   silu
| sin                   sinus                  sin
| slice                 sectio                 cắt
| softmax               activatio_softmax      kích_hoạt_softmax
| softmax_causal        softmax_causal         kích_hoạt_softmax_nhân_quả
| sort                  ordina                 sắp_xếp
| sorted                ordinata               đã_sắp_xếp
| split                 divide                 tách
| sqrt                  radix                  căn_bậc_hai
| start                 principium             bắt_đầu
| starts_with           initium                bắt_đầu_bằng
| store                 store                  lưu
| subtract              subtrahe               trừ
| subtracted            subtracta              đã_trừ
| sum                   summa                  tổng
| swizzle               swizzle                swizzle
| take                  prima                  lấy_đầu
| take_last             ultima                 lấy_cuối
| tan                   tangens                tan
| text                  inventum               văn_bản
| transpose             transpone              chuyển_vị
| trim                  recide                 cắt_khoảng_trắng
| truncate              trunca                 cắt_bỏ
| union                 unio                   hợp
| union                 union                  hợp
| uppercase             maiuscula              chữ_hoa
| values                valores                giá_trị
```

---

[All reader locales](/language/reader-locales.html) · [Keyword reference](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
