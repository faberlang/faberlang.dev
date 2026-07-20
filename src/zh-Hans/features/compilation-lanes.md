+++
translation_kind = "translated"

title = "Compilation lanes"
section = "features"
order = 2
sources = []


prose_hash = "sha256:24bf11962b4a33f41f7c1f5746e0022669763b2d5d7c4982302e6337dc877817"
code_hash = "sha256:c3c0a1262dc6618a5d0012cd094f1b9482ac31149830c36bb11762a3690ac665"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
Faber 拥有单一共享的前端 —— 词法分析、解析、类型检查 —— 之后根据目标需求分叉到多个下层路径。中间表示构成一条流水线：源码被分析为 HIR，可选择性地下层到 MIR，并可选择性地绕行经过 AIR 后再进行最终发射。每种 IR 都服务于不同的目的，每个目标从与其需求匹配的 IR 中消费。

## 流水线概览 {#overview}

```text
Source (.fab)  →  Lex  →  Parse  →  Collect  →  Resolve  →  Lower  →  Typecheck  →  Analysis
                                                              │
                                                    HIR (semantic core)
                                                    ┌─────┴─────┐
                                                    │           │
                                              Reader locale    MIR lowering
                                              (input/output)    │
                                                                │
                                                      ┌─────────┴─────────┐
                                                      │                   │
                                                CPU lanes           GPU lanes
                                                      │                   │
                                            ┌────┬────┼────┬────┐     ┌───┴───┐
                                            │    │    │    │    │     │       │
                                          FMIR LLVM WASM  TS  Go   WGSL   Metal
                                                                          (hold)
```

同一个前端服务于所有目标。语义分析生成 HIR 之后，编译器根据目标选择一条路径：

- **HIR 直接发射** —— 直接从带类型的 HIR 发射，用于语言形态的后端（Rust、Faber、TypeScript、Go）
- **HIR → MIR** —— 下层到执行形态的 MIR，再为系统和底层目标发射
- **HIR → MIR → AIR → MIR** —— 为自动微分和融合变换绕行经过纯函数式 AIR，然后重新并入 MIR

## HIR —— 高级中间表示 {#hir}

HIR 是真相所在。它是一种带类型、语言形态的 IR，保留了声明、类型信息和结构关系。每个 Faber 程序，无论其原始区域设置或目标去向如何，都会经过这种表示。

### 读者区域设置集成 {#reader-locale-integration}

读者区域设置通过 HIR 发挥作用。一个用泰语关键字编写的 Faber 源文件会被解析并下层为与等价拉丁语源码相同的 HIR。区域设置是 HIR 的一种表层渲染，而非语义核心中的分叉。

- **输入：** 本地化源码（泰语、中文、阿拉伯语等）→ 规范化的 HIR —— **已交付**
- **输出：** HIR → 本地化源码重新发射 —— **进行中**（正在实现）

当输出方向交付时，`faber format --reader-locale=th-TH` 将通过 HIR 对任何 Faber 源码进行往返处理，并以泰语关键字发射，从而完成对称性：同一个 HIR 可以产生任何区域设置的表层形式，正如它可以产生任何目标后端一样。

### HIR 直接发射后端 {#hir-direct-backends}

这些目标直接从带类型的 HIR 发射，不经过到 MIR 的下层。它们更长时间地保留源码级结构，适用于语言形态的输出：

| 目标 | 状态 | 角色 |
|---|---|---|
| `Rust` | **主要** | 生产路径。包、构建、运行、测试。使用 Cargo + rustc 生成原生二进制文件。 |
| `Faber` | **支持** | 通过 `forma` 格式化器提供规范源码视图。具备往返稳定性。 |
| `TypeScript` | 探测 | 仅文件发射。跨目标形态验证语义。 |
| `Go` | 擦除 | 仅文件发射。擦除借用模式；拒绝 `ad`。 |

## MIR —— 中级中间表示 {#mir}

MIR 是执行形态的 IR。它表示控制流、局部变量、运行时调用、位置、分支和错误边 —— 即底层目标所需的事实。HIR 保留源码结构，而 MIR 则将其展平为控制流图。

HIR → MIR 下层将语言形态的构造翻译为执行步骤。MIR 在下层后被验证，以在任何后端尝试发射之前捕获结构问题。

> **语义归属。** Faber 在 HIR/MIR 中强制执行的规则（类型检查、明确赋值、借用模式检查）与留给目标工具链的规则（Rust 生命周期分析、Go 类型安全）之间保持清晰的边界。这防止了编译器重复目标编译器已经正确完成的工作。

## AIR 绕行 {#air}

AIR（Autograd / AI Representation，自动微分/AI 表示）是从 HIR → MIR 路径分叉出的纯函数式变换绕行。通过对单个函数的显式标注进入：

```faber locale=la
@ radix lane "air"
functio loss(numerus predicted, numerus expected) → numerus {
    fixum numerus delta ← predicted - expected
    redde delta * delta
}
```

AIR 通道函数必须满足纯度策略 —— 不可变、无副作用、无循环。违反此规则的函数会在 AIR 下层开始之前被诊断拒绝。程序的其余部分继续使用普通的 Faber，包含可变性、副作用和循环。

在 AIR 变换完成其工作（未来：自动微分、融合）之后，结果会被重新下层到 MIR，并重新并入普通的 MIR 后端流水线。AIR 不拥有任何后端，也没有独立的类型检查器 —— 它是一个变换检查点，而非并行的 IR。

```text
HIR  →  AIR purity check  →  HIR to AIR lowering  →  AIR validation  →  AIR to MIR re-lowering  →  MIR backend
```

这种架构反映了 JAX 的方法：为变换保留纯函数式表示，仅在最后阶段下层到命令式 IR。AIR 的存在是因为在命令式 MIR 上运行自动微分将需要从被下层为可变性的代码中重构出纯度。

## CPU 目标通道 {#cpu}

CPU 目标消费 MIR，并生成可执行工件或供外部工具链使用的文本。Faber 尽可能发射文本，并依赖底层工具链完成最终编译步骤 —— 类似于 C 编译器为汇编器和链接器发射汇编代码。

### FMIR —— Faber 自有的 MIR 运行时 {#fmir}

FMIR 是 MIR 原生的包执行器。编译器将 MIR 提取为二进制载荷，并用一个简短的 Rust 内核加载器将其包装。这产生了一个自包含的可执行文件，通过 Faber 的进程内步进器运行 MIR —— 无需安装单独的运行时。

| 格式 | 描述 |
|---|---|
| `fmir-text` | 可检查的 FMIR 文本映像，位于 `target/faber-mir/image.fmir.txt` |
| `fmir` | 紧凑的二进制 FMIR 映像，位于 `target/faber-mir/image.fmir` |
| `fmir-bin` | 自包含的运行器，位于 `target/faber-mir/exe/run` —— 内嵌 FMIR 字节 |

### LLVM 文本 {#llvm}

Faber 将 LLVM IR 作为文本（`.ll`）发射，而非集成的 LLVM 代码生成。发射的 IR 用于外部工具链步骤 —— 验证、优化和原生代码生成由下游 LLVM 工具处理。这是一个分阶段和验证目标，而非嵌入编译器的原生代码生成路径。

### WASM {#wasm}

Faber 发射 WebAssembly 文本（`.wat`）和二进制（`.wasm`）格式。发射的 Wasm 使用外部宿主导入（`faber_*` 运行时符号），并通过 `wasm-tools validate` 进行验证。Wasm 是一个受支持但有限制的目标 —— 它为一种开放标准格式验证 MIR 下层流水线，但不是包交付运行时。

| 格式 | CLI 目标 | 输出 |
|---|---|---|
| `wasm-text` | `-t wasm-text`（别名 `wat`） | WAT 文本格式 |
| `wasm` | `-t wasm` | 二进制 Wasm 模块 |

### TypeScript 和 Go（HIR 直接发射） {#typescript-go}

虽然通常用于应用级文件发射，但 TypeScript 和 Go 也作为验证目标：它们验证 Faber 的语义能够转化为广泛使用的类型系统，即使目前包编译和运行时执行仍仅限于 Rust。

## GPU 目标通道 {#gpu}

### WGSL（通过 WGPU） {#wgsl}

Faber 通过 MIR 流水线发射 WGSL 计算着色器源码。发射的 WGSL 通过 `naga`（30.x）进行验证，并包含用于绑定组元数据的反射副件。这涵盖设备安全的内核子集：支持 rank-1 `f32` 设备视图；rank-2 视图会被拒绝。WGSL 不是 GPU 启动运行时 —— Faber 发射着色器源码，但执行需要外部的 WebGPU 运行时。

### Metal（暂停） {#metal}

Metal 计算着色器文本发射已设计并部分实现，但目前处于暂停状态。该架构遵循与 WGSL 相同的模式：Faber 为设备安全的内核子集发射 Metal Shading Language 源码，由外部工具链处理编译和执行。计划恢复此项工作。

## 架构说明 {#comparison}

Faber 的编译架构在精神上类似于 Rust 编译器的工作方式。Rust 通过 HIR → MIR → LLVM IR 进行下层，直接嵌入 LLVM 工具链以进行最终的原生代码生成。Faber 采取了更为柔和的方式：它为外部工具链（LLVM 文本、WGSL、Metal、WAT）发射文本，而非嵌入它们，同时为自身的运行时（FMIR）和主要包目标（Rust，由 Cargo 和 rustc 处理下游流水线）保留直接代码发射。

文本发射方式意味着 Faber 永远不需要捆绑 LLVM、Wasm 运行时或 GPU 驱动 —— 这些仍然是用户选择的外部依赖。其权衡是 Faber 无法为每个目标提供单一命令的构建；用户必须为其选择的后端安装相应的工具链。

## 目标汇总 {#matrix}

| 目标 | IR | 家族 | 构建 | 运行 | 包 |
|---|---|---|---|---|---|
| `Rust` | HIR | CPU | 是 | 是 | 是 |
| `fmir` / `fmir-bin` | MIR | CPU | 是 | 是 | 是 |
| `Faber`（格式化） | HIR | — | 否 | 否 | 否 |
| `TypeScript` | HIR | CPU | 否 | 否 | 否 |
| `Go` | HIR | CPU | 否 | 否 | 否 |
| `LLVM 文本` | MIR | CPU | 否 | 否 | 否 |
| `WASM` / `WAT` | MIR | CPU | 否 | 否 | 否 |
| `WGSL` | MIR | GPU | 否 | 否 | 否 |
| `Metal`（暂停） | MIR | GPU | 否 | 否 | 否 |

*`build`、`run` 和 `package` 描述的是 Faber 的工作流。外部工具链（rustc、wasm-tools、naga）为文本发射目标处理最终编译。*
