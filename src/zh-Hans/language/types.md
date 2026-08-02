+++
translation_kind = "translated"

title = "Types and values"
section = "language"
order = 2
sources = [
  "radix/README.md (Core Type Surfaces, Numeric Widths, Tensors And Sparsa, GPU Core Types)",
  "radix/docs/design/numeric-type-sugar.md",
  "radix/docs/design/tensor-intrinsics.md",
  "radix/docs/design/lista-intrinsics.md",
  "radix/docs/design/comparison-operators.md",
  "radix/EBNF.md",
  "examples/corpus/typi/",
  "examples/corpus/tensor/",
  "examples/corpus/lista/",
  "radix/README.md (Runtime binding vs structural definition, Language Orientation)",
  "examples/corpus/fixum/",
  "examples/corpus/sit/",
  "radix/README.md (Tensors And Sparsa)",
  "radix/docs/design/tabula-intrinsics.md",
  "examples/corpus/tabula/",
  "examples/corpus/sparsa/",
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
  "radix/README.md (Nullability and Optionality)",
  "examples/corpus/nihil/",
  "examples/corpus/sponte/",
  "examples/corpus/nonnihil/",
  "radix/README.md (Conversion and Construction)",
  "radix/docs/design/conversio-valor.md",
  "radix/docs/design/failable-conversio.md",
]
+++

## Data types

Faber 拥有静态、类型优先的类型系统。每个声明都把类型放在名称之前：`textus nomen`，而不是 `nomen: textus`。类型系统涵盖标量原语、泛型集合、定宽数值、张量，以及面向 GPU 的寄存器类型。

### 原语类型 {#primitive-types}

| 类型 | 作用 | 示例字面量 |
|------|------|-----------------|
| `textus` | Unicode 字符串 | `"Salve, munde"` |
| `ascii` | 固定机器令牌 | `'solum:lege'` |
| `numerus` | 有符号整数（默认 i64） | `42` |
| `fractus` | 浮点数（默认 f64） | `3.14` |
| `bivalens` | 布尔值 | `verum`, `falsum` |
| `vacuum` | 单元类型 / 无值 | — |
| `nihil` | 空值 / 缺失 | `nihil` |
| `instans` | 时长 / 时间点 | — |
| `json` | 编译期 JSON 值 | `{ "key": "value" }` |
| `octeti` | 十六进制字节序列 | \|00ff\| |

### 定宽数值类型 {#sized-numeric-types}

`numerus` 和 `fractus` 拥有默认位宽（i64 和 f64）以及显式位宽形式：

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

类型位置支持位宽简写：`i8` … `u64`、`f16`、`f32`、`f64` 等价于 `numerus<W>` / `fractus<W>`。

### 可空类型 {#nullable-types}

可空值使用联合语法 `T ∪ nihil`：

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio maybe() → textus ∪ nihil {
    redde nihil
}
```

Faber 中没有 `T?` 或 `Option<T>` 语法。联合是显式的。

### 类型别名 {#type-aliases}

```faber
typus UserId = numerus
```

### 泛型 {#generics}

函数、类型别名、`genus` 和 `implendum` 接受使用 `<T>` 语法的类型参数：

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

支持在调用处显式指定类型参数：

```faber
functio identitas<T>(T valor) → T { redde valor }

fixum numerus value ← identitas<numerus>(7)
```

### 集合 {#collections}

| 类型 | 作用 | 简写 |
|------|------|-------|
| `lista<T>` | 有序动态集合 | `lf32`, `lu32` |
| `tabula<K, V>` | 键值映射 | — |
| `tensor<T, Figura>` | 稠密定形缓冲区 | `tf32[4]`, `ti64[2,3]` |
| `sparsa<T, Figura>` | 稀疏定形缓冲区 | `sf32[4]`, `si64[2,3]` |
| `intervallum` | 区间类型 | — |
| `copia<T>` | 无序集合 | — |
| `cursor<T>` | 惰性流 | — |

```faber
fixum lista<numerus> nums ← [1, 2, 3]
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

### 张量类型 {#tensor-types}

`tensor<T, Figura>` 是稠密定形容器：

| 形式 | 含义 |
|------|---------|
| `tensor<T, Figura>` | 规范写法 |
| `tensor<T, []>` | 0 阶（标量容器） |
| `tensor<T, _>` | 形状推断占位符 |
| `tensor<T, [N]>` | 1 阶向量 |
| `tensor<T, [N, M]>` | 2 阶矩阵 |

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

### GPU 核心类型 {#gpu-core-types}

这些类型由系统通道识别，用于 GPU 和寄存器相关工作。缺乏硬件支持的包目标会拒绝它们：

```faber
functio half(f16 x) → f16 { redde x }

functio add(matrix<f32, [2, 2]> a, matrix<f32, [2, 2]> b) → matrix<f32, [2, 2]> {
    redde a.addita(b)
}

functio swap(atomic<i32> cell, i32 value) → i32 {
    redde cell.exchange(value)
}
```

### 类型上的借用标记 {#borrow-markers}

借用标记（`de`、`in`、`ex`）可以出现在参数位置的类型上，用于表示值的传递方式：

```faber locale=la
# shared borrow — caller retains ownership
functio imprime(de textus label) → vacuum { }

# mutable borrow — caller lends mutable access
functio duplica(in numerus value) → vacuum { }

# move — caller gives up ownership
functio consume(ex textus buffer) → textus {
    redde buffer
}
```

### 比较策略 {#comparison-policy}

| 运算符 | 家族 | 行为 |
|----------|--------|-----------|
| `≡`, `≠` | 精确相等 | 要求类型完全相同；`nihil` 旁路 |
| `≈`, `≉` | 数值相等 | 仅限数值格 |
| `<`, `≤`, `>`, `≥` | 排序 | 数值、时间点、标量文本 |
| `intra` | 区间包含 | 数值在区间内 |
| `inter` | 集合归属 | 元素在集合中 |

## Variables and binding

Faber 拥有三个变量关键字和一个专门的赋值符。核心区别在于 `fixum`（一次写入）与 `varia`（可自由重赋值），以及 `←`（运行时流）与 `=`（结构体字段形状）。

### fixum — 不可变绑定 {#fixum-immutable-binding}

`fixum` 绑定只能写入一次。声明时可带或不带初始化式；若声明时不带，则必须在读取之前精确赋值一次。第二次赋值会被拒绝。

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

延迟初始化：

```faber
incipit {
    fixum numerus factor
    si verum {
        factor ← 10
    } secus {
        factor ← 100
    }
    nota factor
}
```

### varia — 可变绑定 {#varia-mutable-binding}

`varia` 绑定可自由重赋值：

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

### sit — 推断不可变语法糖 {#sit-inferred-immutable-sugar}

`sit` 是 `fixum _` 的语法糖——一种类型推断的不可变绑定：

```faber
incipit {
    sit salve ← "Salve"
    sit nomen ← "Marcus"
    sit x ← 42

    # Deferred form
    sit label
    label ← "deferred"
}
```

### 运行时绑定与结构体定义 {#runtime-binding-vs-structural-definition}

Faber 将大多数语言合并为 `=` 的语义拆分为两种：

| 符号 | 角色 | 用途 |
|-------|------|---------|
| `←` | 运行时流 | 初始绑定、重赋值、变更 |
| `=` | 结构形状 | 字面量与元数据内的字段名 |

```faber
genus Point {
    numerus x
    numerus y
}

incipit {
    # Runtime: ← attaches a value to a name at execution time
    varia numerus count ← 0
    varia textus label ← "ready"
    count ← count + 1

    # Structural: = defines field values inside a type literal
    fixum _ p ← Point {
        x = 10,
        y = 20
    }
}
```

### ex 字段提取 {#ex-field-extraction}

`ex` 将值的字段提取为局部绑定：

```faber
genus Persona {
    textus nomen
    numerus aetas
}

incipit {
    fixum _ p ← Persona { nomen = "Marcus", aetas = 30 }
    ex p fixum nomen, aetas
    # prints "Marcus"
    nota nomen
}
```

### 后缀自增与自减 {#postfix-increment-and-decrement}

`⊕` 和 `⊖` 是用于可变 `numerus` 位置的后缀自增/自减语句。它们仅作为语句使用——没有表达式值，也没有前缀形式：

```faber
incipit {
    varia numerus i ← 0
    # i becomes 1
    i ⊕
    # i becomes 0
    i ⊖
}
```

## Collections

Faber 拥有多种由编译器内置的集合类型。其规范方法位于编译器中，而非标准库中。

### Lista — 有序动态集合 {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

使用 `sparge` 展开：

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

关键方法：`longitudo`、`accipe`、`appende`、`summa`、`primus`、`novissimus`。

### Tabula — 键值映射 {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

### Tensor — 密集定形缓冲区 {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

Tensor 语法糖（用于数值密集型代码）：

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

关键方法：`forma`、`accipe`、`ponde`、`crea`、`structa`、`strue`，以及逐元素算术、矩阵乘法（`multiplicatio`）和归约（`summa`、`productum`）。

### Sparsa — 稀疏定形缓冲区 {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

密集与稀疏之间的转换：

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

### 游标 — 惰性流 {#cursors}

`cursor<T>` 是一种惰性流类型。可由集合迭代器、tuus 视图或生成器函数创建。通过 `itera ex` 消费：

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

### Intervallum — 范围 {#intervallum}

```faber
# exclusive range: 0, 1, 2, 3, 4
itera ab 0‥5 fixum i {
    nota i
}
# inclusive range: 0, 1, 2, 3, 4, 5
itera ab 0…5 fixum i {
    nota i
}
```

`‥` 是排他范围的端点；`…` 是包含端点。

## String and template literals

Faber 使用分隔符语义 — 每种引号形式表示不同的源代码形态。它们之间不能互换。

### 字面量形式 {#literal-forms}

| 形式 | 类型 | 角色 |
|------|------|------|
| `'…'` | `ascii` | 固定机器令牌；无 `§`；无 `(…)` |
| `"…"` | `textus` | 短 Unicode 单行字符串；`(…)` 渲染 |
| `«…»` | `textus` | 块/多行 Unicode；`(…)` 渲染 |
| `` `…` `` | `forma` | 捕获模板；`(…)` 捕获 |
| `{ … }` | `json` | 编译期 JSON 文档 |
| `|…|` | `octeti` | 编译期十六进制字节 |
| `[ … ]` | `lista<T>` | Faber 列表字面量 |

### 字符串模板应用 {#string-template-application}

Faber 通过字符串模板应用格式化文本：一个带有 `§` 占位符的 `"…"` 或 `«…»` 字面量，后接括号参数：

```faber
functio greet(textus nomen) → textus {
    redde "Salve, §!"(nomen)
}

fixum numerus pagina ← 3
fixum numerus totum ← 10
fixum textus code ← "200"
fixum textus label ← "OK"

fixum _ msg ← "Page § of §"(pagina, totum)
fixum _ block ← «status: § (§)»(code, label)
```

关键规则：
- `§` (U+00A7) 是模板占位符
- 位置占位符：`§0`、`§1`、…… 用于显式排序
- 结尾的 `!` 选择显示格式化：`"Salve, §!"(nomen)`
- `(args)` 后缀是模板应用，不是函数调用

### 块字符串 {#block-strings}

多行块使用书名号 `«…»`：

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

### 捕获模板 (forma) {#captured-templates}

反引号模板捕获文本和参数而不渲染。
对于绑定的 SQL/URL 载荷是安全的：

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

### 内联 JSON {#inline-json}

裸 `{ … }` 是内联 JSON：一个编译期的 `json` 文档，不是匿名的 Faber 对象。键是用 `:` 分隔的带引号字符串：

```faber
fixum _ empty ← {}
fixum _ user ← { "name": "Marcus", "age": 30, "active": true }
fixum _ nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
```

若要构造有类型的属，请使用类型名和 `=` 字段形态：

```faber
genus Point {
    numerus x
    numerus y
}
fixum _ p ← Point { x = 10, y = 20 }
```

## Nullability and optionality

Faber 在值层面区分"空缺"与声明位置的"可选提供"。

### 可空值 — T ∪ nihil {#nullable-values}

当值可能缺失时，使用 `T ∪ nihil`：

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### 可选声明槽 — sponte {#optional-declaration-slots}

当参数或字段可由调用者或构造函数省略时，在名称之后使用 `sponte`：

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

借用标记可与可选参数组合使用：

```faber
functio process(de numerus depth sponte) → vacuum { }
```

### 非空断言 — ! {#non-null-assertion}

使用 `!.`, `![`, `!(` 来断言某个可空值不是 `nihil`：

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

对 `nihil` 进行非空断言会在运行时中止。

### 空值合并 — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

### ignotum {#ignotum}

`ignotum` 是用于应急通道和不完整知识的顶层未知类型。它不是一种可空性机制。

## Conversion and construction

两个重要的转换运算符,一个用于运行时,一个用于编译时:

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus value ← 7
fixum _ text ← value ∷ textus
```

### 运行时转换 — ↦ {#runtime-conversion}

使用 `↦` 进行运行时转换,尤其是可能失败的解析或强制转换。用 `⇥` 提供内联恢复:

```faber
fixum textus input ← "9"
fixum _ n ← "42" ↦ numerus
fixum _ safe ← input ↦ numerus ⇥ 0
```

类型驱动的具象化:

```faber
fixum textus path ← "/etc/hosts"
fixum _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
fixum _ body ← ad 'solum:lege' (path) ↦ textus
```

### 静态标注 — ∷ {#static-ascription}

使用 `∷` 进行显式静态类型标注。它是后置的,并且由目标类型驱动:

```faber
fixum numerus value ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

### 空值合并 — vel {#nullish-coalescing}

当值为 `nihil` 时,使用 `vel` 进行空值合并:

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
