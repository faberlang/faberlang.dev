+++
translation_kind = "translated"

title = "In-process scripting"
section = "tooling"
order = 3
sources = [
  "radix/docs/design/faber-scripting.md",
]


prose_hash = "sha256:0a78a5f2ec00dd6ec6d024631c78979f8b92ea90caed72c43a20785002145e14"
code_hash = "sha256:49d88b2d9c376e533ab8e397f53f2c4f96d2aeb99771c4ca89350b6fe05bb93d"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
除了编译后的 Rust 路径之外，Faber 还通过 MIR 步进器支持进程内的解释执行。

## 用法 {#usage}

```bash
faber run --interpret script.fab
```

该过程在编译器的常规前端（从解析到类型检查与 MIR 下推）之后，在进程内运行 Faber 源代码，而不会调用 `rustc` 或启动构建进程。

## 工作原理 {#how-it-works}

编译器生成已分析的 HIR、已验证的 MIR 以及已解析的运行时内部表。MIR 步进器将 MIR 块直接分派给宿主，跳过 wasm 的发射/实例化往返：

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck
                                                      ↓
                                                 MIR lowering
                                                      ↓
                                              MIR stepper + Host
```

## 延迟 {#latency}

脚本路径与编译路径运行相同的线性前端，外加与脚本实际执行内容成正比的步进时间：

| 阶段 | 开销 |
|-------|------|
| 前端（100 行脚本） | 约 0.6 毫秒 |
| MIR 步进 | 与已执行语句成正比 |

步进器从不调用 `rustc` 或启动进程，因此启动速度足够快，感觉就像一个 shell 脚本。

## 限制 {#limitations}

- MIR 步进器并不支持编译路径所支持的所有主机 I/O 路由——一些 `norma:*` 包装器仍仅限编译时使用
- 步进器是一个 MIR 原生的诊断/参考执行器，并非用于已部署应用程序的生产运行时
- 通过 Cargo 进行包编译仍然是主要的产品路径
