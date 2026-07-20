+++
translation_kind = "translated"

title = "Reader locale"
section = "features"
order = 1
sources = []


prose_hash = "sha256:4b909cabbc40f43896ed8b7b15ac304b8a10b008d73df027bf4a3c2ac975ffed"
code_hash = "sha256:ee712d08c1cd8884f42aa5e872441223a539f58bf4cdcc50824748dc1108f58d"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
阅读器语言区域是 Faber 用于以读者的人类语言渲染源代码、编译器诊断和语言关键字的系统——而无需分叉语义。一位泰国程序员可以用泰语关键字读写 Faber 源代码，以泰语接收编译器错误，并通过同一个 HIR 与拉丁或中文用户协作。将代码从拉丁文本地化为泰语的机制，与将代码发射为 Rust 的机制相同：`HIR → surface`——两者均不享有特权。

## 问题 {#problem}

大语言模型已经本地化了编程周围的**对话**——一位泰国计算机科学家可以用泰语向 LLM 寻求帮助——但并未本地化持久的**制品**。生成的代码、API、编译器错误和文档仍然保持英语形态。英语熟练度成为了计算机科学的门槛，而不仅仅是对话的门槛。

阅读器语言区域是对此的设计回应：人类用来*理解* Faber 的语言——源代码、诊断，以及可选的标准库拼写——而无需以英语为先决条件。它不是应用国际化（完整的字符串矩阵覆盖）。它是阅读器方言支持：在语义核心之上的选择性启用、部分覆盖包，且不分叉语义。

> **产品论点：** 英语不应是软件意图的必需审查语言。LLM 已本地化编程周围的对话；阅读器语言区域本地化持久的制品。

## 工作原理 {#how}

阅读器语言区域包将 Faber 关键字、原始类型拼写和诊断模板映射到目标语言。包是 TOML 文件，包含三个表：

- `[keywords]` —— 将关键字名称映射到其本地化拼写
- `[types]` —— 将原始类型名称映射到本地化拼写
- `[diagnostics.*]` —— 将诊断代码映射到本地化消息模板
- `[llm]` —— 用于 LLM 代码生成的系统提示片段和示例

编译器根据生成的拉丁语骨架验证包——每个关键字和类型都必须有定义的拼写，或显式从拉丁语继承。缺失的行会产生可见的回退，而不是静默的缺口。

在命令行或 `faber.toml` 中选择语言区域：

```text
faber check --reader-locale th-TH program.fab
```

```toml
# faber.toml
[reader]
locale = "zh-Hans"
```

### 本地化的内容与非本地化的内容 {#what-localises}

| 层 | 在 HIR 中？ | 行为 |
|---|---|---|
| 关键字、类型、成对短语 | 是 | 在所有渲染中无损 |
| 字符 `← → ∴ ≡ ∪ ⇥` | 是（不变） | 在每个渲染中相同 |
| 类型优先结构 | 是 | 在每个渲染中相同 |
| 数字 | — | 在所有语言区域中仅限 ASCII |
| 注释 | 否 | 超出编译器范围；LLM 中介，选择性启用 |
| 标识符名称 | 否 | 逐字节保留 |
| 标准库拼写 | 否 | 每个语言区域的覆盖层 |

关键的架构保证：任何语言区域表面都可以在任何时候成为任何其他语言区域，包括拉丁语。本地化的 Faber 文件永远不会成为陷阱，因为它永远不会是代码可以采取的唯一形式。`faber format --canonical` 恰好就是 `faber format --reader-locale=la`。

## 内置包 {#locales}

Radix 今天内置了七个包：

| 代码 | 语言 | 文字 | 状态 |
|---|---|---|---|
| `la` | Latina（拉丁语） | 拉丁 | **规范** |
| `th-TH` | ไทย | 泰文 | **参考证明** |
| `zh-Hans` | 简体中文 | 简体中文 | 覆盖证明 |
| `zh-Hant` | 繁體中文 | 繁体中文 | 覆盖证明 |
| `ar` | العربية | 阿拉伯文 | 覆盖证明 |
| `hi` | हिन्दी | 天城文 | 覆盖证明 |
| `vi` | Tiếng Việt | 越南语（拉丁） | 覆盖证明 |

这五个参考语言区域是为**集体架构压力**而选择的——它们共同迫使底层必须经受每一个 Unicode 和发射问题。其中四个使用非拉丁文字；越南语是拉丁文字的对照案例：

| 语言区域 | 访问 | 架构压力 |
|---|---|---|
| `th-TH` | 高 | 无空格文字——词法分析器的压力测试 |
| `zh-Hans` / `zh-Hant` | 非常高 | 成对关键字；兄弟包继承；NFKC 宽度塌缩 |
| `ar` | 高 | 从右到左；诊断中的双向隔离 |
| `hi` | 非常高 | Matra/virama 聚类；印度数字 |
| `vi` | 高 | 拉丁文字上的重度变音符号；NFKC 边缘案例 |

*参考集的选取基于架构覆盖，而非人口规模。仅凭人口规模无法证明底层尚未处理的任何问题。*

## 本地化源代码示例 {#examples}

六个非规范语言区域中的每一个在 `examples/reader-locale/` 下都有一个完整的 Faber 包，包含本地化源代码、诊断测试案例和 `faber.toml` 清单。同一个 `greet` 程序在所有内置语言区域中的渲染：

**拉丁语** `la` —— *规范*

```faber
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
```

规范渲染。`faber format --canonical` 恰好就是 `faber format --reader-locale=la`。拉丁语关键字映射到自身；类型名称是规范拼写。

**ไทย** `th-TH` —— *参考证明*

```text
ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ {
    ค่าคงที่ ข้อความ msg ← "Salve, §!"(nomen)
    คืนค่า msg
}

เริ่มต้น {
    ค่าคงที่ ข้อความ m ← salve("มุนเด")
    แจ้ง m
}
```

访问楔入证明。泰语是一种无空格文字——没有词间边界——这使其成为词法分析器的压力测试，也是阅读器语言区域系统的最初架构驱动力。每个标记边界必须由词法分析器仅通过关键字匹配来解析。

**简体中文** `zh-Hans`

```text
函数 问候(文本 名字) → 文本 {
    常量 文本 问候语 ← "你好，§!"(名字)
    返回 问候语
}

入口 {
    常量 文本 消息 ← 问候("世界")
    显示 消息
}
```

成对关键字（如果/否则，对应 si/secus），需要包关键字分组；全角/半角标点；词法入口处的 NFKC 宽度塌缩。由于 CJK 词法分析器边界，这是最难的 LLM 发射案例。繁体中文（zh-Hant）的兄弟包继承并覆盖 zh-Hans 的根。

**العربية** `ar`

```text
دالة salve(نص nomen) → نص {
    ثابت نص msg ← "مرحبا، §!"(nomen)
    أعد msg
}

بداية {
    ثابت نص m ← salve("عالم")
    اعرض m
}
```

嵌入在逻辑顺序 LTR 代码块内的从右到左文字。关键字在编译器的 HTML 诊断输出中被包裹在 `<bdi>`（双向隔离）中，以防止 RFO（右随左）扭曲。原始源代码使用逻辑顺序的阿拉伯文字；显示层处理双向呈现。

**हिन्दी** `hi`

```text
फलन salve(पाठ nomen) → पाठ {
    स्थिर पाठ msg ← "Salve, §!"(nomen)
    लौटा msg
}

आरंभ {
    स्थिर पाठ m ← salve("जगत")
    दिखा m
}
```

带有 matra/virama 辅音聚类的天城文。为更广泛的印度语系证明了路径——孟加拉语、泰米尔语、泰卢固语继承了相同的成形基础设施——尽管每个包的编写仍是独立的工作。印度数字字形（०-९）在数字字面量中不被接受；ASCII 数字在所有语言区域中保留。

**Tiếng Việt** `vi`

```text
hàm chào(vănbản tên) → vănbản {
    hằng vănbản lời_chào ← "Xin chào, §!"(tên)
    trả lời_chào
}

bắtđầu {
    hằng vănbản thông_điệp ← chào("thế giới")
    in thông_điệp
}
```

对照案例：拉丁文字但非英语。重度变音符号负载（ế、ệ、ả）对词法分析器中的 NFKC 边缘案例造成压力。防止一种在异国文字上有效但在带变音符号的拉丁文字上未经证实的架构。标识符使用越南语词汇（chào、tên、lời_chào、thông_điệp），由编译器逐字节保留。

> 字符（`← → ∴ ≡ ∪ ⇥`）、结构位置和标识符名称在上述所有六种渲染中都是**相同的**。只有关键字和类型名称改变。HIR 完全是同一个程序——编译器将这六种视为等价。将 Faber 渲染为泰语与将其渲染为 Rust 是相同的编译器操作：`HIR → surface`，两者均不享有特权。

## 本地化诊断 {#diagnostics}

诊断是**先于散文的结构化事实**。每个诊断都带有一个稳定的代码（`LEX###`、`PARSE###`、`SEM###`、`WARN###`）和命名参数；包拥有渲染的模板文本。这意味着诊断渲染器可以在任何语言区域中发射消息，而无需更改诊断基础设施。

阅读器语言区域示例包包含诊断测试案例——类型不匹配、未定义变量、非 ASCII 数字——证明整个管道是语言区域感知的：

- `examples/reader-locale/vi/src/type-mismatch.fab`
- `examples/reader-locale/vi/src/undefined-variable.fab`
- `examples/reader-locale/vi/src/non-ascii-number.fab`
- `examples/reader-locale/vi/src/keyword-suggestion.fab`
- `examples/reader-locale/vi/src/keyword-edit-distance.fab`

双向隔离是内置的：逻辑顺序 LTR 代码块内的阿拉伯语关键字在 HTML 输出中被包裹在 `<bdi>` 元素中，防止原本会使 RTL 运行不可读的 RFO（右随左）扭曲。

## 状态 {#status}

| 层 | 状态 |
|---|---|
| 包模式、别名、继承、验证、诊断、LLM 制品 | **已发布** |
| 包感知的词法分析、类型解析、清单/CLI 选择、可见回退 | **已发布** |
| 包拥有的诊断渲染、`faber explain`、双向隔离显示 | **已发布** |
| 规范 Faber 格式化 | **已发布** |
| 本地化 Faber 再发射（`format --reader-locale`） | 部分 |
| 标准库词汇覆盖层、测量的 LLM 发射保真度、完整的语言区域覆盖 | 延期 |
| 多语言文档生成 | 已提议 |

底层先决条件——词法入口处的 NFKC 规范化——已经落地。关键字表、诊断命名参数、渲染器和包交付均已发布。北极星层（本地化再发射、标准库词汇、LLM 发射基准、生成的多语言文档）仍然明确地处于部分或延期状态。

## 参考 {#references}

1. `radix/docs/design/reader-locale.md` —— 完整设计文档（69 KB）
2. `examples/reader-locale/` —— 6 个带有本地化源代码的语言区域包
3. `stdlib/reader/*/pack.toml` —— 7 个已安装的包定义
4. `radix/crates/radix/src/reader_locale.rs` —— 运行时实现
5. `radix/docs/design/faber-canonical-surface.md` —— 规范模式和 `faber format`
6. `radix/docs/factory/lex-nfkc-normalization/` —— NFKC 先决条件交付
