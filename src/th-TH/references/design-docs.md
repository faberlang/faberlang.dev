+++
translation_kind = "translated"

title = "Design documents"
section = "references"
order = 2
sources = [
  "radix/docs/design/README.md",
]


prose_hash = "sha256:c668ff445d22132defdedd2c1535366f6ce81513e0ae589bd1ab450683a06c3f"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
คลัง Radix มีเอกสารการออกแบบที่เป็นแหล่งอ้างอิงหลักเกี่ยวกับการทำงานของ Faber ในฐานะภาษาและคอมไพเลอร์ เอกสารเหล่านี้อยู่ภายใต้ `radix/docs/design/`

## ดัชนี {#index}

| ด้าน | ไฟล์ |
|------|-------|
| เป้าหมายและการลดรูป | `target-capability-matrix.md`, `lowering-routes.md`, `semantic-ownership.md` |
| ชนิดข้อมูลและไวยากรณ์ย่อ | `numeric-type-sugar.md`, `comparison-operators.md`, `annotation-sugar.md` |
| อินทรินสิกของคอลเลกชัน | `lista-intrinsics.md`, `tabula-intrinsics.md`, `tensor-intrinsics.md`, `numerus-intrinsics.md`, `fractus-intrinsics.md`, `textus-intrinsics.md`, `intervallum-intrinsics.md`, `instans-intrinsics.md`, `copia-intrinsics.md` |
| การแปลงค่า | `conversio-valor.md`, `failable-conversio.md` |
| เฟรมและเอฟเฟกต์ | `frame-stream-types.md`, `host-provider-gateway.md` |
| รีดเดอร์และรูปแบบ | `reader-locale.md`, `faber-canonical-surface.md` |
| ระบบ / AIR | `air-dialect.md`, `aiml-foundation.md`, `systems-shaped-values.md` |
| พื้นผิวเครื่องมือ | `faber-scripting.md` |
| หนี้ค้างด้านการตั้งชื่อ | `mixed-case-naming-debt.md` |

## เอกสารการออกแบบไลบรารีมาตรฐาน {#stdlib-design-docs}

ไดเรกทอรี `radix/docs/stdlib/` ประกอบด้วย:

| เอกสาร | บทบาท |
|-----|------|
| `morphologia.md` | นโยบายการผันรูปสำหรับชื่อเมธอดทั้งหมดในไลบรารีมาตรฐาน |
| `tensor-methods.md` | เอกสารอ้างอิงเมธอดของตัวรับ Tensor |
| `chorda-methods.md` | เอกสารอ้างอิงเมธอดของ Chorda (ข้อความ) |
| `mathesis-methods.md` | เอกสารอ้างอิงเมธอดทางคณิตศาสตร์ |
| `tempus-methods.md` | เอกสารอ้างอิงเมธอดด้านเวลา |
| `stdlib-mechanical-verbs.md` | นโยบายสามคำกริยา `pange`/`solve`/`tempta` |
