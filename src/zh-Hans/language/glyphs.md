+++
# This page discusses Latin keywords as Latin. Rendering them in
# the reader locale would turn its own examples into nonsense.
translate_spans = false
translation_kind = "translated"

title = "Glyphs and Latin"
section = "language"
order = 5
sources = [
  "radix/README.md (Glyphs and Words)",
  "examples/corpus/operatores/",
  "examples/corpus/assignatio/",
  "radix/EBNF.md",
]
+++

## Glyphs and operators

Faber 在符号具有结构意义时使用字形。以下是词法分析器识别的源字形完整清单。

### 值流 {#value-flow}

| 字形 | 含义 |
|-------|---------|
| `←` | 运行时绑定、重新赋值与变更 |
| `→` | 函数返回类型 |
| `⇥` | 备用出口——错误通道类型或内联转换恢复 |
| `∴` | 闭包连接符 — 将闭包体与其签名相连（`(a, b) → T ∴ a + b`） |

### 类型形状 {#type-shape}

| 字形 | 含义 |
|-------|---------|
| `∷` | 静态类型标注（编译时转换） |
| `↦` | 运行时转换（可能失败的解析/强制转换） |
| `∪` | 内联联合类型（`T ∪ nihil`） |

### 比较 {#comparison}

| 字形 | 含义 |
|-------|---------|
| `≡` `≠` | 精确相等与不等 |
| `<` `>` `≤` `≥` | 排序 |
| `≈` `≉` | 数值相等 |

### 逻辑与位运算 {#logical-and-bitwise}

| 字形 | 含义 |
|-------|---------|
| `∧` `∨` `⊻` `¬` | 与、或、异或、非 |
| `⇐` `⇒` | 左移与右移 |

### 赋值更新 {#assignment-updates}

| 字形 | 含义 |
|-------|---------|
| `←` | 表达式中唯一的赋值运算符 |
| `⊕` `⊖` | 后缀自增/自减语句（仅限可变 numerus） |

### 可选链与非空断言 {#optional-chaining-and-non-null-assertion}

| 字形 | 含义 |
|-------|---------|
| `?` `?.` `?[` `?(` | 可选链 |
| `!` `!.` `![` `!(` | 非空断言 |

### 范围 {#ranges}

| 字形 | 含义 |
|-------|---------|
| `‥` | 排除型范围端点 |
| `…` | 包含型范围端点 |

### 字面量分隔符 {#literal-delimiters}

| 字形 | 类型 | 角色 |
|-------|------|------|
| `'` | `ascii` | 固定机器标记 |
| `"` | `textus` | 行字符串 |
| `«` `»` | `textus` | 块字符串（书名号） |
| `` ` `` | `forma` | 捕获模板 |
| `|` | `octeti` | 十六进制字面量 |
| `§` | 模板孔 | `"…"`、`«…»`、`` `…` `` 内的占位符 |

### 标点符号 {#punctuation}

| 字形 | 角色 |
|-------|------|
| `(` `)` | 分组与调用 |
| `{` `}` | 块、genus 字面量或 JSON 文档 |
| `[` `]` | 列表字面量与索引 |
| `.` | 成员访问 |
| `,` | 分隔符 |
| `;` | 语句分隔符 |
| `:` | JSON 字段分隔符 |
| `=` | 结构字段形状（非运行时赋值） |
| `@` | 注解标记 |
| `#` | 行注释 |

## Latin vocabulary and structural glyphs

*三处信号选择，使 Faber 源码一眼可辨。*

Faber 作出了三处刻意的信号选择，它们协同作用，生成具有稳定语法形态的源码。读者在了解代码将被编译到哪个目标后端之前，就能看出每个构造的语义角色。

### 三处信号 {#three}

| 信号 | 示例 | 角色 |
|--------|----------|------|
| 类型优先声明 | `textus nomen`、`numerus aetas` | 形态朝绑定方向阅读——先类型，后名称。 |
| 拉丁语行为词 | `functio`、`genus`、`si`、`redde`、`fixum` | 声明、语句、生命周期与行为意图。 |
| 结构字形 | `← → ∴ ≡ ∪ ⇥` | 值流、类型流与结构衔接——通用，绝不本地化。 |

这三者被设计为相互加强。在一个 locale 下熟悉 Faber 的读者，可以在任何 locale 下阅读它，因为字形和结构从不改变。熟悉 Rust 后端的读者仍然能识别 Faber 源码，因为拉丁语关键字和类型优先的顺序产生了一种独特的视觉调性。

### 类型优先声明 {#type-first}

Faber 在每个声明中把类型置于名称之前。这与主流的 C 语系语法相反，且是刻意为之：

| 构造 | C 语系习惯 | Faber |
|-----------|----------------|-------|
| 变量 | `int count = 0` | `numerus count ← 0` |
| 函数 | `fn greet(name: String) → String` | `functio salve(textus nomen) → textus` |
| 参数 | `(String name)` | `(textus nomen)` |

类型优先声明意味着数据的形态是读者看到的第一件事。这自然契合那些从左到右按语义广度阅读的语言——中文、印地语和阿拉伯语的声明遵循同样的顺序。

```faber
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### 拉丁语行为词汇 {#latin}

Faber 为每个具有行为或语法形态的构造使用拉丁语词汇。该词汇小而规整，源自单一古典源头，而非大多数编程语言那种混合词源。

#### 声明 {#declarations}

| 关键字 | 角色 | 近似等价物 |
|---------|------|------------------------|
| `functio` | 声明具名函数或方法 | `fn`、`def`、`function` |
| `genus` | 声明带字段的具体类型 | `class`、`struct` |
| `implendum` | 声明行为契约 | `interface`、`trait` |
| `typus` | 声明类型别名 | `typedef`、`type` |
| `discretio` | 声明标签联合 | `enum`、sum type |

#### 绑定与转移 {#bindings-and-transfer}

| 关键字 | 角色 | 近似等价物 |
|---------|------|------------------------|
| `fixum` | 不可变绑定（一次写入） | `let`、`const` |
| `varia` | 可变绑定 | `let mut`、`var` |
| `sit` | 简洁的推断式不可变 | `let`（推断） |
| `redde` | 从函数返回值 | `return` |
| `iace` | 抛出到错误通道 | `throw`、`raise` |
| `mori` | 延后处理——行为尚不可表达 | `unimplemented!`、`todo` |

#### 控制流 {#control-flow}

| 关键字 | 角色 | 近似等价物 |
|---------|------|------------------------|
| `si` | 条件分支 | `if` |
| `sin` | else-if 分支 | `else if` |
| `secus` | else 分支 | `else` |
| `dum` | while 循环 | `while` |
| `itera` | 迭代（值、键或范围） | `for` |
| `elige` | 模式匹配（首条臂胜出） | `match`、`switch` |
| `fac` | 带错误恢复的 try 块 | `try`、`do` |
| `cape` | fac 的错误处理器 | `catch` |

> 拉丁语词汇是**可绑定的**——它随规范包一同发布，但可通过 reader locale 重新映射。泰国程序员看到的是 `ถ้า` 而不是 `si`；中国程序员看到的是 `函数` 而不是 `functio`。该词汇并非特权；只有语法才是。

### 结构字形 {#glyphs}

在行为词汇使用拉丁语单词之处，结构含义使用通用字形。这些字形绝不本地化，也绝不在不同渲染中改变含义。它们是使 Faber 源码可被识别的视觉锚点，无论关键字以哪种人类语言渲染。

#### 值流 {#value-flow}

| 字形 | 含义 |
|-------|---------|
| `←` | 运行时绑定、重新赋值与突变——唯一的赋值运算符 |
| `→` | 函数返回类型声明 |
| `⇥` | 备用出口：错误通道类型或内联转换恢复 |
| `∴` | 闭包连接符 — 将闭包体与其签名相连 |

#### 类型形态 {#type-shape}

| 字形 | 含义 |
|-------|---------|
| `∷` | 静态类型归属——对值类型的编译期断言 |
| `↦` | 运行时转换——可能失败的解析或强制转换 |
| `∪` | 内联联合类型——连接两个类型（如 `T ∪ nihil`） |

#### 比较与逻辑 {#comparison-and-logic}

| 字形 | 含义 |
|-------|---------|
| `≡` `≠` | 精确相等与不等——要求严格类型匹配 |
| `<` `>` `≤` `≥` | 排序比较 |
| `∧` `∨` `⊻` `¬` | 逻辑与位运算：与、或、异或、非 |

#### 绑定约定至关重要 {#the-binding-convention-matters}

有一个字形选择值得特别关注，因为它是新读者最容易混淆的点：

| 字形 | 角色 | 用于 |
|-------|------|---------|
| `←` | **运行时流** | 执行期的初始绑定、重新赋值与突变 |
| `=` | **结构形态** | 字面量内部的字段名和声明元数据——非运行时存储 |

大多数语言对 `=` 进行重载，既用于"在类型中定义此字段"，又用于"在此变量中放入运行时值"。Faber 拆分了这些工作。每个 `←` 都是活跃的数据流；每个 `Type { … }` 内部的 `=` 都是 genus 字段布局。

```text
# Runtime binding: ← attaches a value to a name
fixum numerus count ← 0
varia textus label ← "ready"
count ← count + 1

# Structural shape: = defines field values inside a literal
fixum _ p ← Point {
    x = 10,
    y = 20
}
```

### 与主流语言对比 {#compare}

下表展示了常见编程语言模式如何映射到 Faber 的三信号系统。Faber 一列为每个不同的语义任务使用不同的字形或关键字——没有重载。

| 语义任务 | 其他语言中常见 | Faber |
|--------------|---------------------------|-------|
| 参数类型声明 | `name: String` | `textus nomen` |
| 返回类型 | `→ String`、`: String` | `→` `textus` |
| 运行时赋值 | `x = value` | `←` |
| 相等性测试 | `==` | `≡` |
| 可空性 | `T?`、`Option<T>` | `T ∪ nihil` |
| 分支 + 单语句 | `if (cond) return x` | `si cond ergo redde x` |
| 类型转换 | `(T)value`、`value as T` | `value ∷ T` |
| 转换（可能失败） | `try_into()` | `value ↦ T` |

### 参考资料 {#references}

1. EBNF 语法——完整的字形与关键字清单
2. examples/corpus/——包含 292 个示例文件的语言语料库，覆盖所有关键字
3. examples/corpus/operatores/——运算符与字形示例
4. 戒律——守护这些信号的九条设计法则

### 读者包片段

```faber locale=la
函数 问候(文本 姓名) → 文本 {
    若 姓名 ≡ "" 则 返回 "你好，世界"
    返回 "你好，" ⊕ 姓名
}

类型-first 声明：
数字 计数 ← 0
文本 名字 ← "费伯"

固定 圆周率 ← 3.14
可变 计数器 ← 0
当 计数器 < 10 {
    计数器 ← 计数器 + 1
}

迭代 项 于 列表 {
    若 项 > 100 则 返回 项
}

枚举 颜色 {
    红色
    绿色
    蓝色
}

否则 情况 {
    红 ⇒ 返回 "停止"
    绿 ⇒ 返回 "通行"
}

## Canonical vs sugar surfaces

*多种可解析形式，一种语义形态。*

Faber 设计中的一个反复出现的模式：语言为每个构造定义**唯一的规范拼写**，但接受多个**糖式拼写**，它们在语义上完全等价。编译器不会偏好其中之一——两者都解析为同一个 AST 节点。格式化器根据上下文和模式决定输出哪种拼写。

> **规则：** 糖式拼写与长形式在语义上完全等价。
> 多种形式都解析为同一个 `HirAnnotation` 或类型节点。
> `faber format --canonical` 偏好规范拼写；作者模式则保留作者书写的糖式形式。

### 数值类型糖 {#numeric-type-sugar}

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

### 注解糖 {#annotation-sugar}

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

### 作者模式与规范格式化 {#author-vs-canonical-formatting}

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

### 设计原则 {#design-principle}

"规范 vs 糖式"模式在多处出现，因为它是一个有意的设计原则，而非一系列零散的便利措施：

| 领域 | 规范形式 | 糖式 |
|--------|-----------|-------|
| 数值类型 | `numerus<i32>` | `i32` |
| 张量类型 | `tensor<f32, [4]>` | `tf32[4]` |
| 注解 | `@ optio { binding = verbose }` | `@ optio verbose ...` |
| 格式化 | `faber format --canonical` | `faber format`（作者模式） |
| 读者区域设置 | 拉丁语（`la`） | 任意区域设置包 |

该模式服务于两个目标。其一，降低入门门槛——新用户可以书写 `tf32[4]`，而无需键入 `tensor<fractus<f32>, [4]>`。其二，保持规范语言无歧义——当精度至关重要时，长形式表达的含义明确无误。格式化器在两者之间架起桥梁：作者书写糖式，审阅者可以请求规范形式，而 CI 可以强制执行任意一种。

### 参考资料 {#references}

1. `radix/docs/design/numeric-type-sugar.md`——完整的糖式家族、拼写偏好
2. `radix/docs/design/annotation-sugar.md`——双形式注解模型
3. `radix/docs/design/faber-canonical-surface.md`——作者模式与规范格式策略
4. `radix/EBNF.md`——糖式形式的语法表
