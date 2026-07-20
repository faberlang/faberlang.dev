编写一个最小但有用的 Faber 程序：一个格式化字符串并将其打印出来的包入口点。

## 前置条件 {#prerequisites}

请先完成[安装和下载](/start/install.html)。你应该已经有一个位于
`PATH` 中的 `faber` 二进制文件，并且有一个处于工作目录中的 shell，以便创建文件。

## 创建一个包 {#create-package}

<<<FENCE 0>>>

## 检查它 {#check}

<<<FENCE 1>>>

`faber check` 运行前端：词法分析、语法分析、类型检查，以及足以捕获普通包错误的降级过程，但不会构建本机二进制文件。
如果命令失败，请先读取诊断代码；Faber 诊断代码旨在作为稳定的搜索句柄。

## 运行它 {#run}

<<<FENCE 2>>>

预期输出：

<<<FENCE 3>>>

## 你刚才使用的内容 {#what-you-used}

| Source | Meaning |
|---|---|
| `functio salve(textus nomen) → textus` | 名为 `salve` 的函数，类型优先的参数，返回文本 |
| `fixum textus msg ← ...` | 不可变绑定 |
| `"Salve, §!"(nomen)` | 带显示插值的格式字符串 |
| `redde msg` | 返回 |
| `incipit` | 包入口点 |
| `nota m` | 打印注释/输出值 |

## 区域设置证明 {#locale-proof}

上面的程序是规范的拉丁语阅读器渲染结果。阅读器区域设置可以使用不同的关键词包来渲染同一个语义程序，同时保留字形和标识符。在编写非拉丁语包之前，请先从[阅读器区域设置](/features/reader-locale.html)中的完整证明开始。

## 下一步 {#next}

| Previous | Next |
|---|---|
| [安装和下载](/start/install.html) | [你将使用的命令](/start/commands.html) |
