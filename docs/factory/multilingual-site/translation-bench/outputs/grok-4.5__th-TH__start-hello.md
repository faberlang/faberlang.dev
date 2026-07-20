เขียนโปรแกรม Faber ที่เล็กและมีประโยชน์ที่สุด: จุดเข้าแพ็กเกจที่จัดรูปแบบสตริงแล้วพิมพ์ออกมา

## Prerequisites {#prerequisites}

ทำ [Install and download](/start/install.html) ให้เสร็จก่อน คุณควรมีไบนารี `faber` บน `PATH` และมีเชลล์อยู่ในไดเรกทอรีทำงานที่สร้างไฟล์ได้

## Create a package {#create-package}

<<<FENCE 0>>>

## Check it {#check}

<<<FENCE 1>>>

`faber check` รันส่วนหน้า: การแยกเลกซีม การพาร์ส การตรวจชนิด และการลดระดับให้ไกลพอที่จะจับข้อผิดพลาดแพ็กเกจทั่วไปได้โดยไม่สร้างไบนารีเนทีฟ หากคำสั่งล้มเหลว ให้อ่านรหัสการวินิจฉัยก่อน ระบบวินิจฉัยของ Faber ออกแบบมาให้เป็นตัวจับค้นหาที่เสถียร

## Run it {#run}

<<<FENCE 2>>>

ผลลัพธ์ที่คาดหวัง:

<<<FENCE 3>>>

## What you just used {#what-you-used}

| Source | Meaning |
|---|---|
| `functio salve(textus nomen) → textus` | ฟังก์ชันชื่อ `salve` พารามิเตอร์แบบชนิดก่อน คืนค่าเป็นข้อความ |
| `fixum textus msg ← ...` | การผูกค่าแบบไม่เปลี่ยนได้ |
| `"Salve, §!"(nomen)` | สตริงจัดรูปแบบพร้อมการแทรกค่าแสดงผล |
| `redde msg` | คืนค่า |
| `incipit` | จุดเข้าแพ็กเกจ |
| `nota m` | พิมพ์ค่าโน้ต/ผลลัพธ์ |

## Locale proof {#locale-proof}

โปรแกรมด้านบนคือการเรนเดอร์สำหรับผู้อ่านแบบละตินตามมาตรฐาน โลเคลสำหรับผู้อ่านสามารถเรนเดอร์โปรแกรมเชิงความหมายเดียวกันด้วยชุดคำสำคัญที่ต่างกัน โดยยังคงไกลฟ์และตัวระบุไว้ เริ่มจากหลักฐานฉบับเต็มที่ [Reader locale](/features/reader-locale.html) ก่อนเขียนแพ็กเกจที่ไม่ใช่ละติน

## Next {#next}

| Previous | Next |
|---|---|
| [Install and download](/start/install.html) | [Commands you will use](/start/commands.html) |
