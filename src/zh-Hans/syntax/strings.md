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
Faber 使用分隔符语义 — 每种引号形式表示不同的源代码形态。它们之间不能互换。

## 字面量形式 {#literal-forms}

| 形式 | 类型 | 角色 |
|------|------|------|
| `'…'` | `ascii` | 固定机器令牌；无 `§`；无 `(…)` |
| `"…"` | `textus` | 短 Unicode 单行字符串；`(…)` 渲染 |
| `«…»` | `textus` | 块/多行 Unicode；`(…)` 渲染 |
| `` `…` `` | `forma` | 捕获模板；`(…)` 捕获 |
| `{ … }` | `json` | 编译期 JSON 文档 |
| `|…|` | `octeti` | 编译期十六进制字节 |
| `[ … ]` | `lista<T>` | Faber 列表字面量 |

## 字符串模板应用 {#string-template-application}

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

## 块字符串 {#block-strings}

多行块使用书名号 `«…»`：

```faber
fixum _ sql ← «
    select id, email
    from accounts
»
```

## 捕获模板 (forma) {#captured-templates}

反引号模板捕获文本和参数而不渲染。
对于绑定的 SQL/URL 载荷是安全的：

```faber
fixum numerus user_id ← 42
fixum _ query ← `select * from users where id = §`(user_id)
```

## 内联 JSON {#inline-json}

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
