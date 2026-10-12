## การแตกแขนงตามเงื่อนไข {#conditional-branching}

### si / sin / secus {#si-sin-secus}

<<<FENCE 0>>>

พร้อมด้วย `else-if` และ `else`:

<<<FENCE 1>>>

### การแตกแขนงแบบกระชับด้วย ∴ {#compact-branch-with}

บอดี้ของการแตกแขนงที่มีคำสั่งเดียวใช้ `∴` (หรือชื่อพ้อง `ergo`):

<<<FENCE 2>>>

## การวนซ้ำ {#iteration}

### ค่า — itera ex {#values-itera-ex}

<<<FENCE 3>>>

### คีย์ — itera de {#keys-itera-de}

<<<FENCE 4>>>

### ช่วง — itera ab {#range-itera-ab}

<<<FENCE 5>>>

## ลูป While {#while-loops}

<<<FENCE 6>>>

## ส่วน Guard — custodi {#guard-sections-custodi}

`custodi` ใช้จัดกลุ่มการตรวจสอบเพื่อออกจากฟังก์ชันก่อนเวลาไว้ก่อนบอดี้หลักของฟังก์ชัน  
แต่ละเคลาส์ `si` คือ guard ตามลำดับ:

<<<FENCE 7>>>

ใน v1 `custodi` ไม่สามารถใช้เพื่อหยุดการวนซ้ำได้ — มันเป็นราวกั้นสำหรับตรวจสอบ ไม่ใช่ลูป

## การจับคู่รูปแบบ — elige {#pattern-matching-elige}

`elige` เลือกแขนงแรกที่ตรงกัน:

<<<FENCE 8>>>

## การจับคู่ Tagged Union — discerne {#tagged-union-matching-discerne}

`discerne` จับคู่ตัวแปรของ `discretio` ได้ครบทุกกรณี:

<<<FENCE 9>>>

## บล็อก Try — fac / cape {#try-blocks-cape}

`fac` เปิดบล็อกที่อาจทำให้เกิดข้อผิดพลาด และ `cape` ใช้กู้คืน:

<<<FENCE 10>>>
