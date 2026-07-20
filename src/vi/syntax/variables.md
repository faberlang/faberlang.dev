+++
translation_kind = "translated"

title = "Variables and binding"
section = "syntax"
order = 2
sources = [
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "examples/corpus/fixum/",
  "examples/corpus/sit/",
]


prose_hash = "sha256:2e0180766e816022e87ea9eb6c8c531d30993227db9aa56c9224c9a98d3d984f"
code_hash = "sha256:122027c8f10ed33d224e3b23653279e91d19d9a17f432190340909eea5dd9ab3"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber có ba từ khóa biến và một ký hiệu gán riêng. Điểm khác biệt chính nằm giữa `fixum` (chỉ ghi một lần) và `varia` (có thể gán lại tự do), cũng như giữa `←` (luồng thực thi) và `=` (hình dạng trường mang tính cấu trúc).

## fixum — liên kết bất biến {#fixum-immutable-binding}

Các liên kết `fixum` chỉ được ghi một lần. Có thể khai báo chúng có hoặc không có trình khởi tạo; nếu khai báo mà không có trình khởi tạo, chúng phải được gán đúng một lần trước khi đọc. Lần gán thứ hai sẽ bị từ chối.

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

Khởi tạo trì hoãn:

```faber
incipit {
    fixum numerus factor
    si verum {
        factor ← 10
    } secus {
        factor ← 100
    }
    nota factor
}
```

## varia — liên kết khả biến {#varia-mutable-binding}

Các liên kết `varia` có thể được gán lại tự do:

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

## sit — cú pháp rút gọn cho liên kết bất biến suy luận kiểu {#sit-inferred-immutable-sugar}

`sit` là cú pháp rút gọn của `fixum _` — một liên kết bất biến với kiểu được suy luận:

```faber
incipit {
    sit salve ← "Salve"
    sit nomen ← "Marcus"
    sit x ← 42

    # Deferred form
    sit label
    label ← "deferred"
}
```

## Liên kết thời gian chạy và định nghĩa cấu trúc {#runtime-binding-vs-structural-definition}

Faber tách biệt hai vai trò mà hầu hết các ngôn ngữ gộp chung vào `=`:

| Ký hiệu | Vai trò | Dùng cho |
|---------|---------|----------|
| `←` | Luồng thời gian chạy | Liên kết ban đầu, gán lại, biến đổi |
| `=` | Hình dạng cấu trúc | Tên trường bên trong literal và siêu dữ liệu |

```faber
genus Point {
    numerus x
    numerus y
}

incipit {
    # Runtime: ← attaches a value to a name at execution time
    varia numerus count ← 0
    varia textus label ← "ready"
    count ← count + 1

    # Structural: = defines field values inside a type literal
    fixum _ p ← Point {
        x = 10,
        y = 20
    }
}
```

## Trích xuất trường bằng ex {#ex-field-extraction}

`ex` trích xuất các trường từ một giá trị vào các liên kết cục bộ:

```faber
genus Persona {
    textus nomen
    numerus aetas
}

incipit {
    fixum _ p ← Persona { nomen = "Marcus", aetas = 30 }
    ex p fixum nomen, aetas
    # prints "Marcus"
    nota nomen
}
```

## Tăng và giảm hậu tố {#postfix-increment-and-decrement}

`⊕` và `⊖` là các câu lệnh tăng/giảm hậu tố dành cho các vị trí `numerus` khả biến. Chúng chỉ được dùng như câu lệnh — không có giá trị biểu thức và không có dạng tiền tố:

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ⊕
    # i becomes 0
    i ⊖
}
```
