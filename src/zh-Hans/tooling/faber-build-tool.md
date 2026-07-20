+++
translation_kind = "translated"

title = "Faber build tool"
section = "tooling"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
]


prose_hash = "sha256:5d8304941413ba003c019f0b1c43cd19e99ad0f25fa9b7a4ffadbc1327e8dfb6"
code_hash = "sha256:7657ec817fefbfb88c20a7b862970c668ebe2835de88c17eda584340fd2d6654"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
`faber` CLI 是构建、检查、运行、格式化和测试 Faber 源码的主要入口。它将 Radix 编译器封装为一个便捷的开发者工具。

## 核心命令 {#core-commands}

| 命令 | 用途 |
|---|---|
| `faber build <path>` | 将软件包编译为目标后端（默认：Rust） |
| `faber check <path>` | 进行类型检查，不输出代码 |
| `faber run <path>` | 构建并执行 |
| `faber test <path>` | 运行 proba 测试套件 |
| `faber format <path>` | 应用规范格式化 |
| `faber explain <code>` | 解释诊断代码 |
| `faber emit <path>` | 将源码输出到目标表面 |

## 构建软件包 {#building}

```text
faber build my-package/ -t rust
```

`-t` 标志用于选择代码生成目标。支持的目标包括 `rust`（默认）、`wasm`、`typescript` 和 `go`。

## 检查而不输出 {#checking}

```text
faber check my-package/
```

运行完整的前端流程（词法分析 → 解析 → 类型检查 → MIR 下沉），但不产生输出产物。请在 CI 和编辑器集成中使用此命令。

## 运行测试 {#testing-command}

```text
faber test my-package/
```

将软件包中的所有 `probandum` 套件编译为 Rust 的 `#[test]` 函数，并通过 Cargo 运行。内联测试与源码并存——无需单独的测试二进制文件。

## 格式化 {#formatting}

```text
faber format my-package/
```

应用规范的 Faber 格式化工具。该格式化工具强制执行一致的布局：每行一个声明、规范的间距，以及标准化的关键字表面。

## 解释诊断 {#explaining}

```text
faber explain SEM001
```

打印编译器可输出的任何诊断代码的人类可读说明。用于了解错误的含义及修复方法。
