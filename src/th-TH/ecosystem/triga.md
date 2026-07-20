+++
translation_kind = "translated"

title = "Triga graphics library"
section = "ecosystem"
order = 2
sources = [
  "sibling triga/ repository",
  "radix/README.md (mentions triga)",
]


prose_hash = "sha256:d2d83d9401309c449bba9b993db7ec74cdb97afc4e8cc1b2195e769c043f07a1"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Triga เป็นไลบรารีซอร์สสาธารณะเสริมสำหรับสัญญาประเภทที่เกี่ยวกับเรขาคณิต ฉาก และ GPU ในโครงการทั่วไป ให้ประกาศ Triga เป็นแพ็กเกจที่ Cista ใช้เป็นดีเพนเดนซีใน `faber.toml`; Cista จะบันทึกซอร์สที่แก้ไขแล้วลงใน `faber.lock` และคอมไพเลอร์จะค้นหาแพ็กเกจจากคลังแพ็กเกจ

เมื่อกำหนดค่า `FABER_LIBRARY_HOME` ระบบจะใช้ค่านี้เป็นตัวเลือกแทนสำหรับการพัฒนาในเครื่อง ค่านี้ไม่ใช่เส้นทางหลักสำหรับการใช้งาน Triga

Triga มีชนิดข้อมูลและการดำเนินการสำหรับ:

- พื้นฐานเรขาคณิต เช่น จุด เวกเตอร์ เมทริกซ์ และทรานส์ฟอร์ม
- โครงสร้างกราฟฉาก
- สัญญาประเภทสำหรับ GPU ที่สอดคล้องกับเลนระบบของ Faber

Triga ไม่ได้เป็นส่วนหนึ่งของ Norma แต่เป็นดีเพนเดนซีเสริมที่แพ็กเกจสามารถเลือกใช้ได้เมื่อต้องทำงานด้านกราฟิกหรือเรขาคณิต
