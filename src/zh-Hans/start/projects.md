+++
translation_kind = "translated"

title = "Projects and examples"
section = "projects"
order = 4
sources = []

prose_hash = "sha256:8a914c63394e5bd0bf08ccef737eb95ec4cfb7df1813f3475c78d6ef579fb14d"
code_hash = "sha256:08056868d41c8d2a2925beb910fea8adcf4ac708fa67559e5a160dd900429a06"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
在完成 hello-world 之后，进入真实的包。Faber 是面向包的语言；最快的学习方式是检查并阅读现有的包，这些包所使用的编译器特性与你计划使用的相同。

## 公共仓库 {#repositories}

| 仓库 | 从这里开始 | 原因 |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`、应用包、tracks | 公开的语料库与应用示例 |
| [`faberlang/norma`](https://github.com/faberlang/norma) | `norma:*` 包 | 标准库源码 |
| [`faberlang/faber`](https://github.com/faberlang/faber) | CLI 包装器 | 面向用户的构建工具 |
| [`faberlang/cista`](https://github.com/faberlang/cista) | 包存储 CLI/库 | 包管理接口 |
| [`faberlang/triga`](https://github.com/faberlang/triga) | `triga:*` 源码 | 图形与几何库 |

## 克隆学习工作区 {#clone-workspace}

```bash
mkdir faber-learning
cd faber-learning
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

带有 `norma:*` 导入的包会从 `faber.lock` 中记录的 Cista 包存储解析依赖项。仅在你出于库开发目的需要有意的本地解析器覆盖时，才使用 `FABER_LIBRARY_HOME`。

## 按此顺序阅读示例 {#read-order}

1. [快速导览](/start/) 了解表层语法。
2. [Hello, Faber](/start/hello.html) 了解单个包。
3. [语料库](/corpus/) 每个关键字或构造对应一页。
4. [示例](/start/examples.html) 了解更大的应用程序。
5. [Faber 构建工具](/tooling/faber-build-tool.html) 了解 CLI 细节。

## 代理工作流 {#agent-workflow}

代理不应仅凭文字推断语法。请使用机器接口，然后验证生成的代码：

```bash
curl -fsSL https://faberlang.dev/llms.txt
faber check path/to/package
```

对于包相关的工作，在报告中引用仓库、包路径、命令和诊断代码。如果你在本站点中编辑了包含 Faber 代码围栏的文档，在声称示例仍可编译之前，请运行围栏验证器。

## 起步阶段之后 {#after-start}

| 目标 | 阅读 |
|---|---|
| 学习语法 | [语法](/syntax/) |
| 了解语言区域 | [阅读器语言区域](/features/reader-locale.html) |
| 使用编译器 | [Faber 构建工具](/tooling/faber-build-tool.html) 与 [Radix 编译器](/tooling/radix-compiler.html) |
| 浏览构造 | [语料库](/corpus/) |
| 使用库构建 | [生态系统](/ecosystem/) |

## 下一步 {#next}

| 上一页 | 下一页 |
|---|---|
| [你会使用的命令](/start/commands.html) | [示例](/start/examples.html) |
