+++
translation_kind = "translated"

title = "Functions"
section = "syntax"
order = 3
sources = [
  "radix/README.md (Language Orientation, Borrowing and Mutability, How Faber Feels)",
  "examples/corpus/functio/",
  "examples/corpus/de/",
  "examples/corpus/in/",
  "examples/corpus/ex/",
  "radix/docs/design/semantic-ownership.md",
]


prose_hash = "sha256:ccb89a2cbb2274f10a9cf14807cb355ac88f2a65ac03fb0a5d6cea62f999df28"
code_hash = "sha256:c87e3ad8847578d6410ecd0d2147894a502f9700487a2d53bf6e86334209d5ad"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Các hàm trong Faber được khai báo bằng `functio`, sử dụng cú pháp tham số đặt kiểu trước và kiểu trả về bằng glyph.

## Cú pháp cơ bản {#basic-syntax}

```faber
functio twice(numerus n) → numerus {
    redde n
}
```

Với kênh lỗi:

```faber
functio parse(textus input) → numerus ⇥ textus {
    redde 0
}
```

## Ví dụ {#examples}

```faber
# No parameters, no return
functio saluta() {
    nota "Salve, Mundus!"
}

# Parameter, no explicit return
functio dic(textus verbum) {
    nota verbum
}

# Parameter and return type
functio duplica(numerus n) → numerus {
    redde n * 2
}

# Multiple parameters
functio adde(numerus a, numerus b) → numerus {
    redde a + b
}
```

## Giá trị trả về {#return-values}

Sử dụng `redde` để trả về thông thường:

```faber
functio porta(numerus x) → numerus {
    si x < 0 ∴ redde 0
    redde x * 2
}
```

Dùng `redde` không kèm giá trị cho kiểu trả về `vacuum`:

```faber
functio tace() → vacuum {
    redde
}
```

## Mượn và tính khả biến (de, in, ex) {#borrowing-and-mutability}

Faber đánh dấu cách truyền một giá trị bằng các giới từ ngắn đặt trên tham số:

| Dấu | Ý nghĩa | Hạ cấp Rust điển hình |
|--------|---------|----------------------|
| *(không có)* | Giá trị sở hữu | `T` truyền theo giá trị |
| `de` | Mượn dùng chung (chỉ đọc) | `&T` |
| `in` | Mượn có thể thay đổi | `&mut T` |
| `ex` | Tiêu thụ (move vào hàm gọi) | `T` move |

```faber
# Shared borrow
functio imprime(de textus label) → vacuum {
    nota label
}

# Mutable borrow
functio duplica(in numerus value) → vacuum {
    value ← value * 2
}

# Consume
functio consume(ex textus buffer) → textus {
    redde buffer
}

# Owned
functio salve(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}
```

Các từ tương tự (`de`, `ex`) cũng được dùng lại trong những cấu trúc khác — không được hiểu mọi `ex` là “tiêu thụ”:

| Cú pháp | Vai trò |
|---------|---------|
| `de textus name` trên tham số | Mượn dùng chung |
| `in numerus count` trên tham số | Mượn có thể thay đổi |
| `ex textus buffer` trên tham số | Move vào hàm gọi |
| `itera ex items fixum item` | Lặp qua các giá trị |
| `itera de tabula fixum key` | Lặp qua các khóa |
| `ex source fixum x, ceteri rest` | Phân rã các trường |
| `importa ex "path"` | Nhập từ mô-đun |

## Điểm vào {#entry-point}

Điểm vào của chương trình là `incipit`:

```faber
incipit {
    nota "ingressus"
}
```

## Điểm vào CLI {#cli-entry-point}

Đối với các chương trình CLI, `incipit argumenta` nhận các đối số lệnh đã được phân tích:

```faber
@ cli "echo"
@ descriptio "Prints text"
@ operandus ceteri textus words
incipit argumenta args {
    itera ex args.words fixum word {
        nota word
    }
}
```

## Chế độ truyền — `sponte` {#passing-mode-sponte}

`sponte` đánh dấu một tham số có thể được lược bỏ bởi bên gọi:

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```
