+++
title = "ติดตั้งและดาวน์โหลด"
section = "install"
order = 1
sources = []
translation_kind = "translated"


prose_hash = "sha256:662becbb3dd5349058bcdfec9219fd07f6fe4217c2e5115c0aade45e0f17f0d4"
code_hash = "sha256:cc9de43077b1262ee3d9edfbd3bd56c4ae51bcca18d0316fa0bb95312f3033b7"
source_commit = "ee93015caac71f7b89ddef8d9010ffbe22d6cd7e"
source_locale = "en-US"
+++
ติดตั้ง CLI ของ **Faber** จากรุ่นที่คอมไพล์ไว้ล่วงหน้าปัจจุบัน ฟรอนต์เอนด์ของคอมไพเลอร์มาพร้อมกับไบนารี `faber` คุณไม่จำเป็นต้องติดตั้ง Radix แยกต่างหากสำหรับงานแพ็กเกจทั่วไป

หน้านี้เขียนตามสิ่งประดิษฐ์รุ่นจาก Repository สำหรับ Faber 1.1.1 สูตรของ Package Manager อาจล้าหลังกว่ารุ่นใน Repository ถ้า Homebrew หรือตัวจัดการอื่นรายงานเวอร์ชัน Radix/Faber ที่เก่ากว่า ให้ใช้ไฟล์เก็บถาวรด้านล่างสำหรับแทร็กนี้

## รุ่นปัจจุบัน {#current-release}

| ฟิลด์ | ค่า |
|---|---|
| **เวอร์ชัน** | 1.1.1 |
| **แท็ก** | `faber-v1.1.1` |
| **หน้ารุ่น** | [faber-v1.1.1 on GitHub](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1) |
| **ทุกรุ่น** | [Site releases inventory](/history/releases.html) |
| **สัญญาอนุญาต** | MIT |

## ไฟล์เก็บสำเร็จรูป {#archives}

| แพลตฟอร์ม | ดาวน์โหลด | SHA-256 |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

ไฟล์เก็บถาวรจะแตกไปที่ `faber-v1.1.1-<target-triple>/faber` ไฟล์ Checksum อาจระบุพาธบิวด์ดั้งเดิม ดังนั้นให้ตรวจสอบโดยเปรียบเทียบฟิลด์แฮชแรกกับไฟล์เก็บถาวรในเครื่องแทนที่จะพึ่งพาการจับคู่พาธของ `sha256sum -c`

### macOS arm64 {#macos}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
# place on PATH, e.g.:
sudo mv faber-v1.1.1-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

### Linux x64 {#linux}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(sha256sum faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.1.1-x86_64-unknown-linux-gnu/faber /usr/local/bin/
faber --version
```

## ตรวจสอบ {#verify}

```bash
faber --version
faber explain SEM001
```

คุณควรเห็นบรรทัดเวอร์ชันของ CLI และคำอธิบายการวินิจฉัย ถ้าไม่พบ `faber` ให้ตรวจสอบว่าไดเรกทอรีที่มีไบนารีนั้นอยู่ใน `PATH`

## ตรวจแพ็กเกจครั้งแรก {#first-package}

เมื่อ CLI อยู่ใน `PATH` แล้ว ให้โคลนตัวอย่างสาธารณะ (หรือแพ็กเกจ Faber ใดๆ) และตรวจสอบชนิด แพ็กเกจผลิตภัณฑ์จะแก้ไขการพึ่งพาจาก Cista store ผ่าน `faber.lock` การเช็คเอาต์ซอร์สในเครื่องมีไว้สำหรับการแทนที่การพัฒนาไลบรารีอย่างชัดเจนเท่านั้น

```bash
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

แพ็กเกจเพิ่มเติม: [Examples](/start/examples.html) พื้นผิว CLI: [Faber build tool](/tooling/faber-build-tool.html)

## สถานะ Homebrew {#homebrew}

Homebrew publication ยังไม่เป็นผู้มีอำนาจสำหรับแทร็กเริ่มต้นนี้ ถ้าสูตรให้บริการคอมไพเลอร์รุ่นเก่าอย่าง Radix 0.38.0 ในขณะที่ไซต์นี้จัดทำเอกสาร Faber 1.1.1 ให้ถือว่าสูตรนั้นล้าหลังและใช้ไฟล์เก็บถาวรรุ่นที่คอมไพล์ไว้ล่วงหน้า ประตูตรวจสอบคอนเทนเนอร์สำหรับหน้านี้ยังคงเป็นสิ่งตกค้างจนกว่าการเผยแพร่สูตรจะตามทัน

## บิลด์จากซอร์ส {#from-source}

รุ่นที่คอมไพล์ไว้ล่วงหน้าเป็นเส้นทางที่แนะนำสำหรับ Agent และนักพัฒนาส่วนใหญ่ การบิวด์จากซอร์สต้องใช้ Radix compiler tree ส่วนตัวและอยู่นอกขอบเขตของหน้านี้ ให้ใช้ไฟล์เก็บถาวรด้านบนเว้นแต่คุณกำลังทำงานกับคอมไพเลอร์เอง

## เส้นทางสำหรับเอเจนต์ {#agent-path}

Agent ควรโหลดสกิล **install** และดัชนี Agent แทนที่จะขูดข้อมูล HTML นี้:

- [`/llms.txt`](/llms.txt)
- [install skill](/.well-known/agent-skills/install/SKILL.md)
- [Agent guide](/agents/index.md)

## ถัดไป {#next}

| ก่อนหน้า | ถัดไป |
|---|---|
| [ทัวร์ด่วน](/start/) | [สวัสดี Faber](/start/hello.html) |
