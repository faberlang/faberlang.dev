ติดตั้ง CLI ของ **Faber** จากรุ่นที่สร้างไว้ล่วงหน้ารุ่นปัจจุบัน ส่วนหน้าของคอมไพเลอร์รวมอยู่ภายในไบนารี `faber` แล้ว คุณไม่จำเป็นต้องติดตั้ง Radix แยกต่างหากสำหรับการทำงานกับแพ็กเกจทั่วไป

หน้านี้อ้างอิงอาร์ทิแฟกต์รุ่นรีลีสของ repository สำหรับ Faber 1.1.1 สูตรของตัวจัดการแพ็กเกจอาจเผยแพร่ตามหลังรีลีสของ repository หาก Homebrew หรือตัวจัดการแพ็กเกจอื่นรายงานเวอร์ชัน Radix/Faber ที่เก่ากว่า ให้ใช้ไฟล์เก็บถาวรด้านล่างสำหรับเส้นทางนี้

## รีลีสปัจจุบัน {#current-release}

| ฟิลด์ | ค่า |
|---|---|
| **เวอร์ชัน** | 1.1.1 |
| **แท็ก** | `faber-v1.1.1` |
| **หน้ารีลีส** | [faber-v1.1.1 บน GitHub](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1) |
| **รีลีสทั้งหมด** | [รายการรีลีสของเว็บไซต์](/history/releases.html) |
| **ใบอนุญาต** | MIT |

## ไฟล์เก็บถาวรที่สร้างไว้ล่วงหน้า {#archives}

| แพลตฟอร์ม | ดาวน์โหลด | SHA-256 |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

ไฟล์เก็บถาวรจะแตกไฟล์เป็น `faber-v1.1.1-<target-triple>/faber` ไฟล์ checksum อาจระบุพาธการสร้างเดิม ดังนั้นให้ตรวจสอบโดยเปรียบเทียบฟิลด์แฮชแรกกับไฟล์เก็บถาวรในเครื่อง แทนการพึ่งพาการจับคู่พาธของ `sha256sum -c`

### macOS arm64 {#macos}

<<<FENCE 0>>>

### Linux x64 {#linux}

<<<FENCE 1>>>

## ตรวจสอบ {#verify}

<<<FENCE 2>>>

คุณควรเห็นบรรทัดเวอร์ชันของ CLI และคำอธิบายการวินิจฉัย หากไม่พบ `faber` ให้ตรวจสอบว่าไดเรกทอรีที่มีไบนารีอยู่ใน `PATH`

## ตรวจสอบแพ็กเกจแรก {#first-package}

เมื่อ CLI อยู่ใน `PATH` แล้ว ให้โคลนตัวอย่างสาธารณะ (หรือแพ็กเกจ Faber ใดก็ได้) แล้วตรวจสอบชนิด Product packages จะแก้ไข dependency จาก Cista store ผ่าน `faber.lock`; checkout ของซอร์สในเครื่องใช้เฉพาะสำหรับการแทนที่ไลบรารีระหว่างการพัฒนาโดยระบุไว้อย่างชัดเจนเท่านั้น

<<<FENCE 3>>>

ดูแพ็กเกจเพิ่มเติมได้ที่ [ตัวอย่าง](/start/examples.html) พื้นผิวของ CLI:
[เครื่องมือสร้าง Faber](/tooling/faber-build-tool.html)

## สถานะของ Homebrew {#homebrew}

การเผยแพร่ผ่าน Homebrew ยังไม่ใช่แหล่งอ้างอิงหลักสำหรับเส้นทางเริ่มต้นนี้ หากสูตรให้บริการคอมไพเลอร์รุ่นเก่า เช่น Radix 0.38.0 ขณะที่เว็บไซต์นี้จัดทำเอกสารสำหรับ Faber 1.1.1 ให้ถือว่าสูตรดังกล่าวเผยแพร่ล่าช้า และใช้ไฟล์เก็บถาวรของรีลีสที่สร้างไว้ล่วงหน้า ประตูตรวจสอบในคอนเทนเนอร์สำหรับหน้านี้ยังคงเป็นงานคงค้างจนกว่าการเผยแพร่สูตรจะตามทัน

## สร้างจากซอร์ส {#from-source}

ไฟล์ที่สร้างไว้ล่วงหน้าเป็นเส้นทางที่แนะนำสำหรับเอเจนต์และนักพัฒนาส่วนใหญ่ การสร้างจากซอร์สต้องใช้ทรีคอมไพเลอร์ Radix แบบส่วนตัว และอยู่นอกขอบเขตของหน้านี้ ให้ใช้ไฟล์เก็บถาวรด้านบนเป็นหลัก เว้นแต่คุณกำลังทำงานกับตัวคอมไพเลอร์เอง

## เส้นทางสำหรับเอเจนต์ {#agent-path}

เอเจนต์ควรโหลดสกิล **install** และดัชนีเอเจนต์ แทนการดึงข้อมูลจาก HTML นี้:

- [`/llms.txt`](/llms.txt)
- [สกิล install](/.well-known/agent-skills/install/SKILL.md)
- [คู่มือเอเจนต์](/agents/index.md)

## ถัดไป {#next}

| ก่อนหน้า | ถัดไป |
|---|---|
| [ทัวร์ด่วน](/start/) | [สวัสดี Faber](/start/hello.html) |
