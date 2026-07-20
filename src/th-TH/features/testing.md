+++
translation_kind = "translated"

title = "Inline testing"
section = "features"
order = 7
sources = []


prose_hash = "sha256:85bf7bf8e3bbf81859e9163f3f1898d0a41aa347101b4ea5a299599abf47f756"
code_hash = "sha256:5c17d1f1d1850fa59128bd6e4a57dce82f2b3ef4be816ff3f5d7275481335af9"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
Faber มีเฟรมเวิร์กการทดสอบแบบมากับภาษาโดยตรง โดยมีคีย์เวิร์ดสามคำ ได้แก่ `probandum` สำหรับประกาศชุดทดสอบ, `proba` สำหรับประกาศกรณีทดสอบแต่ละกรณี และ `adfirma` สำหรับยืนยันเงื่อนไข การทดสอบจะอยู่ในไฟล์เดียวกับโค้ดที่ต้องการทดสอบ ทำงานผ่าน `faber test` และรองรับไปป์ไลน์คอมไพเลอร์เดียวกับโค้ดสำหรับการใช้งานจริง ทั้งการรองรับโลแคล การตรวจสอบชนิดข้อมูล และหลายเป้าหมายการคอมไพล์

## คีย์เวิร์ดทั้งสามคำ {#keywords}

| คีย์เวิร์ด | หน้าที่ | คำเทียบเคียงโดยประมาณ |
|---------|------|------------------------|
| `probandum` | ประกาศชุดทดสอบที่มีชื่อ | `describe`, `#[cfg(test)] mod` |
| `proba` | ประกาศกรณีทดสอบแต่ละกรณี | `it`, `#[test]` |
| `adfirma` | ยืนยันเงื่อนไขขณะรันไทม์ | `assert!`, `assert_eq!` |

### probandum — ชุดทดสอบ {#probandum-test-suite}

บล็อก `probandum` ใช้จัดกลุ่มกรณีทดสอบที่เกี่ยวข้องกัน ชุดทดสอบสามารถซ้อนกันได้เพื่อจัดระเบียบการทดสอบเป็นลำดับชั้น:

```faber
probandum "arithmetica" {
    proba "unum plus unum" {
        adfirma 1 + 1 ≡ 2
    }

    proba "multiplicatio" {
        adfirma 3 * 4 ≡ 12
    }

    probandum "implicata" {
        proba "comparatio" {
            fixum _ x ← 10
            adfirma x ≥ 10
        }
    }
}
```

### proba — กรณีทดสอบ {#proba-test-case}

บล็อก `proba` บรรจุตรรกะของการทดสอบ โดยใช้โค้ด Faber ใดก็ได้ เช่น การผูกตัวแปร การเรียกฟังก์ชัน และการควบคุมลำดับการทำงาน จากนั้นจบด้วยการยืนยันด้วย `adfirma` อย่างน้อยหนึ่งรายการ การทดสอบสามารถกำกับด้วยมาร์กเกอร์ `tag` ที่เป็นตัวเลือก เพื่อเรียกใช้งานเฉพาะบางรายการ:

```text
proba "echo formats operands with one space" tag "coreutils" {
    adfirma echo_textus(["hello", "world"]) ≡ "hello world"
}
```

### adfirma — การยืนยัน {#adfirma-assertion}

`adfirma` จะประเมินนิพจน์บูลีน และรายงานความล้มเหลวหากผลลัพธ์เป็นเท็จ สามารถระบุสตริงข้อความเพิ่มเติมเพื่อให้บริบทเมื่อเกิดความล้มเหลวได้:

```faber
incipit {
    fixum _ x ← 10

    # Simple assertion
    adfirma x > 0

    # With custom message
    adfirma x ≡ 10, "x decem esse debet"

    # Multiple assertions in sequence
    fixum _ nomen ← "Marcus"
    adfirma nomen ≡ "Marcus"
    adfirma nomen ≠ "", "nomen vacuum non sit"
}
```

## เวิร์กโฟลว์ {#workflow}

การทดสอบทำงานผ่านคำสั่ง `faber test`:

```text
faber test                        # run all tests in the current package
faber test examples/coreutils/packages/echo  # run tests for a specific package
```

เนื่องจากการทดสอบอยู่ร่วมกับซอร์สโค้ดในไฟล์ `.fab` เดียวกัน จึงไม่ต้องมีโครงสร้างไดเรกทอรีทดสอบแยกต่างหาก ไม่ต้องประกาศโมดูลทดสอบ และไม่มีความแตกต่างของสคริปต์การบิลด์ระหว่างบิลด์สำหรับการทดสอบกับบิลด์สำหรับการใช้งานจริง คอมไพเลอร์จะแยกได้ว่าบล็อกใดเป็นโค้ดทดสอบและบล็อกใดเป็นโค้ดสำหรับการใช้งานจริงจากคีย์เวิร์ดที่ใช้ — `probandum` และ `proba` จะถูกพาร์ส แต่จะถูกตัดออกจากบิลด์สำหรับการใช้งานจริง

## ตัวอย่างการใช้งานจริง {#real-world}

แพ็กเกจ `echo` ใน coreutils แสดงการใช้งานเฟรมเวิร์กการทดสอบในทางปฏิบัติ การทดสอบอยู่ในไฟล์เดียวกับส่วนการทำงานจริง และครอบคลุมการพาร์สออปชัน การขยายเอสเคป และกรณีขอบ:

```text
probandum "echo formatting" tag "coreutils" {
    proba "empty operands format as empty text" {
        fixum lista<textus> words ← vacua
        adfirma echo_textus(words) ≡ ""
    }

    proba "single operand is unchanged" {
        adfirma echo_textus(["hello"]) ≡ "hello"
    }

    proba "-E is a leading no-op option" {
        adfirma echo_textus(["-E", "hello", "world"]) ≡ "hello world"
    }

    proba "-n suppresses the trailing newline flag" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }

    proba "-e expands the declared escape subset" {
        adfirma echo_textus(["-e", "a\\nb"]) ≡ "a\nb"
        adfirma echo_textus(["-e", "a\\tb"]) ≡ "a\tb"
    }
}
```

## หมายเหตุด้านการออกแบบ {#design}

ตัวเลือกด้านการออกแบบหลายประการทำให้เฟรมเวิร์กการทดสอบของ Faber แตกต่างจากแนวทางทั่วไป:

- **ไม่มีไบนารีทดสอบแยกต่างหาก** การทดสอบเป็นการประกาศในไฟล์ซอร์สเดียวกัน ไม่ใช่เป้าหมายการคอมไพล์แยกต่างหาก คอมไพเลอร์จะกรองบล็อกการทดสอบออกจากเอาต์พุตสำหรับการใช้งานจริง
- **ใช้แท็กแทนไดเรกทอรี** การทดสอบจัดระเบียบด้วยมาร์กเกอร์ `tag` แทนโครงสร้างไดเรกทอรี การทดสอบหนึ่งรายการจึงสังกัดแกนการจัดระเบียบได้หลายแบบโดยไม่ต้องย้ายตำแหน่ง
- **ใช้ไปป์ไลน์คอมไพเลอร์เต็มรูปแบบ** การทดสอบจะถูกตรวจสอบชนิดข้อมูล วิเคราะห์ และรองรับโลแคล เช่นเดียวกับโค้ดส่วนอื่น — แฟล็ก `--reader-locale` เดียวกันนี้ใช้กับเอาต์พุตการทดสอบ
- **รองรับหลายเป้าหมาย** การทดสอบทำงานผ่านแบ็กเอนด์ที่แพ็กเกจเลือกใช้ — MIR stepper สำหรับ `faber test --interpret` และ Rust ที่คอมไพล์แล้วสำหรับ `faber test`
- **ชุดทดสอบซ้อนกันได้** บล็อก `probandum` สามารถซ้อนกันได้ เพื่อสะท้อนโครงสร้างของโค้ดที่กำลังทดสอบ

## แหล่งอ้างอิง {#references}

1. `examples/corpus/probandum/` — ไฟล์ตัวอย่างของ probandum
2. `examples/corpus/proba/` — ไฟล์ตัวอย่างของ proba
3. `examples/corpus/adfirma/` — ไฟล์ตัวอย่างของ adfirma
4. `examples/coreutils/packages/echo/src/main.fab` — การใช้งานจริงพร้อมแท็ก
