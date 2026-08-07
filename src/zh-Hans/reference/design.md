+++
translation_kind = "translated"

title = "Design notes"
section = "reference"
order = 3
sources = [
  "radix/docs/design/README.md",
]
+++

## Commandments

*让 Faber 之所以为 Faber 的九条法则。*

这些是定义 Faber 特质的设计法则。语法可以演进，特性可以增补，但任何改动都应保留这些原则。违反这些原则的程序或许仍是合法的 Faber，但它读起来不像 Faber。

这些戒律适用于每一个层级——从语法本身，到标准库 API 的命名方式。正因为如此，读者一眼就能认出 Faber 源码，无论其关键字渲染成哪种自然语言，也无论代码编译到哪个目标后端。

### 一、类型先于名称 {#i-types-before-names}

声明从形状读到绑定。类型在前，是因为读者需要先知道*这是什么样的东西*，名称随后才告诉他们*是哪一个*。这与那些语法顺序从类别读到实例的语言相契合——如中文、印地语、阿拉伯语——并产生出读法一致的声明。

```text
# Type before name in every declaration
textus nomen
numerus aetas
functio salve(textus name) → textus
```

### 二、机械胜于魔法 {#ii-mechanical-over-magical}

同一构造在任何地方都应表示同一含义。如果读者需要远处的上下文才能知道某个符号的作用，那么这种语法就是可疑的。Faber 偏好显式、局部的推理——声明处就携带了足够的信息，足以理解使用处将会发生什么。

```faber
# The meaning of a call is determined by the function's signature,
# not by invisible trait resolution or implicit conversions.
functio duplica(numerus n) → numerus {
    redde n * 2
}
```

### 三、字形承载结构 {#iii-glyphs-carry-structure}

结构和运算符的含义使用字形，而非词语：`←`
表示绑定，`→` 表示返回类型，`⇥`
表示错误退出，`ergo` 表示紧凑分支体，
`≡` 表示相等，`∪` 表示联合
类型。字形是普世的——它们从不本地化，也从不随渲染不同而改变含义。一位泰语读者和一位法语读者看到的是同样的字形，即便它们周围的关键字各不相同。

### 四、拉丁语承载行为 {#iv-latin-carries-behaviour}

词语用于声明、语句、生命周期，以及行为意图：
`functio`、`genus`、`fixum`、
`varia`、`redde`、`cape`。
这些可以通过读者语言包绑定——它们是词汇，不是语法。选择拉丁语并非因为拉丁语更为优越；而是为了选取*一个*一致的古典来源，使所有关键字属于同一语体，且没有任何关键字因为恰好是实现的编写语言而享有特权。

### 五、变位承载时间与流 {#v-conjugation-carries-time-and-flow}

当同一根逻辑可以同步、异步或作为生成器运行时，动词的变位形式应当承载这种执行模式。所有权配对——就地修改与返回副本——使用同一词干的相关形式。这是形态学原则（morphologia）。标准库（Norma）的所有方法命名都遵循此约定：`lege`（同步读取）对应 `leget`（异步读取），`adde`（就地修改）对应 `addita`（返回新副本）。编译器并不强制或推导变位——这是一项命名策略，而非语言特性。

### 六、一符一职 {#vi-one-sign-one-job}

一个字形或关键字可以有精确的别名，但不应当承载无关的含义。别名必须指向同一个规范概念。正是这一原则驱动了 Faber 在 `←`（运行时绑定）与 `=`（结构字段形状）之间的区分——大多数语言把两者都折叠进 `=`，但那种重载掩盖了一行代码究竟是数据流操作，还是类型层定义。

```text
# ← is always runtime flow
fixum numerus count ← 0
count ← count + 1

# = is always structural shape inside Type { }
fixum _ p ← Point {
    x = 10,
    y = 20
}
```

### 七、运行时流必须显式 {#vii-runtime-flow-is-explicit}

运行时绑定、重新赋值和修改使用 `←`；结构定义使用 `=`。扫视源码的读者能立刻看到每一个数据流操作：每一个 `←` 都是一次运行时事件。对于某个特定的 `=` 究竟是"存入这个变量"还是"定义这个字段"，不存在语法上的歧义。

### 八、缺失是有类型的 {#viii-absence-is-typed}

可空值类型写作联合：`T ∪ nihil`。可选的声明槽位使用名称后标记：`sponte`。这是两个不同的概念——*一个可能缺席的值*对应*一个调用者可以省略的槽位*——Faber 在语法上把它们分开，而不是把两者折叠进 `T?` 或 `Option<T>`。

```text
# Absence in a value: T ∪ nihil
functio find(textus key) → numerus ∪ nihil

# Omission at declaration: sponte
functio connect(textus host, numerus port sponte) → vacuum
```

### 九、编译器不靠猜测来掩盖信息缺失 {#ix-compiler-does-not-guess}

缺失的类型信息是一个需要在源头修复的分析问题，而不是一个需要掩盖的代码生成细节。当信息确实缺失时，编译器绝不静默推断程序员未曾提供的类型——它会报告缺口并停止。正是这条法则让 Faber 保持诚实：如果读者无法从局部源码判断某个符号的含义，编译器就不应假装自己能。

### 宗旨 {#purpose}

这些戒律的存在，是为了回答每一次语言设计讨论中都会出现的问题："这次改动之后还是 Faber 吗？"它们是不变性检查——不是对照特性清单，而是对照一种特质。违反某条戒律的改动可能仍是好主意，但应当被承认为偏离了 Faber 的设计特质，而非一次例行的增补。

在实践中，这些戒律最常作为新语法提案的评审准则。若一项提案通过增加"名称在前"的替代方案削弱了"类型先于名称"，或通过重载某个字形模糊了"一符一职"，就必须说明为何 Faber 应当为那个特性弯折自己的特质。

## Design documents

Radix 仓库收录了 Faber 作为语言和编译器的权威设计文档。这些文档位于 `radix/docs/design/`。

### 索引 {#index}

| 领域 | 文件 |
|------|-------|
| 目标与降级 | `target-capability-matrix.md`、`lowering-routes.md`、`semantic-ownership.md` |
| 类型与语法糖 | `numeric-type-sugar.md`、`comparison-operators.md`、`annotation-sugar.md` |
| 集合内建方法 | `lista-intrinsics.md`、`tabula-intrinsics.md`、`tensor-intrinsics.md`、`numerus-intrinsics.md`、`fractus-intrinsics.md`、`textus-intrinsics.md`、`intervallum-intrinsics.md`、`instans-intrinsics.md`、`copia-intrinsics.md` |
| 类型转换 | `conversio-valor.md`、`failable-conversio.md` |
| 帧与效果 | `frame-stream-types.md`、`host-provider-gateway.md` |
| 读取器与格式 | `reader-locale.md`、`faber-canonical-surface.md` |
| 系统 / AIR | `air-dialect.md`、`aiml-foundation.md`、`systems-shaped-values.md` |
| 工具表面 | `faber-scripting.md` |
| 命名债务 | `mixed-case-naming-debt.md` |

### 标准库设计文档 {#stdlib-design-docs}

`radix/docs/stdlib/` 目录包含：

| 文档 | 职责 |
|-----|------|
| `morphologia.md` | 全部标准库方法名的变位策略 |
| `tensor-methods.md` | Tensor 接收者方法参考 |
| `chorda-methods.md` | Chorda（文本）方法参考 |
| `mathesis-methods.md` | 数学方法参考 |
| `tempus-methods.md` | 时间方法参考 |
| `stdlib-mechanical-verbs.md` | pange/solve/tempta 三件套策略 |

## History

### 起源 {#origins}

Radix 编译器的第一次提交发生在 **2025 年 12 月 20 日**，当时是一个基于 Bun + TypeScript 的项目，仅包含一个 `docs/decisions.md` 文件。第二次提交将五份架构决策记录（ADR）固化为文档，这些决策至今仍塑造着这门语言的形态。

**ADR-003** 题为"词尾承载语义含义"，从一开始便确立了拉丁语词形变化不只是关键字外壳——编译器会理解变格与变位，从而推断程序意图。最初的格映射为：

```text
Nominative  (subject)       →  return value, caller
Accusative  (direct object)  →  primary argument
Dative      (indirect obj.)  →  recipient, callback, destination
Genitive    (possession)     →  property access, "of" relationships
Ablative    (instrument)     →  dependencies, context, "using X"
```

同一文档中写道：*"动词变位是一个自然延伸的问题（将来时 → 异步？）。"* 这颗种子最终成长为现代的 **morphologia** 命名约定：标准库使用变位后的拉丁语动词形式来标识同步与异步、可变与拷贝输出——而无需编译器本身理解拉丁语语法。

该项目最初用 TypeScript 编写，后来用 Rust 重写，语法在 2026 版本中为 1.x 系列冻结。最初的五份 ADR（文件扩展名 `.fab`、错误提示、词尾含义、递归下降解析器、自定义 AST）仍可在 git 历史中查见。

### 版本发布 {#releases}

预构建的 CLI 归档——当前 Faber 发行版置顶，其后依次列出 [faberlang/releases](https://github.com/faberlang/releases) 中每一个已发布的标签与二进制文件：

- **[版本发布](/releases/)** —— 下载链接与历史清单
- **[安装与下载](/start/install.html)** —— PATH 设置与首次 `faber check`
