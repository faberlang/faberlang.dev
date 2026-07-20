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
ฟังก์ชันใน Faber ประกาศด้วย `functio` โดยใช้ไวยากรณ์พารามิเตอร์ที่ระบุชนิดข้อมูลก่อน และใช้ glyph สำหรับชนิดข้อมูลส่งคืน

## ไวยากรณ์พื้นฐาน {#basic-syntax}

```faber
functio twice(numerus n) → numerus {
    redde n
}
```

พร้อมช่องทางรายงานข้อผิดพลาด:

```faber
functio parse(textus input) → numerus ⇥ textus {
    redde 0
}
```

## ตัวอย่าง {#examples}

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

## ค่าส่งคืน {#return-values}

ใช้ `redde` สำหรับการส่งคืนตามปกติ:

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

ใช้ `redde` โดยไม่ระบุค่า เมื่อชนิดข้อมูลส่งคืนเป็น `vacuum`:

```faber
functio tace() → vacuum {
    redde
}
```

## การยืมและความเปลี่ยนแปลงได้ (de, in, ex) {#borrowing-and-mutability}

Faber ระบุวิธีส่งค่าด้วยคำบุพบทสั้น ๆ บนพารามิเตอร์:

| เครื่องหมาย | ความหมาย | การแปลงเป็น Rust โดยทั่วไป |
|--------|---------|----------------------|
| *(ไม่มี)* | ค่าที่เป็นเจ้าของ | `T` แบบส่งด้วยค่า |
| `de` | การยืมร่วม (อ่านอย่างเดียว) | `&T` |
| `in` | การยืมที่เปลี่ยนแปลงได้ | `&mut T` |
| `ex` | การใช้จนหมด (ย้ายค่าเข้า callee) | `T` แบบย้ายค่า |

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

คำเดียวกัน (`de`, `ex`) ยังถูกใช้ซ้ำในโครงสร้างอื่นด้วย อย่าตีความ `ex` ทุกแห่งว่าแปลว่า “ใช้จนหมด”:

| รูปแบบ | บทบาท |
|---------|------|
| `de textus name` บนพารามิเตอร์ | การยืมร่วม |
| `in numerus count` บนพารามิเตอร์ | การยืมที่เปลี่ยนแปลงได้ |
| `ex textus buffer` บนพารามิเตอร์ | การย้ายค่าเข้า callee |
| `itera ex items fixum item` | วนซ้ำค่าต่าง ๆ |
| `itera de tabula fixum key` | วนซ้ำคีย์ |
| `ex source fixum x, ceteri rest` | แยกโครงสร้างฟิลด์ |
| `importa ex "path"` | นำเข้าจากโมดูล |

## จุดเริ่มต้นโปรแกรม {#entry-point}

จุดเริ่มต้นของโปรแกรมคือ `incipit`:

```faber
incipit {
    nota "ingressus"
}
```

## จุดเริ่มต้นของ CLI {#cli-entry-point}

สำหรับโปรแกรม CLI, `incipit argumenta` จะรับอาร์กิวเมนต์คำสั่งที่แยกวิเคราะห์แล้ว:

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

## โหมดการส่งค่า — `sponte` {#passing-mode-sponte}

`sponte` ใช้ระบุพารามิเตอร์ที่ผู้เรียกอาจละเว้นได้:

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```
