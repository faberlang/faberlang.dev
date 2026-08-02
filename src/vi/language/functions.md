+++
translation_kind = "translated"

title = "Functions and control flow"
section = "language"
order = 3
sources = [
  "radix/README.md (Language Orientation, Borrowing and Mutability, How Faber Feels)",
  "examples/corpus/functio/",
  "examples/corpus/de/",
  "examples/corpus/in/",
  "examples/corpus/ex/",
  "radix/docs/design/semantic-ownership.md",
  "radix/README.md (Control Flow Shape, Canonical Surface)",
  "examples/corpus/si/",
  "examples/corpus/itera/",
  "examples/corpus/dum/",
  "examples/corpus/custodi/",
  "examples/corpus/discerne/",
  "examples/corpus/elige/",
  "radix/README.md (Type and Size Generics)",
  "examples/corpus/generic/",
  "examples/corpus/functio/generic-call-type-args.fab",
]
+++

## Functions

Các hàm trong Faber được khai báo bằng `functio`, sử dụng cú pháp tham số đặt kiểu trước và kiểu trả về bằng glyph.

### Cú pháp cơ bản {#basic-syntax}

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

### Ví dụ {#examples}

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

### Giá trị trả về {#return-values}

Sử dụng `redde` để trả về thông thường:

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

Dùng `redde` không kèm giá trị cho kiểu trả về `vacuum`:

```faber
functio tace() → vacuum {
    redde
}
```

### Mượn và tính khả biến (de, in, ex) {#borrowing-and-mutability}

Faber đánh dấu cách truyền một giá trị bằng các giới từ ngắn đặt trên tham số:

| Dấu | Ý nghĩa | Hạ cấp Rust điển hình |
|--------|---------|----------------------|
| *(không có)* | Giá trị sở hữu | `T` truyền theo giá trị |
| `de` | Mượn dùng chung (chỉ đọc) | `&T` |
| `in` | Mượn có thể thay đổi | `&mut T` |
| `ex` | Tiêu thụ (move vào hàm gọi) | `T` move |

```faber locale=la
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

### Điểm vào {#entry-point}

Điểm vào của chương trình là `incipit`:

```faber
incipit {
    nota "ingressus"
}
```

### Điểm vào CLI {#cli-entry-point}

Đối với các chương trình CLI, `incipit argumenta` nhận các đối số lệnh đã được phân tích:

```faber locale=la
@ cli "echo"
@ descriptio "Prints text"
@ operandus ceteri textus words
incipit argumenta args {
    itera ex args.words fixum word {
        nota word
    }
}
```

### Chế độ truyền — `sponte` {#passing-mode-sponte}

`sponte` đánh dấu một tham số có thể được lược bỏ bởi bên gọi:

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```

## Control flow

### Rẽ nhánh điều kiện {#conditional-branching}

#### si / sin / secus {#si-sin-secus}

```faber
incipit {
    fixum _ condition ← verum
    si condition {
        # truthy branch
        nota "matched"
    }
}
```

Với `else-if` và `else`:

```faber
incipit {
    fixum _ score ← 85
    si score ≥ 90 {
        nota "A"
    } sin score ≥ 80 {
        nota "B"
    } secus {
        nota "C"
    }
}
```

#### Nhánh rút gọn với ergo {#compact-branch-with-ergo}

Thân nhánh chỉ gồm một câu lệnh sử dụng `ergo`:

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    si ready ergo redde value
    redde nihil
}
```

### Lặp {#iteration}

#### Giá trị — itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ergo redde item
    }
    redde nihil
}
```

#### Khóa — itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

#### Khoảng — itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

### Vòng lặp while {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

### Khối bảo vệ — custodi {#guard-sections-custodi}

`custodi` nhóm các kiểm tra thoát sớm trước thân chính của một hàm.
Mỗi mệnh đề `si` là một điều kiện bảo vệ được kiểm tra tuần tự:

```faber
functio divide(numerus a, numerus b) → numerus {
    custodi {
        si b ≡ 0 {
            redde 0
        }
    }
    redde a / b
}
```

Trong v1, không thể dùng `break` trong `custodi` — đây là lan can bảo vệ, không phải vòng lặp.

### Đối sánh mẫu — elige {#pattern-matching-elige}

`elige` chọn nhánh khớp đầu tiên:

```faber
functio describe(numerus value) → textus {
    elige value {
        casu 1 { redde "one" }
        casu 2 { redde "two" }
        ceterum { redde "many" }
    }
}
```

### Đối sánh union có thẻ — discerne {#tagged-union-matching-discerne}

`discerne` đối sánh đầy đủ các biến thể của `discretio`:

```faber
discretio Exitus {
    Bonum { textus nuntius },
    Malum { textus causa }
}

functio refer(Exitus eventus) → textus {
    discerne eventus {
        casu Bonum fixum nuntius { redde nuntius }
        casu Malum fixum causa { redde "Error: §"(causa) }
    }
}
```

### Khối try — fac / cape {#try-blocks-fac-cape}

`fac` mở một khối có thể phát sinh lỗi, còn `cape` khôi phục khi lỗi xảy ra:

```faber
functio divide(numerus a, numerus b) → numerus {
    redde a / b
}

functio tutus(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    } cape err {
        mone err
        redde 0
    }
}
```

## Generics

Các hàm, bí danh kiểu, `genus` và `implendum` chấp nhận tham số kiểu theo cú pháp `<T>`.

### Hàm tổng quát {#generic-functions}

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

### Đối số kiểu tường minh tại vị trí gọi {#explicit-callsite-type-arguments}

```faber
functio identitas<T>(T valor) → T { redde valor }

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde nihil
}

fixum _ value ← identitas<numerus>(7)
fixum _ maybe ← primum<numerus>([value])
```

### `genus` tổng quát {#generic-genus}

```faber
genus Par<T> {
    T primus
    T secundus
}
```

### Tham số kích thước {#size-parameters}

`magnitudo` khai báo một tham số kích thước/chỉ mục trong các danh sách tham số tổng quát:

```faber
functio crea<T, magnitudo N>() → tensor<T, [N]> {
    redde vacua
}
```
