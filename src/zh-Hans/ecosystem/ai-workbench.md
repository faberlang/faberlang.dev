+++
translation_kind = "translated"

title = "AI Workbench"
section = "ecosystem"
order = 4
sources = [
  "examples/ai-workbench/ (README.md, package, harness)",
]


prose_hash = "sha256:3a8940d1ee168b9bdf75f40f70ce5e5eb6b6446f47510df9c3511b2d4d1bef33"
code_hash = "sha256:dc8f04249d6a95c65b63ba0ccd58c402d6f8ed47a96bc15da4b6ad844922d007"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
AI 工作台是一个 Faber CLI 应用程序，用于本地模型清单、元数据检查、嵌入、索引和推理工作流。它展示了 Faber 如何构建一个具备真实 I/O、JSON 输出和 Python 测试套件验证的多命令 CLI 应用程序。

## 包 {#package}

`examples/ai-workbench/packages/faber-ai/`，包含以下 CLI 子命令：

- `model inspect` — 查询本地模型别名、路由和状态
- `embed` — 从文本输入生成嵌入

## 命令 {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

## 验证 {#validation}

AI 工作台包含 20 多个 Python 测试套件脚本，用于将 Faber 输出与固定映射进行比较，涵盖模型清单、推理、GPU 证据、会话生命周期和包复用——展示了编译后的 Faber 二进制文件的跨语言验证。
