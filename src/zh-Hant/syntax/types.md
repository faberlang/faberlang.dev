+++
translation_kind = "translated"

title = "Data types"
section = "syntax"
order = 1
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
]


prose_hash = "sha256:b3f22d05ed3eb8bbc5d3322fd71f7677a77ba9909b6c80f1cfa00455320e7de5"
code_hash = "sha256:c2351c4cdd58a84dd89c4adc956cce28ce5d7a3db572eae85b44d4a6dbb5d48a"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber 採用靜態、型別優先的型別系統。每個宣告都將型別置於名稱之前：`textus nomen`，而非 `nomen: textus`。型別系統涵蓋純量原始型別、泛型集合、定寬數值、張量，以及面向 GPU 的暫存器型別。

## 原始型別 {#primitive-types}

| 型別 | 作用 | 字面值範例 |
|------|------|-------------|
| `textus` | Unicode 字串 | `"Salve, munde"` |
| `ascii` | 固定機器權杖 | `'solum:lege'` |
| `numerus` | 有號整數（預設為 i64） | `42` |
| `fractus` | 浮點數（預設為 f64） | `3.14` |
| `bivalens` | 布林值 | `verum`、`falsum` |
| `vacuum` | 單位／無值 | — |
| `nihil` | 空值／不存在 | `nihil` |
| `instans` | 持續時間／時間瞬間 | — |
| `json` | 編譯期 JSON 值 | `{ "key": "value" }` |
| `octeti` | 十六進位位元組序列 | \|00ff\| |

## 定寬數值型別 {#sized-numeric-types}

`numerus` 和 `fractus` 具有預設定寬（i64 和 f64），也支援明確指定定寬的形式：

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

在型別位置可使用定寬簡寫：`i8` … `u64`、`f16`、`f32`、`f64` 分別等同於 `numerus<W>`／`fractus<W>`。

## 可空型別 {#nullable-types}

可空值使用聯集語法 `T ∪ nihil`：

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio maybe() → textus ∪ nihil {
    redde nihil
}
```

Faber 不提供 `T?` 或 `Option<T>` 語法。聯集必須明確寫出。

## 型別別名 {#type-aliases}

```faber
typus UserId = numerus
```

## 泛型 {#generics}

函式、型別別名、`genus` 和 `implendum` 使用 `<T>` 語法接受型別參數：

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

支援在呼叫位置明確指定型別引數：

```faber
functio identitas<T>(T valor) → T { redde valor }

fixum numerus value ← identitas<numerus>(7)
```

## 集合 {#collections}

| 型別 | 作用 | 簡寫 |
|------|------|-------|
| `lista<T>` | 有序動態集合 | `lf32`、`lu32` |
| `tabula<K, V>` | 鍵值對映 | — |
| `tensor<T, Figura>` | 密集固定形狀緩衝區 | `tf32[4]`、`ti64[2,3]` |
| `sparsa<T, Figura>` | 稀疏固定形狀緩衝區 | `sf32[4]`、`si64[2,3]` |
| `intervallum` | 範圍型別 | — |
| `copia<T>` | 無序集合 | — |
| `cursor<T>` | 惰性串流 | — |

```faber
fixum lista<numerus> nums ← [1, 2, 3]
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## 張量型別 {#tensor-types}

`tensor<T, Figura>` 是密集固定形狀容器：

| 形式 | 意義 |
|---------|---------|
| `tensor<T, Figura>` | 標準拼寫 |
| `tensor<T, []>` | 秩 0（純量容器） |
| `tensor<T, _>` | 形狀推論缺口 |
| `tensor<T, [N]>` | 秩 1 向量 |
| `tensor<T, [N, M]>` | 秩 2 矩陣 |

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

## GPU 核心型別 {#gpu-core-types}

系統層會辨識這些型別，以支援 GPU 與暫存器工作。
不具備硬體支援的套件目標會拒絕這些型別：

```faber
functio half(f16 x) → f16 { redde x }

functio add(matrix<f32, [2, 2]> a, matrix<f32, [2, 2]> b) → matrix<f32, [2, 2]> {
    redde a.addita(b)
}

functio swap(atomic<i32> cell, i32 value) → i32 {
    redde cell.exchange(value)
}
```

## 型別上的借用標記 {#borrow-markers}

借用標記（`de`、`in`、`ex`）可出現在參數位置的型別上，用來指出值的傳遞方式：

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

## 比較規則 {#comparison-policy}

| 運算子 | 類別 | 行為 |
|----------|--------|-----------|
| `≡`、`≠` | 精確相等 | 必須使用相同型別；`nihil` 可略過此要求 |
| `≈`、`≉` | 數值相等 | 僅限數值格 |
| `<`、`≤`、`>`、`≥` | 排序 | 數值、瞬間、純量文字 |
| `intra` | 範圍包含 | 數值位於範圍內 |
| `inter` | 集合成員資格 | 元素位於集合內 |
