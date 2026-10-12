AI 工作台是一个 Faber CLI 应用程序，用于本地模型清单、元数据检查、嵌入、索引和推理工作流。它展示了 Faber 如何构建一个具备真实 I/O、JSON 输出和 Python 测试套件验证的多命令 CLI 应用程序。

## 包 {#package}

`examples/ai-workbench/packages/faber-ai/`，包含以下 CLI 子命令：

- `model inspect` — 查询本地模型别名、路由和状态
- `embed` — 从文本输入生成嵌入

## 命令 {#commands}

<<<FENCE 0>>>

## 验证 {#validation}

AI 工作台包含 20 多个 Python 测试套件脚本，用于将 Faber 输出与固定映射进行比较，涵盖模型清单、推理、GPU 证据、会话生命周期和包复用——展示了编译后的 Faber 二进制文件的跨语言验证。
