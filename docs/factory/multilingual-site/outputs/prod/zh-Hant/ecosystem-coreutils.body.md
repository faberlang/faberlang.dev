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

<<<FENCE 0>>>

## 執行 {#running}

<<<FENCE 1>>>
