+++
translation_kind = "translated"

title = "History"
section = "history"
order = 0
sources = []


prose_hash = "sha256:99390038c112db9d79c728a21f5bc2c804af48f6de648df7e6ff6f2f0bc32a99"
code_hash = "sha256:8cfe9c845ef9a1247454bc890937eafa78a38164428679c7a6981c3c8cf3b9c4"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
## 起源 {#origins}

Radix 编译器的第一次提交发生在 **2024 年 12 月 20 日**，当时是一个基于 Bun + TypeScript 的项目，仅包含一个 `docs/decisions.md` 文件。第二次提交将五份架构决策记录（ADR）固化为文档，这些决策至今仍塑造着这门语言的形态。

**ADR-003** 题为"词尾承载语义含义"，从一开始便确立了拉丁语词形变化不只是关键字外壳——编译器会理解变格与变位，从而推断程序意图。最初的格映射为：

```text
Nominative  (subject)       →  return value, caller
Accusative  (direct object)  →  primary argument
Dative      (indirect obj.)  →  recipient, callback, destination
Genitive    (possession)     →  property access, "of" relationships
Ablative    (instrument)     →  dependencies, context, "using X"
```

同一文档中写道：*"动词变位是一个自然延伸的问题（将来时 → 异步？）。"* 这颗种子最终成长为现代的 **morphologia** 命名约定：标准库使用变位后的拉丁语动词形式来标识同步与异步、可变与拷贝输出——而无需编译器本身理解拉丁语语法。

该项目最初用 TypeScript 编写，后来用 Rust 重写，语法在 2026 版本中为 1.x 系列冻结。最初的五份 ADR（文件扩展名 `.fab`、错误提示、词尾含义、递归下降解析器、自定义 AST）仍可在 git 历史中查见。

## 版本发布 {#releases}

预构建的 CLI 归档——当前 Faber 发行版置顶，其后依次列出 [faberlang/releases](https://github.com/faberlang/releases) 中每一个已发布的标签与二进制文件：

- **[版本发布](/history/releases.html)** —— 下载链接与历史清单
- **[安装与下载](/start/install.html)** —— PATH 设置与首次 `faber check`
