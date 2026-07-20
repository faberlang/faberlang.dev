+++
translation_kind = "translated"

title = "Radix compiler"
section = "tooling"
order = 2
sources = [
  "radix/README.md",
  "radix/AGENTS.md",
]


prose_hash = "sha256:a3572e734d3a664b9ce7f7d1dd57e9a3190982a284e82db7f4c2e1c9dfc4aff3"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Radix 是 Faber 编译器。它是一个私有 crate (`radix/`)，实现了从源码文本到目标后端的完整编译流水线。

## 流水线 {#pipeline}

Radix 通过三层中间表示逐步降低 Faber 源码：

1. **HIR**（高级 IR）—— 语义核心。读者区域集成、类型检查以及基于 HIR 的后端都在此运行。
2. **MIR**（中级 IR）—— 面向执行的 IR。这是借用与效果分析的语义归属边界。
3. **AIR**（自动微分 IR）—— 用于自动微分与融合的纯函数式变换，由 GPU 目标通道使用。

## 目标通道 {#target-lanes}

| 通道 | IR | 输出 | 状态 |
|---|---|---|---|
| CPU 运行时 | MIR | FMIR（Rust 运行时） | 已发布 |
| LLVM | MIR | LLVM 文本 | 实验性 |
| WASM | MIR | WebAssembly 文本 | 实验性 |
| TypeScript | HIR | TypeScript 源码 | 实验性 |
| Go | HIR | Go 源码 | 实验性 |
| GPU/WGSL | AIR | 经由 WGPU 的 WGSL | 实验性 |

## 架构 {#architecture}

Radix 采用文本生成的方式，而非嵌入 LLVM。目标后端以各自的语言生成文本，随后由该目标自身的工具链进行编译。这使得编译器保持自包含，并使目标输出对人类可读。

## 诊断 {#diagnostics}

Radix 发出带有稳定标识符的结构化诊断代码：

- `LEX0xx` —— 词法分析错误
- `PARSE0xx` —— 语法分析错误
- `SEM0xx` —— 语义分析错误
- `DEFER0xx` —— 延迟特性（语法有效，尚未实现）

每个诊断均可通过 `faber explain <code>` 进行解释。
