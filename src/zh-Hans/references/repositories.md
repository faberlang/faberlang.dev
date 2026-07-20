+++
translation_kind = "translated"

title = "Repositories"
section = "references"
order = 3
sources = [
  "github.com/faberlang",
]


prose_hash = "sha256:1f00ec1ce77844348776b258be2b9246bf876b614a2849a0e8dcbb54a8dc82f0"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
Faber 在 `faberlang` 组织下跨多个代码库开发。

## 公开代码库 {#public-repositories}

| 代码库 | 描述 |
|-----------|-------------|
| `faber` | 面向用户的 CLI：check、build、run、test、format、explain |
| `faber-runtime` | 核心运行时类型（Valor、张量、帧）；crate 名称为 `faber` |
| `norma` | 标准库源码（`norma:*` 模块） |
| `triga` | 可选的图形/几何库 |
| `cista` | 包管理器与存储（实验性） |
| `examples` | 语言语料库、coreutils、AI Workbench、reader-locale 包 |
| `faberlang.dev` | 本网站 |

## 私有代码库 {#private-repositories}

| 代码库 | 描述 |
|-----------|-------------|
| `radix` | 编译器：词法分析、语法分析、语义分析、HIR/MIR/AIR、诊断、代码生成 |

## 宿主平台代码库 {#host-platform-repositories}

| 代码库 | 描述 |
|-----------|-------------|
| `host-kernel-rs` | 轻量路由器：Frame、Conversation、前缀分发、结构化错误 |
| `host-native-rs` | 原生 attach：workers、register_providers 钩子 |
| `host-providers-rs` | Provider 实现：solum、processus、consolum、tempus、aleator、http |
