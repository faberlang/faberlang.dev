五分钟了解 Faber 的形态：安装 CLI，阅读一个函数，然后打开一个真实的包。如需按顺序学习，请遵循：[安装](/start/install.html) →
[你好](/start/hello.html) →
[命令](/start/commands.html) →
[项目](/start/projects.html)。

## 1. 安装 CLI {#install}

从[安装页面](/start/install.html)下载适用于您平台的最新版本（**1.1.1**），校验归档校验和，并将解压后的 `faber-v1.1.1-<target-triple>/faber` 二进制文件放入您的 `PATH` 中。确认：

<<<FENCE 0>>>

## 2. 函数形态 {#shape}

类型优先的参数，字形返回类型，拉丁控制词，可空联合类型：

<<<FENCE 1>>>

| 信号 | 含义 |
|---|---|
| `functio` | 函数声明 |
| `numerus a` | 类型在前，名称在后 |
| `→` | 返回类型 |
| `∪ nihil` | 可空（`T ∪ nihil`） |
| `si … ∴` | 紧凑分支 |
| `redde` | 返回 |

## 3. 包布局 {#package}

一个包是一个包含 `faber.toml` 和 `src/` 的目录：

<<<FENCE 2>>>

常用命令：

<<<FENCE 3>>>

详情请见：[Faber 构建工具](/tooling/faber-build-tool.html)。

## 4. 真实应用 {#applications}

不要止步于 hello-world。公开的 **示例** 仓库包含多命令 CLI、本地邮件空间、GPU 工作负载轨道和完整的语言语料库。

| 包 | 展示内容 |
|---|---|
| AI 工作台 | 多命令 CLI，模型检查，嵌入 |
| ViviLite | 基于文件的邮件空间 / 代理协调 CLI |
| coreutils | 更大的应用活动（对齐测试套件） |
| gpu-workload | 系统 / GPU 等级 |
| corpus | 每个语言构造一个目录 |

请在[示例页面](/start/examples.html)上浏览它们。

## 5. 如果您是代理 {#agents}

1. 阅读 [`/llms.txt`](/llms.txt)。
2. 打开 [`/agents/index.md`](/agents/index.md)。
3. 从 [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json) 中选择一个技能。

## 学习路径 {#start-track}

| 步骤 | 页面 | 成果 |
|---|---|---|
| 1 | [安装与下载](/start/install.html) | 将 Faber 1.1.1 放入 `PATH` 并验证它 |
| 2 | [你好，Faber](/start/hello.html) | 创建并运行 `salve-munde` |
| 3 | [您将使用的命令](/start/commands.html) | 学习 `check`、`build`、`run`、`test`、`explain` |
| 4 | [项目与示例](/start/projects.html) | 进入真实的包和语料库页面 |

## 下一步 {#next}

| 主题 | 链接 |
|---|---|
| 安装与下载 | [安装](/start/install.html) |
| 你好，Faber | [你好](/start/hello.html) |
| 命令 | [命令](/start/commands.html) |
| 项目 | [项目](/start/projects.html) |
| 语法参考 | [语法](/syntax/) |
| 功能（区域设置，通道） | [功能](/features/) |
| 生态系统库 | [生态系统](/ecosystem/) |
| 关键词语料库 | [语料库](/corpus/) |
