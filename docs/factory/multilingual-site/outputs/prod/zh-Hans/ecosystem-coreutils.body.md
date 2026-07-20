Faber 以应用通道作为凭证，重新实现了 GNU coreutils。这些是真实的 CLI 程序，展示了 Faber 如何构建出可工作的二进制文件，涵盖 argv、stdio、退出码与宿主 I/O，并通过一致性测试框架对照宿主上的 GNU 工具进行验证。

## 已实现的工具 {#implemented-utilities}

**第 1 阶段 —— 脚手架 + true/false**
`true`、`false`

**第 2 阶段 —— 共享通用辅助模块 + 内联测试**
`echo`、`basename`、`dirname`、`printf`、`seq`

**第 3 阶段 —— 可空 stdin 切片**
`cat`、`head`、`tail`、`wc`、`tac`、`uniq`、`fold`、`nl`、`expand`、`unexpand`、`sort`、`cut`、`grep`、`tr`、`tee`、`paste`

**脚手架已就位 —— 第 5 阶段及以后**
`rm`、`cp`、`mv`、`mkdir`、`touch`、`pwd`、`readlink`、`realpath`、`join`、`comm`、`od`、`cksum`、`split`、`yes`、`printenv`

## 示例 —— echo {#example--echo}

`echo` 包展示了贯穿 coreutils 的 Faber 范式：CLI 注解、选项解析、使用 `probandum`/`proba`/`adfirma` 的内联测试，以及共享的通用模块：

<<<FENCE 0>>>

## 运行 {#running}

<<<FENCE 1>>>
