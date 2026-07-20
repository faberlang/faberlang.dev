+++
translation_kind = "translated"

title = "Compiler performance"
section = "tooling"
order = 2
sources = [
  "radix/README.md (Compiler Performance section)",
]


prose_hash = "sha256:6202471aeac8f93c0bfc712bbd7449a4303b3bd8da122bb7a91de4af66c343d2"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Radix 前端的扩展与源码大小大致呈线性关系，在进程内单线程运行。

## 前端编译时间 {#frontend-compile-times}

| 程序规模 | 源码 | 中位编译时间 |
|-------------|--------|---------------|
| 100 个函数 / 约 650 行 | 约 10 KB | 约 0.6 ms |
| 500 个函数 / 约 3.3K 行 | 约 52 KB | 约 3 ms |
| 1,000 个函数 / 约 6.5K 行 | 约 105 KB | 约 6 ms |
| 5,000 个函数 / 约 32K 行 | 约 530 KB | 约 37 ms |

目前最大的真实示例约为 140 行，远低于噪声基准。

## 后端开销（Rust 目标） {#backend-costs-rust-target}

对于 `faber build`，用户感知的时间主要由 Cargo/rustc 决定，而非 Faber 前端：

| 阶段 | 开销 |
|-------|------|
| 冷启动 `faber` 依赖编译（每个目标目录一次） | 约 2.8 s |
| 冷启动 `tokio` 依赖编译（仅在需要时） | 约 2.3 s |
| 热启动单程序构建（缓存依赖） | 约 30–110 ms |
| 单程序 Cargo 调用开销 | 约 400 ms |

## 增量编译 {#incremental-compilation}

`faber-runtime` crate 在每个目标目录中编译一次，并作为 `.rlib` 产物缓存：

| 更改内容 | faber-runtime crate | 您的程序 |
|-----------|-------------------|-------------|
| 您的程序源码 | 已缓存 | 重新编译 |
| `norma/src/*.fab`（Faber 源码） | 已缓存 | 重新编译 |
| `faber-runtime/src/*.rs` | 重新编译一次 | 重新编译 |

需要避免的陷阱是将每个程序构建到全新的 `target/` 目录中。复用共享的 `--target-dir` 可保持缓存的 `.rlib` 处于热状态。
