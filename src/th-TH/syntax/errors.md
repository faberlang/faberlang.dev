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
Faber แยกแนวคิดที่เกี่ยวข้องกันสามอย่าง ซึ่งในหลายภาษาถูกรวมเป็นรูปแบบเดียวกัน:

| โครงสร้าง | ความหมาย |
|-----------|---------|
| `→ T` | ช่องทางคืนค่าความสำเร็จตามปกติ |
| `T ∪ nihil` | การไม่มีค่าในโดเมนค่าความสำเร็จ |
| `⇥ E` | ช่องทางออกทางเลือกสำหรับข้อผิดพลาดที่กู้คืนได้ |

## การคืนค่าตามปกติ {#normal-return}

```faber
functio porta(numerus x) → numerus {
    si x < 0 ∴ redde 0
    redde x * 2
}
```

## ฟังก์ชันที่อาจล้มเหลว {#failable-functions}

ใช้ `⇥` เมื่อฟังก์ชันสามารถออกผ่านช่องทางข้อผิดพลาดได้:

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ∴ iace "division by zero"
    redde a / b
}
```

## การโยนข้อผิดพลาด — iace {#throwing--iace}

`iace` ส่งค่าผ่านช่องทางข้อผิดพลาด:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ∴ iace "negative value"
}
```

## การกู้คืน — fac / cape {#recovery--fac--cape}

ผู้เรียกสามารถกู้คืนภายในบริบทได้ด้วยบล็อก `fac` และตัวจัดการ `cape`:

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

การเรียกฟังก์ชันที่อาจล้มเหลวโดยตรงไม่ใช่นิพจน์ทั่วไป ให้วางการเรียกฟังก์ชัน `→ T ⇥ E` ไว้ภายในขอบเขต `fac` / `cape` ที่กำลังทำงานอยู่

## การกู้คืนจากการแปลงแบบแทรกในบรรทัด {#inline-conversion-recovery}

นอกจากนี้ `⇥` ยังใช้ระบุค่าการกู้คืนแบบแทรกในบรรทัดสำหรับการแปลง `↦` ได้:

```faber
fixum textus raw ← "42"
fixum _ n ← raw ↦ numerus ⇥ 0
```

## ฟังก์ชันที่อาจล้มเหลวและมีเฉพาะผลข้างเคียง {#effectonly-failable}

สำหรับฟังก์ชันที่เกิดข้อผิดพลาดแต่ไม่คืนค่าความสำเร็จ ให้ละเว้น `→ T`:

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ∴ iace "negative value"
}
```

## สถานะปัจจุบัน {#current-status}

`→`, `redde`, `⇥`, `iace` และ `fac` / `cape` เป็นไวยากรณ์และพื้นผิวของตัวตรวจสอบที่ใช้งานได้แล้ว การลดรูปไปยัง Rust และ Go สำหรับพฤติกรรมรันไทม์ของ `⇥` / `iace` / `cape` แบบเต็มรูปแบบยังเป็นช่องว่างของแบ็กเอนด์อยู่ — โค้ดเหล่านี้ผ่านการตรวจสอบชนิด แต่ยังไม่สร้างโค้ดรันไทม์ที่อาจล้มเหลวสำหรับทุกเป้าหมาย
