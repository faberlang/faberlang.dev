+++
translation_kind = "translated"

title = "Error handling"
section = "syntax"
order = 5
sources = [
  "radix/README.md (Return and Error Channels)",
  "examples/corpus/iace/",
  "examples/corpus/fac/",
  "examples/corpus/cape/",
  "radix/docs/design/failable-conversio.md",
]


prose_hash = "sha256:7b9b055ee1b8fc13b23faefb29514dd947982a0f768d911767255fdc0ee9f738"
code_hash = "sha256:81aa5174263eeb0a80a64870335680dec64748cbdb7896e4de78021d8c4f197f"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber tách biệt ba ý liên quan mà nhiều ngôn ngữ gộp vào cùng một dạng:

| Cấu trúc | Ý nghĩa |
|-----------|---------|
| `→ T` | Kênh trả về thành công thông thường |
| `T ∪ nihil` | Sự vắng mặt trong miền giá trị thành công |
| `⇥ E` | Kênh thoát thay thế có thể phục hồi dành cho lỗi |

## Trả về thông thường {#normal-return}

```faber
functio porta(numerus x) → numerus {
    si x < 0 ∴ redde 0
    redde x * 2
}
```

## Hàm có thể thất bại {#failable-functions}

Dùng `⇥` khi một hàm có thể thoát qua kênh lỗi:

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ∴ iace "division by zero"
    redde a / b
}
```

## Ném — iace {#throwing--iace}

`iace` gửi một giá trị qua kênh lỗi:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ∴ iace "negative value"
}
```

## Phục hồi — fac / cape {#recovery--fac--cape}

Bên gọi phục hồi cục bộ bằng khối `fac` và trình xử lý `cape`:

```faber
functio divide(numerus a, numerus b) → numerus {
    si b ≡ 0 {
        redde 0
    }
    redde a / b
}

functio tutum(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    }
    cape err {
        mone err
        redde 0
    }
}
```

Một lời gọi hàm có thể thất bại trực tiếp không phải là một biểu thức thông thường. Đặt lời gọi đến các hàm `→ T ⇥ E` bên trong một ranh giới `fac` / `cape` đang hoạt động.

## Phục hồi chuyển đổi nội tuyến {#inline-conversion-recovery}

`⇥` cũng có thể chỉ định một giá trị phục hồi nội tuyến trên các phép chuyển đổi `↦`:

```faber
fixum textus raw ← "42"
fixum _ n ← raw ↦ numerus ⇥ 0
```

## Hàm có thể thất bại chỉ tạo hiệu ứng {#effectonly-failable}

Đối với các hàm có lỗi nhưng không trả về giá trị thành công, hãy bỏ qua `→ T`:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ∴ iace "negative value"
}
```

## Trạng thái hiện tại {#current-status}

`→`, `redde`, `⇥`, `iace` và `fac` / `cape` là các bề mặt ngữ pháp và trình kiểm tra đang hoạt động. Việc hạ cấp cho Rust và Go đối với toàn bộ hành vi thời gian chạy của `⇥` / `iace` / `cape` vẫn còn thiếu ở phần backend — các cấu trúc này vượt qua bước kiểm tra kiểu, nhưng hiện chưa phát sinh mã thời gian chạy có thể thất bại cho tất cả các đích.
