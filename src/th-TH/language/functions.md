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

ฟังก์ชันใน Faber ประกาศด้วย `functio` โดยใช้ไวยากรณ์พารามิเตอร์ที่ระบุชนิดข้อมูลก่อน และใช้ glyph สำหรับชนิดข้อมูลส่งคืน

### ไวยากรณ์พื้นฐาน {#basic-syntax}

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

### ตัวอย่าง {#examples}

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

### ค่าส่งคืน {#return-values}

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

### การยืมและความเปลี่ยนแปลงได้ (de, in, ex) {#borrowing-and-mutability}

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

### จุดเริ่มต้นโปรแกรม {#entry-point}

จุดเริ่มต้นของโปรแกรมคือ `incipit`:

```faber
incipit {
    nota "ingressus"
}
```

### จุดเริ่มต้นของ CLI {#cli-entry-point}

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

### โหมดการส่งค่า — `sponte` {#passing-mode-sponte}

`sponte` ใช้ระบุพารามิเตอร์ที่ผู้เรียกอาจละเว้นได้:

```faber
functio connect(textus host, numerus port sponte) → vacuum {
    nota host
}
```

## Control flow

### การแตกแขนงแบบมีเงื่อนไข {#conditional-branching}

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

เมื่อใช้ `else-if` และ `else`:

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

#### การแตกแขนงแบบกระชับด้วย ergo {#compact-branch-with-ergo}

บล็อกของแขนงที่มีคำสั่งเดียวใช้ `ergo`:

```faber
functio classify(numerus b, bivalens ready, numerus value) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    si ready ergo redde value
    redde nihil
}
```

### การวนซ้ำ {#iteration}

#### ค่า — itera ex {#values-itera-ex}

```faber
functio inveni(lista<numerus> items, numerus target) → numerus ∪ nihil {
    itera ex items fixum item {
        si item ≡ target ergo redde item
    }
    redde nihil
}
```

#### คีย์ — itera de {#keys-itera-de}

```faber
incipit {
    fixum _ tabula ← { "unus": 1, "duo": 2 }
    itera de tabula fixum key {
        nota key
    }
}
```

#### ช่วง — itera ab {#range-itera-ab}

```faber
itera ab 0‥10 fixum i {
    nota i
}
```

### ลูป While {#while-loops}

```faber
incipit {
    fixum _ condition ← verum
    dum condition {
        # body
        tacet
    }
}
```

### ส่วนตรวจสอบเงื่อนไข — custodi {#guard-sections-custodi}

`custodi` ใช้จัดกลุ่มการตรวจสอบเพื่อออกจากฟังก์ชันก่อนเวลาไว้ก่อนบอดีหลักของฟังก์ชัน  
แต่ละเคลาส์ `si` คือการตรวจสอบตามลำดับ:

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

ใน v1 `custodi` ไม่สามารถใช้สำหรับการหยุดลูปได้ — มันเป็นราวกั้นสำหรับการตรวจสอบ ไม่ใช่ลูป

### การจับคู่รูปแบบ — elige {#pattern-matching-elige}

`elige` เลือกแขนงแรกที่ตรงกับรูปแบบ:

```faber
functio describe(numerus value) → textus {
    elige value {
        casu 1 { redde "one" }
        casu 2 { redde "two" }
        ceterum { redde "many" }
    }
}
```

### การจับคู่ยูเนียนแบบติดแท็ก — discerne {#tagged-union-matching-discerne}

`discerne` จับคู่กับตัวแปรของ `discretio` ได้ครบทุกกรณี:

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

### บล็อก Try — fac / cape {#try-blocks-fac-cape}

`fac` เปิดบล็อกที่อาจส่งข้อผิดพลาด และ `cape` ใช้กู้คืนการทำงาน:

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

ฟังก์ชัน นามแฝงชนิดข้อมูล `genus` และ `implendum` รองรับพารามิเตอร์ชนิดข้อมูลด้วยไวยากรณ์ `<T>`

### ฟังก์ชันเจเนอริก {#generic-functions}

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

### อาร์กิวเมนต์ชนิดข้อมูลที่ระบุ ณ จุดเรียกใช้ {#explicit-callsite-type-arguments}

```faber
functio identitas<T>(T valor) → T { redde valor }

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde nihil
}

fixum _ value ← identitas<numerus>(7)
fixum _ maybe ← primum<numerus>([value])
```

### `genus` แบบเจเนอริก {#generic-genus}

```faber
genus Par<T> {
    T primus
    T secundus
}
```

### พารามิเตอร์ขนาด {#size-parameters}

`magnitudo` ใช้ประกาศพารามิเตอร์ขนาด/ดัชนีในรายการพารามิเตอร์เจเนอริก:

```faber
functio crea<T, magnitudo N>() → tensor<T, [N]> {
    redde vacua
}
```
