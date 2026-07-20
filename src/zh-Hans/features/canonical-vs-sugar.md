+++
translation_kind = "translated"

title = "Canonical vs sugar surfaces"
section = "features"
order = 6
sources = []


prose_hash = "sha256:af0aea6696c347bf589234a18320a6d9b7f95f6fbaf8bc3d83979b40f4212a43"
code_hash = "sha256:2fcab63f1bda97519d332924a5675a802a8a06cc8b303b8eaec72c6196ea1a43"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
*多种可解析形式，一种语义形态。*

Faber 设计中的一个反复出现的模式：语言为每个构造定义**唯一的规范拼写**，但接受多个**糖式拼写**，它们在语义上完全等价。编译器不会偏好其中之一——两者都解析为同一个 AST 节点。格式化器根据上下文和模式决定输出哪种拼写。

> **规则：** 糖式拼写与长形式在语义上完全等价。
> 多种形式都解析为同一个 `HirAnnotation` 或类型节点。
> `faber format --canonical` 偏好规范拼写；作者模式则保留作者书写的糖式形式。

## 数值类型糖 {#numeric-type-sugar}

数值类型既有长形式的规范拼写，也有紧凑的糖式形式。选择以模块为单位，而非以代码库为单位——一个 CLI 包可以全部使用长形式，而一个张量内核模块使用糖式：

| 糖式 | 规范形式 | 领域 |
|-------|----------------|--------|
| `f32`, `f64`, `i32`, `u64` | `fractus<f32>`, `numerus<i32>` | 位宽标记——标量数值类型 |
| `tf32`, `tf32[4]`, `ti64[2, 3]` | `tensor<f32, _>`, `tensor<f32, [4]>` | 稠密张量——`t` + 位宽 + 可选形状 |
| `sf32`, `sf32[2, 3]`, `si64[N]` | `sparsa<f32, _>`, `sparsa<f32, [2, 3]>` | 稀疏张量——`s` + 位宽 + 可选形状 |
| `mf32[4, 4]`, `mu32[3, 3]` | `matrix<f32, [4, 4]>` | 寄存器类矩阵——`m` + 位宽 + 形状 |
| `lf32`, `lu32`, `li64` | `lista<f32>`, `lista<u32>` | 列表——`l` + 位宽 |
| `f16` | `fractus<f16>` | 半精度浮点位宽标记（仅用于语义/布局） |

**通用 Faber（偏好长形式）：**

```faber
fixum lista<f32> values ← vacua
fixum tensor<f32, [2, 3]> grid ← vacua
fixum numerus<i32> narrow ← 7
```

**数值模块（偏好糖式）：**

```faber
fixum lf32 values ← vacua
fixum tf32[2, 3] grid ← vacua
fixum i32 narrow ← 7
```

糖式**仅适用于类型位置**。命名为 `f32`、`tf32` 或 `mf32` 的值标识符不受影响——编译器只有当它们出现在类型位置时，才将其解释为糖式。一个一致使用糖式的文件，应在文件顶部声明一次：

```faber
# STYLE: numeric sugar (tf32, mf32, sf32, lf32, lu32)
```

## 注解糖 {#annotation-sugar}

Faber 注解遵循与数值类型相同的双形式模型。注解是附加在声明上的编译器所拥有的元数据——例如 `@ optio` 用于 CLI 选项定义，或 `@ futura` 用于异步函数。

**规范形式：** 带有显式字段名的花括号记录：

```text
@ optio {
    binding = verbose,
    brevis = "v",
    longum = "verbose",
    typus = bivalens,
    ubique = verum,
    descriptio = "Enable verbose output"
}
```

**糖式形式：** 位置参数和命名别名：

```text
@ optio verbose brevis "v" longum "verbose" typus bivalens ubique descriptio "Enable verbose output"
```

两种形式都生成相同的 `HirAnnotation` 记录。规范形式显式且自文档化；糖式形式简洁，适用于字段顺序已广为人知的常用注解。`faber format --canonical` 偏好花括号记录；作者模式则保留作者选择的形式。

## 作者模式与规范格式化 {#author-vs-canonical-formatting}

`faber format` 命令有两种模式，与"规范 vs 糖式"原则相对应：

| 模式 | 命令 | 输入 | 输出 |
|------|---------|-------|--------|
| 作者 | `faber format` | 已解析的 AST + 前导 trivia | 保留 `#` 注释、空行和糖式拼写的 Faber 源码 |
| 规范 | `faber format --canonical` | 已分析的 HIR + `TypeTable` | 归一化的 Faber——无注释、规范拼写、无糖式 |

两种模式都经过编译器的完整前端处理（词法分析、解析、分析——用于规范模式）。无效的源码会产生编译器诊断信息——格式化器不会悄悄地格式化有错误的输入。

两种模式的关键规则：

- 四空格缩进
- Stroustrup 风格花括号：左花括号 `{` 与控制头位于同一行
- 作者模式保留空行的*存在*，但会合并多于一个的连续空行
- 作者模式不会插入源码中原本不存在的空行
- 规范模式将类型拼写归一化为长形式，将张量糖式归一化为规范形式，将注解归一化为花括号记录
- 规范模式对可空联合输出 `T ∪ nihil`，对可选参数输出 `sponte`

## 设计原则 {#design-principle}

"规范 vs 糖式"模式在多处出现，因为它是一个有意的设计原则，而非一系列零散的便利措施：

| 领域 | 规范形式 | 糖式 |
|--------|-----------|-------|
| 数值类型 | `numerus<i32>` | `i32` |
| 张量类型 | `tensor<f32, [4]>` | `tf32[4]` |
| 注解 | `@ optio { binding = verbose }` | `@ optio verbose ...` |
| 格式化 | `faber format --canonical` | `faber format`（作者模式） |
| 读者区域设置 | 拉丁语（`la`） | 任意区域设置包 |

该模式服务于两个目标。其一，降低入门门槛——新用户可以书写 `tf32[4]`，而无需键入 `tensor<fractus<f32>, [4]>`。其二，保持规范语言无歧义——当精度至关重要时，长形式表达的含义明确无误。格式化器在两者之间架起桥梁：作者书写糖式，审阅者可以请求规范形式，而 CI 可以强制执行任意一种。

## 参考资料 {#references}

1. `radix/docs/design/numeric-type-sugar.md`——完整的糖式家族、拼写偏好
2. `radix/docs/design/annotation-sugar.md`——双形式注解模型
3. `radix/docs/design/faber-canonical-surface.md`——作者模式与规范格式策略
4. `radix/EBNF.md`——糖式形式的语法表
