+++
translation_kind = "translated"

title = "The faber CLI"
section = "toolchain"
order = 1
sources = [
  "faber/README.md",
  "faber/AGENTS.md",
  "radix/docs/design/faber-scripting.md",
]
+++

## Faber build tool

`faber` CLI 是构建、检查、运行、格式化和测试 Faber 源码的主要入口。它将 Radix 编译器封装为一个便捷的开发者工具。

### 核心命令 {#core-commands}

| 命令 | 用途 |
|---|---|
| `faber build <path>` | 将软件包编译为目标后端（默认：Rust） |
| `faber check <path>` | 进行类型检查，不输出代码 |
| `faber run <path>` | 构建并执行 |
| `faber test <path>` | 运行 proba 测试套件 |
| `faber format <path>` | 应用规范格式化 |
| `faber explain <code>` | 解释诊断代码 |
| `faber emit <path>` | 将源码输出到目标表面 |

### 构建软件包 {#building}

```text
faber build my-package/ -t rust
```

`-t` 标志用于选择代码生成目标。支持的目标包括 `rust`（默认）、`wasm`、`typescript` 和 `go`。

### 检查而不输出 {#checking}

```text
faber check my-package/
```

运行完整的前端流程（词法分析 → 解析 → 类型检查 → MIR 下沉），但不产生输出产物。请在 CI 和编辑器集成中使用此命令。

### 运行测试 {#testing-command}

```text
faber test my-package/
```

将软件包中的所有 `probandum` 套件编译为 Rust 的 `#[test]` 函数，并通过 Cargo 运行。内联测试与源码并存——无需单独的测试二进制文件。

### 格式化 {#formatting}

```text
faber format my-package/
```

应用规范的 Faber 格式化工具。该格式化工具强制执行一致的布局：每行一个声明、规范的间距，以及标准化的关键字表面。

### 解释诊断 {#explaining}

```text
faber explain SEM001
```

打印编译器可输出的任何诊断代码的人类可读说明。用于了解错误的含义及修复方法。

## In-process scripting

除了编译后的 Rust 路径之外，Faber 还通过 MIR 步进器支持进程内的解释执行。

### 用法 {#usage}

```bash
faber run --interpret script.fab
```

该过程在编译器的常规前端（从解析到类型检查与 MIR 下推）之后，在进程内运行 Faber 源代码，而不会调用 `rustc` 或启动构建进程。

### 工作原理 {#how-it-works}

编译器生成已分析的 HIR、已验证的 MIR 以及已解析的运行时内部表。MIR 步进器将 MIR 块直接分派给宿主，跳过 wasm 的发射/实例化往返：

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck
                                                      ↓
                                                 MIR lowering
                                                      ↓
                                              MIR stepper + Host
```

### 延迟 {#latency}

脚本路径与编译路径运行相同的线性前端，外加与脚本实际执行内容成正比的步进时间：

| 阶段 | 开销 |
|-------|------|
| 前端（100 行脚本） | 约 0.6 毫秒 |
| MIR 步进 | 与已执行语句成正比 |

步进器从不调用 `rustc` 或启动进程，因此启动速度足够快，感觉就像一个 shell 脚本。

### 限制 {#limitations}

- MIR 步进器并不支持编译路径所支持的所有主机 I/O 路由——一些 `norma:*` 包装器仍仅限编译时使用
- 步进器是一个 MIR 原生的诊断/参考执行器，并非用于已部署应用程序的生产运行时
- 通过 Cargo 进行包编译仍然是主要的产品路径
