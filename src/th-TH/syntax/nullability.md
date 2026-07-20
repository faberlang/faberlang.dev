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
Faber แยกความแตกต่างระหว่างการไม่มีค่าในค่าหนึ่ง กับการระบุให้เป็นทางเลือก ณ จุดประกาศ

## ค่าที่อาจไม่มีค่า — T ∪ nihil {#nullable-values}

ใช้ `T ∪ nihil` เมื่อค่านั้นอาจไม่มีค่า:

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## ช่องประกาศที่เป็นทางเลือก — sponte {#optional-declaration-slots}

ใช้ `sponte` ต่อท้ายชื่อ เมื่อผู้เรียกใช้หรือคอนสตรักเตอร์อาจละเว้นพารามิเตอร์หรือฟิลด์นั้น:

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

เครื่องหมายการยืมสามารถใช้ร่วมกับพารามิเตอร์ที่เป็นทางเลือกได้:

```faber
functio process(de numerus depth sponte) → vacuum { }
```

## การยืนยันว่าไม่เป็นค่าว่าง — ! {#non-null-assertion}

ใช้ `!.`, `![`, `!(` เพื่อยืนยันว่าค่าที่อาจไม่มีค่าไม่ใช่ `nihil`:

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

การยืนยันว่าไม่เป็นค่าว่างกับ `nihil` จะยุติการทำงานขณะรันไทม์

## การรวมค่าเมื่อเป็นค่าว่าง — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

## ignotum {#ignotum}

`ignotum` คือชนิดข้อมูลไม่ทราบค่าระดับบนสุดสำหรับทางออกชั่วคราวและกรณีที่ความรู้ยังไม่สมบูรณ์ ไม่ใช่กลไกสำหรับค่าที่อาจเป็นค่าว่าง
