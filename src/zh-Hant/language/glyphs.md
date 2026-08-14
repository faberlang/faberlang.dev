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
  "faber/docs/EBNF.md",
]
+++

## Glyphs and operators

Faber 使用符號，其中符號本身具有結構意義。以下是詞法分析器所辨識的完整來源符號清單。

### 值流程 {#value-flow}

| 符號 | 意義 |
|-------|---------|
| `←` | 執行期繫結、重新指派與變更 |
| `→` | 函式回傳型別 |
| `⇥` | 替代退出 — 錯誤通道型別或內嵌轉換復原 |
| `∴` | 閉包連接符 — 將閉包體與其簽名相連（`(a, b) → T ∴ a + b`） |

### 型別形狀 {#type-shape}

| 符號 | 意義 |
|-------|---------|
| `∷` | 靜態型別標註（編譯期轉型） |
| `↦` | 執行期轉換（可能失敗的剖析／強制轉型） |
| `∪` | 內嵌聯集型別（`T ∪ nihil`） |

### 比較 {#comparison}

| 符號 | 意義 |
|-------|---------|
| `≡` `≠` | 精確相等與不相等 |
| `<` `>` `≤` `≥` | 順序比較 |
| `≈` `≉` | 數值相等 |

### 邏輯與位元運算 {#logical-and-bitwise}

| 符號 | 意義 |
|-------|---------|
| `∧` `∨` `⊻` `¬` | 且、或、互斥或、非 |
| `⇐` `⇒` | 左移與右移 |

### 指派更新 {#assignment-updates}

| 符號 | 意義 |
|-------|---------|
| `←` | 運算式中唯一的指派運算子 |
| `⊕` `⊖` | 後置遞增／遞減述句（僅限可變的 `numerus`） |

### 選用鏈結與非空斷言 {#optional-chaining-and-non-null-assertion}

| 符號 | 意義 |
|-------|---------|
| `?` `?.` `?[` `?(` | 選用鏈結 |
| `!` `!.` `![` `!(` | 非空斷言 |

### 範圍 {#ranges}

| 符號 | 意義 |
|-------|---------|
| `‥` | 不包含終點的範圍端點 |
| `…` | 包含終點的範圍端點 |

### 字面值分隔符 {#literal-delimiters}

| 符號 | 型別 | 作用 |
|-------|------|------|
| `'` | `ascii` | 固定的機器符號 |
| `"` | `textus` | 行字串 |
| `«` `»` | `textus` | 區塊字串（書名號） |
| `` ` `` | `forma` | 擷取的範本 |
| `|` | `octeti` | 十六進位字面值 |
| `§` | 範本插槽 | `"…"`、`«…»`、`` `…` `` 內的預留位置 |

### 標點符號 {#punctuation}

| 符號 | 作用 |
|-------|------|
| `(` `)` | 分組與呼叫 |
| `{` `}` | 區塊、`genus` 字面值或 JSON 文件 |
| `[` `]` | 清單字面值與索引 |
| `.` | 成員存取 |
| `,` | 分隔符 |
| `;` | 述句分隔符 |
| `:` | JSON 欄位分隔符 |
| `=` | 結構欄位形狀（不是執行期指派） |
| `@` | 註解標記 |
| `#` | 行註解 |

## Latin vocabulary and structural glyphs

*三個訊號選擇，讓 Faber 原始碼一眼即可辨識。*

Faber 有意採用三個彼此協作的訊號選擇，打造出語法形狀穩定的原始碼。讀者無須先知道程式碼將編譯至哪個目標後端，就能看出每個建構的語意角色。

### 三個訊號 {#three}

| 訊號 | 範例 | 角色 |
|--------|----------|------|
| 型別優先宣告 | `textus nomen`、`numerus aetas` | 形狀朝向綁定——先型別，再名稱。 |
| 拉丁文行為詞 | `functio`、`genus`、`si`、`redde`、`fixum` | 宣告、陳述式、生命週期與行為意圖。 |
| 結構字形 | `← → ∴ ≡ ∪ ⇥` | 值流、型別流與結構接點——通用，永不在地化。 |

這三者經過設計，能彼此強化。熟悉某個語系的 Faber 讀者，可以閱讀任何語系的內容，因為字形與結構永遠不變。熟悉 Rust 後端的讀者，也仍能辨識 Faber 原始碼，因為拉丁文關鍵字與型別優先的順序，會產生獨特的視覺風格。

### 型別優先宣告 {#type-first}

Faber 在每個宣告中都將型別放在名稱之前。這與主流 C 家族語法相反，而且是刻意如此：

| 建構 | C 家族慣例 | Faber |
|-----------|----------------|-------|
| 變數 | `int count = 0` | `numerus count ← 0` |
| 函式 | `fn greet(name: String) → String` | `functio salve(textus nomen) → textus` |
| 參數 | `(String name)` | `(textus nomen)` |

型別優先宣告讓資料的形狀成為讀者首先看到的內容。這自然符合按語意廣度由左至右閱讀的語言——中文、印地語與阿拉伯語的宣告也遵循相同順序。

```faber
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

### 拉丁文行為詞彙 {#latin}

Faber 使用拉丁文詞彙表示每個具有行為或文法形狀的建構。這套詞彙規模小且規則一致，取自單一的古典來源，而非多數程式語言所採用的混合詞源。

#### 宣告 {#declarations}

| 關鍵字 | 角色 | 約略對應 |
|---------|------|------------------------|
| `functio` | 宣告具名函式或方法 | `fn`、`def`、`function` |
| `genus` | 宣告帶有欄位的具體型別 | `class`、`struct` |
| `implendum` | 宣告行為契約 | `interface`、`trait` |
| `typus` | 宣告型別別名 | `typedef`、`type` |
| `discretio` | 宣告標籤聯合 | `enum`、`sum type` |

#### 綁定與轉移 {#bindings-and-transfer}

| 關鍵字 | 角色 | 約略對應 |
|---------|------|------------------------|
| `fixum` | 不可變綁定（寫入一次） | `let`、`const` |
| `varia` | 可變綁定 | `let mut`、`var` |
| `sit` | 簡潔的推導型別不可變綁定 | `let`（推導型別） |
| `redde` | 從函式傳回值 | `return` |
| `iace` | 在錯誤通道上拋出錯誤 | `throw`、`raise` |
| `mori` | 延後處理——尚未能表達的行為 | `unimplemented!`、`todo` |

#### 控制流程 {#control-flow}

| 關鍵字 | 角色 | 約略對應 |
|---------|------|------------------------|
| `si` | 條件分支 | `if` |
| `sin` | 其他條件分支 | `else if` |
| `secus` | 其他分支 | `else` |
| `dum` | While 迴圈 | `while` |
| `itera` | 迭代（值、鍵或範圍） | `for` |
| `elige` | 模式比對（第一個分支優先） | `match`、`switch` |
| `fac` | 具錯誤復原的嘗試區塊 | `try`、`do` |
| `cape` | `fac` 的錯誤處理器 | `catch` |

> 拉丁文詞彙是**可綁定的**——它隨附於標準詞彙包，但可透過讀者語系重新映射。泰語程式設計師會看到 `ถ้า` 而不是 `si`；中文程式設計師會看到 `函數` 而不是 `functio`。詞彙並不享有特權；只有文法不變。

### 結構字形 {#glyphs}

行為詞彙使用拉丁文，而結構意義使用通用字形。這些字形永不在地化，也不會在不同轉譯中改變意義。無論關鍵字以哪種人類語言呈現，它們都是讓 Faber 原始碼保持可辨識的視覺錨點。

#### 值流 {#value-flow}

| 字形 | 意義 |
|-------|---------|
| `←` | 執行期綁定、重新指派與變異——唯一的指派運算子 |
| `→` | 函式回傳型別宣告 |
| `⇥` | 替代出口：錯誤通道型別或行內轉換復原 |
| `∴` | 閉包連接符 — 將閉包體與其簽名相連 |

#### 型別形狀 {#type-shape}

| 字形 | 意義 |
|-------|---------|
| `∷` | 靜態型別標註——對值型別的編譯期斷言 |
| `↦` | 執行期轉換——可能失敗的解析或強制轉型 |
| `∪` | 行內聯合型別——連接兩個型別（例如 `T ∪ nihil`） |

#### 比較與邏輯 {#comparison-and-logic}

| 字形 | 意義 |
|-------|---------|
| `≡` `≠` | 精確相等與不相等——必須符合嚴格型別 |
| `<` `>` `≤` `≥` | 順序比較 |
| `∧` `∨` `⊻` `¬` | 邏輯與位元運算：且、或、異或、非 |

#### 綁定慣例很重要 {#the-binding-convention-matters}

有一個字形選擇值得特別注意，因為它是新讀者最常混淆的地方：

| 字形 | 角色 | 用於 |
|-------|------|---------|
| `←` | **執行期流動** | 執行時的初始綁定、重新指派與變異 |
| `=` | **結構形狀** | 常值中的欄位名稱與宣告中繼資料——不是執行期儲存 |

多數語言會重載 `=`，同時表示「在型別中定義此欄位」與「將執行期值放入此變數」。Faber 將這兩項工作分開。每個 `←` 都是即時資料流；每個 `Type { … }` 中的 `=` 都表示 `genus` 的欄位配置。

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

### 與主流語言比較 {#compare}

下表展示常見程式語言模式如何對應至 Faber 的三訊號系統。Faber 欄位會針對每個不同的語意工作使用不同的字形或關鍵字——不進行重載。

| 語意工作 | 其他語言常見寫法 | Faber |
|--------------|---------------------------|-------|
| 參數型別宣告 | `name: String` | `textus nomen` |
| 回傳型別 | `→ String`、`: String` | `→` `textus` |
| 執行期指派 | `x = value` | `←` |
| 相等測試 | `==` | `≡` |
| 可空性 | `T?`、`Option<T>` | `T ∪ nihil` |
| 分支加上單一陳述式 | `if (cond) return x` | `si cond ergo redde x` |
| 型別轉換 | `(T)value`、`value as T` | `value ∷ T` |
| 轉換（可能失敗） | `try_into()` | `value ↦ T` |

### 參考資料 {#references}

1. EBNF 文法——完整的字形與關鍵字清單
2. examples/corpus/——包含所有關鍵字的語言語料庫，共有 292 個範例檔案
3. examples/corpus/operatores/——運算子與字形範例
4. Commandments——維持這些訊號的九項設計法則

## Canonical vs sugar surfaces

*多個可解析表面，共用一個語意形狀。*

Faber 設計中反覆出現一種模式：語言為每個建構定義**一種規範拼寫**，但也接受多種語意相同的**語法糖拼寫**。編譯器不偏好其中任何一種——兩者都會解析為相同的 AST 節點。格式化工具會根據上下文與模式決定要輸出哪一種拼寫。

> **規則：**語法糖拼寫在語意上等同於長形式。
> 多個表面會解析為相同的 `HirAnnotation` 或型別節點。
> `faber format --canonical` 偏好規範拼寫；作者模式則保留作者所寫的語法糖。

### 數值型別語法糖 {#numeric-type-sugar}

數值型別具有長形式的規範拼寫，以及精簡的語法糖形式。
選擇以模組為單位，而不是以儲存庫為單位——CLI 套件可以全面使用長形式，而張量核心模組則可以使用語法糖：

| 語法糖 | 規範形式 | 領域 |
|-------|----------------|--------|
| `f32`、`f64`、`i32`、`u64` | `fractus<f32>`、`numerus<i32>` | 寬度標記——純量數值型別 |
| `tf32`、`tf32[4]`、`ti64[2, 3]` | `tensor<f32, _>`、`tensor<f32, [4]>` | 密集張量——`t` + 寬度 + 可選形狀 |
| `sf32`、`sf32[2, 3]`、`si64[N]` | `sparsa<f32, _>`、`sparsa<f32, [2, 3]>` | 稀疏張量——`s` + 寬度 + 可選形狀 |
| `mf32[4, 4]`、`mu32[3, 3]` | `matrix<f32, [4, 4]>` | 暫存器類別矩陣——`m` + 寬度 + 形狀 |
| `lf32`、`lu32`、`li64` | `lista<f32>`、`lista<u32>` | 清單——`l` + 寬度 |
| `f16` | `fractus<f16>` | 半精度浮點寬度標記（僅限語意／配置） |

**一般 Faber（偏好長形式）：**

```faber
fixum lista<f32> values ← vacua
fixum tensor<f32, [2, 3]> grid ← vacua
fixum numerus<i32> narrow ← 7
```

**數值模組（偏好語法糖）：**

```faber
fixum lf32 values ← vacua
fixum tf32[2, 3] grid ← vacua
fixum i32 narrow ← 7
```

語法糖**僅限型別位置**。名為 `f32`、`tf32` 或 `mf32` 的值識別字維持不變——編譯器只會在它們出現在型別位置時，將其解讀為語法糖。若檔案一致使用語法糖，應在檔案頂端說明一次：

```faber
# STYLE: numeric sugar (tf32, mf32, sf32, lf32, lu32)
```

### 註解語法糖 {#annotation-sugar}

Faber 註解遵循與數值型別相同的雙表面模型。
註解是附加至宣告的編譯器管理中繼資料——例如 CLI 選項定義的
`@ optio`，或非同步函式的 `@ futura`。

**規範形式：**具有明確欄位名稱的花括號記錄：

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

**語法糖形式：**位置引數與具名別名：

```text
@ optio verbose brevis "v" longum "verbose" typus bivalens ubique descriptio "Enable verbose output"
```

兩種形式都會產生相同的 `HirAnnotation` 記錄。規範形式明確且便於自我說明；語法糖形式則適用於欄位順序已廣為人知的常用註解，因此更為精簡。
`faber format --canonical` 偏好花括號記錄；作者模式則保留作者選擇的形式。

### 作者與規範格式化 {#author-vs-canonical-formatting}

`faber format` 指令以兩種模式運作，對應規範與語法糖原則：

| 模式 | 指令 | 輸入 | 輸出 |
|------|---------|-------|--------|
| 作者 | `faber format` | 已解析的 AST + 開頭雜項 | 保留 `#` 註解、空白行與語法糖拼寫的 Faber 原始碼 |
| 規範 | `faber format --canonical` | 已分析的 HIR + `TypeTable` | 正規化的 Faber——無註解、使用規範拼寫、不含語法糖 |

兩種模式都會經過編譯器完整的前半部流程（詞法分析、解析；規範模式另含分析）。無效原始碼會產生編譯器診斷——格式化工具不會默默格式化損壞的輸入。

兩種模式共同遵循的主要規則：

- 四個空格縮排
- Stroustrup 大括號：開啟的 `{` 與控制標頭位於同一行
- 作者模式保留空白行的*存在與否*，但會將多於一個的連續空白行折疊
- 作者模式不會插入來源中不存在的空白行
- 規範模式會將型別拼寫正規化為長形式、將張量語法糖正規化為規範形式，並將註解正規化為花括號記錄
- 規範模式會對可為空的聯集輸出 `T ∪ nihil`，並對可選參數輸出 `sponte`

### 設計原則 {#design-principle}

規範與語法糖模式會出現在多個地方，是因為這是一項刻意的設計原則，而不是一組零散的一次性便利功能：

| 領域 | 規範 | 語法糖 |
|--------|-----------|-------|
| 數值型別 | `numerus<i32>` | `i32` |
| 張量型別 | `tensor<f32, [4]>` | `tf32[4]` |
| 註解 | `@ optio { binding = verbose }` | `@ optio verbose ...` |
| 格式化 | `faber format --canonical` | `faber format`（作者模式） |
| 讀者語系 | 拉丁文（`la`） | 任一語系套件 |

這個模式服務於兩個目標。第一，它降低入門門檻——新使用者可以直接撰寫 `tf32[4]`，而不必輸入
`tensor<fractus<f32>, [4]>`。第二，它讓規範語言保持明確無歧義——當精確度很重要時，長形式會清楚表達其確切含義。格式化工具則在兩者之間搭起橋樑：作者撰寫語法糖，審閱者可以要求規範形式，而 CI 可以強制執行其中任一形式。

### 參考資料 {#references}

1. `radix/docs/design/numeric-type-sugar.md` — 完整語法糖系列、拼寫偏好
2. `radix/docs/design/annotation-sugar.md` — 雙表面註解模型
3. `radix/docs/design/faber-canonical-surface.md` — 作者與規範格式政策
4. `faber/docs/EBNF.md` — 語法糖形式的文法表格
