+++
translation_kind = "translated"

title = "Conversion and construction"
section = "syntax"
order = 9
sources = [
  "radix/README.md (Conversion and Construction)",
  "radix/docs/design/conversio-valor.md",
  "radix/docs/design/failable-conversio.md",
]


prose_hash = "sha256:5804f612f8d3df38cbb8bf659a1e16484df7bab2c0fb0ca31f24f2281821aeb6"
code_hash = "sha256:a9b4077c5847b3cd815b5494ca2fdaed9f8eb83835307924dacd7a7fb6b72270"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Hai toán tử chuyển đổi quan trọng, một toán tử dùng khi chạy chương trình và một toán tử dùng tại thời điểm biên dịch:

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus value ← 7
fixum _ text ← value ∷ textus
```

## Chuyển đổi khi chạy chương trình — ↦ {#runtime-conversion}

Dùng `↦` để chuyển đổi khi chạy chương trình, đặc biệt là khi phân tích cú pháp hoặc ép kiểu có thể thất bại. Cung cấp xử lý phục hồi nội tuyến bằng `⇥`:

```faber
fixum textus input ← "9"
fixum _ n ← "42" ↦ numerus
fixum _ safe ← input ↦ numerus ⇥ 0
```

Vật chất hóa theo kiểu:

```faber
fixum textus path ← "/etc/hosts"
fixum _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
fixum _ body ← ad 'solum:lege' (path) ↦ textus
```

## Gán kiểu tĩnh — ∷ {#static-ascription}

Dùng `∷` để gán kiểu tĩnh một cách tường minh. Toán tử này đặt ở hậu tố và được điều khiển bởi kiểu đích:

```faber
fixum numerus value ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

## Kết hợp giá trị null — vel {#nullish-coalescing}

Dùng `vel` để kết hợp giá trị null khi một giá trị là `nihil`:

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
