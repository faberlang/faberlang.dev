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
Faber 以應用程式軌證明的方式重新實作 GNU coreutils。這些是真實的 CLI 程式，示範 Faber 如何使用 argv、stdio、結束碼與主機 I/O 建置可運作的二進位檔，並透過 parity harness 與主機上的 GNU 工具進行驗證。

## 已實作的工具 {#implemented-utilities}

**階段 1 — 腳手架 + true/false**  
`true`、`false`

**階段 2 — 共用通用輔助程式 + 內嵌測試**  
`echo`、`basename`、`dirname`、`printf`、`seq`

**階段 3 — 可為空的 stdin 切片**  
`cat`、`head`、`tail`、`wc`、`tac`、`uniq`、`fold`、`nl`、`expand`、  
`unexpand`、`sort`、`cut`、`grep`、`tr`、`tee`、`paste`

**已建立腳手架 — 階段 5+**  
`rm`、`cp`、`mv`、`mkdir`、`touch`、`pwd`、`readlink`、`realpath`、  
`join`、`comm`、`od`、`cksum`、`split`、`yes`、`printenv`

## 範例 — echo {#example--echo}

`echo` 套件示範 coreutils 各處使用的 Faber 模式：CLI 註解、選項剖析、使用 `probandum`/`proba`/`adfirma` 的內嵌測試，以及共用的通用模組：

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

## 執行 {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
