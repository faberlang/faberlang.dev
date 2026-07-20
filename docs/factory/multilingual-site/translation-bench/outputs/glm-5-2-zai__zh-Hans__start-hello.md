编写最小的实用 Faber 程序：一个格式化字符串并打印它的包入口点。

## 前置条件 {#prerequisites}

请先完成[安装与下载](/start/install.html)。你的 `PATH` 中应有一个 `faber` 二进制文件，并在一个可以创建文件的工作目录中拥有一个 shell。

## 创建包 {#create-package}

<<<FENCE 0>>>

## 检查它 {#check}

<<<FENCE 1>>>

`faber check` 运行前端：词法分析、解析、类型检查，以及足够深度的下译，以便在不构建原生二进制文件的情况下捕获普通包错误。如果命令失败，请先阅读诊断代码；Faber 诊断旨在作为稳定的搜索句柄。

## 运行它 {#run}

<<<FENCE 2>>>

预期输出：

<<<FENCE 3>>>

## 你刚刚使用的内容 {#what-you-used}

| 源码 | 含义 |
|---|---|
| `functio salve(textus nomen) → textus` | 名为 `salve` 的函数，类型优先参数，文本返回 |
| `fixum textus msg ← ...` | 不可变绑定 |
| `"Salve, §!"(nomen)` | 带显示插值的格式字符串 |
| `redde msg` | 返回 |
| `incipit` | 包入口点 |
| `nota m` | 打印注释/输出值 |

## 语言区域证明 {#locale-proof}

上面的程序是规范的拉丁语阅读器渲染。阅读器语言区域可以使用不同的关键字包渲染相同的语义程序，同时保留字形和标识符。在编写非拉丁语包之前，请先从 [阅读器语言区域](/features/reader-locale.html) 阅读完整证明。

## 下一步 {#next}

| 上一页 | 下一页 |
|---|---|
| [安装与下载](/start/install.html) | [你将使用的命令](/start/commands.html) |
