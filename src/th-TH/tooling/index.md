+++
translation_kind = "translated"

title = "Tooling and compiler"
section = "tooling"
order = 0
sources = []


prose_hash = "sha256:23ae82d266e39d96b2059d2b97d4b03c5e6efcba389ab0bfb621d32a2e7caad2"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
ชุดเครื่องมือ Faber ประกอบด้วยเครื่องมือสามรายการ ได้แก่ CLI `faber` สำหรับการสร้างและทดสอบ, คอมไพเลอร์ Radix สำหรับการสร้างโค้ด และตัวจัดการแพ็กเกจ Cista สำหรับการแก้ไขการพึ่งพา

## เครื่องมือสร้าง Faber {#faber-cli}

อินเทอร์เฟซหลักสำหรับนักพัฒนา ใช้คำสั่งเดียวเพื่อสร้าง ตรวจสอบ เรียกใช้ ทดสอบ จัดรูปแบบ และอธิบายโปรเจกต์ [อ่านเพิ่มเติม →](/tooling/faber-build-tool.html)

## คอมไพเลอร์ Radix {#radix}

แบ็กเอนด์ของคอมไพเลอร์ แปลงซอร์ส Faber ผ่าน HIR → MIR → AIR ไปยังเลนเป้าหมายหลายรูปแบบ [อ่านเพิ่มเติม →](/tooling/radix-compiler.html)

## ตัวจัดการแพ็กเกจ Cista {#cista}

ใช้สำหรับแก้ไขแพ็กเกจและจัดการคลังแพ็กเกจสาธารณะ จัดการแม니เฟสต์ `faber.toml` และล็อกการพึ่งพา [อ่านเพิ่มเติม →](/tooling/cista-package-manager.html)

## เป้าหมายการสร้างโค้ด {#codegen-targets}

Faber คอมไพล์เป็น Rust (ค่าเริ่มต้น), WASM, TypeScript, Go และ GPU/WGSL  
แต่ละเลนเป้าหมายมีเส้นทาง IR และการเชื่อมโยงกับรันไทม์เป็นของตนเอง [อ่านเพิ่มเติม →](/tooling/codegen-targets.html)

## ประสิทธิภาพ {#performance}

ประสิทธิภาพของการคอมไพล์และการทำงานที่วัดได้ในแต่ละเลนเป้าหมาย [อ่านเพิ่มเติม →](/tooling/performance.html)

## การเขียนสคริปต์ {#scripting}

การใช้ Faber เป็นภาษาเขียนสคริปต์ด้วยคำสั่ง `faber run` [อ่านเพิ่มเติม →](/tooling/scripting.html)
