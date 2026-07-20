+++
translation_kind = "translated"

title = "Nullability and optionality"
section = "syntax"
order = 11
sources = [
  "radix/README.md (Nullability and Optionality)",
  "examples/corpus/nihil/",
  "examples/corpus/sponte/",
  "examples/corpus/nonnihil/",
]


prose_hash = "sha256:0bf95ac93cff7571775fd0874fcd4d1b00ce96a7a3f47f75b6da1ed1c2dd2d57"
code_hash = "sha256:08e8387c2c18e42258c69e0ff67816e5f9d187787ef444f20380f76264a4827b"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber phân biệt sự vắng mặt trong một giá trị với việc cung cấp tùy chọn tại vị trí khai báo.

## Giá trị nullable — T ∪ nihil {#nullable-values}

Dùng `T ∪ nihil` khi giá trị có thể vắng mặt:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## Vị trí khai báo tùy chọn — sponte {#optional-declaration-slots}

Đặt `sponte` sau tên khi tham số hoặc trường có thể được lược bỏ bởi bên gọi hoặc hàm khởi tạo:

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

Các dấu mượn có thể kết hợp với tham số tùy chọn:

```faber
functio process(de numerus depth sponte) → vacuum { }
```

## Khẳng định non-null — ! {#non-null-assertion}

Dùng `!.`, `![`, `!(` để khẳng định rằng một giá trị nullable không phải là `nihil`:

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

Khẳng định non-null trên `nihil` sẽ hủy thực thi tại thời điểm chạy.

## Kết hợp nullish — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

## ignotum {#ignotum}

`ignotum` là kiểu unknown cấp cao nhất dành cho các lối thoát tạm thời và tri thức chưa hoàn chỉnh. Đây không phải là cơ chế biểu diễn tính nullable.
