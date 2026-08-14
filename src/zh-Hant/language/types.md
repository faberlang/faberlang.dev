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
  "faber/docs/EBNF.md",
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

Faber 採用靜態、型別優先的型別系統。每個宣告都將型別置於名稱之前：`textus nomen`，而非 `nomen: textus`。型別系統涵蓋純量原始型別、泛型集合、定寬數值、張量，以及面向 GPU 的暫存器型別。

### 原始型別 {#primitive-types}

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

### 定寬數值型別 {#sized-numeric-types}

`numerus` 和 `fractus` 具有預設定寬（i64 和 f64），也支援明確指定定寬的形式：

```faber
fixum numerus<i32> narrow ← 7 ∷ numerus<i32>
fixum numerus<u64> wide ← 255 ∷ numerus<u64>
fixum fractus<f32> single ← 1.5 ∷ fractus<f32>
```

在型別位置可使用定寬簡寫：`i8` … `u64`、`f16`、`f32`、`f64` 分別等同於 `numerus<W>`／`fractus<W>`。

### 可空型別 {#nullable-types}

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

### 型別別名 {#type-aliases}

```faber
typus UserId = numerus
```

### 泛型 {#generics}

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

### 集合 {#collections}

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

### 張量型別 {#tensor-types}

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

### GPU 核心型別 {#gpu-core-types}

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

### 型別上的借用標記 {#borrow-markers}

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

### 比較規則 {#comparison-policy}

| 運算子 | 類別 | 行為 |
|----------|--------|-----------|
| `≡`、`≠` | 精確相等 | 必須使用相同型別；`nihil` 可略過此要求 |
| `≈`、`≉` | 數值相等 | 僅限數值格 |
| `<`、`≤`、`>`、`≥` | 排序 | 數值、瞬間、純量文字 |
| `intra` | 範圍包含 | 數值位於範圍內 |
| `inter` | 集合成員資格 | 元素位於集合內 |

## Variables and binding

Faber 有三個變數關鍵字，以及專用的指派字元。關鍵差異在於 `fixum`（只能寫入一次）與 `varia`（可自由重新指派），以及 `←`（執行期流程）與 `=`（結構欄位形狀）之間的區別。

### fixum — 不可變繫結 {#fixum-immutable-binding}

`fixum` 繫結只能寫入一次。宣告時可以提供初始值，也可以不提供；若未提供初始值，則必須在讀取前恰好指派一次。第二次指派會被拒絕。

```faber
fixum numerus count ← 0
fixum textus name ← "Marcus"
fixum _ inferred ← [1, 2, 3]
```

延遲初始化：

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

### varia — 可變繫結 {#varia-mutable-binding}

`varia` 繫結可以自由重新指派：

```faber
incipit {
    varia numerus count ← 0
    count ← count + 1
    count ← count * 2
}
```

### sit — 推導的不可變語法糖 {#sit-inferred-immutable-sugar}

`sit` 是 `fixum _` 的語法糖——具有推導型別的不可變繫結：

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

### 執行期繫結與結構定義 {#runtime-binding-vs-structural-definition}

Faber 將多數語言合併在 `=` 中的概念分開：

| 字元 | 作用 | 用於 |
|-------|------|---------|
| `←` | 執行期流程 | 初始繫結、重新指派、變更 |
| `=` | 結構形狀 | 常值與中繼資料中的欄位名稱 |

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

### ex 欄位擷取 {#ex-field-extraction}

`ex` 將值中的欄位擷取至區域繫結：

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

### 後置遞增與遞減 {#postfix-increment-and-decrement}

`⊕` 與 `⊖` 是可變 `numerus` 儲存處的後置遞增／遞減陳述式。它們只能作為陳述式使用——沒有運算式值，也沒有前置形式：

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

Faber 有數種由編譯器擁有的集合型別。它們的標準方法定義於編譯器中，而非標準函式庫。

### Lista — 有序動態集合 {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

使用 `sparge` 展開：

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

主要方法：`longitudo`、`accipe`、`appende`、`summa`、`primus`、`novissimus`。

### Tabula — 鍵值對映射 {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

### Tensor — 密集固定形狀緩衝區 {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

Tensor 語法糖（數值運算密集的程式碼）：

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

主要方法：`forma`、`accipe`、`ponde`、`crea`、`structa`、`strue`，以及逐元素算術、矩陣乘法（`multiplicatio`）和歸約（`summa`、`productum`）。

### Sparsa — 稀疏固定形狀緩衝區 {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

在密集與稀疏格式之間轉換：

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

### Cursors — 延遲串流 {#cursors}

`cursor<T>` 是延遲串流型別。它可以由集合迭代器、`tuus` 檢視或產生器函式建立。使用 `itera ex` 消費：

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

### Intervallum — 範圍 {#intervallum}

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

`‥` 表示不包含終點的範圍；`…` 表示包含終點的範圍。

## String and template literals

Faber 使用分隔符語義——每種引號形式都代表不同的原始碼形狀。它們不是可互換的同義詞。

### 字面形式 {#literal-forms}

| 形式 | 類型 | 作用 |
|------|------|------|
| `'…'` | `ascii` | 固定機器標記；不含 `§`；不含 `(…)` |
| `"…"` | `textus` | 短 Unicode 行字串；可解析 `(…)` |
| `«…»` | `textus` | 區塊／多行 Unicode；可解析 `(…)` |
| `` `…` `` | `forma` | 擷取的範本；可擷取 `(…)` |
| `{ … }` | `json` | 編譯期 JSON 文件 |
| `|…|` | `octeti` | 編譯期十六進位位元組 |
| `[ … ]` | `lista<T>` | Faber 清單字面值 |

### 字串範本套用 {#string-template-application}

Faber 使用字串範本套用來格式化文字：先寫入含有 `§` 佔位符的 `"…"` 或 `«…»` 字面值，再接上括號引數：

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

主要規則：

- `§`（U+00A7）是範本佔位符
- 位置佔位符：`§0`、`§1`、…，用於明確指定順序
- 尾端的 `!` 選取顯示格式：`"Salve, §!"(nomen)`
- `(args)` 尾碼是範本套用，不是函式呼叫

### 區塊字串 {#block-strings}

多行區塊使用書名號 `«…»`：

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

### 擷取的範本（forma） {#captured-templates}

反引號範本會擷取文字與參數，但不進行解析。
適合用於繫結的 SQL／URL 承載內容：

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

### 內嵌 JSON {#inline-json}

裸露的 `{ … }` 是內嵌 JSON：它是編譯期的 `json` 文件，不是匿名的 Faber 物件。鍵是以引號括起、並以 `:` 分隔的字串：

```faber
fixum _ empty ← {}
fixum _ user ← { "name": "Marcus", "age": 30, "active": true }
fixum _ nested ← { "meta": { "version": 1 }, "tags": ["alpha", "beta"] }
```

若要建構具型別的 `genus`，請使用型別名稱與 `=` 欄位形狀：

```faber
genus Point {
    numerus x
    numerus y
}
fixum _ p ← Point { x = 10, y = 20 }
```

## Nullability and optionality

Faber 區分值中的缺失與宣告位置上的可選提供。

### 可為空值 — T ∪ nihil {#nullable-values}

當值可能缺失時，使用 `T ∪ nihil`：

```faber
functio find(textus key) → numerus ∪ nihil {
    redde nihil
}

functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### 可選宣告槽位 — sponte {#optional-declaration-slots}

當參數或欄位可由呼叫者或建構函式省略時，在名稱後使用 `sponte`：

```faber
functio connect(textus host, numerus port sponte) → vacuum { }

genus User {
    textus email sponte
}
```

借用標記可以與可選參數結合：

```faber
functio process(de numerus depth sponte) → vacuum { }
```

### 非空值斷言 — ! {#non-null-assertion}

使用 `!.`、`![`、`!(` 來斷言可為空值不是 `nihil`：

```faber
genus Box { numerus ∪ nihil val }
fixum Box ∪ nihil maybe_name ← Box { val = 7 }
fixum _ name ← maybe_name!.val
```

對 `nihil` 進行非空值斷言會在執行階段中止。

### 空值合併 — vel {#nullish-coalescing}

```faber
fixum textus ∪ nihil provided ← nihil
fixum _ name ← provided vel "default"
```

### ignotum {#ignotum}

`ignotum` 是頂層未知型別，用於逃生閘道與不完整的知識。它不是可為空值的機制。

## Conversion and construction

兩個重要的轉換運算子，一個用於執行期，另一個用於編譯期：

```faber
# runtime conversion
fixum _ parsed ← "42" ↦ numerus
# static ascription
fixum numerus value ← 7
fixum _ text ← value ∷ textus
```

### 執行期轉換 — ↦ {#runtime-conversion}

使用 `↦` 進行執行期轉換，尤其適用於可能失敗的剖析或強制轉型。使用 `⇥` 提供行內復原：

```faber
fixum textus input ← "9"
fixum _ n ← "42" ↦ numerus
fixum _ safe ← input ↦ numerus ⇥ 0
```

由型別導向的具現化：

```faber
fixum textus path ← "/etc/hosts"
fixum _ lanes ← [1.0, 2.0, 3.0, 4.0] ↦ vf32[4]
fixum _ body ← ad 'solum:lege' (path) ↦ textus
```

### 靜態歸屬 — ∷ {#static-ascription}

使用 `∷` 明確標註靜態型別。它是後綴運算子，並由目標型別決定：

```faber
fixum numerus value ← 7
fixum _ x ← 7 ∷ numerus<i32>
fixum _ text ← value ∷ textus
```

### 空值合併 — `vel` {#nullish-coalescing}

當值為 `nihil` 時，使用 `vel` 進行空值合併：

```faber
fixum textus ∪ nihil provided_name ← nihil
fixum _ name ← provided_name vel "default"
```
