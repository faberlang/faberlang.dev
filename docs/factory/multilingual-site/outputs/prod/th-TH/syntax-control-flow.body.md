## การแตกแขนงแบบมีเงื่อนไข {#conditional-branching}

### si / sin / secus {#si-sin-secus}

<<<FENCE 0>>>

เมื่อใช้ `else-if` และ `else`:

<<<FENCE 1>>>

### การแตกแขนงแบบกระชับด้วย ∴ {#compact-branch-with}

บล็อกของแขนงที่มีคำสั่งเดียวใช้ `∴` (หรือชื่อพ้อง `ergo`):

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

## ส่วนตรวจสอบเงื่อนไข — custodi {#guard-sections-custodi}

`custodi` ใช้จัดกลุ่มการตรวจสอบเพื่อออกจากฟังก์ชันก่อนเวลาไว้ก่อนบอดีหลักของฟังก์ชัน  
แต่ละเคลาส์ `si` คือการตรวจสอบตามลำดับ:

<<<FENCE 7>>>

ใน v1 `custodi` ไม่สามารถใช้สำหรับการหยุดลูปได้ — มันเป็นราวกั้นสำหรับการตรวจสอบ ไม่ใช่ลูป

## การจับคู่รูปแบบ — elige {#pattern-matching-elige}

`elige` เลือกแขนงแรกที่ตรงกับรูปแบบ:

<<<FENCE 8>>>

## การจับคู่ยูเนียนแบบติดแท็ก — discerne {#tagged-union-matching-discerne}

`discerne` จับคู่กับตัวแปรของ `discretio` ได้ครบทุกกรณี:

<<<FENCE 9>>>

## บล็อก Try — fac / cape {#try-blocks-fac-cape}

`fac` เปิดบล็อกที่อาจส่งข้อผิดพลาด และ `cape` ใช้กู้คืนการทำงาน:

<<<FENCE 10>>>
