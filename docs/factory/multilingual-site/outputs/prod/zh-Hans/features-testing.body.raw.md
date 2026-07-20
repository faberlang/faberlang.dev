Faber 在语言层面内置了一流测试框架，包含三个关键字：`probandum` 声明测试套件，`proba` 声明单个测试用例，`adfirma` 断言某个条件。测试与被测代码位于同一文件中，通过 `faber test` 运行，并支持与生产代码相同的编译流水线 —— 具备区域感知能力、类型检查和多目标支持。

## 三个关键字 {#keywords}

| 关键字 | 角色 | 近似等价物 |
|---------|------|------------------------|
| `probandum` | 声明具名测试套件 | `describe`, `#[cfg(test)] mod` |
| `proba` | 声明单个测试用例 | `it`, `#[test]` |
| `adfirma` | 在运行时断言某个条件 | `assert!`, `assert_eq!` |

### probandum —— 测试套件 {#probandum-test-suite}

`probandum` 块对相关测试用例进行分组。套件可以嵌套，以层级方式组织测试：

<<<FENCE 0>>>

### proba —— 测试用例 {#proba-test-case}

`proba` 块包含测试逻辑。它可以使用任意 Faber 代码 —— 变量绑定、函数调用、控制流 —— 并以一个或多个 `adfirma` 断言结束。测试可以通过可选的 `tag` 标记打标签，以便选择性执行：

<<<FENCE 1>>>

### adfirma —— 断言 {#adfirma-assertion}

`adfirma` 对一个布尔表达式求值，若为假则报告失败。可选的消息字符串在失败时提供上下文：

<<<FENCE 2>>>

## 工作流 {#workflow}

测试通过 `faber test` 命令运行：

<<<FENCE 3>>>

由于测试与源代码位于同一个 `.fab` 文件中，因此没有独立的测试目录结构，没有测试模块声明，构建脚本在测试构建与生产构建之间也没有区别。编译器通过所用关键字来区分哪些块是测试代码、哪些是生产代码 —— `probandum` 和 `proba` 会被解析，但从生产构建中排除。

## 实战示例 {#real-world}

coreutils 的 `echo` 包在实践中展示了该测试框架的用法。测试与实现位于同一文件中，涵盖选项解析、转义扩展和边界情况：

<<<FENCE 4>>>

## 设计说明 {#design}

若干设计选择使 Faber 的测试框架区别于传统方法：

- **无独立测试二进制文件。** 测试是同一源文件中的声明，而非独立的编译目标。编译器将测试块从生产输出中过滤掉。
- **以标签代替目录。** 测试通过 `tag` 标记而非目录结构来组织。一个测试可以属于多个组织维度，而无需被移动。
- **完整编译流水线。** 测试经过类型检查、分析，并具备区域感知能力 —— 同一个 `--reader-locale` 标志也适用于测试输出。
- **多目标。** 测试通过包所面向的任意后端运行 —— `faber test --interpret` 使用 MIR 步进器，`faber test` 使用编译后的 Rust。
- **嵌套套件。** `probandum` 块可以嵌套，镜像被测代码的结构。

## 参考 {#references}

1. `examples/corpus/probandum/` —— probandum 示例文件
2. `examples/corpus/proba/` —— proba 示例文件
3. `examples/corpus/adfirma/` —— adfirma 示例文件
4. `examples/coreutils/packages/echo/src/main.fab` —— 带标签的实战用法
