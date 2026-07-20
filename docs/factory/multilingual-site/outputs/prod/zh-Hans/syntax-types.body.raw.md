Faber 拥有静态、类型优先的类型系统。每个声明都把类型放在名称之前：`textus nomen`，而不是 `nomen: textus`。类型系统涵盖标量原语、泛型集合、定宽数值、张量，以及面向 GPU 的寄存器类型。

## 原语类型 {#primitive-types}

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

## 定宽数值类型 {#sized-numeric-types}

`numerus` 和 `fractus` 拥有默认位宽（i64 和 f64）以及显式位宽形式：

<<<FENCE 0>>>

类型位置支持位宽简写：`i8` … `u64`、`f16`、`f32`、`f64` 等价于 `numerus<W>` / `fractus<W>`。

## 可空类型 {#nullable-types}

可空值使用联合语法 `T ∪ nihil`：

<<<FENCE 1>>>

Faber 中没有 `T?` 或 `Option<T>` 语法。联合是显式的。

## 类型别名 {#type-aliases}

<<<FENCE 2>>>

## 泛型 {#generics}

函数、类型别名、`genus` 和 `implendum` 接受使用 `<T>` 语法的类型参数：

<<<FENCE 3>>>

支持在调用处显式指定类型参数：

<<<FENCE 4>>>

## 集合 {#collections}

| 类型 | 作用 | 简写 |
|------|------|-------|
| `lista<T>` | 有序动态集合 | `lf32`, `lu32` |
| `tabula<K, V>` | 键值映射 | — |
| `tensor<T, Figura>` | 稠密定形缓冲区 | `tf32[4]`, `ti64[2,3]` |
| `sparsa<T, Figura>` | 稀疏定形缓冲区 | `sf32[4]`, `si64[2,3]` |
| `intervallum` | 区间类型 | — |
| `copia<T>` | 无序集合 | — |
| `cursor<T>` | 惰性流 | — |

<<<FENCE 5>>>

## 张量类型 {#tensor-types}

`tensor<T, Figura>` 是稠密定形容器：

| 形式 | 含义 |
|------|---------|
| `tensor<T, Figura>` | 规范写法 |
| `tensor<T, []>` | 0 阶（标量容器） |
| `tensor<T, _>` | 形状推断占位符 |
| `tensor<T, [N]>` | 1 阶向量 |
| `tensor<T, [N, M]>` | 2 阶矩阵 |

<<<FENCE 6>>>

## GPU 核心类型 {#gpu-core-types}

这些类型由系统通道识别，用于 GPU 和寄存器相关工作。缺乏硬件支持的包目标会拒绝它们：

<<<FENCE 7>>>

## 类型上的借用标记 {#borrow-markers}

借用标记（`de`、`in`、`ex`）可以出现在参数位置的类型上，用于表示值的传递方式：

<<<FENCE 8>>>

## 比较策略 {#comparison-policy}

| 运算符 | 家族 | 行为 |
|----------|--------|-----------|
| `≡`, `≠` | 精确相等 | 要求类型完全相同；`nihil` 旁路 |
| `≈`, `≉` | 数值相等 | 仅限数值格 |
| `<`, `≤`, `>`, `≥` | 排序 | 数值、时间点、标量文本 |
| `intra` | 区间包含 | 数值在区间内 |
| `inter` | 集合归属 | 元素在集合中 |
