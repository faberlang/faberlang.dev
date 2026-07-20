Faber นำ GNU coreutils กลับมาใช้งานใหม่เพื่อเป็นบทพิสูจน์ในเลนแอปพลิเคชัน โปรแกรม CLI เหล่านี้ทำงานได้จริง และแสดงให้เห็นว่า Faber สามารถสร้างไบนารีที่ทำงานร่วมกับ `argv`, `stdio`, รหัสทางออก และการทำงานกับ I/O ของโฮสต์ได้ โดยตรวจสอบความสอดคล้องกับยูทิลิตี GNU บนโฮสต์ผ่านชุดทดสอบความเท่าเทียม

## ยูทิลิตีที่พัฒนาแล้ว {#implemented-utilities}

**ขั้นที่ 1 — โครงร่างพื้นฐาน + true/false**  
`true`, `false`

**ขั้นที่ 2 — ตัวช่วยร่วมพื้นฐาน + การทดสอบแบบอินไลน์**  
`echo`, `basename`, `dirname`, `printf`, `seq`

**ขั้นที่ 3 — ส่วนย่อยของ stdin ที่อาจเป็นค่าว่าง**  
`cat`, `head`, `tail`, `wc`, `tac`, `uniq`, `fold`, `nl`, `expand`,  
`unexpand`, `sort`, `cut`, `grep`, `tr`, `tee`, `paste`

**สร้างโครงร่างแล้ว — ขั้นที่ 5 เป็นต้นไป**  
`rm`, `cp`, `mv`, `mkdir`, `touch`, `pwd`, `readlink`, `realpath`,  
`join`, `comm`, `od`, `cksum`, `split`, `yes`, `printenv`

## ตัวอย่าง — echo {#example--echo}

แพ็กเกจ `echo` แสดงรูปแบบการใช้งานของ Faber ที่ใช้ทั่วทั้ง coreutils ได้แก่ คำอธิบายประกอบ CLI การแยกวิเคราะห์ตัวเลือก การทดสอบแบบอินไลน์ด้วย `probandum`/`proba`/`adfirma` และโมดูลร่วมพื้นฐาน:

<<<FENCE 0>>>

## การเรียกใช้ {#running}

<<<FENCE 1>>>
