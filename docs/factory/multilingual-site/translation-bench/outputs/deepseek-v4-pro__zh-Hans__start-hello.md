## 编写一个最小的 Faber 程序 {#write-smallest-faber-program}

编写一个最小的有用 Faber 程序：一个格式化字符串并打印输出的包入口点。

## 前提条件 {#prerequisites}

首先完成[安装与下载](/start/install.html)。您应该在 `PATH` 中有一个 `faber` 二进制文件，并有一个可以创建文件的工作目录中的 shell。

## 创建包 {#create-package}

<<<FENCE 0>>>

## 检查它 {#check}

<<<FENCE 1>>>

`faber check` 运行前端：词法分析、语法解析、类型检查和降低，足以捕获普通的包错误，而无需构建原生二进制文件。如果命令失败，请先阅读诊断代码；Faber 诊断旨在作为稳定的搜索句柄。

## 运行它 {#run}

<<<FENCE 2>>>

预期输出：

<<<FENCE 3>>>

## 您刚刚使用了什么 {#what-you-used}

| Source | 含义 |
|---|---|
| `functio salve(textus nomen) → textus` | 名为 `salve` 的函数，类型优先的参数，文本返回 |
| `fixum textus msg ← ...` | 不可变绑定 |
| `"Salve, §!"(nomen)` | 带显示插值的格式字符串 |
| `redde msg` | 返回 |
| `incipit` | 包入口点 |
| `nota m` | 打印一条注释/输出值 |

## 区域语言证明 {#locale-proof}

上述程序是规范拉丁文阅读器渲染。阅读器区域语言可以用不同的关键词包渲染相同的语义程序，同时保留字形和标识符。在编写非拉丁文包之前，请从[阅读器区域语言](/features/reader-locale.html)的完整证明开始。

## 下一步 {#next}

| 上一步 | 下一步 |
|---|---|
| [安装与下载](/start/install.html) | [您将使用的命令](/start/commands.html) |
