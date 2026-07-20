+++
translation_kind = "translated"

title = "Commands you will use"
section = "commands"
order = 3
sources = []

prose_hash = "sha256:0e56e02cfc5bc616178712a8ff6e3d914b95257913dbd22db2e8e8aac3c0e72e"
code_hash = "sha256:adf615632f084c7edf7f1f0dfc205ee4912e8b497b19c9c96167bf9b97e443cc"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
本页面是 Faber 入门第一周的实用 CLI 速查表。可将其用作命令索引；当需要了解具体标志和编译器流水线细节时，请打开详细的 [Faber 构建工具](/tooling/faber-build-tool.html)页面。

## 每日循环 {#daily-loop}

| 命令 | 用途 |
|---|---|
| `faber check <package>` | 快速前端校验：词法分析、解析、类型检查、降阶 |
| `faber build <package> -t rust` | 生成 Rust 项目以供审阅或原生编译 |
| `faber run <package>` | 构建并执行应用程序包 |
| `faber test <package>` | 当包定义了测试入口时运行包测试 |
| `faber explain <code>` | 读取稳定的诊断说明 |

请从 `check` 开始。它是最轻量的命令，也是代理在将生成的代码作为有效 Faber 提交之前应当运行的命令。

## Check {#check}

```bash
faber check .
faber check examples/ai-workbench/packages/faber-ai
```

通过 check 意味着该包在语法和语义上被编译器前端所接受。这并不代表最终的原生工具链已被调用。

## Build {#build}

```bash
faber build . -t rust
```

Rust 目标的设计初衷是便于审阅。生成的 Rust 是编译器产物，而非事实来源；请编辑 Faber 包并重新构建，而不要手动修补已生成的 Rust。

## Run {#run}

```bash
faber run .
```

对带有 `incipit` 入口点的应用程序包请使用 `run`。仅作为库的包应当通过 check 和 test 进行验证。

## 解读诊断 {#explain}

```bash
faber explain SEM001
faber explain LEX006
```

诊断族是稳定的句柄：`LEX` 表示词法错误，`PAR` 表示解析器错误，`SEM` 表示语义/类型错误。在文档和代理报告中，请引用诊断代码，而不要含糊地转述编译器失败信息。

## 读取器区域命令 {#reader-locale}

```bash
faber format --reader-locale=la path/to/file.fab
faber format --reader-locale=th-TH path/to/file.fab
faber emit -t faber --reader-locale=zh-Hans path/to/file.fab
```

读取器区域输出是对编译器语义模型的渲染，而非浏览器运行时的翻译层。区域化工作应当在包以规范形式通过 check 之后进行。

## 下一步 {#next}

| 上一页 | 下一页 |
|---|---|
| [你好，Faber](/start/hello.html) | [项目与示例](/start/projects.html) |
