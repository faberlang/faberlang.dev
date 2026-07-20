编写最小但有用的 Faber 程序：一个用于格式化字符串并打印它的包入口点。

## 前置条件 {#prerequisites}

首先完成[安装和下载](/start/install.html)。你应该已经在 `PATH` 中拥有
`faber` 二进制文件，并处于一个可以创建文件的工作目录中。

## 创建包 {#create-package}

<<<FENCE 0>>>

## 检查程序 {#check}

<<<FENCE 1>>>

`faber check` 运行前端：词法分析、语法分析、类型检查，以及足以捕获常见包错误的降级处理，但不会构建本机二进制文件。
如果命令失败，请先读取诊断代码；Faber 诊断信息的设计目标是提供稳定的搜索定位标识。

## 运行程序 {#run}

<<<FENCE 2>>>

预期输出：

<<<FENCE 3>>>

## 刚才使用的内容 {#what-you-used}

| 源代码 | 含义 |
|---|---|
| `functio salve(textus nomen) → textus` | 名为 `salve` 的函数、类型优先的参数、文本返回值 |
| `fixum textus msg ← ...` | 不可变绑定 |
| `"Salve, §!"(nomen)` | 带显示插值的格式字符串 |
| `redde msg` | 返回 |
| `incipit` | 包入口点 |
| `nota m` | 打印备注/输出值 |

## 语言环境验证 {#locale-proof}

上面的程序是规范的拉丁语读者渲染结果。读者语言环境可以使用不同的关键字包来渲染同一个语义程序，同时保留字形和标识符。在编写非拉丁语包之前，请先从[读者语言环境](/features/reader-locale.html)中的完整验证开始。

## 下一步 {#next}

| 上一步 | 下一步 |
|---|---|
| [安装和下载](/start/install.html) | [你将使用的命令](/start/commands.html) |
