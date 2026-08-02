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

*九條讓 Faber 感覺像 Faber 的規則。*

這些是定義 Faber 性格的設計法則。語法可以演進，功能也可以增加，但變更應保留這些原則。違反這些原則的程式可能仍是有效的 Faber，但它不會讓人感覺像 Faber。

這些誡命適用於每一個層次——從語法本身，到標準函式庫 API 的命名方式。無論關鍵字以哪一種人類語言呈現，也無論程式編譯至哪一個目標後端，它們都是讀者能一眼辨認 Faber 原始碼的原因。

### I. 型別先於名稱 {#i-types-before-names}

宣告會從形狀讀到繫結。型別放在前面，因為讀者需要先知道這是「哪一類事物」，名稱才告訴他們這是「哪一個事物」。這與語法順序從類別讀到實例的語言一致——中文、印地語、阿拉伯語——並產生掃讀方式一致的宣告。

```text
# Type before name in every declaration
textus nomen
numerus aetas
functio salve(textus name) → textus
```

### II. 機械勝於魔法 {#ii-mechanical-over-magical}

相同的結構在任何地方都應表示相同的事物。如果讀者需要遙遠的上下文才能知道某個符號的作用，這個語法就值得懷疑。Faber 偏好明確且區域性的推理——宣告位置攜帶足夠資訊，讓人能在使用位置理解將會發生什麼。

```faber
# The meaning of a call is determined by the function's signature,
# not by invisible trait resolution or implicit conversions.
functio duplica(numerus n) → numerus {
    redde n * 2
}
```

### III. 字形承載結構 {#iii-glyphs-carry-structure}

結構與運算子的意義使用字形，而不是文字：`←`
表示繫結，`→` 表示回傳型別，`⇥`
表示錯誤退出，`ergo` 表示簡潔分支主體，
`≡` 表示相等，`∪` 表示聯集
型別。字形是通用的——它們永不在地化，也不會在不同呈現中改變意義。
泰語讀者與法語讀者看到的是相同的字形，即使它們周圍的關鍵字不同。

### IV. 拉丁文承載行為 {#iv-latin-carries-behaviour}

文字用於宣告、陳述、生命週期與行為意圖：
`functio`、`genus`、`fixum`、
`varia`、`redde`、`cape`。
這些文字可以透過讀者語系套件繫結——它們是詞彙，而不是文法。選擇拉丁文並不是因為拉丁文優越；而是為了選定一個一致的古典來源，使所有關鍵字都屬於相同的語域，也不讓任何關鍵字因為實作所使用的語言而享有特權。

### V. 變化承載時間與流程 {#v-conjugation-carries-time-and-flow}

當相同的根邏輯可以同步、非同步執行，或作為產生器執行時，動詞的變化形式應承載該執行模式。所有權成對形式——變更與複製輸出——使用同一詞幹的相關形式。這是 morphologia 原則。標準函式庫（Norma）對所有方法名稱都遵循此慣例：`lege`（同步讀取）對
`leget`（非同步讀取），`adde`（就地變更）對
`addita`（回傳新的複本）。編譯器不會強制或推導變化形式——這是命名政策，而不是語言功能。

### VI. 一個符號，一項工作 {#vi-one-sign-one-job}

字形或關鍵字可以有完全相同的別名，但不應承載無關的意義。別名必須回指一個單一的規範概念。這項原則促成 Faber 將 `←`
（執行期繫結）與 `=`（結構欄位形狀）分開——大多數
語言把兩者都合併為 `=`，但這種多重使用掩蓋了一行究竟是資料流操作，還是型別層級定義。

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

### VII. 執行期流程是明確的 {#vii-runtime-flow-is-explicit}

執行期繫結、重新指派與變更使用 `←`；
結構定義使用 `=`。讀者掃讀原始碼時，可以立即看見每一個資料流操作：每個 `←` 都是
一個執行期事件。特定的 `=` 究竟表示「儲存至這個變數」，還是「定義這個欄位」，在語法上沒有歧義。

### VIII. 缺失具有型別 {#viii-absence-is-typed}

可為空值的值型別寫成聯集：`T ∪ nihil`。可選的
宣告槽位使用名稱後置標記：`sponte`。這是兩個不同的概念——「可能缺失的值」與「呼叫者可以省略的槽位」——Faber 讓它們在語法上保持分離，而不是把兩者都合併為 `T?` 或 `Option<T>`。

```text
# Absence in a value: T ∪ nihil
functio find(textus key) → numerus ∪ nihil

# Omission at declaration: sponte
functio connect(textus host, numerus port sponte) → vacuum
```

### IX. 編譯器不會猜測以掩蓋缺失的資訊 {#ix-compiler-does-not-guess}

缺失的型別資訊是應在上游修正的分析問題，而不是可以用程式碼生成細節掩蓋的問題。當資訊確實缺失時，編譯器絕不會默默推斷出程式設計師未提供的型別——它會報告這個缺口並停止。這項規則讓 Faber 保持誠實：如果讀者無法從區域性原始碼判定某個符號的意義，編譯器就不應假裝自己可以。

### 目的 {#purpose}

這些誡命旨在回答每次語言設計討論都會出現的問題：「這項變更還是 Faber 嗎？」它們是衡量不變性的檢查——不是對照功能清單，而是對照一種性格。違反某項誡命的變更可能仍是好主意，但應被認定為偏離 Faber 的設計性格，而不是例行的功能增加。

在實務上，這些誡命最常作為新語法提案的審查標準。一項提案若藉由加入名稱優先的替代形式而削弱「型別先於名稱」，或藉由讓字形承載多重意義而模糊「一個符號，一項工作」，就必須說明為何 Faber 應為該功能彎曲自己的性格。

## Design documents

Radix 儲存了說明 Faber 作為語言與編譯器運作方式的權威設計文件。這些文件位於
`radix/docs/design/`。

### 索引 {#index}

| 範疇 | 檔案 |
|------|-------|
| 目標與降低層級 | `target-capability-matrix.md`、`lowering-routes.md`、`semantic-ownership.md` |
| 型別與語法糖 | `numeric-type-sugar.md`、`comparison-operators.md`、`annotation-sugar.md` |
| 集合內建操作 | `lista-intrinsics.md`、`tabula-intrinsics.md`、`tensor-intrinsics.md`、`numerus-intrinsics.md`、`fractus-intrinsics.md`、`textus-intrinsics.md`、`intervallum-intrinsics.md`、`instans-intrinsics.md`、`copia-intrinsics.md` |
| 轉換 | `conversio-valor.md`、`failable-conversio.md` |
| 框架與效果 | `frame-stream-types.md`、`host-provider-gateway.md` |
| 讀取器與格式 | `reader-locale.md`、`faber-canonical-surface.md` |
| 系統／AIR | `air-dialect.md`、`aiml-foundation.md`、`systems-shaped-values.md` |
| 工具表面 | `faber-scripting.md` |
| 命名技術債 | `mixed-case-naming-debt.md` |

### 標準函式庫設計文件 {#stdlib-design-docs}

`radix/docs/stdlib/` 目錄包含：

| 文件 | 作用 |
|-----|------|
| `morphologia.md` | 所有標準函式庫方法名稱的變化政策 |
| `tensor-methods.md` | Tensor 接收器方法參考 |
| `chorda-methods.md` | Chorda（文字）方法參考 |
| `mathesis-methods.md` | Math 方法參考 |
| `tempus-methods.md` | 時間方法參考 |
| `stdlib-mechanical-verbs.md` | `pange`／`solve`／`tempta` 三元組政策 |

## History

### 起源 {#origins}

Radix 編譯器的第一個提交於 **2025 年 12 月 20 日**完成，當時是一個 Bun + TypeScript 專案，只有一個 `docs/decisions.md` 檔案。第二個提交制定了五份至今仍影響這門語言的架構決策紀錄。

**ADR-003** 的標題是「格位詞尾承載語義」，它從一開始就確立了拉丁語形態不只是關鍵字外觀——編譯器會理解變格與變位，以推斷程式意圖。最初的格位對應如下：

```text
Nominative  (subject)       →  return value, caller
Accusative  (direct object)  →  primary argument
Dative      (indirect obj.)  →  recipient, callback, destination
Genitive    (possession)     →  property access, "of" relationships
Ablative    (instrument)     →  dependencies, context, "using X"
```

同一份文件也記載：「動詞變位自然會引出下一個問題（未來式 → 非同步？）。」這個種子逐漸發展成現代的 **morphologia** 命名慣例：標準函式庫使用經變位的拉丁動詞形式來表示同步與非同步，以及變更與複製輸出，而不要求編譯器本身理解拉丁語文法。

專案最初以 TypeScript 開始，後來改寫為 Rust；語法則隨著 2026 版次為 1.x 系列定型。最初的五份 ADR（檔案副檔名 `.fab`、錯誤提示、格位詞尾、遞迴下降解析器、自訂 AST）至今仍可在 git 歷史中看到。

### 發行版本 {#releases}

預先建置的 CLI 封存檔——最上方是目前的 Faber 發行版本，接著列出 [faberlang/releases](https://github.com/faberlang/releases) 中每個已發佈的標籤與二進位檔：

- **[發行版本](/reference/releases.html)** — 下載連結與歷史清單
- **[安裝與下載](/start/install.html)** — PATH 設定與第一次執行 `faber check`
