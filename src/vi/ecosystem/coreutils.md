+++
translation_kind = "translated"

title = "Coreutils"
section = "ecosystem"
order = 3
sources = [
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]


prose_hash = "sha256:b413d7a121a8c7e90239de4231360a6ce0ed3d98da0d5752cc0e5bb53490c34d"
code_hash = "sha256:738161c1d064c275b5fb317f3dd18f6cf674c347cbf6d95b5a3e5edcf69af505"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Faber tái triển khai GNU coreutils như một minh chứng cho làn ứng dụng. Đây là các chương trình CLI thực tế, cho thấy Faber có thể xây dựng các tệp nhị phân hoạt động với argv, stdio, mã thoát và I/O của máy chủ. Kết quả được kiểm chứng bằng các tiện ích GNU trên máy chủ thông qua một bộ kiểm tra tương đương.

## Các tiện ích đã triển khai {#implemented-utilities}

**Giai đoạn 1 — khung ban đầu + true/false**  
`true`, `false`

**Giai đoạn 2 — các trình trợ giúp dùng chung + kiểm thử nội tuyến**  
`echo`, `basename`, `dirname`, `printf`, `seq`

**Giai đoạn 3 — các lát stdin nullable**  
`cat`, `head`, `tail`, `wc`, `tac`, `uniq`, `fold`, `nl`, `expand`,  
`unexpand`, `sort`, `cut`, `grep`, `tr`, `tee`, `paste`

**Đã tạo khung — Giai đoạn 5+**  
`rm`, `cp`, `mv`, `mkdir`, `touch`, `pwd`, `readlink`, `realpath`,  
`join`, `comm`, `od`, `cksum`, `split`, `yes`, `printenv`

## Ví dụ — echo {#example--echo}

Gói `echo` minh họa các mẫu Faber được sử dụng xuyên suốt coreutils:
chú thích CLI, phân tích tùy chọn, kiểm thử nội tuyến với
`probandum`/`proba`/`adfirma`, và các mô-đun dùng chung:

```faber
importa ex "norma:consolum" privata consolum
importa ex "../../../common/gnu/format" privata gnu_format

functio echo_textus(lista<textus> words) → textus {
    redde ""
}

functio echo_novam_lineam(lista<textus> words) → bivalens {
    redde falsum
}

probandum "echo formatting" tag "coreutils" {
    proba "empty operands" {
        adfirma echo_textus([]) ≡ ""
    }
    proba "-n suppresses newline" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }
}

@ cli "echo"
@ descriptio "GNU coreutils echo parity exemplum"
@ operandus ceteri textus words
incipit argumenta args {
    # ... CLI logic here
}
```

## Chạy chương trình {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
