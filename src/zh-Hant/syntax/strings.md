+++
translation_kind = "translated"

title = "String and template literals"
section = "syntax"
order = 8
sources = [
  "radix/README.md (String and Template Literals, String-template application, Inline JSON)",
  "examples/corpus/literalia/",
  "examples/corpus/scriptum/",
  "radix/docs/factory/textus-literal-family/",
]


prose_hash = "sha256:61bc93552e4a6ccc2a3a51453c146c31eee8331c6e82a3b17de5bc70f4ce24b0"
code_hash = "sha256:e7cba6e75a702466f92ecdbaa2c9d777b027a09a7f1b0414387cc746376d3075"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber 使用分隔符語義——每種引號形式都代表不同的原始碼形狀。它們不是可互換的同義詞。

## 字面形式 {#literal-forms}

| 形式 | 類型 | 作用 |
|------|------|------|
| `'…'` | `ascii` | 固定機器標記；不含 `§`；不含 `(…)` |
| `"…"` | `textus` | 短 Unicode 行字串；可解析 `(…)` |
| `«…»` | `textus` | 區塊／多行 Unicode；可解析 `(…)` |
| `` `…` `` | `forma` | 擷取的範本；可擷取 `(…)` |
| `{ … }` | `json` | 編譯期 JSON 文件 |
| `|…|` | `octeti` | 編譯期十六進位位元組 |
| `[ … ]` | `lista<T>` | Faber 清單字面值 |

## 字串範本套用 {#string-template-application}

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

## 區塊字串 {#block-strings}

多行區塊使用書名號 `«…»`：

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

## 擷取的範本（forma） {#captured-templates}

反引號範本會擷取文字與參數，但不進行解析。
適合用於繫結的 SQL／URL 承載內容：

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

## 內嵌 JSON {#inline-json}

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
