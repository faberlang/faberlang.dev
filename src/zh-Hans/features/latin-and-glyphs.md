+++
translation_kind = "translated"

title = "Latin vocabulary and structural glyphs"
section = "features"
order = 4
sources = []


prose_hash = "sha256:e460f8b157e7a98e6ecfc93d025078296877a974b90af1780945825df87741e5"
code_hash = "sha256:af40f7de992982b8319f9aed102017b00ded01ddee4d3d48ecb75d1b7b746b92"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
*三处信号选择，使 Faber 源码一眼可辨。*

Faber 作出了三处刻意的信号选择，它们协同作用，生成具有稳定语法形态的源码。读者在了解代码将被编译到哪个目标后端之前，就能看出每个构造的语义角色。

## 三处信号 {#three}

| 信号 | 示例 | 角色 |
|--------|----------|------|
| 类型优先声明 | `textus nomen`、`numerus aetas` | 形态朝绑定方向阅读——先类型，后名称。 |
| 拉丁语行为词 | `functio`、`genus`、`si`、`redde`、`fixum` | 声明、语句、生命周期与行为意图。 |
| 结构字形 | `← → ∴ ≡ ∪ ⇥` | 值流、类型流与结构衔接——通用，绝不本地化。 |

这三者被设计为相互加强。在一个 locale 下熟悉 Faber 的读者，可以在任何 locale 下阅读它，因为字形和结构从不改变。熟悉 Rust 后端的读者仍然能识别 Faber 源码，因为拉丁语关键字和类型优先的顺序产生了一种独特的视觉调性。

## 类型优先声明 {#type-first}

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

## 拉丁语行为词汇 {#latin}

Faber 为每个具有行为或语法形态的构造使用拉丁语词汇。该词汇小而规整，源自单一古典源头，而非大多数编程语言那种混合词源。

### 声明 {#declarations}

| 关键字 | 角色 | 近似等价物 |
|---------|------|------------------------|
| `functio` | 声明具名函数或方法 | `fn`、`def`、`function` |
| `genus` | 声明带字段的具体类型 | `class`、`struct` |
| `implendum` | 声明行为契约 | `interface`、`trait` |
| `typus` | 声明类型别名 | `typedef`、`type` |
| `discretio` | 声明标签联合 | `enum`、sum type |

### 绑定与转移 {#bindings-and-transfer}

| 关键字 | 角色 | 近似等价物 |
|---------|------|------------------------|
| `fixum` | 不可变绑定（一次写入） | `let`、`const` |
| `varia` | 可变绑定 | `let mut`、`var` |
| `sit` | 简洁的推断式不可变 | `let`（推断） |
| `redde` | 从函数返回值 | `return` |
| `iace` | 抛出到错误通道 | `throw`、`raise` |
| `mori` | 延后处理——行为尚不可表达 | `unimplemented!`、`todo` |

### 控制流 {#control-flow}

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

## 结构字形 {#glyphs}

在行为词汇使用拉丁语单词之处，结构含义使用通用字形。这些字形绝不本地化，也绝不在不同渲染中改变含义。它们是使 Faber 源码可被识别的视觉锚点，无论关键字以哪种人类语言渲染。

### 值流 {#value-flow}

| 字形 | 含义 |
|-------|---------|
| `←` | 运行时绑定、重新赋值与突变——唯一的赋值运算符 |
| `→` | 函数返回类型声明 |
| `⇥` | 备用出口：错误通道类型或内联转换恢复 |
| `∴` | 闭包连接符 — 将闭包体与其签名相连 |

### 类型形态 {#type-shape}

| 字形 | 含义 |
|-------|---------|
| `∷` | 静态类型归属——对值类型的编译期断言 |
| `↦` | 运行时转换——可能失败的解析或强制转换 |
| `∪` | 内联联合类型——连接两个类型（如 `T ∪ nihil`） |

### 比较与逻辑 {#comparison-and-logic}

| 字形 | 含义 |
|-------|---------|
| `≡` `≠` | 精确相等与不等——要求严格类型匹配 |
| `<` `>` `≤` `≥` | 排序比较 |
| `∧` `∨` `⊻` `¬` | 逻辑与位运算：与、或、异或、非 |

### 绑定约定至关重要 {#the-binding-convention-matters}

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

## 与主流语言对比 {#compare}

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

## 参考资料 {#references}

1. EBNF 语法——完整的字形与关键字清单
2. examples/corpus/——包含 292 个示例文件的语言语料库，覆盖所有关键字
3. examples/corpus/operatores/——运算符与字形示例
4. 戒律——守护这些信号的九条设计法则

## 读者包片段

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
