编写一个最小可用的 Faber 程序：一个包入口点，用于格式化字符串并打印它。

## 前置条件 {#prerequisites}

请先完成[安装与下载](/start/install.html)。你应已在 `PATH` 中拥有 `faber` 可执行文件，并在可创建文件的工作目录中打开 shell。

## 创建包 {#create-package}

<<<FENCE 0>>>

## 检查 {#check}

<<<FENCE 1>>>

`faber check` 运行前端：词法分析、语法分析、类型检查，以及足够深度的 lowering，以便在不构建原生二进制的情况下捕获常见的包错误。若命令失败，请先阅读诊断码；Faber 诊断旨在作为稳定的搜索句柄。

## 运行 {#run}

<<<FENCE 2>>>

预期输出：

<<<FENCE 3>>>

## 你刚用到的内容 {#what-you-used}

| 源码 | 含义 |
|---|---|
| `functio salve(textus nomen) → textus` | 名为 `salve` 的函数，类型在前的参数，返回文本 |
| `fixum textus msg ← ...` | 不可变绑定 |
| `"Salve, §!"(nomen)` | 带显示插值的格式字符串 |
| `redde msg` | 返回 |
| `incipit` | 包入口点 |
| `nota m` | 打印说明/输出值 |

## 区域证明 {#locale-proof}

上面的程序是规范的拉丁语 reader 呈现。Reader 区域设置可以用不同的关键字包呈现同一语义程序，同时保留字形与标识符。在编写非拉丁语包之前，请先阅读[Reader 区域设置](/features/reader-locale.html)中的完整证明。

## 下一步 {#next}

| 上一篇 | 下一篇 |
|---|---|
| [安装与下载](/start/install.html) | [你会用到的命令](/start/commands.html) |
