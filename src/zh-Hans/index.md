+++
translation_kind = "translated"

title = "Faber"
section = ""
order = 0
sources = []

prose_hash = "sha256:e63352acf54515593d9aeccf392881d72018d55e6b21d6e1ddd5a3979bef91b8"
code_hash = "sha256:a02ba6ea46d65efd212b09e097d3240402bfe1d46f89b993e389cd53ca1a9c9e"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
**Faber** 是一种面向包的编程语言，具有拉丁语行为词汇、简洁而规则的语法，以及类型优先的静态类型系统。源代码通过 Radix 编译器编译为可审查的 Rust 代码和原生二进制文件。其核心架构特性在于：语义存在于一个语义核心——HIR（高级中间表示）——之中，而非存在于任何特定的渲染形式中。

其名称源自拉丁语中表示*制造者*或*工匠*的词。编译器名为 Radix，源自拉丁语的*根*。该语言由 Ian Zepp 开发，并基于 MIT 许可证发布。

**初次接触？** 请从 [安装与下载](/start/install.html) 开始，然后依次运行入门学习轨道：[Hello](/start/hello.html)、[命令](/start/commands.html) 和 [项目](/start/projects.html)。

## 下载 Faber 1.1.1 {#download}

当前发布版本：**Faber 1.1.1**（标签 `faber-v1.1.1`）。提供 macOS 和 Linux 的预构建 CLI 归档文件；解压 `faber-v1.1.1-<target-triple>/faber` 二进制文件并将其放入您的 `PATH` 中。

| 平台 | 归档文件 | 校验和 |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [faber-v1.1.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

快速安装（以 macOS arm64 为例）：

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.1.1-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

所有发行说明和资源：[github.com/faberlang/releases · faber-v1.1.1](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1)。
详细步骤：[安装指南](/start/install.html)。完整历史清单：
[发行版本](/history/releases.html)。

| | |
|---|---|
| **范式** | 面向包；语义化分阶段 |
| **类型系统** | 静态，类型优先；通过 `T ∪ nihil` 实现可空 |
| **符号** | `← → ∴ ≡ ∪ ⇥` |
| **设计者** | Ian Zepp |
| **首次出现** | 2024 年 |
| **编译器** | Radix (Rust) |
| **轨道** | 应用 (HIR) · 系统 (MIR) |
| **主要目标** | Rust → 原生二进制 |
| **读者区域** | 已发布 7 种 (la, ar, hi, vi, th-TH, zh-Hans, zh-Hant) |
| **标准库** | Norma (`norma:*`) |
| **许可证** | MIT |

## 从这里开始 {#start-here}

| 路径 | 适用对象 | 内容 |
|---|---|---|
| [安装](/start/install.html) | 人类用户 | 下载、PATH 配置、首次 `faber check` |
| [Hello](/start/hello.html) | 人类用户 | 创建并运行 `salve-munde` |
| [命令](/start/commands.html) | 人类用户 + 代理 | 日常 CLI 循环：检查、构建、运行、测试、解释 |
| [项目](/start/projects.html) | 人类用户 + 代理 | 从 Hello World 迈向真正的包 |
| [快速导览](/start/) | 人类用户 | 五分钟了解语言形态 |
| [示例](/start/examples.html) | 人类用户 + 代理 | 真实的包：CLI 应用、邮件空间、GPU、语料库 |
| [`/llms.txt`](/llms.txt) | 代理 | 机器索引——如果您是模型，请从这里开始 |
| [代理指南](/agents/index.md) | 代理 | 如何学习 Faber 并交付一个包 |
| [代理技能](/.well-known/agent-skills/index.json) | 代理 | 专题技能指南（安装、语言、示例等） |

## 入口状态 {#portal-status}

此 `/` 页面是英文站点的 Speculum Porta：一个无区域设置的入口点，将用户引导至安装/入门页面，将代理引导至机器接口，并说明区域包的状态，无需在浏览器端进行协商。阶段 7 是多区域的部分验证，而非完整的本地化站点：只有 `th-TH`、`zh-Hans`、`zh-Hant`、`vi`、`ar` 和 `hi` 具有生成的入口/入门原创分片以及生成的语料库页面，且原创散文仍回退到英文。

| 区域 | 状态 | 说明 |
|---|---|---|
| `la` | 规范正式站点 | 完整生成的英文/拉丁文站点 |
| `th-TH` | 阶段 7 部分验证 | 入口/入门原创分片及生成的语料库；英文散文回退；完整的原创文档待完善 |
| `zh-Hans` | 阶段 7 部分验证 | 入口/入门原创分片及生成的语料库；英文散文回退；完整的原创文档待完善 |
| `vi` | 阶段 7 部分验证 | 入口/入门原创分片及生成的语料库；英文散文回退；完整的原创文档待完善 |
| `zh-Hant` | 阶段 7 部分验证 | 入口/入门原创分片及生成的语料库；英文散文回退；完整的原创文档待完善 |
| `ar` | 阶段 7 部分验证 | 入口/入门原创分片及生成的语料库；英文散文回退；完整的原创文档待完善 |
| `hi` | 阶段 7 部分验证 | 入口/入门原创分片及生成的语料库；英文散文回退；完整的原创文档待完善 |

以规范拉丁语编写的示例：

```faber
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
```

请参阅 [读者区域](/features/reader-locale.html)，查看通过泰语、简体中文、繁体中文、阿拉伯语、印地语和越南语包渲染的同一语义程序。

## 概览 {#overview}

Faber 的设计围绕一个核心见解：中间表示即是真理，没有任何目标或人类语言接口具有特权。一个用拉丁语关键词编写的 Faber 程序，可以通过与将其渲染为 Rust、Go 或 WebAssembly 相同的机制，被渲染为泰语、阿拉伯语或中文关键词——因为 HIR 是权威，而每一种输出都是其*渲染*结果。

该语言做出了三个精心设计的信号选择，它们协同工作：

- **类型优先声明** —— 形状朝向绑定读取：`textus nomen`，而非 `nomen: textus`。
- **拉丁语行为词汇** —— 声明、语句和生命周期：`functio`、`genus`、`fixum`、`redde`、`si`。
- **结构化符号** —— 值流和类型接合：`←`（绑定）、`→`（返回类型）、`∴`（紧凑分支）、`≡`（相等）、`∪`（联合）。

其结果是具有稳定语法形态的源代码，可以在不失去读者意图感的情况下进行审查、转换和降级。

## 文档 {#documentation}

| 部分 | 描述 |
|---|---|
| [历史](/history/) | 开发时间线、影响和发布历史 |
| [发行版本](/history/releases.html) | 最新的 Faber 下载以及每个已发布的标签和二进制文件 |
| [特性](/features/) | 读者区域、编译轨道、拉丁词汇、符号系统、设计原则 |
| [语法](/syntax/) | 完整参考：类型、函数、控制流、错误、泛型、集合 |
| [工具](/tooling/) | Radix 编译器管道、Faber CLI、代码生成目标、脚本 |
| [生态系统](/ecosystem/) | Norma、Cista、Triga、coreutils、AI Workbench、语料库 |
| [语料库](/corpus/) | 从公共语料库生成的关键词和构造页面 |
| [参考](/references/) | EBNF 语法、设计文档、代码库 |

## 快速示例 {#quick-example}

一个演示关键 Faber 模式的简单函数——类型优先参数、符号返回类型、可空联合、拉丁语控制词：

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ∴ redde nihil
    redde a / b
}
```

## 实时渲染 {#live-rendering}

上面的 divide 函数默认以拉丁语包渲染。编译器可以在七种读者区域中渲染同一程序——泰语、简体中文、繁体中文、阿拉伯语、印地语、越南语——每种都将关键字和类型重新映射为该语言，同时保持符号和标识符不变。这并不是应用于页面的翻译层；它是编译器用于生成本地化源代码的同一机制。

有关完整讨论，请参阅 [读者区域](/features/reader-locale.html) 文档。

## 代码库 {#repositories}

| 代码库 | 角色 |
|---|---|
| [faberlang/faber](https://github.com/faberlang/faber) | 公共用户 CLI |
| [faberlang/releases](https://github.com/faberlang/releases) | 带标签的 CLI 发布资源 |
| [faberlang/faber-runtime](https://github.com/faberlang/faber-runtime) | 生成的 Rust 的运行时类型 |
| [faberlang/norma](https://github.com/faberlang/norma) | 标准库源码 |
| [faberlang/cista](https://github.com/faberlang/cista) | 包存储 CLI/库 |
| [faberlang/triga](https://github.com/faberlang/triga) | 图形/几何库 |
| [faberlang/examples](https://github.com/faberlang/examples) | 语料库、学习轨道、应用包 |
| [faberlang/faberlang.dev](https://github.com/faberlang/faberlang.dev) | 本文档站点 |
