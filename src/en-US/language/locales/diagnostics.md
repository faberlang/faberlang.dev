+++
title = "Diagnostics by locale"
section = "locales"
order = 2
sources = [
  "generator/locale-captures/",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

Diagnostics are structured facts before prose. Each carries a stable code and named arguments, and the reader pack owns the rendered template — so the same failure can be printed in any locale without changing the diagnosis.

One deliberately broken program, checked once per reader pack:

```console locale=la
# The closing quote is missing, so the string literal runs to the end of the
# line. Every reader pack renders the same LEX001 in its own language.
fixum textus nuntius ← "Salve, munde!
```

The failure is lexical, so it is identical in every locale: a string literal with no closing quote, `LEX001`. Only the message text moves. Run `faber check --diagnostics-locale <locale>` to reproduce it.

## English (`en`) {#en}

```console locale=la
error[LEX001:newline_in_string_literal] lex generator/locale-captures/error.fab
phase: lex
file: generator/locale-captures/error.fab
span: 173..187
source: ⁨fixum textus nuntius ← "Salve, munde!⁩
message: unterminated string literal (newline in string)
help: Double-quoted text strings are single-line; write `\n` for a newline or use `«...»` for multiline text.
explain: faber explain LEX001.newline_in_string_literal
```

## Latin (`la`) {#la}

```console locale=la
error[LEX001:newline_in_string_literal] lex generator/locale-captures/error.fab
phase: lex
file: generator/locale-captures/error.fab
span: 173..187
source: ⁨fixum textus nuntius ← "Salve, munde!⁩
message: unterminated string literal (newline in string)
help: close the string literal before the end of the line or file
explain: faber explain LEX001.newline_in_string_literal
```

## Arabic (`ar`) {#ar}

```console locale=la
error[LEX001:newline_in_string_literal] lex generator/locale-captures/error.fab
phase: lex
file: generator/locale-captures/error.fab
span: 173..187
source: ⁨fixum textus nuntius ← "Salve, munde!⁩
message: حرفية سلسلة غير مغلقة (سطر جديد في السلسلة)
help: أغلق حرفية السلسلة قبل نهاية السطر أو الملف
explain: faber explain LEX001.newline_in_string_literal
```

## Hindi (`hi`) {#hi}

```console locale=la
error[LEX001:newline_in_string_literal] lex generator/locale-captures/error.fab
phase: lex
file: generator/locale-captures/error.fab
span: 173..187
source: ⁨fixum textus nuntius ← "Salve, munde!⁩
message: समाप्त न हुआ string literal (string में newline)
help: पंक्ति या फ़ाइल के अंत से पहले string literal बंद करें
explain: faber explain LEX001.newline_in_string_literal
```

## Thai (`th-TH`) {#th-th}

```console locale=la
error[LEX001:newline_in_string_literal] lex generator/locale-captures/error.fab
phase: lex
file: generator/locale-captures/error.fab
span: 173..187
source: ⁨fixum textus nuntius ← "Salve, munde!⁩
message: ลิเทอรัลสตริงไม่ปิดท้าย (มีบรรทัดใหม่ในสตริง)
help: ปิดลิเทอรัลสตริงก่อนจบบรรทัดหรือไฟล์
explain: faber explain LEX001.newline_in_string_literal
```

## Vietnamese (`vi`) {#vi}

```console locale=la
error[LEX001:newline_in_string_literal] lex generator/locale-captures/error.fab
phase: lex
file: generator/locale-captures/error.fab
span: 173..187
source: ⁨fixum textus nuntius ← "Salve, munde!⁩
message: literal chuỗi chưa được kết thúc (có dòng mới trong chuỗi)
help: đóng literal chuỗi trước cuối dòng hoặc tệp
explain: faber explain LEX001.newline_in_string_literal
```

## Simplified Chinese (`zh-Hans`) {#zh-hans}

```console locale=la
error[LEX001:newline_in_string_literal] lex generator/locale-captures/error.fab
phase: lex
file: generator/locale-captures/error.fab
span: 173..187
source: ⁨fixum textus nuntius ← "Salve, munde!⁩
message: 未闭合字符串字面量（字符串中出现换行）
help: 在行尾或文件结束前闭合字符串字面量
explain: faber explain LEX001.newline_in_string_literal
```

## Traditional Chinese (`zh-Hant`) {#zh-hant}

```console locale=la
error[LEX001:newline_in_string_literal] lex generator/locale-captures/error.fab
phase: lex
file: generator/locale-captures/error.fab
span: 173..187
source: ⁨fixum textus nuntius ← "Salve, munde!⁩
message: 未結束的字串字面值（字串中出現換行）
help: 在行尾或檔案結束前結束字串字面值
explain: faber explain LEX001.newline_in_string_literal
```

---

[All reader locales](/language/reader-locales.html) · [Keyword reference](/language/locales/keywords.html)
