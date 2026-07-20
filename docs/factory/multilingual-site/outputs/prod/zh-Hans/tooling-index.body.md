Faber 工具链包含三个工具：用于构建和测试的 `faber` CLI、用于代码生成的 Radix 编译器，以及用于依赖解析的 Cista 包管理器。

## Faber 构建工具 {#faber-cli}

主要的开发者接口。构建、检查、运行、测试、格式化与解释——全部通过一个命令完成。[阅读更多 →](/tooling/faber-build-tool.html)

## Radix 编译器 {#radix}

编译器后端。将 Faber 源码经由 HIR → MIR → AIR 降低至多个目标通道。[阅读更多 →](/tooling/radix-compiler.html)

## Cista 包管理器 {#cista}

包解析与公共包仓库。管理 `faber.toml` 清单和依赖锁。[阅读更多 →](/tooling/cista-package-manager.html)

## 代码生成目标 {#codegen-targets}

Faber 可编译为 Rust（默认）、WASM、TypeScript、Go 和 GPU/WGSL。每个目标通道拥有独立的 IR 路径和运行时绑定。
[阅读更多 →](/tooling/codegen-targets.html)

## 性能 {#performance}

各目标通道的编译与执行性能测量数据。
[阅读更多 →](/tooling/performance.html)

## 脚本 {#scripting}

通过 `faber run` 命令将 Faber 作为脚本语言使用。
[阅读更多 →](/tooling/scripting.html)
