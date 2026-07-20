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
*多個可解析表面，共用一個語意形狀。*

Faber 設計中反覆出現一種模式：語言為每個建構定義**一種規範拼寫**，但也接受多種語意相同的**語法糖拼寫**。編譯器不偏好其中任何一種——兩者都會解析為相同的 AST 節點。格式化工具會根據上下文與模式決定要輸出哪一種拼寫。

> **規則：**語法糖拼寫在語意上等同於長形式。
> 多個表面會解析為相同的 `HirAnnotation` 或型別節點。
> `faber format --canonical` 偏好規範拼寫；作者模式則保留作者所寫的語法糖。

## 數值型別語法糖 {#numeric-type-sugar}

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

## 註解語法糖 {#annotation-sugar}

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

## 作者與規範格式化 {#author-vs-canonical-formatting}

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

## 設計原則 {#design-principle}

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

## 參考資料 {#references}

1. `radix/docs/design/numeric-type-sugar.md` — 完整語法糖系列、拼寫偏好
2. `radix/docs/design/annotation-sugar.md` — 雙表面註解模型
3. `radix/docs/design/faber-canonical-surface.md` — 作者與規範格式政策
4. `radix/EBNF.md` — 語法糖形式的文法表格
