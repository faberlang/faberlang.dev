+++
translation_kind = "translated"

title = "Examples"
section = "examples"
order = 2
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
]

prose_hash = "sha256:fe9855413a019d0aebf6228e219c1fab4b694d7fa3fd7d7f7cacab4def2f3700"
code_hash = "sha256:7fce5618203f2537ec7b775252d4ce66501a659a385973e9ec6cc1414c49e9e6"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
真实的 Faber 包，而非玩具片段。源码托管于公开的 [faberlang/examples](https://github.com/faberlang/examples) 仓库。当你需要了解应用的结构、CLI 的接法，或语言语料库的组织方式时，请参考这些示例。

## 如何运行示例 {#how-to-run}

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

## 应用包 {#applications}

| 包 | 角色 | 从这里开始 |
|---|---|---|
| **AI Workbench** | 多命令 CLI，用于本地模型盘点、嵌入与推理工作流；包含 Python 测试夹具验证 | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · 站点：[AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | Faber 原生的本地邮件空间 CLI（文件存储 + 可选 SQLite 通道），用于代理协调命令 | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | 更大规模的应用战役，以对等测试夹具重新实现常见工具 | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU / 系统工作负载梯队与契约 | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | 脚本与面向内核的演示 | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | 自动化草图包 | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | 用于关键字重映射的区域设置包演示 | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | 包仓库实验材料 | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## 语言语料库 {#corpus}

**corpus**（语料库）树是关键字与构造的参考：每个构造一个目录，包含许多小型 `.fab` 程序。它是本站生成的 [Corpus](/corpus/) 页面的真源。

| 界面 | URL |
|---|---|
| 源码树 | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| 生成的文档 | [/corpus/](/corpus/) |
| 生态说明 | [语言语料库](/ecosystem/corpus.html) |

## 标准库导览 {#stdlib}

Norma 标准库示例位于 **norma** 仓库，而不在 `examples/` 之下：

- [faberlang/norma](https://github.com/faberlang/norma) — 若存在则为 `norma/exempla/`
- 站点：[Norma](/ecosystem/norma.html)

## 建议的学习顺序 {#order}

1. [安装](/start/install.html) CLI。
2. 浏览[快速导览](/start/)以了解语言形态。
3. 对于任何你不认识的关键字，打开 **corpus** 页面查看（[语料库中心](/corpus/)）。
4. 通读 **AI Workbench** 或 **ViviLite** 以了解应用形态。
5. 编辑时将[语法](/syntax/)与[工具链](/tooling/)作为参考。

## 代理路径 {#agent-path}

- 技能：[examples](/.well-known/agent-skills/examples/SKILL.md)
- 技能：[corpus](/.well-known/agent-skills/corpus/SKILL.md)
- 索引：[`/llms.txt`](/llms.txt)

## 上一页 {#previous}

| 上一页 | 下一页 |
|---|---|
| [项目与示例](/start/projects.html) | [特性](/features/) |
