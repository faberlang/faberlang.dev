+++
translation_kind = "translated"

title = "Examples"
section = "examples"
order = 5
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
  "examples/ai-workbench/ (README.md, package, harness)",
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]
+++

## Examples

真实的 Faber 包，而非玩具片段。源码托管于公开的 [faberlang/examples](https://github.com/faberlang/examples) 仓库。当你需要了解应用的结构、CLI 的接法，或语言语料库的组织方式时，请参考这些示例。

### 如何运行示例 {#how-to-run}

```bash
# CLI on PATH (see Install)
faber --version

# Clone examples
git clone https://github.com/faberlang/examples.git

# Type-check a package; dependencies resolve through faber.lock
# and the Cista package store.
faber check examples/ai-workbench/packages/faber-ai

# Build / run / test when the package supports it
faber build examples/ai-workbench/packages/faber-ai -t rust
faber test examples/ai-workbench/packages/faber-ai
```

各包的确切入口命令有所不同，请阅读每个包的 `README.md`。

### 应用包 {#applications}

| 包 | 角色 | 从这里开始 |
|---|---|---|
| **AI Workbench** | 多命令 CLI，用于本地模型盘点、嵌入与推理工作流；包含 Python 测试夹具验证 | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · 站点：[AI Workbench](/start/examples.html) |
| **ViviLite** | Faber 原生的本地邮件空间 CLI（文件存储 + 可选 SQLite 通道），用于代理协调命令 | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | 更大规模的应用战役，以对等测试夹具重新实现常见工具 | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU / 系统工作负载梯队与契约 | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | 脚本与面向内核的演示 | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | 自动化草图包 | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | 用于关键字重映射的区域设置包演示 | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | 包仓库实验材料 | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

### 语言语料库 {#corpus}

**corpus**（语料库）树是关键字与构造的参考：每个构造一个目录，包含许多小型 `.fab` 程序。它是本站生成的 [Corpus](/corpus/) 页面的真源。

| 界面 | URL |
|---|---|
| 源码树 | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| 生成的文档 | [/corpus/](/corpus/) |
| 生态说明 | [语言语料库](/libraries/corpus.html) |

### 标准库导览 {#stdlib}

Norma 标准库示例位于 **norma** 仓库，而不在 `examples/` 之下：

- [faberlang/norma](https://github.com/faberlang/norma) — 若存在则为 `norma/exempla/`
- 站点：[Norma](/libraries/norma.html)

### 建议的学习顺序 {#order}

1. [安装](/start/install.html) CLI。
2. 浏览[快速导览](/start/)以了解语言形态。
3. 对于任何你不认识的关键字，打开 **corpus** 页面查看（[语料库中心](/corpus/)）。
4. 通读 **AI Workbench** 或 **ViviLite** 以了解应用形态。
5. 编辑时将[语法](/language/)与[工具链](/toolchain/)作为参考。

### 代理路径 {#agent-path}

- 技能：[examples](/.well-known/agent-skills/examples/SKILL.md)
- 技能：[corpus](/.well-known/agent-skills/corpus/SKILL.md)
- 索引：[`/llms.txt`](/llms.txt)

### 上一页 {#previous}

| 上一页 | 下一页 |
|---|---|
| [项目与示例](/start/projects.html) | [特性](/language/) |

## AI Workbench

AI 工作台是一个 Faber CLI 应用程序，用于本地模型清单、元数据检查、嵌入、索引和推理工作流。它展示了 Faber 如何构建一个具备真实 I/O、JSON 输出和 Python 测试套件验证的多命令 CLI 应用程序。

### 包 {#package}

`examples/ai-workbench/packages/faber-ai/`，包含以下 CLI 子命令：

- `model inspect` — 查询本地模型别名、路由和状态
- `embed` — 从文本输入生成嵌入

### 命令 {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

### 验证 {#validation}

AI 工作台包含 20 多个 Python 测试套件脚本，用于将 Faber 输出与固定映射进行比较，涵盖模型清单、推理、GPU 证据、会话生命周期和包复用——展示了编译后的 Faber 二进制文件的跨语言验证。

## Coreutils

Faber 以应用通道作为凭证，重新实现了 GNU coreutils。这些是真实的 CLI 程序，展示了 Faber 如何构建出可工作的二进制文件，涵盖 argv、stdio、退出码与宿主 I/O，并通过一致性测试框架对照宿主上的 GNU 工具进行验证。

### 已实现的工具 {#implemented-utilities}

**第 1 阶段 —— 脚手架 + true/false**
`true`、`false`

**第 2 阶段 —— 共享通用辅助模块 + 内联测试**
`echo`、`basename`、`dirname`、`printf`、`seq`

**第 3 阶段 —— 可空 stdin 切片**
`cat`、`head`、`tail`、`wc`、`tac`、`uniq`、`fold`、`nl`、`expand`、`unexpand`、`sort`、`cut`、`grep`、`tr`、`tee`、`paste`

**脚手架已就位 —— 第 5 阶段及以后**
`rm`、`cp`、`mv`、`mkdir`、`touch`、`pwd`、`readlink`、`realpath`、`join`、`comm`、`od`、`cksum`、`split`、`yes`、`printenv`

### 示例 —— echo {#example--echo}

`echo` 包展示了贯穿 coreutils 的 Faber 范式：CLI 注解、选项解析、使用 `probandum`/`proba`/`adfirma` 的内联测试，以及共享的通用模块：

```faber locale=la
importa ex "norma:consolum" privata consolum

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

### 运行 {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
