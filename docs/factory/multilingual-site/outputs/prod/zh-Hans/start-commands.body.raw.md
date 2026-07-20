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

<<<FENCE 0>>>

通过 check 意味着该包在语法和语义上被编译器前端所接受。这并不代表最终的原生工具链已被调用。

## Build {#build}

<<<FENCE 1>>>

Rust 目标的设计初衷是便于审阅。生成的 Rust 是编译器产物，而非事实来源；请编辑 Faber 包并重新构建，而不要手动修补已生成的 Rust。

## Run {#run}

<<<FENCE 2>>>

对带有 `incipit` 入口点的应用程序包请使用 `run`。仅作为库的包应当通过 check 和 test 进行验证。

## 解读诊断 {#explain}

<<<FENCE 3>>>

诊断族是稳定的句柄：`LEX` 表示词法错误，`PAR` 表示解析器错误，`SEM` 表示语义/类型错误。在文档和代理报告中，请引用诊断代码，而不要含糊地转述编译器失败信息。

## 读取器区域命令 {#reader-locale}

<<<FENCE 4>>>

读取器区域输出是对编译器语义模型的渲染，而非浏览器运行时的翻译层。区域化工作应当在包以规范形式通过 check 之后进行。

## 下一步 {#next}

| 上一页 | 下一页 |
|---|---|
| [你好，Faber](/start/hello.html) | [项目与示例](/start/projects.html) |
